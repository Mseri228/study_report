from fastapi import FastAPI
from db_report import get_hours_per_topic

app = FastAPI()

@app.get("/hours-per-topic")
def hours_per_topic():
    rows = get_hours_per_topic()
    return [{"topic": t, "hours": float(h)} for t, h in rows]