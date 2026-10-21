# 💜 OmniSocial
### One Platform. Every Connection.

OmniSocial is an all-in-one social networking platform inspired by Instagram, Snapchat, and WhatsApp. It aims to bring social sharing, community discovery, multimedia posts, user profiles, and direct messaging together in one modern application.

The project focuses on creating a clean, responsive, dark-themed interface with purple accents and a foundation that can grow into a comprehensive social networking platform.

> **Project status:** Development / MVP  
> **Purpose:** Full-stack social networking application  
> **Repository:** `omnisocial`

---

## 📌 Table of Contents

1. Introduction
2. Project Vision
3. Objectives
4. Features
5. Technology Stack
6. Application Architecture
7. Project Structure
8. Installation
9. Local Development
10. Environment Configuration
11. User Guide
12. Database Design
13. Authentication and Security
14. Media Management
15. Messaging System
16. Responsive Design
17. API and Backend Roadmap
18. Testing
19. Deployment
20. GitHub Workflow
21. Known Limitations
22. Future Enhancements
23. Contributing
24. License
25. Disclaimer

---

## 1. Introduction

Social networking has become an essential part of modern communication. People use different platforms to share photographs, publish updates, discover communities, watch videos, and communicate privately.

OmniSocial explores the idea of combining these everyday social experiences into one application.

Instead of switching between several applications, users should eventually be able to manage their social interactions through a single, unified interface.

The platform is designed around three principles:

- **Connection:** Make it easier for users to find and interact with other people.
- **Expression:** Allow users to share text, photographs, videos, and personal updates.
- **Simplicity:** Provide a consistent and easy-to-use interface across devices.

OmniSocial is an evolving development project. Features are implemented progressively, and the repository should clearly distinguish working functionality from planned functionality.

## 2. Project Vision

The long-term vision is to develop a versatile social networking application that combines elements commonly associated with Instagram, Snapchat, and WhatsApp.

### Instagram-inspired experiences

- Social feeds
- User profiles
- Image and video posts
- Likes and comments
- Following and followers
- Short-form video feeds

### Snapchat-inspired experiences

- Temporary stories
- Quick photo and video sharing
- Expiring content
- Camera-oriented social interactions

### WhatsApp-inspired experiences

- Direct messaging
- Conversation history
- Message notifications
- Media sharing in conversations
- Future support for group conversations

These comparisons describe product inspiration, not affiliation with or ownership by the companies behind those services.

## 3. Project Objectives

The primary objectives of OmniSocial are:

1. Develop a functional full-stack social networking application.
2. Provide a consistent interface for social interactions.
3. Implement account registration and authentication.
4. Support persistent posts, likes, and comments.
5. Allow users to discover and follow other members.
6. Introduce private messaging between registered users.
7. Build a foundation for stories and short-form videos.
8. Organize the codebase for future development.
9. Support local development and GitHub-based collaboration.
10. Prepare the application for a secure production deployment.

## 4. Features

### 4.1 User Authentication

The authentication system provides the foundation for individual user accounts.

Implemented starter functionality includes:

- User registration
- Login using a username or email
- Password hashing
- Session-based authentication
- Logout
- Restricted access to authenticated pages

Each account has a unique username and email address.

**Planned improvements:**

- Email verification
- Password reset
- Optional two-factor authentication
- Login rate limiting
- Account recovery
- Session management

### 4.2 Social Feed

The social feed is the central area for viewing community posts.

Users can publish text updates and, in the starter implementation, upload supported image or video files.

Feed functionality includes:

- Creating posts
- Displaying posts from registered users
- Showing the author's display name and username
- Displaying post timestamps
- Showing like counts
- Showing comment counts
- Opening individual post pages

Posts are stored in the database rather than existing only as temporary interface elements.

Future improvements may include personalized feeds, pagination, content recommendations, and chronological or relevance-based sorting.

### 4.3 Image and Video Sharing

OmniSocial supports basic media uploads through its post creation form.

