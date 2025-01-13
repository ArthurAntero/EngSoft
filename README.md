# EngSoft

The project uses Streamlit to create the graphical interface in Python and integrates with a PostgreSQL database.

## Getting Started

Follow these steps to set up and run the project on a Linux system:

### Prerequisites

- Python 3.x installed
- Docker installed
- Docker Compose installed

### How to run

1. run `python3 -m venv venv`
2. run `source ./venv/bin/activate`
3. run `pip install -r requirements.txt`
4. run `docker-compose up -d`
5. run `streamlit run src/App.py`

## Folder Structure

The project follows the following folder structure:


- The `src/` directory contains the project's source code, including subdirectories for the database, API functions, and Streamlit screens.
- The `db/` directory holds files related to the database, including the `schema.sql` file that defines the database structure.
- The `api/` directory contains API functions, each file corresponding to interactions with a specific database table.
- The `_pages/` directory hosts Streamlit screens, with each file representing a separate screen of the application.
- The `App.py` file in the `src/` directory serves as the main entry point that calls the Streamlit screens.
- The `requirements.txt` file lists Python dependencies.
- The `.env` file is used for configuring environment variables.
- The `docker-compose.yml` file is the Docker Compose configuration for setting up the PostgreSQL database.

This organized structure helps keep the project clean and facilitates maintenance and code expansion.

Notes:

- All screen, function and variable names must follow the snake_case pattern
- Page file names must start with a capital letter