from app.models.db import get_db_connection

class WorkRecord:
    @staticmethod
    def create(job_id, work_date, clock_in=None, clock_out=None, total_hours=0.0, overtime_hours=0.0, estimated_salary=0.0, note=""):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO work_records (job_id, work_date, clock_in, clock_out, total_hours, overtime_hours, estimated_salary, note)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (job_id, work_date, clock_in, clock_out, total_hours, overtime_hours, estimated_salary, note))
        record_id = cursor.lastrowid
        conn.commit()
        conn.close()
        return record_id

    @staticmethod
    def get_by_date(work_date):
        conn = get_db_connection()
        record = conn.execute('SELECT * FROM work_records WHERE work_date = ?', (work_date,)).fetchone()
        conn.close()
        return dict(record) if record else None

    @staticmethod
    def update(id, clock_in=None, clock_out=None, total_hours=0.0, overtime_hours=0.0, estimated_salary=0.0, note=""):
        conn = get_db_connection()
        conn.execute('''
            UPDATE work_records 
            SET clock_in = ?, clock_out = ?, total_hours = ?, overtime_hours = ?, estimated_salary = ?, note = ?
            WHERE id = ?
        ''', (clock_in, clock_out, total_hours, overtime_hours, estimated_salary, note, id))
        conn.commit()
        conn.close()

    @staticmethod
    def get_month_records(year, month):
        conn = get_db_connection()
        like_pattern = f"{year}-{month:02d}-%"
        records = conn.execute('SELECT * FROM work_records WHERE work_date LIKE ? ORDER BY work_date ASC', (like_pattern,)).fetchall()
        conn.close()
        return [dict(r) for r in records]
