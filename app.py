import os, sqlite3
from datetime import datetime, timedelta
from functools import wraps
from flask import Flask, g, request, redirect, url_for, session, flash, render_template, abort
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename

BASE = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE, "omnisocial.db")
UPLOAD_DIR = os.path.join(BASE, "static", "uploads")
os.makedirs(UPLOAD_DIR,exist_ok=True) 
    

       
app= Flask(__name__)
gunicorn app:app --bind 0.0.0.0:$PORT --workers 1 --timeout 120
app.secret_key = os.environ.get("OMNISOCIAL_SECRET", "change-this-development-secret-before-deploying")
app.config["MAX_CONTENT_LENGTH"] = 25 * 1024 * 1024
ALLOWED = {"png", "jpg", "jpeg", "gif", "webp", "mp4", "webm"}

def db():
    if "db" not in g:
        g.db = sqlite3.connect(DB_PATH)
        g.db.row_factory = sqlite3.Row
        g.db.execute("PRAGMA foreign_keys = ON")
    return g.db

@app.teardown_appcontext
def close_db(_=None):
    conn = g.pop("db", None)
    if conn is not None:
        conn.close()

def init_db():
    conn = sqlite3.connect(DB_PATH)
    conn.executescript("""
    PRAGMA foreign_keys = ON;
    CREATE TABLE IF NOT EXISTS users (
      id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT UNIQUE NOT NULL,
      display_name TEXT NOT NULL, email TEXT UNIQUE NOT NULL,
      password_hash TEXT NOT NULL, bio TEXT DEFAULT '', created_at TEXT NOT NULL
    );
    CREATE TABLE IF NOT EXISTS posts (
      id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
      body TEXT NOT NULL, media TEXT, created_at TEXT NOT NULL
    );
    CREATE TABLE IF NOT EXISTS likes (
      user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
      post_id INTEGER NOT NULL REFERENCES posts(id) ON DELETE CASCADE,
      PRIMARY KEY(user_id, post_id)
    );
    CREATE TABLE IF NOT EXISTS comments (
      id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
      post_id INTEGER NOT NULL REFERENCES posts(id) ON DELETE CASCADE, body TEXT NOT NULL, created_at TEXT NOT NULL
    );
    CREATE TABLE IF NOT EXISTS follows (
      follower_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
      followed_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
      created_at TEXT NOT NULL, PRIMARY KEY(follower_id, followed_id), CHECK(follower_id != followed_id)
    );
    CREATE TABLE IF NOT EXISTS messages (
      id INTEGER PRIMARY KEY AUTOINCREMENT, sender_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
      receiver_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
      body TEXT NOT NULL, created_at TEXT NOT NULL
    );
    """)
    conn.commit()
    conn.close()

def current_user():
    if "user_id" not in session:
        return None
    return db().execute("SELECT id, username, display_name, email, bio FROM users WHERE id=?", (session["user_id"],)).fetchone()

@app.context_processor
def inject_user():
    return {"me": current_user()}

def login_required(fn):
    @wraps(fn)
    def wrapped(*args, **kwargs):
        if not current_user():
            flash("Please sign in to continue.", "info")
            return redirect(url_for("login"))
        return fn(*args, **kwargs)
    return wrapped

def allowed_file(name):
    return "." in name and name.rsplit(".", 1)[1].lower() in ALLOWED

@app.route("/")
def index():
    if not current_user():
        return render_template("landing.html")
    posts = db().execute("""
      SELECT p.*, u.username, u.display_name,
      (SELECT COUNT(*) FROM likes l WHERE l.post_id=p.id) AS like_count,
      (SELECT COUNT(*) FROM comments c WHERE c.post_id=p.id) AS comment_count,
      EXISTS(SELECT 1 FROM likes l WHERE l.post_id=p.id AND l.user_id=?) AS liked
      FROM posts p JOIN users u ON u.id=p.user_id ORDER BY p.id DESC
    """, (session["user_id"],)).fetchall()
    return render_template("feed.html", posts=posts)

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username", "").strip().lower()
        display = request.form.get("display_name", "").strip()
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")
        if not username or not display or not email or len(password) < 8:
            flash("Complete every field. Password must be at least 8 characters.", "error")
        elif not username.replace("_", "").isalnum():
            flash("Username can contain letters, numbers and underscores.", "error")
        else:
            try:
                db().execute("INSERT INTO users(username,display_name,email,password_hash,created_at) VALUES(?,?,?,?,?)",
                  (username, display, email, generate_password_hash(password), datetime.utcnow().isoformat()))
                db().commit()
                user = db().execute("SELECT id FROM users WHERE username=?", (username,)).fetchone()
                session.clear()
                session["user_id"] = user["id"]
                return redirect(url_for("index"))
            except sqlite3.IntegrityError:
                flash("That username or email is already registered.", "error")
    return render_template("auth.html", mode="register")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        identity = request.form.get("identity", "").strip().lower()
        password = request.form.get("password", "")
        user = db().execute("SELECT * FROM users WHERE username=? OR email=?", (identity, identity)).fetchone()
        if user and check_password_hash(user["password_hash"], password):
            session.clear()
            session["user_id"] = user["id"]
            return redirect(url_for("index"))
        flash("Invalid username/email or password.", "error")
    return render_template("auth.html", mode="login")

