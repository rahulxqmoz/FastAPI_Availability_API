# FastAPI Availability API - README

## Installation Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/rahulxqmoz/FastAPI_Availability_API-.git
cd fastapi-availability-api
```

### 2. Set Up Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # On Windows use: venv\\Scripts\\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

Create a `.env` file in the project root with the following content:

```
DATABASE_URL=postgresql://<username>:<password>@localhost/availability_db
```

*Replace `<username>` and `<password>` with your PostgreSQL credentials.*

### 5. Configure Alembic

Edit the `alembic.ini` file and set the following line:

```
sqlalchemy.url = postgresql://<username>:<password>@localhost/availability_db
```

### 6. Run Alembic Migrations

Create a new migration revision:

```bash
alembic revision --autogenerate -m "Initial migration"
```

Apply the migrations:

```bash
alembic upgrade head
```

### 7. Initialize Database

Use the following SQL commands to populate initial data:

```sql
INSERT INTO users (id, name, timezone) VALUES(1, 'Alice', 'UTC'),(2, 'Bob', 'UTC'),(3, 'Charlie', 'UTC');

INSERT INTO availabilities (id, user_id, date, start_time, end_time, is_specific) VALUES(1, 1, '2025-02-14', '09:00:00', '12:00:00', 1),(2, 2, '2025-02-14', '10:00:00', '13:00:00', 1),(3, 3, '2025-02-14', '11:00:00', '14:00:00', 1);

INSERT INTO events (id, user_id, date, start_time, end_time) VALUES(1, 1, '2025-02-14', '10:30:00', '11:30:00'),(2, 2, '2025-02-14', '11:00:00', '12:00:00');
```

### 8. Start the FastAPI Server

```bash
uvicorn app.main:app --reload
```

---


## Postman Collection

Include the provided Postman collection JSON file with sample input data. The sample request body is:

```json
{
  "user_ids": [1, 2, 3],
  "start_date": "2025-02-14",
  "end_date": "2025-02-14",
  "timezone": "UTC"
}
```





