# Marksfidels Integrated Services Limited Real Estate Platform

Welcome to the Marksfidels Integrated Services Limited Real Estate Platform! This web application is built using Python and Django, providing a comprehensive solution for real estate activities. The platform features authentication, email notifications, house and property listings, and various functionalities to enhance the real estate experience.

## Features

- **User Authentication**: Secure user authentication system to ensure user data privacy.

- **Email Notifications**: Automated email notifications for various events, enhancing communication with users.

- **Property Listings**: Browse and search through a wide range of houses and properties.

- **Advanced Search**: Filter properties based on location, price range, features, and more.

- **User Dashboard**: Personalized dashboards for users to manage their listings, preferences, and account settings.

- **Admin Panel**: Administrative interface for managing property listings, user accounts, and system configurations.

- **Responsive Design**: A user-friendly interface accessible on various devices.

## Getting Started

### Prerequisites

- [Python](https://www.python.org/) installed
- [Django](https://www.djangoproject.com/) installed
- [Virtualenv](https://virtualenv.pypa.io/) for managing Python environments

### Installation

1. Clone the repository:

   ```bash
   git clone
   ```

2. Create and activate a virtual environment:

   ```bash
   cd marksfidels-real-estate
   python -m venv venv
   source venv/bin/activate  # On Windows, use 'venv\Scripts\activate'
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Configure environment variables:

   Create a `.env` file in the root directory and set the required variables:

   ```env
   SECRET_KEY=your_secret_key
   DEBUG=True
   EMAIL_HOST=your_email_host
   EMAIL_PORT=your_email_port
   ```

5. Apply migrations:

   ```bash
   python manage.py migrate
   ```

6. Create a superuser:

   ```bash
   python manage.py createsuperuser
   ```

7. Run the development server:

   ```bash
   python manage.py runserver
   ```

   The application should now be accessible at `http://localhost:8000`.

## Usage

1. Access the admin panel at `http://localhost:8000/admin` and log in with the superuser credentials.

2. Add property listings and manage user accounts through the admin interface.

3. Users can register, log in, and explore available properties on the platform.
