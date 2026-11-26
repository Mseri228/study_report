-- 1. total hours
SELECT ROUND(SUM(minutes) / 60.0, 1) AS total_hours FROM study_log;

-- 2. hours per topic
SELECT topic, ROUND(SUM(minutes) / 60.0, 1) AS hours
FROM study_log
GROUP BY topic
ORDER BY hours DESC;

-- 3. hours per session
SELECT session, ROUND(SUM(minutes) / 60.0, 1) AS hours
FROM study_log
GROUP BY session
ORDER BY hours DESC;

-- 4. hours per day
SELECT log_date, ROUND(SUM(minutes) / 60.0, 1) AS hours
FROM study_log
GROUP BY log_date
ORDER BY log_date;

-- 5. average block length
SELECT ROUND(AVG(minutes), 1) AS avg_minutes FROM study_log;