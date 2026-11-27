# Study Report

A small end-to-end reporting project built on my own study log: CSV → PostgreSQL → FastAPI → dashboard → LLM-written summary.

## What it does

1. Cleans the raw study log (pandas) and loads it into a PostgreSQL table (`study_log`, 51 rows).
2. Answers questions with SQL (total hours, hours per topic, per session, per day, average block).
3. Serves the results as JSON through a FastAPI endpoint.
4. Shows hours per topic as a bar chart on a simple dashboard (Chart.js).
5. Sends the SQL results to the Anthropic API, which writes a 3-sentence summary. SQL does the maths; the model only writes the words.

## Stack

Python, pandas, PostgreSQL, psycopg 3, FastAPI, Chart.js, Anthropic API

## Files

| File | Purpose |
|---|---|
| `report.py` | First version: report straight from the CSV |
| `clean_log.csv` | Cleaned study log |
| `load_db.py` | Loads the CSV into the `study_log` table |
| `queries.sql` | The SQL queries |
| `db_report.py` | `get_hours_per_topic()`: reads from the database |
| `api.py` | FastAPI app: `/hours-per-topic` (JSON) and `/` (dashboard) |
| `dashboard.html` | Bar chart page |
| `summary.py` | LLM summary of the study log |

## Run it

Requirements: PostgreSQL running with a database called `study_report`.

```bash
python -m venv venv
source venv/bin/activate
pip install pandas psycopg fastapi[standard] anthropic

python load_db.py          # load the CSV into PostgreSQL
fastapi dev api.py         # dashboard at http://127.0.0.1:8000
```

For the summary, set your API key in the same terminal first:

```bash
export ANTHROPIC_API_KEY="your-key"
python summary.py
```

The key is read from the environment and never stored in the code.