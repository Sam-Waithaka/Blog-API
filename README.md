
# Blog API

A fully functional Blog API built with Django and Django Rest Framework (DRF). This project includes features for user management, permissions, and full CRUD (Create-Read-Update-Delete) operations on blog posts. Additionally, it explores the use of viewsets, routers, and auto-generated API documentation.

## Features

- User Authentication and Management
- Permissions and Role-based Access Control
- CRUD Functionality for Blog Posts
- Viewsets and Routers for Streamlined API Development
- Auto-generated API Documentation with DRF

## Technologies Used

- [Django](https://www.djangoproject.com/)
- [Django Rest Framework (DRF)](https://www.django-rest-framework.org/)

## Getting Started

### Prerequisites

- Python 3.x
- Django 3.x or higher
- Django Rest Framework 3.x or higher
- pip (Python package installer)
- Virtual environment tool (optional but recommended)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Sam-Waithaka/Blog-API.git
   cd blog-api
   ```

2. Create and activate a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```bash
   python manage.py migrate
   ```

5. Run the development server:
   ```bash
   python manage.py runserver
   ```

6. Access the API at `http://localhost:8000/api/`.

## API Endpoints

- **Users**
  - `POST /api/users/` - Create a new user
  - `GET /api/users/` - List all users
  - `GET /api/users/{id}/` - Retrieve a specific user
  - `PUT /api/users/{id}/` - Update a user
  - `DELETE /api/users/{id}/` - Delete a user

- **Blog Posts**
  - `POST /api/posts/` - Create a new blog post
  - `GET /api/posts/` - List all blog posts
  - `GET /api/posts/{id}/` - Retrieve a specific blog post
  - `PUT /api/posts/{id}/` - Update a blog post
  - `DELETE /api/posts/{id}/` - Delete a blog post

## Documentation

API documentation is auto-generated by Django Rest Framework and is available at `http://localhost:8000/api/docs/`.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/YourFeature`.
3. Make your changes and commit them: `git commit -m 'Add new feature'`.
4. Push to the branch: `git push origin feature/YourFeature`.
5. Submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any inquiries or support, please contact [your email address].
