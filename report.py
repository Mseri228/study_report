import pandas as pd 
df = pd.read_csv("study_log_v2.csv")
def clean_log(df):
    df = df.copy()
    df["minutes"] = pd.to_numeric(df["minutes"], errors="coerce")
    bad = df["minutes"].isna() | (df["minutes"] < 1) | (df["minutes"] > 180) | (df["minutes"] % 1 != 0)
    rejected = df[bad]
    clean = df[~bad].copy()
    clean["topic"] = clean["topic"].str.strip().str.title().fillna("Unknown")
    clean = clean.drop_duplicates()
    return clean, rejected
clean, rejected = clean_log(df)
total_hours = clean["minutes"].sum() / 60
by_topic = clean.groupby("topic")["minutes"].sum().sort_values(ascending=False) / 60
by_session = clean.groupby("session")["minutes"].sum().sort_values(ascending=False) / 60
by_date = clean.groupby("date")["minutes"].sum() / 60
avg_minutes = clean["minutes"].mean().round(1)
def tests():
    assert len(clean) == 51, "rows amount is incorrect"
    assert len(rejected) == 3, "amount of incorrect rows is incorrect"
    assert clean["minutes"].between(1,180).all(), "every minutes value is within the limits"
    assert not clean.duplicated().any(), "Duplicates are still present"
    assert abs(total_hours - by_topic.sum()) < 0.001, "topic hours don't add up to total"
tests()
    

with open("report.txt", "w") as f:
    f.write("STUDY REPORT\n")
    f.write(f"Total hours: {total_hours}\n")
    f.write(f"Study blocks: {len(clean)}\n")
    f.write(f"Average block: {avg_minutes} min\n")
    f.write(f"Rejected rows: {len(rejected)}\n\n")
    f.write("Hours per topic\n")
    f.write(by_topic.to_string() + "\n\n")
    f.write("Hours per session\n")
    f.write(by_session.to_string() + "\n\n")
    f.write("Hours per day\n")
    f.write(by_date.to_string() + "\n")
clean ["minutes"] = clean["minutes"].astype(int)
clean.to_csv("clean_log.csv", index=False)
