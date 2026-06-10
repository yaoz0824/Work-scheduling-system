from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models.work_record import WorkRecord
from app.models.leave_record import LeaveRecord
import datetime

record_bp = Blueprint('record', __name__, url_prefix='/records')

@record_bp.route('/')
def list_records():
    """顯示所有工時與請假紀錄列表"""
    now = datetime.datetime.now()
    year = request.args.get('year', now.year, type=int)
    month = request.args.get('month', now.month, type=int)
    
    work_records = WorkRecord.get_month_records(year, month)
    leave_records = LeaveRecord.get_month_records(year, month)
    
    records = []
    for w in work_records:
        w_dict = dict(w)
        w_dict['type'] = 'work'
        w_dict['date'] = w_dict['work_date']
        records.append(w_dict)
        
    for l in leave_records:
        l_dict = dict(l)
        l_dict['type'] = 'leave'
        l_dict['date'] = l_dict['leave_date']
        records.append(l_dict)
        
    records.sort(key=lambda x: x['date'], reverse=True)
    
    return render_template('records.html', records=records, year=year, month=month)

@record_bp.route('/add', methods=['POST'])
def add_record():
    """手動新增一筆紀錄 (未完整實作)"""
    flash("手動新增功能即將推出", "info")
    return redirect(url_for('record.list_records'))

@record_bp.route('/<int:id>/delete', methods=['POST'])
def delete_record(id):
    """刪除指定的工作紀錄"""
    from app.models.db import get_db_connection
    conn = get_db_connection()
    conn.execute('DELETE FROM work_records WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    flash("紀錄已刪除", "success")
    return redirect(url_for('record.list_records'))

@record_bp.route('/export/<int:year>/<int:month>')
def export_records(year, month):
    """匯出指定月份的紀錄為 CSV"""
    flash("報表匯出功能即將推出", "info")
    return redirect(url_for('record.list_records'))
