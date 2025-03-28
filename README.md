
# VaultCheck API

VaultCheck is a simple password strength checker API built using FastAPI. It evaluates password security based on length, character variety, and common password patterns.

## Features
- Checks password strength based on length and complexity.
- Identifies weak passwords (e.g., common patterns like "password", "1234", "admin").
- Returns a hashed version of the password using bcrypt.
- Provides a simple API endpoint for integration into other applications.

## Installation

### Clone the Repository
```bash
git clone https://github.com/obasan12/VaultCheck-API.git
cd VaultCheck-API
```

### Install Dependencies
Create a virtual environment (recommended) and install dependencies:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
pip install -r requirements.txt
```

## Running the API

Start the FastAPI server using Uvicorn:
```bash
uvicorn main:app --host 127.0.0.1 --port 8000 --reload
```
The API will be accessible at: `http://127.0.0.1:8000`

## API Endpoints

### Check Password Strength
- **Endpoint:** `POST /check_password/`
- **Request Body:**
```json
{
  "password": "YourPasswordHere"
}
```
- **Response:**
```json
{
  "password": "YourPasswordHere",
  "strength": "Strong - Good to go!",
  "hashed": "$2b$12$..."
}
```

## Deployment
To deploy, use services like:
- **Docker**: Build and run as a container.
- **Cloud Providers**: AWS, Heroku, DigitalOcean, etc.
- **Reverse Proxy**: Use Nginx for production setups.

## Contributing
Feel free to fork, submit issues, or contribute to the project.

## License
This project is licensed under the MIT License.

## Author
Developed by [obasan12](https://github.com/obasan12).

