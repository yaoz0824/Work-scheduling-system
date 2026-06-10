from app.models.db import get_db_connection

class LeaveRecord:
    @staticmethod
    def create(leave_date, leave_type, hours=8.0, note=""):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO leave_records (leave_date, leave_type, hours, note)
            VALUES (?, ?, ?, ?)
        ''', (leave_date, leave_type, hours, note))
        record_id = cursor.lastrowid
        conn.commit()
        conn.close()
        return record_id

    @staticmethod
    def get_month_records(year, month):
        conn = get_db_connection()
        like_pattern = f"{year}-{month:02d}-%"
        records = conn.execute('SELECT * FROM leave_records WHERE leave_date LIKE ?', (like_pattern,)).fetchall()
        conn.close()
        return [dict(r) for r in records]