@app.route("/logout", methods=["POST"])
def logout():
    session.clear()
    return redirect(url_for("index"))

@app.route("/post", methods=["POST"])
@login_required
def create_post():
    body = request.form.get("body", "").strip()
    upload = request.files.get("media")
    media_name = None
    if upload and upload.filename:
        if not allowed_file(upload.filename):
            flash("Allowed media: PNG, JPG, GIF, WEBP, MP4, WEBM.", "error")
            return redirect(url_for("index"))
        ext = upload.filename.rsplit(".", 1)[1].lower()
        media_name = secure_filename(f"{session['user_id']}_{int(datetime.utcnow().timestamp()*1000)}.{ext}")
        upload.save(os.path.join(UPLOAD_DIR, media_name))
    if not body and not media_name:
        flash("Write something or attach media before posting.", "error")
    else:
        db().execute("INSERT INTO posts(user_id,body,media,created_at) VALUES(?,?,?,?)",
          (session["user_id"], body, media_name, datetime.utcnow().isoformat()))
        db().commit()
    return redirect(url_for("index"))

@app.route("/like/<int:post_id>", methods=["POST"])
@login_required
def like(post_id):
    post = db().execute("SELECT id FROM posts WHERE id=?", (post_id,)).fetchone()
    if not post: abort(404)
    conn = db()
    existing = conn.execute("SELECT 1 FROM likes WHERE user_id=? AND post_id=?", (session["user_id"], post_id)).fetchone()
    if existing:
        conn.execute("DELETE FROM likes WHERE user_id=? AND post_id=?", (session["user_id"], post_id))
    else:
        conn.execute("INSERT INTO likes(user_id,post_id) VALUES(?,?)", (session["user_id"], post_id))
    conn.commit()
    return redirect(request.referrer or url_for("index"))

@app.route("/comment/<int:post_id>", methods=["POST"])
@login_required
def comment(post_id):
    body = request.form.get("body", "").strip()
    if body and db().execute("SELECT id FROM posts WHERE id=?", (post_id,)).fetchone():
        db().execute("INSERT INTO comments(user_id,post_id,body,created_at) VALUES(?,?,?,?)",
          (session["user_id"], post_id, body[:2000], datetime.utcnow().isoformat()))
        db().commit()
    return redirect(request.referrer or url_for("index"))

@app.route("/post/<int:post_id>")
@login_required
def post_detail(post_id):
    post = db().execute("""SELECT p.*,u.username,u.display_name,
      (SELECT COUNT(*) FROM likes WHERE post_id=p.id) like_count,
      EXISTS(SELECT 1 FROM likes WHERE post_id=p.id AND user_id=?) liked
      FROM posts p JOIN users u ON u.id=p.user_id WHERE p.id=?""", (session["user_id"], post_id)).fetchone()
    if not post: abort(404)
    comments = db().execute("""SELECT c.*,u.username,u.display_name FROM comments c JOIN users u ON u.id=c.user_id
      WHERE c.post_id=? ORDER BY c.id ASC""", (post_id,)).fetchall()
    return render_template("post.html", post=post, comments=comments)

@app.route("/people")
@login_required
def people():
    q = request.args.get("q", "").strip()
    users = db().execute("""SELECT u.id,u.username,u.display_name,u.bio,
      EXISTS(SELECT 1 FROM follows f WHERE f.follower_id=? AND f.followed_id=u.id) following
      FROM users u WHERE u.id != ? AND (u.username LIKE ? OR u.display_name LIKE ?)
      ORDER BY u.username LIMIT 100""",
      (session["user_id"], session["user_id"], f"%{q}%", f"%{q}%")).fetchall()
    return render_template("people.html", users=users, q=q)

