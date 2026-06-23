# Viva Preparation Guide: TAG Social Media Platform

## 1. Project Description
**TAG** is a comprehensive, full-stack social networking platform designed to facilitate robust user interactions. It allows users to create accounts, share thoughts and images via posts, engage in discussions through a nested comment system, express appreciation using a like feature, and build customized content feeds through a follower-following social graph. The frontend is built using raw CSS to ensure maximum performance while maintaining a state-of-the-art dark/light mode UI.

## 2. Objectives
- **Core Functionality**: Deliver a bug-free CRUD (Create, Read, Update, Delete) experience across Posts, Profiles, and Comments.
- **Scalability**: Structure the database and queries efficiently to prevent N+1 query bottlenecks commonly found in social feeds.
- **Security**: Implement strict ownership constraints so users can only manipulate their own content, and use Django's built-in CSRF defenses to prevent malicious form submissions.
- **User Experience**: Provide an intuitive, modern, responsive interface accessible on desktop, tablet, and mobile.

## 3. Technology Stack
- **Backend Framework**: Django (Python)
- **Database**: SQLite (Development)
- **Frontend**: HTML5, Vanilla CSS, Vanilla JavaScript (for theme toggling and image previews)
- **Image Processing**: Pillow (Python Imaging Library)

## 4. Database Design & Architecture
The project is modularized into three Django apps:
- `users`: Manages authentication and the `UserProfile` model. Relies on Django's built-in `User` model. Uses `post_save` signals to automatically spin up a `UserProfile` upon registration.
- `posts`: Houses the `Post` model, connected to the `User` via ForeignKey.
- `interactions`: Handles the `Comment`, `Like`, and `Follow` models. 
  - *Likes* and *Follows* use `unique_together` constraints at the schema level to absolutely prevent duplicate relations.
  - *Follows* utilize a `CheckConstraint` to prevent a user from following themselves.

## 5. Challenges Faced & Solutions
- **N+1 Query Optimization**: 
  - *Challenge*: Displaying the home feed initially resulted in hundreds of database queries (fetching the author, checking if the logged-in user liked the post, etc., for every single post).
  - *Solution*: Utilized Django's `select_related()` and `prefetch_related()` methods to execute massive table joins in memory. Passed a flattened list of `liked_post_ids` and `following_ids` to the template to resolve UI state in O(1) time complexity.
- **UI State Persistence**:
  - *Challenge*: Maintaining the user's Dark/Light mode preference across page navigations without incurring database overhead.
  - *Solution*: Leveraged the browser's `localStorage` API in JavaScript to instantly read and apply the theme preference before the page fully renders, eliminating CSS flickering.

## 6. Future Scope
If this project were to be scaled for a production environment:
- **Database Migration**: Transition from SQLite to a robust relational database like PostgreSQL.
- **Caching**: Implement Redis to cache the global home feed and reduce database load during traffic spikes.
- **Asynchronous Features**: Integrate Django Channels (WebSockets) to power real-time notifications and live chat.
- **Media Hosting**: Offload static and media files from the local server to a CDN (e.g., AWS S3).
