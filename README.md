# Inventory Management API

## Overview

The **Inventory Management API** is a backend system built using Django and Django REST Framework.

The system allows users to:

* Manage inventory items
* Track stock levels
* Authenticate using JWT
* Filter, search, and sort inventory data
* Track inventory change history

**Live API URL**

```
https://danamaz.pythonanywhere.com
```

---

# Technology Stack

* Backend Framework: Django
* API Toolkit: Django REST Framework
* Authentication: JWT via Django REST Framework SimpleJWT
* Database ORM: Django ORM
* Filtering: django-filter

---

# Authentication

The API uses **JSON Web Token (JWT)** authentication.

## Obtain Token

```
POST /api/token/
```

Full endpoint:

```
POST https://danamaz.pythonanywhere.com/api/token/
```

### Request Body

```json
{
  "username": "string",
  "password": "string"
}
```

### Response

```json
{
  "access": "jwt_access_token",
  "refresh": "jwt_refresh_token"
}
```

---

## Refresh Token

```
POST https://danamaz.pythonanywhere.com/api/token/refresh/
```

Request:

```json
{
  "refresh": "refresh_token"
}
```

---

## Using Token

Add request header:

```
Authorization: Bearer YOUR_ACCESS_TOKEN
```

---

# User Management

## Register User

```
POST https://danamaz.pythonanywhere.com/api/users/
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

## User Endpoints

| Method | Endpoint         | Description       |
| ------ | ---------------- | ----------------- |
| GET    | /api/users/      | Get own user data |
| POST   | /api/users/      | Register user     |
| GET    | /api/users/{id}/ | Retrieve user     |
| PUT    | /api/users/{id}/ | Update user       |
| DELETE | /api/users/{id}/ | Delete user       |

Users can only manage their own account.

---

# Inventory Item Management

Inventory items are associated with their owners.

## Inventory Item Fields

* Name
* Description
* Quantity
* Price
* Category
* Date Added
* Last Updated

---

## Create Item

```
POST https://danamaz.pythonanywhere.com/api/inventory/items/
```

---

## Get Items

```
GET https://danamaz.pythonanywhere.com/api/inventory/items/
```

Supports:

* Pagination
* Searching
* Sorting
* Filtering

---

## Update Item

```
PATCH https://danamaz.pythonanywhere.com/api/inventory/items/{id}/
```

Example:

```json
{
  "quantity": 20
}
```

---

## Delete Item

```
DELETE https://danamaz.pythonanywhere.com/api/inventory/items/{id}/
```

---

# Filtering System

## Category Filter

```
GET https://danamaz.pythonanywhere.com/api/inventory/items/?category=Electronics
```

Case insensitive version:

```
GET https://danamaz.pythonanywhere.com/api/inventory/items/?category__iexact=Electronics
```

---

## Price Range Filter

```
GET https://danamaz.pythonanywhere.com/api/inventory/items/?price__gte=100&price__lte=500
```

---

## Low Stock Filter

```
GET https://danamaz.pythonanywhere.com/api/inventory/items/?quantity__lte=10
```

---

# Searching

```
GET https://danamaz.pythonanywhere.com/api/inventory/items/?search=laptop
GET https://danamaz.pythonanywhere.com/api/inventory/items/?search=electronics
```

Searches item name or category.

---

# Sorting (Ordering)

Use the `ordering` parameter.

Examples:

```
GET https://danamaz.pythonanywhere.com/api/inventory/items/?ordering=price
GET https://danamaz.pythonanywhere.com/api/inventory/items/?ordering=-price
GET https://danamaz.pythonanywhere.com/api/inventory/items/?ordering=name
GET https://danamaz.pythonanywhere.com/api/inventory/items/?ordering=-quantity
```

---

# Inventory Change Tracking

The system logs stock quantity changes.

Endpoint:

```
GET https://danamaz.pythonanywhere.com/api/inventory/history/
```

Returns:

* Old quantity
* New quantity
* User who modified stock
* Timestamp
* Item name

---

# Permissions

* Authentication required for inventory operations
* Users can only manage their own inventory
* Ownership enforcement is implemented

---

# Pagination

Default page size:

```
10 items per page
```

Example:

```
GET https://danamaz.pythonanywhere.com/api/inventory/items/?page=2
```

---

# Deployment

This project is deployed on **PythonAnywhere**

Production considerations:

* `DEBUG = False`
* `ALLOWED_HOSTS` configured
* Secure JWT authentication
* Environment variables recommended

---

# Error Handling

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

# Project Features Summary

* User authentication with JWT
* CRUD operations
* Inventory tracking system
* Filtering, searching, sorting
* Pagination
* Ownership permissions
* Change history logging

---

# Future Improvements

* Low stock notification system
* Analytics dashboard
* Email notification integration
* Soft delete system
* Audit trail enhancement

---
