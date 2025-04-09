# MCDA550_HotelRes_Django
A Django REST Framework API for managing hotel listings.

**GitHub Repository:** [Fearlouise/MCDA550_HotelRes_Django](https://github.com/Fearlouise/MCDA550_HotelRes_Django)

This project was developed as part of **MCDA5550**, demonstrating how to build a RESTful API using **Django**, **SQLite**, and **Postman** for testing.

---

# How to Run the API Locally

1. ## Ensure you have Python installed 
   - Check with: `python --version`  
   - If not installed, download it from [https://www.python.org](https://www.python.org)

2. ## Clone this repository:
   ```bash
   git clone https://github.com/Fearlouise/MCDA550_HotelRes_Django.git
   cd MCDA550_HotelRes_Django

3. ## Create and activate a virtual environment:
    ```bash
    python -m venv venv

    #Activate the environment:
    #On macOS/Linux:
    source venv/bin/activate

    #On Windows:
    venv\Scripts\activate

4. ## Install Dependencies:
    ```bash
    pip install -r requirements.txt

5. ## Run migrations to create the database:
    ```bash
    python manage.py makemigrations
    python manage.py migrate

6.  ## Start the Django development server:
    ```bash
    python manage.py runserver

7. ## Open http://localhost:8000/api/hotels/ to access the API.

8. ## Testing Options:
    1. **Option 1: Browser**
        - Open http://localhost:8000/api/hotels/ in your browser to:
            - View hotel data (GET)
            - Use built-in POST form to add new hotels in JSON format:
                ```bash
                {
                    "hotel_name": "Hilton Garden Inn",
                    "street_number": "123",
                    "street_name": "Main St",
                    "city": "New York",
                    "province": "NY",
                    "country": "USA",
                    "postal_code": "10001",
                    "price_per_night": 150.00,
                    "available": true
                  }

    2. **Option 2: Postman**
        - Use GET to retrieve all hotels
        - Use POST to send hotel in JSON format (as shown above)
        - View and test API responses manually

9. ## Closing the Django development server:
    - To shut down the Django server, press:
    ```bash
    CTRL + C #In the terminal where it's running

10. ## Future Improvements:
    - Add PUT & DELETE functionality
    - Add a reservation system with customers and bookings
    - Implement authentication and role-based permissions
    - Deploy the API online