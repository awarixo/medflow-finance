# Clinic Patient Records Backend (FastAPI)

## Setup
1. Install dependencies:
    ```
    pip install -r requirements.txt
    ```
2. Add `.env` with your PostgreSQL config.

3. Run the application:
    ```
    uvicorn app.main:app --reload
    ```

API will be available at `http://localhost:8000/patients` etc.