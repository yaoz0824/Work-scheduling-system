from app.models.db import get_db_connection

class JobSetting:
    @staticmethod
    def get_default():
        conn = get_db_connection()
        record = conn.execute('SELECT * FROM job_settings WHERE is_active = 1 LIMIT 1').fetchone()
        conn.close()
        return dict(record) if record else None

    @staticmethod
    def update_rate(id, hourly_rate):
        conn = get_db_connection()
        conn.execute('UPDATE job_settings SET hourly_rate = ? WHERE id = ?', (hourly_rate, id))
        conn.commit()
        conn.close()
