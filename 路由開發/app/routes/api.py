# 儲存路徑: 路由開發/app/routes/api.py
from flask import jsonify, request, session
from app.routes import api_bp
from app.models.shift import Shift

@api_bp.route('/shifts', methods=['GET'])
def get_shifts_api():
    """
    提供給 FullCalendar.js 的非同步排班資料 API
    讀取查詢參數 start 與 end，回傳該日期區間內的所有排班事件
    若是員工角色，將自動過濾 is_draft=True 的草稿班表
    :return: JSON 格式之班表陣列
    """
    pass

@api_bp.route('/shift/update', methods=['POST'])
def update_shift_api():
    """
    店長在 FullCalendar 上進行拖拉修改或人員替換時的 AJAX API
    接收 JSON 格式之 shift_id、start_time、end_time 與 staff_id。
    後端在寫入前將自動觸發 `check_scheduling_conflict` 進行動態合規與缺工預檢
    - 若完全合規：寫入資料庫，回傳 status: 'success'
    - 若違反限制（例如超過工時）：不寫入資料庫，回傳 status: 'warning/error' 及具體原因，讓前端日曆顯示高亮警告
    :return: 預檢結果之 JSON 回應
    """
    pass
