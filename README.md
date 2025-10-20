## Backend for Sell (Django REST API)

A Django REST Framework backend for a simple e-commerce domain with products, categories, colors, customers, permissions, and JWT-based authentication.

### Tech stack
- **Django 5.2**
- **Django REST Framework**
- **SimpleJWT** for authentication
- **django-cors-headers** and **django-debug-toolbar**
- **SQLite** (development)

### Project layout
```
backend_for_sell/
  backend_for_sell/        # Django project (settings, urls, wsgi/asgi)
  customer/                # Customers and permissions app
  product/                 # Products, categories, colors, ratings app
  photos/                  # Uploaded media storage (by date)
  manage.py
  db.sqlite3               # Dev database
```

### Quick start
1) Python 3.12+ and virtualenv recommended.
2) Create and activate a venv:
```bash
python3 -m venv venv
source venv/bin/activate
```
3) Install dependencies:
```bash
pip install -U pip
pip install django djangorestframework djangorestframework-simplejwt django-cors-headers django-debug-toolbar Pillow
```
4) Run migrations and start server:
```bash
python manage.py migrate
python manage.py runserver
```
The API will be available at `http://127.0.0.1:8000/`.

### Environment configuration
- `DEBUG`: enabled by default in `settings.py` for development.
- `ALLOWED_HOSTS`: empty by default; set for production.
- Database: SQLite (`db.sqlite3`). For production, configure `DATABASES` in `settings.py`.
- CORS: `django-cors-headers` middleware is enabled; adjust settings as needed.
- Auth: DRF set to use JWT via SimpleJWT.

### Authentication (JWT)
Obtain access/refresh tokens:
```http
POST /login
Content-Type: application/json

{ "username": "<username>", "password": "<password>" }
```
Refresh access token:
```http
POST /api/token/refresh/
Content-Type: application/json

{ "refresh": "<refresh_token>" }
```
Blacklist/logout refresh token:
```http
POST /logout
Authorization: Bearer <access_token>
Content-Type: application/json

{ "refresh": "<refresh_token>" }
```
Use the access token with:
```
Authorization: Bearer <access_token>
```

### Core models (overview)
- `customer`: full name, birth date, email, username, password, image, verification, many-to-many `permission`.
- `permission`: title, API link, HTTP method.
- `category`: title, productsNumber, creationDate.
- `color`: colorName.
- `product`: title, description, price, many-to-many `color`, image, discountPercentage, status, rate, creationDate, foreign key `category`.
- `customer_rate`: unique pair of (`customer`, `product`) with numeric `rate`.

### API routes
Project `urls.py`:
- `GET /admin/` – Django admin
- Includes `product` routes at root "/"
- Includes `customer` routes at "/customers"
- `POST /login` – obtain JWT pair
- `POST /api/token/refresh/` – refresh access token
- `POST /logout` – blacklist refresh token

Product app (`product/urls.py`):
- `GET|POST /products` – list or create products
- `GET|PUT|DELETE /products/<int:pk>` – retrieve/update/delete a product
- `GET|POST /ratings/<int:product_id>/<int:customer_id>` – list all ratings or create rating for a product by a customer
- `GET|POST /categories` – list or create categories
- `GET|PUT|DELETE /categories/<int:pk>` – retrieve/update/delete a category
- `GET|POST /colors` – list or create colors
- `GET|PUT|DELETE /colors/<int:pk>` – retrieve/update/delete a color

Customer app (`customer/urls.py`):
- `GET|POST /customers` – list or create customers
- `GET|PUT|DELETE /customers/<int:pk>` – retrieve/update/delete a customer
- `GET|POST /customers` – list or create permissions
- `GET|PUT|DELETE /customers/<int:pk>` – retrieve/update/delete a permission

Notes:
- Most endpoints require JWT auth (`IsAuthenticated`) in the product app.
- Some responses in views use `302 FOUND` for list GETs; clients should handle that status code accordingly.

### Running tests
```bash
python manage.py test
```

### Admin
Create a superuser to access `/admin/`:
```bash
python manage.py createsuperuser
```

### Media uploads
Uploaded images are stored under `photos/%y/%m/%d` per the model `ImageField` definitions. Ensure the directory exists and your server is configured to serve media in development.

### Debug toolbar
Available at `/__debug__/` when `DEBUG=True`.

### License
MIT or as specified by the repository owner.


