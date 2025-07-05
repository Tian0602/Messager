# Simple FastAPI Project - Messager

Messager is a lightweight messaging API built with FastAPI and SQLAlchemy. It allows users to send, receive, read and delete messages.

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/messager.git
cd messager
```

### 2. Create and activate a virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

From the root directory:

```bash
uvicorn src.app.main:app --reload
```

The API will be available at [http://127.0.0.1:8000](http://127.0.0.1:8000)

### 5. Test the API

Visit the interactive Swagger UI at:

[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## Project Structure

```
messager/
├── src/
│   └── app/
│       ├── api/
│       ├── database/
│       ├── models/
│       ├── services/
│       └── main.py
├── requirements.txt
└── README
```
