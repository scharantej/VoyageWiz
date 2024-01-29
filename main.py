
# Import necessary modules
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask app
app = Flask(__name__)

# Set up the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///airline.db'
db = SQLAlchemy(app)

# Define the User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

# Define the Ticket model
class Ticket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    origin = db.Column(db.String(80), nullable=False)
    destination = db.Column(db.String(80), nullable=False)
    travel_date = db.Column(db.Date, nullable=False)
    return_date = db.Column(db.Date, nullable=True)
    passenger_count = db.Column(db.Integer, nullable=False)
    flight_class = db.Column(db.String(80), nullable=False)

# Define the Discount model
class Discount(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    discount_code = db.Column(db.String(20), unique=True, nullable=False)
    discount_type = db.Column(db.String(20), nullable=False)
    discount_amount = db.Column(db.Float, nullable=False)
    expiration_date = db.Column(db.Date, nullable=False)

# Create the database tables
db.create_all()

# Define the home page route
@app.route('/')
def index():
    return render_template('index.html')

# Define the registration route
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Get the form data
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        # Validate the form data
        if not name or not email or not password or not confirm_password:
            return render_template('register.html', error='All fields are required.')
        elif password != confirm_password:
            return render_template('register.html', error='Passwords do not match.')
        elif User.query.filter_by(email=email).first():
            return render_template('register.html', error='Email already exists.')

        # Create a new user
        new_user = User(name=name, email=email, password=password)

        # Add the new user to the database
        db.session.add(new_user)
        db.session.commit()

        # Redirect to the home page
        return redirect(url_for('index'))

    # Display the registration form
    return render_template('register.html')

# Define the book ticket route
@app.route('/book_ticket', methods=['GET', 'POST'])
def book_ticket():
    if request.method == 'POST':
        # Get the form data
        origin = request.form['origin']
        destination = request.form['destination']
        travel_date = request.form['travel_date']
        return_date = request.form['return_date']
        passenger_count = request.form['passenger_count']
        flight_class = request.form['flight_class']

        # Validate the form data
        if not origin or not destination or not travel_date:
            return render_template('book_ticket.html', error='All fields are required.')
        elif passenger_count < 1:
            return render_template('book_ticket.html', error='Passenger count must be at least 1.')

        # Create a new ticket
        new_ticket = Ticket(origin=origin, destination=destination, travel_date=travel_date, return_date=return_date, passenger_count=passenger_count, flight_class=flight_class)

        # Add the new ticket to the database
        db.session.add(new_ticket)
        db.session.commit()

        # Redirect to the home page
        return redirect(url_for('index'))

    # Display the book ticket form
    return render_template('book_ticket.html')

# Define the create discount route
@app.route('/create_discount', methods=['GET', 'POST'])
def create_discount():
    if request.method == 'POST':
        # Get the form data
        discount_code = request.form['discount_code']
        discount_type = request.form['discount_type']
        discount_amount = request.form['discount_amount']
        expiration_date = request.form['expiration_date']

        # Validate the form data
        if not discount_code or not discount_type or not discount_amount or not expiration_date:
            return render_template('create_discount.html', error='All fields are required.')

        # Create a new discount
        new_discount = Discount(discount_code=discount_code, discount_type=discount_type, discount_amount=discount_amount, expiration_date=expiration_date)

        # Add the new discount to the database
        db.session.add(new_discount)
        db.session.commit()

        # Redirect to the home page
        return redirect(url_for('index'))

    # Display the create discount form
    return render_template('create_discount.html')

# Define the discounts route
@app.route('/discounts')
def discounts():
    # Get all the active discounts
    discounts = Discount.query.filter(Discount.expiration_date >= datetime.now()).all()

    # Display the discounts
    return render_template('discounts.html', discounts=discounts)

# Define the remove discount route
@app.route('/remove_discount/<discount_code>', methods=['POST'])
def remove_discount(discount_code):
    # Get the discount to be removed
    discount = Discount.query.filter_by(discount_code=discount_code).first()

    # Remove the discount from the database
    db.session.delete(discount)
    db.session.commit()

    # Redirect to the discounts page
    return redirect(url_for('discounts'))

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
