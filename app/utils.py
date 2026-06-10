from datetime import datetime

def calculate_hours_and_salary(clock_in_str, clock_out_str, hourly_rate):
    """
    計算工時與預估薪水
    回傳 (total_hours, overtime_hours, estimated_salary)
    """
    if not clock_in_str or not clock_out_str:
        return 0.0, 0.0, 0.0
        
    # SQLite DATETIME format is usually "YYYY-MM-DD HH:MM:SS" or ISO 8601 "YYYY-MM-DDTHH:MM:SS"
    # We will unify to use "YYYY-MM-DD HH:MM:SS"
    fmt = "%Y-%m-%d %H:%M:%S"
    
    # 處理可能帶有 'T' 的格式或是小數點的秒數
    clock_in_str = clock_in_str.replace('T', ' ').split('.')[0]
    clock_out_str = clock_out_str.replace('T', ' ').split('.')[0]
    
    try:
        t_in = datetime.strptime(clock_in_str, fmt)
        t_out = datetime.strptime(clock_out_str, fmt)
    except ValueError as e:
        print("Date parse error:", e)
        return 0.0, 0.0, 0.0
        
    diff = t_out - t_in
    duration_hours = diff.total_seconds() / 3600.0
    
    if duration_hours <= 0:
        return 0.0, 0.0, 0.0
        
    # 簡單的扣除休息時間邏輯：超過 5 小時扣 1 小時休息時間
    if duration_hours >= 5.0:
        working_hours = duration_hours - 1.0
    else:
        working_hours = duration_hours
        
    if working_hours > 8.0:
        regular_hours = 8.0
        overtime_hours = working_hours - 8.0
    else:
        regular_hours = working_hours
        overtime_hours = 0.0
        
    # 勞基法加班費：前 2 小時 1.34 倍，後 2 小時以上 1.67 倍
    ot1 = min(2.0, overtime_hours)
    ot2 = max(0.0, overtime_hours - 2.0)
    
    salary = (regular_hours * hourly_rate) + (ot1 * hourly_rate * 1.34) + (ot2 * hourly_rate * 1.67)
    
    return round(working_hours, 2), round(overtime_hours, 2), round(salary)

def get_current_time_str():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def get_current_date_str():
    return datetime.now().strftime("%Y-%m-%d")
