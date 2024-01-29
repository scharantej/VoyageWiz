## Flask Application Design: Airline Reservation System

## HTML Files

### 1. `index.html`
- **Purpose**: Welcome page with navigation options to Register, Book Ticket, Create Discount, and View All Discounts.

### 2. `register.html`
- **Purpose**: Registration form for new users.
- **Content**: Fields for name, email, password, and confirmation password.
- **Button**: Submit button for user registration.

### 3. `book_ticket.html`
- **Purpose**: Form for booking a ticket.
- **Content**: Fields for origin, destination, travel date, return date, passenger count, and flight class.
- **Button**: Submit button for booking the ticket.

### 4. `create_discount.html`
- **Purpose**: Form for creating a custom discount.
- **Content**: Fields for discount code, percentage or amount of discount, and expiration date.
- **Button**: Submit button to create the discount.

### 5. `discounts.html`
- **Purpose**: Displays all the active discounts available.
- **Content**: Table with columns for discount code, percentage or amount, expiration date, and a button to remove the discount.

## Routes

### 1. `/register`
- **Method**: POST
- **Purpose**: Handle user registration.
- **Function**: Validates the registration form and stores the user information in a database.

### 2. `/book_ticket`
- **Method**: POST
- **Purpose**: Book a ticket for a user.
- **Function**: Validates the ticket booking form and stores the ticket information in a database.

### 3. `/create_discount`
- **Method**: POST
- **Purpose**: Create a custom discount.
- **Function**: Validates the discount creation form and stores the discount information in a database.

### 4. `/discounts`
- **Method**: GET
- **Purpose**: Retrieve all the active discounts.
- **Function**: Queries the database and returns a list of all active discounts.

### 5. `/remove_discount/<discount_code>`
- **Method**: POST
- **Purpose**: Remove a custom discount.
- **Function**: Removes the specified discount from the database.

## Additional Notes

- Implement appropriate data validation on both server and client sides.
- Design the layout and styling of the application using CSS and JavaScript.
- Ensure that routes like `/register`, `/book_ticket`, and `/create_discount` redirect to appropriate success or error pages.
- Set up a proper database connection and perform CRUD operations using Flask-SQLAlchemy or a similar library.