Supported starter formats include:

- PNG
- JPEG and JPG
- GIF
- WebP
- MP4
- WebM

Uploaded files are associated with posts and displayed in the feed.

The current implementation stores uploads on the local filesystem. A production deployment should use managed object storage and stronger file validation.

Planned media features include:

- Image galleries
- Video previews
- Video transcoding
- Upload progress indicators
- Media compression
- Content moderation
- Storage quotas

### 4.4 Likes and Reactions

Registered users can like posts and remove their likes.

The application stores likes in a database table with a unique user-and-post combination.

This prevents the same account from creating duplicate likes on one post.

The current implementation provides a basic like action. Rich reactions, animated feedback, and notifications can be added later.

### 4.5 Comments

Users can open a post and submit comments.

Comment functionality includes:

- Adding a comment
- Associating the comment with its author
- Associating the comment with a post
- Displaying saved comments
- Showing the number of comments on a post

Future improvements include comment editing, deletion, threaded replies, reporting, moderation, and pagination.

### 4.6 User Profiles

Every registered user has a profile page.

The starter implementation includes:

- Username
- Display name
- Biography
- Published posts
- Follower count
- Following count
- Profile editing

Users can update their display name and biography.

Future profile enhancements may include profile photographs, cover images, privacy controls, verified-account workflows, and additional profile settings.

### 4.7 Discover Members

The discovery page helps users find other members.

Current functionality includes:

- Searching usernames
- Searching display names
- Viewing member profiles
- Following users
- Unfollowing users
- Viewing basic biography information

The search currently uses a simple database query. Larger deployments should introduce pagination, optimized indexing, abuse prevention, and potentially a dedicated search service.

### 4.8 Direct Messaging

OmniSocial includes a basic direct-messaging implementation.

Registered users can select another member and exchange text messages.

The current system stores messages in the database and displays the conversation history.

**Important limitations:**

- Messages are not end-to-end encrypted.
- Message delivery is not real-time.
- Read receipts are not implemented.
- Typing indicators are not implemented.
- Group conversations are not implemented.
- Push notifications are not implemented.

These capabilities require additional engineering and testing before they can be described as supported features.

### 4.9 Stories — Planned

The planned stories system will allow users to publish temporary photographs or videos.

Potential functionality includes:

- Creating a story
- Viewing stories from followed users
- Story expiration after 24 hours
- Story viewer lists
- Story privacy settings
- Story replies
- Optional highlights

Stories are part of the roadmap and should not be presented as a working feature until implemented.

### 4.10 Reels and Short Videos — Planned

A future short-video experience may include:

- Vertical video playback
- Scrollable video feeds
- Captions
- Likes and comments
- Creator profiles
- Video upload processing
- Playback optimization

Recommendations and analytics would require additional backend logic and appropriate privacy controls.

### 4.11 Notifications — Planned

A future notification system could notify users about:

- New followers
- Likes
- Comments
- Incoming messages
- Story replies
- Relevant account activity

Notifications may eventually support in-app delivery and browser or mobile push notifications.

---

## 5. Technology Stack

The prepared full-stack starter uses the following technologies.

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Flask | Web framework and routing |
| SQLite | Local relational database |
| HTML5 | Page structure |
| CSS3 | Responsive visual design |
| JavaScript | Client-side interactions where implemented |
| Jinja | Server-rendered HTML templates |
| Werkzeug | Password hashing and secure filename utilities |
| Git | Version control |
| GitHub | Source code hosting |

The interface uses a dark background, purple accents, rounded cards, and responsive layouts.

### Potential future technologies

The following technologies may be evaluated as the application grows:

- PostgreSQL for a production relational database
- WebSockets for real-time messaging
- Redis for caching and background coordination
- Object storage for images and videos
- React or Next.js for a separate frontend
- FastAPI for a dedicated REST API
- Docker for reproducible deployment
- Automated testing and continuous integration

These are potential enhancements, not dependencies required by the current starter.

