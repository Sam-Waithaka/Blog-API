
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

6. Access the API at `http://localhost:8000/api/v1/`.

# CORS Configuration

This project supports CORS to allow frontend applications running on different origins to interact with the API. The following origins are whitelisted:

- `http://localhost:3000`
- `http://localhost:8000`

To modify or add additional origins, update the `CORS_ALLOWED_ORIGINS` in the `settings.py` file.

## CSRF Trusted Origins

For secure cross-origin requests, the following origins are included in the `CSRF_TRUSTED_ORIGINS`:

- `http://localhost:3000`
- `http://localhost:8000`

This ensures that CSRF protection is correctly applied for these origins.

## API Endpoints

- List and create posts: `GET /api/v1/`, `POST /api/v1/`
- Retrieve, update, and delete a post: `GET /api/v1/<id>/`, `PUT /api/v1/<id>/`, `DELETE /api/v1/<id>/`

## Testing

Run the tests using:
```bash
python manage.py test


## API Endpoints

### Posts
- `GET /api/v1/` - List all posts
- `GET /api/v1/<id>/` - Retrieve a specific post

### Users
- `GET /api/v1/users/` - List all users
- `POST /api/v1/users/` - Create a new user
- `GET /api/v1/users/<id>/` - Retrieve a specific user
- `PUT /api/v1/users/<id>/` - Update a specific user
- `DELETE /api/v1/users/<id>/` - Delete a specific user

### Authentication and User Management
- `POST /api/v1/rest-auth/registration/` - Register a new user
- `POST /api/v1/rest-auth/login/` - Log in a user
- `GET /api/v1/rest-auth/logout/` - Log out a user
- `POST /api/v1/rest-auth/password/reset/` - Request a password reset
- `POST /api/v1/rest-auth/password/reset/confirm/` - Confirm a password reset



## API Documentation

Interactive API documentation is available via the following tools:

- **Swagger UI**: Explore and test API endpoints with an interactive interface.  
  **URL**: `[BASE_URL]/api/schema/swagger-ui/`

- **Redoc**: View a clean and detailed API documentation interface.  
  **URL**: `[BASE_URL]/api/schema/redoc/`

Replace `[BASE_URL]` with the base URL where your API is hosted (e.g., `http://127.0.0.1:8000` for local development).

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

For any inquiries or support, please contact developersam.w@gmail.com
