# Run API from localmachine
uvicorn main:app --reload --port 8006

# Run API from Docker
docker compose up --build

# Browser:
http://localhost:8000/
http://localhost:8000/customer

# Run Docs
http://localhost:8000/docs