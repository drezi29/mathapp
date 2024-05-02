# MathApp

MathApp is a Django-based web application that provides math learning materials for high school. It uses a PostgreSQL database for data storage.

## Local Setup

Follow these steps to set up and run MathApp locally:

### 1. Create a Python Virtual Environment

Create a new virtual environment using Python 3.10:

```bash
python3.10 -m venv venv/
```

### 2. Activate the Virtual Environment

Activate the newly created virtual environment:

```bash
source venv/bin/activate
```

### 3. Install requirements

Upgrade pip to the latest version:

```bash
pip install --upgrade pip
```

Install the required Python packages:

```bash 
pip install -r requirements.txt
```

### 4. Install PostgreSQL

Install and start PostgreSQL version 14 in your operating system.

For Mac:

* Install using Homebrew:

```bash
brew install postgresql@14
```

* Start the PostgreSQL service:

```bash
brew services start postgresql
```

### 5. Create a PostgreSQL Role

Open the PostgreSQL shell:

```bash
psql postgres
```

Then, create a new role named `mathapp` with login privileges and a password of `mathapp`:

```sql
CREATE ROLE mathapp WITH LOGIN PASSWORD 'mathapp';
```

### 6. Apply Django Migrations

Apply the Django migrations to set up your database schema:

```bash
python manage.py migrate
```

### 7. Load Initial Data

Load the initial data into the database:

TODO - Add instructions for loading initial data
### 8. Run the Django Development Server

Start the Django development server:

```bash
python manage.py runserver
```

Now, you should be able to access the MathApp application by navigating to [http://localhost:8000](http://localhost:8000) in your web browser.

## User Registration

To register a new user, navigate to [http://localhost:8000](http://localhost:8000) and follow the registration prompts.

## Admin Access

To access the Django admin interface, you first need to create a superuser account:

```bash
python manage.py createsuperuser
```

Follow the prompts to enter your desired username, email address, and password. After creating the superuser account, you can access the admin interface by navigating to `http://localhost:8000/admin
