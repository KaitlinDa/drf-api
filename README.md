# Lab 33 - Class 401d24

## Project
Authentication and Production Server

## Author

Kaitlin Davis | February 2024

## About
This project is a rebuild of the "Things API" demo. The primary objective is to create a Django REST Framework (DRF) application from scratch, replacing the `things_project` and `Thing` model with drf_api application and model that includes a foreign key relationship to the user model.

## Features
- **Custom Model**: Implemented a model ensuring a demonstration of DRF's capabilities.
- **User Association**: Included one field in the model that acts as a foreign key to Django's built-in user model, showcasing the handling of relational data in DRF.
- **API Functionality**: The application supports CRUD operations on the custom model via a RESTful API, providing a practical example of how to build and interact with APIs using Django REST Framework.
- **Authentication & Permissions**: Demonstrates the implementation of DRF's authentication and permissions to secure API endpoints, ensuring that only authorized users can perform certain operations.

## User Acceptance Tests
The application includes tests for verifying the correct status codes for the home and about pages and ensuring the appropriate templates are used, including the ancestor template.

## Setup and Installtion
1. **Clone the Repository**
2. **Navigate to the Project Directory**
3. **Create a Virtual Environment**
4. **Activate the Virtual Environment**
5. **Install Dependencies**
6. **Apply Migrations**
7. **Run the Development Server**

## Resources
I used the help of the class demo as well as ChatGPT for this assignment. 