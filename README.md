# Janka News

A web app to get the latest Janka news and stay connected with friends and neighbours.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Used Libraries](#used-libraries)
- [Setup](#setup)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

This is a python django web application for Janka residance to interact with the committee, neighbours and get info for upcoming events. Users can make, edit, delete accounts and retrive their account incase they forget their password. They also can add, read, and remove Posts.

## Features

- Fully functional application built with Django
- User authentication and authorization system
- CRUD operations for managing news posts
- Pagination for displaying a list of blog posts
- User-friendly interface with responsive design

## Used Libraries

The Django Blog application utilizes the following Python libraries:

- **Django**: A high-level Python web framework for rapid development of secure and maintainable web applications.
- **Pillow**: A Python Imaging Library (PIL) fork that adds image processing capabilities to Django, including image upload and manipulation.
- **django-crispy-forms**: A Django application that helps to manage Django forms in a DRY (Don't Repeat Yourself) way.
- **django-crispy-bootstrap5**: A Django template pack for crispy-forms, designed to work with Bootstrap 5 for styling forms.

To install these libraries, run the following command:

    ```bash
pip install -r requirements.txt
    ```
    
## Setup

To get started with this project, follow these steps:

1. Clone the repository:
    ```bash
    git clone <repository_url>
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Database migrations:
    ```bash
    python manage.py migrate
    ```

4. Create a superuser (admin):
    ```bash
    python manage.py createsuperuser
    ```

5. Run the development server:
    ```bash
    python manage.py runserver
    ```

6. Access the application:
    Open a web browser and go to `http://localhost:8000/`


## Usage

To use this Janka News application, follow these steps:

1. **Register/Login:** If you're a new user, register for an account using the registration form. If you already have an account, log in using your credentials.

2. **View Posts:** Once logged in, you'll be redirected to the home page where you can view a list of posts. Click on a post title to view its details.

3. **Create a New Post:** To create a new post, navigate to the "New Post" page using the navigation menu or the link provided. Fill out the form with the title and content of your post, then click "Submit" to publish it.

4. **Edit/Delete Post:** If you're the author of a post, you'll see options to edit or delete the post on the post detail page. Click on the "Edit" button to update the post content or the "Delete" button to remove the post from the database.

5. **View User Profile:** You can view your user profile by clicking on your username in the navigation menu. From the profile page, you can update your profile information and change your profile picture.

6. **Logout:** When you're done using the application, click on the "Logout" button in the navigation menu to log out of your account.

7. **Additional Features:** Explore other features of the application, such as searching for posts, filtering posts by category or tag, commenting on posts, and sharing posts on social media.


## Contributing

- Planning to add posts comments section. So if anyone wants, go for it. I am too overwhelmed with other courses now.


## License

This project is licensed under the [MIT License](LICENSE).
