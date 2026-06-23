<<<<<<< HEAD
# TAG - Social Media Platform

TAG is a robust, full-stack social media application built with Django. It provides a complete environment for user interactions including posting content, commenting, liking, and following other users. The application is completely responsive and supports both Light and Dark themes via a user-friendly toggle.

## Project Structure
```
TAG/
├── TAG/                  # Main project settings and root routing
├── users/                # Authentication, profiles, and follow system
├── posts/                # Feed, post creation, and post detail
├── interactions/         # Centralized logic for Likes and Comments
├── templates/            # Global UI templates
├── static/               # CSS, JS, and Images
├── media/                # User uploaded images (avatars, post images)
└── manage.py             # Django execution script
```

## Features List
- **Authentication & Profiles**: Secure Registration, Login, and automated User Profile creation via Django Signals. Features bio updates and avatar image uploads.
- **Posts**: Users can create, edit, and delete their own posts. Supports rich text and image attachments.
- **Comments**: Nested interactions beneath posts. Users can add, edit, and safely delete comments, equipped with specific ownership validation.
- **Likes**: Highly optimized liking mechanics preventing N+1 queries. Prevents double-likes and updates seamlessly.
- **Follows**: Build a social graph. Users can follow/unfollow each other, view follower metrics, and filter their home feed to exclusively show followed content.
- **UI/UX**: Modern Pine Green (#01796F) aesthetic, responsive flexbox layout, and an instantaneous Dark/Light mode toggle powered by `localStorage`.

## Installation Guide
1. **Clone the repository** (or download the source files):
   ```bash
   git clone <repo-url>
   cd TAG
   ```

2. **Set up a Virtual Environment**:
   ```bash
   python -m venv venv
   # On Windows
   .\venv\Scripts\activate
   # On Mac/Linux
   source venv/bin/activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install django pillow
   ```

4. **Run Migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Start the Development Server**:
   ```bash
   python manage.py runserver
   ```
   Navigate to `http://127.0.0.1:8000/` in your browser.

## Future Enhancements
- **Real-time Notifications**: Implement Django Channels and WebSockets to alert users instantly when someone likes their post or follows them.
- **Direct Messaging**: Build a real-time private messaging system between mutually followed users.
- **Hashtags and Mentions**: Add parsing logic to index hashtags and "@" mentions for easier content discovery.
- **Deployment**: Migrate from SQLite to PostgreSQL and deploy the application securely to a cloud provider like AWS or Heroku using Gunicorn and Nginx.
=======
# codealpha_social-media
>>>>>>> 590686cbcfe2620e2d4e809b1bc28355acbddcce