@app.route("/follow/<int:user_id>", methods=["POST"])
@login_required
def follow(user_id):
    if user_id == session["user_id"]: return redirect(url_for("people"))
    target = db().execute("SELECT id FROM users WHERE id=?", (user_id,)).fetchone()
    if not target: abort(404)
    conn = db()
    exists = conn.execute("SELECT 1 FROM follows WHERE follower_id=? AND followed_id=?", (session["user_id"], user_id)).fetchone()
    if exists:
        conn.execute("DELETE FROM follows WHERE follower_id=? AND followed_id=?", (session["user_id"], user_id))
    else:
        conn.execute("INSERT INTO follows(follower_id,followed_id,created_at) VALUES(?,?,?)",
          (session["user_id"], user_id, datetime.utcnow().isoformat()))
    conn.commit()
    return redirect(request.referrer or url_for("people"))

@app.route("/profile/<username>", methods=["GET", "POST"])
@login_required
def profile(username):
    user = db().execute("SELECT id,username,display_name,email,bio FROM users WHERE username=?", (username.lower(),)).fetchone()
    if not user: abort(404)
    if request.method == "POST":
        if user["id"] != session["user_id"]: abort(403)
        display = request.form.get("display_name", "").strip()
        bio = request.form.get("bio", "").strip()[:300]
        if display:
            db().execute("UPDATE users SET display_name=?,bio=? WHERE id=?", (display, bio, user["id"]))
            db().commit()
            flash("Profile updated.", "success")
        return redirect(url_for("profile", username=username))
    posts = db().execute("""SELECT p.*,(SELECT COUNT(*) FROM likes WHERE post_id=p.id) like_count,
      (SELECT COUNT(*) FROM comments WHERE post_id=p.id) comment_count
      FROM posts p WHERE user_id=? ORDER BY id DESC""", (user["id"],)).fetchall()
    followers = db().execute("SELECT COUNT(*) n FROM follows WHERE followed_id=?", (user["id"],)).fetchone()["n"]
    following = db().execute("SELECT COUNT(*) n FROM follows WHERE follower_id=?", (user["id"],)).fetchone()["n"]
    is_following = db().execute("SELECT 1 FROM follows WHERE follower_id=? AND followed_id=?", (session["user_id"], user["id"])).fetchone() if user["id"] != session["user_id"] else False
    return render_template("profile.html", user=user, posts=posts, followers=followers, following=following, is_following=is_following)

@app.route("/messages", methods=["GET", "POST"])
@login_required
def messages():
    me_id = session["user_id"]
    users = db().execute("""SELECT id,username,display_name FROM users WHERE id != ? ORDER BY username""", (me_id,)).fetchall()
    recipient_id = request.args.get("with", type=int)
    if request.method == "POST":
        recipient_id = request.form.get("recipient_id", type=int)
        body = request.form.get("body", "").strip()
        recipient = db().execute("SELECT id FROM users WHERE id=?", (recipient_id,)).fetchone() if recipient_id else None
        if recipient and recipient_id != me_id and body:
            db().execute("INSERT INTO messages(sender_id,receiver_id,body,created_at) VALUES(?,?,?,?)",
              (me_id, recipient_id, body[:4000], datetime.utcnow().isoformat()))
            db().commit()
        return redirect(url_for("messages", **({"with": recipient_id} if recipient_id else {})))
    selected = db().execute("SELECT id,username,display_name FROM users WHERE id=?", (recipient_id,)).fetchone() if recipient_id else None
    conversation = []
    if selected:
        conversation = db().execute("""SELECT m.*,s.username sender_name FROM messages m JOIN users s ON s.id=m.sender_id
          WHERE (sender_id=? AND receiver_id=?) OR (sender_id=? AND receiver_id=?)
          ORDER BY m.id ASC LIMIT 300""", (me_id, recipient_id, recipient_id, me_id)).fetchall()
    return render_template("messages.html", users=users, selected=selected, conversation=conversation)

@app.errorhandler(404)
def not_found(_):
    return render_template("error.html", code=404, message="That page could not be found."), 404

if __name__ == "__main__":
    init_db()
    app.run(debug=True, port=int(os.environ.get("PORT", "5000")))
