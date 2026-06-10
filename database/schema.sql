CREATE TABLE IF NOT EXISTS job_settings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    job_name TEXT NOT NULL DEFAULT '預設工作',
    hourly_rate REAL NOT NULL DEFAULT 0.0,
    is_active INTEGER NOT NULL DEFAULT 1,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS work_records (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    job_id INTEGER NOT NULL,
    work_date DATE NOT NULL,
    clock_in DATETIME,
    clock_out DATETIME,
    total_hours REAL DEFAULT 0.0,
    overtime_hours REAL DEFAULT 0.0,
    estimated_salary REAL DEFAULT 0.0,
    note TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (job_id) REFERENCES job_settings(id)
);

CREATE TABLE IF NOT EXISTS leave_records (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    leave_date DATE NOT NULL,
    leave_type TEXT NOT NULL,
    hours REAL NOT NULL DEFAULT 8.0,
    note TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- 初始化一筆預設工作設定 (如果需要)
INSERT INTO job_settings (job_name, hourly_rate) 
SELECT '預設工作', 183.0 
WHERE NOT EXISTS (SELECT 1 FROM job_settings);