---

## 6. Application Architecture

The current starter uses a server-rendered architecture.

A typical request follows this sequence:

1. The browser requests a page.
2. Flask receives the request.
3. The backend checks the session where authentication is required.
4. The application queries SQLite when data is needed.
5. Jinja renders the relevant HTML template.
6. The browser receives the response.

For a post submission:

1. The user fills in the post form.
2. The browser submits the form to Flask.
3. Flask validates the text and uploaded file extension.
4. The application saves an allowed upload locally, when provided.
5. The post metadata is written to SQLite.
6. The user is redirected to the feed.

A production implementation should strengthen upload validation, introduce CSRF protection, improve transaction handling, and use persistent managed storage.

---

## 7. Project Structure

The starter repository is organized as follows:

```text
omnisocial/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── omnisocial.db
├── static/
│   ├── style.css
│   └── uploads/
└── templates/
    ├── base.html
    ├── landing.html
    ├── auth.html
    ├── feed.html
    ├── post.html
    ├── people.html
    ├── profile.html
    ├── messages.html
    └── error.html
```

The database file is generated locally when the application runs. It should not be committed to the public repository.

### Main files

**`app.py`**

Contains the Flask application, routes, authentication logic, database access, post operations, follows, comments, profiles, and messaging.

**`requirements.txt`**

Lists the Python dependencies required to run the application.

**`templates/`**

Contains the server-rendered HTML pages.

**`static/style.css`**

Contains the interface styling and responsive layout rules.

**`static/uploads/`**

Stores local uploaded media during development.

**`.gitignore`**

Excludes virtual environments, generated databases, local secrets, and uploaded files from version control.

---

## 8. Installation

### Prerequisites

Install the following software:

- Python 3
- Git
- A code editor such as Visual Studio Code
- A modern web browser

Check your Python installation:

```bash
python3 --version
```

Check Git:

```bash
git --version
```

### Step 1: Download the repository

Clone your GitHub repository:

```bash
git clone https://github.com/YOUR-USERNAME/omnisocial.git
```

Replace the example username and repository with your actual GitHub details.

### Step 2: Open the project

```bash
cd omnisocial
```

### Step 3: Create a virtual environment

On macOS or Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

On Windows PowerShell:

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
```

### Step 4: Install dependencies

```bash
python -m pip install -r requirements.txt
```

### Step 5: Start the application

```bash
python app.py
```

### Step 6: Open OmniSocial

Visit:

http://127.0.0.1:5000

Register an account to start using the application.

The application creates its SQLite database automatically when started through the provided `app.py` entry point.

---

## 9. Local Development

A typical development cycle is:

1. Start the application.
2. Open it in a browser.
3. Test the feature you are working on.
4. Review the terminal for errors.
5. Update the relevant Python route or template.
6. Refresh the browser and test again.
7. Run the available checks before committing changes.

Flask debug mode is enabled in the starter's development entry point. Debug mode must not be enabled on a public production server.

### Common issues

**Python command not found**

Try:

```bash
python3 --version
```

Install Python if it is missing.

**Dependency installation fails**

Confirm that the virtual environment is activated, then run:

```bash
python -m pip install -r requirements.txt
```

**Port 5000 is already in use**

Stop the other process using the port or configure another port for local development.

**Uploaded media does not appear**

Check that the `static/uploads/` directory exists and that the uploaded file is supported.

**Database errors after modifying the schema**

Back up any development data before changing the database. The current starter uses `CREATE TABLE IF NOT EXISTS`; this is not a full database migration system.

---

## 10. Environment Configuration

The application uses an environment variable for its session secret.

For local development on macOS or Linux:

```bash
export OMNISOCIAL_SECRET="replace-with-a-long-random-secret"
python app.py
```

Generate a random value with Python:

```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

Set the generated value as the environment variable.

Do not publish your real secret in source code, README files, screenshots, or public repositories.

The starter includes a development fallback secret for convenience. Replace it before deployment.

---

