# Photography Website

## Installation Instructions

Follow these steps to set up the project locally:

1. **Clone the repository**
   
   If you have not already, download or clone the project to your local machine.
   
   ```sh
   git clone <repository-url>
   cd photography_website
   ```

2. **Set up a virtual environment (recommended for Python projects)**
   
   ```sh
   python3 -m venv venv
   # Activate the virtual environment:
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

   *Ensure the virtual environment is activated before proceeding to the next steps.*

3. **Install dependencies**
   
   ```sh
   pip install -r requirements.txt
   ```

   If the `requirements.txt` file does not exist, you can generate it by running:

   ```sh
   pip freeze > requirements.txt
   ```

   Alternatively, you can manually install the required Python packages for this project:

   This project requires the following Python packages:
   - `Django` (the main web framework)
   - `Pillow` (for image handling with Django's ImageField)

   Install them using:

   ```sh
   pip install django pillow
   ```

4. **Apply migrations**
   
   Before running the server, apply Django's database migrations:
   
   ```sh
   python3 manage.py makemigrations
   python3 manage.py migrate
   ```

5. **Create a superuser (optional, for admin access)**
   
   ```sh
   python3 manage.py createsuperuser
   ```

6. **Run the development server**
   
   ```sh
   python3 manage.py runserver
   ```

7. **Access the website**
   
   Open your browser and go to `http://127.0.0.1:8000/` (or the address shown in the terminal).
   
   To access the Django admin, go to `http://127.0.0.1:8000/admin/`.

---

## Notes
- Make sure you have Python 3.7 or higher installed.
- For additional configuration or troubleshooting, refer to the Django documentation: https://docs.djangoproject.com/
- You may need to adjust settings in `settings.py` for database, static files, or other project-specific configurations.
