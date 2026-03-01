# Inventory Management API

## Overview

The **Inventory Management API** is a backend system built using Django and Django REST Framework.

The system allows users to:

- Manage inventory items
- Track stock levels
- Authenticate using JWT
- Filter, search, and sort inventory data
- Track inventory change history

---

## Technology Stack

- Backend Framework: Django
- API Toolkit: Django REST Framework
- Authentication: JWT via Django REST Framework SimpleJWT
- Database ORM: Django ORM
- Filtering: django-filter

---

## Authentication

The API uses **JSON Web Token (JWT)** authentication.

### Obtain Token

```
POST /api/token/
```

#### Request Body

```json
{
  "username": "string",
  "password": "string"
}
```

#### Response

```json
{
  "access": "jwt_access_token",
  "refresh": "jwt_refresh_token"
}
```

---

### Refresh Token

```
POST /api/token/refresh/
```

Request:

```json
{
  "refresh": "refresh_token"
}
```

---

### Using Token

Add request header:

```
Authorization: Bearer YOUR_ACCESS_TOKEN
```

---

## User Management

### Register User

```
POST /api/users/
```

Example Request:

```json
{
  "username": "string",
  "email": "string",
  "password": "string"
}
```

---

### User Endpoints

| Method | Endpoint         | Description       |
| ------ | ---------------- | ----------------- |
| GET    | /api/users/      | Get own user data |
| POST   | /api/users/      | Register user     |
| GET    | /api/users/{id}/ | Retrieve user     |
| PUT    | /api/users/{id}/ | Update user       |
| DELETE | /api/users/{id}/ | Delete user       |

⚠ Users can only manage their own account.

---

## Inventory Item Management

Inventory items are associated with their owners.

### Inventory Item Fields

- Name
- Description
- Quantity
- Price
- Category
- Date Added
- Last Updated

---

### Create Item

```
POST /api/inventory/items/
```

---

### Get Items

```
GET /api/inventory/items/
```

Supports:

Pagination
Searching
Sorting
Filtering

---

### Update Item

```
PATCH /api/inventory/items/{id}/
```

Example:

```json
{
  "quantity": 20
}
```

---

### Delete Item

```
DELETE /api/inventory/items/{id}/
```

---

## 🔍 Filtering System

### Category Filter

```
GET /api/inventory/items/?category=Electronics
```

---

### Price Range Filter

```
GET /api/inventory/items/?price__gte=100&price__lte=500
```

---

### Low Stock Filter

```
GET /api/inventory/items/?quantity__lte=10
```

---

## Searching

```
GET /api/inventory/items/?search=laptop
```

Searches item name.

---

## Sorting (Ordering)

Use the `ordering` parameter.

Examples:

```
GET /api/inventory/items/?ordering=price
GET /api/inventory/items/?ordering=-price
GET /api/inventory/items/?ordering=name
GET /api/inventory/items/?ordering=-quantity
```

---

## Inventory Change Tracking

The system logs stock quantity changes.

Endpoint:

```
GET /api/inventory/history/
```

Returns:

- Old quantity
- New quantity
- User who modified stock
- Timestamp

---

## Permissions

- Authentication required for inventory operations
- Users can only manage their own inventory
- Ownership enforcement is implemented

---

## Pagination

Default page size:

```
10 items per page
```

Example:

```
GET /api/inventory/items/?page=2
```

---

## Deployment

Recommended hosting:

- PythonAnywhere
- Use production settings:
  - DEBUG = False
  - Secure JWT configuration

---

## Error Handling

Common HTTP Responses:

| Status | Meaning      |
| ------ | ------------ |
| 200    | Success      |
| 201    | Created      |
| 204    | Deleted      |
| 400    | Bad request  |
| 401    | Unauthorized |
| 403    | Forbidden    |
| 404    | Not found    |

---

## Project Features Summary

User authentication with JWT
CRUD operations
Inventory tracking system
Filtering, searching, sorting
Pagination
Ownership permissions
Change history logging

---

## Future Improvements (Optional)

- Low stock notification system
- Analytics dashboard
- Email notification integration
- Soft delete system
- Audit trail enhancement

---