## 11. User Guide

### Creating an account

1. Open the homepage.
2. Select the registration option.
3. Enter your display name.
4. Choose a username.
5. Enter an email address.
6. Create a password with at least eight characters.
7. Submit the form.

The starter checks username and email uniqueness and stores a password hash rather than the original password.

### Logging in

Enter your registered username or email and password.

Successful authentication creates a session and redirects you to the feed.

### Publishing a post

1. Sign in.
2. Open the home feed.
3. Enter text in the post composer, or attach supported media.
4. Select Publish Post.

The post is saved in the database.

### Liking a post

Select the like control beneath a post. Select it again to remove your like.

### Commenting

Open the individual post page, enter a comment, and submit it.

### Discovering members

Open Discover, search for a display name or username, and open the relevant profile.

### Following a member

Select Follow on the member's card or profile. The application saves the relationship.

### Updating your profile

Open your own profile and expand the profile editing section. Update your display name or biography and save the changes.

### Sending a direct message

Open Messages, select another registered member, enter a message, and send it.

The conversation is stored in the application's database. Do not use this demo messaging system for sensitive communications.

---

## 12. Database Design

SQLite stores the application's core data.

### Users

Stores account details, including:

- User ID
- Username
- Display name
- Email
- Password hash
- Biography
- Account creation timestamp

Usernames and email addresses are unique.

### Posts

Stores:

- Post ID
- Author ID
- Text content
- Optional media filename
- Creation timestamp

The author ID references the user who created the post.

### Likes

Stores the relationship between a user and a post.

A composite primary key prevents duplicate likes by the same user on the same post.

### Comments

Stores comment content, the associated user, the associated post, and the creation timestamp.

### Follows

Stores follower and followed-user relationships.

The database prevents duplicate follow relationships and self-following.

### Messages

Stores:

- Message ID
- Sender ID
- Receiver ID
- Message body
- Creation timestamp

The current implementation stores message text in plaintext within SQLite.

### Database relationships

```text
Users
 ├── Posts
 │    ├── Likes
 │    └── Comments
 ├── Follows
 └── Messages
```

The diagram represents the conceptual relationships, not a complete database entity-relationship specification.

For production, PostgreSQL, managed backups, schema migrations, and appropriate retention policies should be evaluated.

---

## 13. Authentication and Security

Security is essential for any social networking application.

The starter implements password hashing through Werkzeug and uses session-based authentication.

However, the current code is an educational MVP, not a completed security-hardened service.

Before public launch, the following work is recommended.

### Session security

- Use a strong, unique secret key.
- Enable secure cookie settings when deployed over HTTPS.
- Configure appropriate session expiration.
- Review session invalidation and account logout behavior.

### Request security

- Add CSRF protection to state-changing forms.
- Validate inputs on the server.
- Add rate limiting to authentication and posting endpoints.
- Apply appropriate security headers.
- Handle errors without revealing internal details.

### Upload security

- Validate actual file content and MIME types.
- Set upload-size and storage limits.
- Consider malware scanning.
- Prevent unsafe file execution.
- Use managed object storage for production media.

Checking a file extension alone does not prove that an uploaded file is safe.

### Account security

- Implement email verification.
- Implement password reset securely.
- Add account blocking and reporting.
- Establish moderation procedures.
- Protect account information from unauthorized access.

### Messaging privacy

The current message system is not end-to-end encrypted.

HTTPS protects network traffic between the browser and a properly configured server, but it does not prevent the server from reading messages stored in plaintext.

End-to-end encryption would require a separate, carefully reviewed cryptographic design and secure key management.

---

## 14. Media Management

The development implementation stores uploaded files in the local `static/uploads/` directory.

This is convenient for testing, but it is not a suitable default for every hosting environment.

Some deployment platforms use temporary filesystems, which can lose uploaded content after a restart or redeployment.

A production media pipeline should consider:

- Persistent object storage
- Private storage permissions
- Signed upload and download URLs where appropriate
- Content-type validation
- File-size limits
- Image resizing
- Video transcoding
- Thumbnail generation
- Storage quotas
- Deletion policies

Media access rules should also respect account privacy and content visibility.

---

## 15. Messaging System

The current messaging implementation supports basic one-to-one text conversations between registered members.

Messages are saved in the database and retrieved when a conversation is opened.

A more advanced messaging architecture could add:

1. WebSocket connections for real-time delivery.
2. Message delivery and read states.
3. Typing indicators.
4. Conversation lists.
5. Group messaging.
6. Attachments and media previews.
7. Message editing and deletion policies.
8. Notification delivery.
9. Abuse prevention and blocking.
10. Optional end-to-end encryption.

These capabilities should be implemented incrementally and tested with multiple accounts and concurrent sessions.

Real-time messaging should not be advertised until delivery, reconnection, authorization, and failure handling have been implemented.

---

## 16. Responsive Design

The interface uses a dark visual theme with purple accents.

Design goals include:

- Clear page hierarchy
- Consistent navigation
- Rounded cards
- Readable text
- Responsive feed layouts
- Mobile-friendly navigation
- Consistent form controls
- Accessible contrast and focus indicators

The stylesheet includes responsive breakpoints for smaller screens.

Responsive styling alone does not guarantee accessibility. Keyboard navigation, screen-reader labels, reduced-motion preferences, and contrast should be tested independently.

---

## 17. API and Backend Roadmap

The current starter is built around Flask routes that render HTML pages. It does not yet provide a complete REST API.

A future API layer could introduce structured endpoints for:

- Authentication
- Users and profiles
- Posts
- Likes and comments
- Follows
- Stories
- Conversations
- Messages
- Notifications
- Media uploads

A potential future API might use versioned paths such as `/api/v1/posts` and `/api/v1/users`.

This is a design proposal, not a claim that these endpoints already exist.

The API should include request validation, authentication and authorization, consistent error responses, pagination, rate limiting, and automated tests.

---

## 18. Testing

Testing helps ensure that features continue to work as the application changes.

Recommended test areas include:

### Authentication

- Register a new account.
- Reject duplicate usernames.
- Reject duplicate email addresses.
- Reject invalid credentials.
- Verify that protected pages require login.
- Confirm that logout ends the session.

### Posts

- Create a text post.
- Create a media post.
- Reject unsupported file extensions.
- Verify that posts persist after restarting the application.
- Confirm that posts appear on the correct profiles.

### Likes and comments

- Like a post.
- Unlike a post.
- Prevent duplicate likes.
- Add a comment.
- Verify that comment counts are accurate.

### Following

- Follow another account.
- Unfollow an account.
- Prevent self-following.
- Confirm follower counts update correctly.

### Messaging

- Send a message between two accounts.
- Verify that the intended conversation displays the message.
- Confirm that unrelated users cannot access another person's conversation.

### Production readiness

- Test upload-size limits.
- Test invalid and malformed requests.
- Check CSRF protections.
- Test session expiration.
- Verify database backups and restoration.

A future continuous integration workflow can run automated tests whenever code is pushed to GitHub.

---

## 19. Deployment

The starter is designed primarily for local development.

Public deployment requires additional configuration.

### Deployment checklist

- Set a strong production secret.
- Disable Flask debug mode.
- Configure HTTPS.
- Use a production WSGI server.
- Configure a persistent database.
- Configure persistent media storage.
- Add database backups.
- Add monitoring and error reporting.
- Configure rate limiting and CSRF protection.
- Test the application under realistic traffic.
- Establish privacy and moderation policies.

SQLite and local file uploads may work for small experiments, but production hosting requirements should determine whether a managed database and object storage are necessary.

The deployment process should be documented for the specific hosting provider selected by the project owner.

---

## 20. GitHub Workflow

GitHub is used to track changes and collaborate on the project.

### Initialize the repository

```bash
git init
git add .
git commit -m "Initial OmniSocial MVP"
```

### Connect the remote repository

```bash
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/omnisocial.git
git push -u origin main
```

If the remote is already configured, do not add it again. Check the existing configuration with:

```bash
git remote -v
```

### Push subsequent changes

```bash
git add .
git commit -m "Improve social feed"
git push
```

### Recommended development practices

- Use descriptive commit messages.
- Keep secrets out of commits.
- Create branches for larger changes.
- Test before merging.
- Document new environment variables.
- Update the README when behavior changes.
- Use issue tracking for bugs and feature requests.

---

## 21. Known Limitations

The current MVP has several important limitations.

| Area | Current limitation |
|---|---|
| Authentication | No email verification or password reset |
| Feed | Basic database-backed feed |
| Stories | Not implemented |
| Reels | Not implemented |
| Messaging | Stored text messages; no real-time transport |
| Encryption | No end-to-end encryption |
| Notifications | Not implemented |
| Media | Local filesystem storage |
| Search | Basic username and display-name search |
| Database | SQLite development database |
| API | Server-rendered routes, not a complete REST API |
| Deployment | Requires production hardening |
| Testing | Automated test suite still needs to be developed |

These limitations are intentional areas for future work. The project should not claim functionality that has not been implemented and tested.

---

## 22. Future Enhancements

### Phase 1 — Core stability

- Improve input validation.
- Add automated tests.
- Add CSRF protection.
- Improve error handling.
- Improve database migrations.
- Refine the responsive interface.

### Phase 2 — Social experience

- Add profile photographs.
- Improve feed pagination.
- Add post editing and deletion.
- Add comment moderation.
- Add blocking and reporting.
- Add profile privacy settings.

### Phase 3 — Stories and videos

- Build story creation and viewing.
- Add automatic story expiration.
- Implement a vertical short-video feed.
- Add thumbnail generation and video processing.
- Introduce media-storage integration.

### Phase 4 — Real-time communication

- Add WebSocket-based message delivery.
- Add conversation lists.
- Add delivery and read states.
- Add group conversations.
- Add media attachments.
- Introduce message notifications.

### Phase 5 — Production readiness

- Migrate to a managed database if needed.
- Add managed media storage.
- Configure HTTPS and secure cookies.
- Add monitoring and backups.
- Conduct security testing.
- Document deployment and recovery procedures.

### Phase 6 — Mobile experience

Potential future work includes a progressive web app or dedicated mobile applications, depending on project priorities.

---

## 23. Contributing

Contributions, suggestions, and bug reports are welcome.

### Suggested contribution process

1. Fork the repository.
2. Create a feature branch.
3. Make a focused change.
4. Test the change locally.
5. Update relevant documentation.
6. Commit your work.
7. Open a pull request describing the change.

### Contribution guidelines

- Keep code readable.
- Avoid committing credentials or private data.
- Document new dependencies.
- Explain changes that affect database schemas.
- Include reproducible steps when reporting bugs.
- Be respectful in discussions and reviews.

---

## 24. License

Choose an appropriate open-source license before publishing the repository for public reuse.

For example, the MIT License may be suitable if you want to permit broad reuse, modification, and redistribution subject to its terms.

Do not claim that this project is licensed under MIT until the repository actually contains an appropriate `LICENSE` file.

---

## 25. Disclaimer

OmniSocial is an independent development project. It is not affiliated with, endorsed by, or sponsored by Instagram, Snapchat, WhatsApp, or their parent companies.

Names of existing services are used only to describe general product inspiration.

The current implementation is a development MVP and should not be treated as a production-ready service without further security, reliability, privacy, and deployment work.

Features described as planned or future enhancements may not yet be implemented.

---

## 💜 Final Note

OmniSocial aims to make social interaction simpler by bringing sharing, discovery, and communication into one application.

The immediate goal is to build a reliable foundation, implement features incrementally, and document the project honestly as it evolves.

**One platform. Every connection. Welcome to OmniSocial.**
