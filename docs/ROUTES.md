# 路由與頁面設計 (ROUTES)

## 1. 路由總覽表格

| 功能 | HTTP 方法 | URL 路徑 | 對應模板 | 說明 |
| :--- | :--- | :--- | :--- | :--- |
| **首頁面板** | GET | `/` | `templates/index.html` | 顯示今日打卡狀態、快速打卡按鈕、今日預估薪資 |
| **上班打卡** | POST | `/clock-in` | — | 寫入 `clock_in` 時間，然後重導向回首頁 `/` |
| **下班打卡** | POST | `/clock-out` | — | 寫入 `clock_out`，計算總工時與薪資，重導向回 `/` |
| **月曆視圖** | GET | `/calendar` | `templates/calendar.html` | 顯示整個月的工時統計、休假與總薪水估算 |
| **紀錄列表** | GET | `/records` | `templates/records.html` | 表格條列式顯示所有的工作與請假紀錄 |
| **新增紀錄** | POST | `/records/add` | — | 從表單接收資料，手動新增工時或請假，重導向至 `/records` |
| **刪除紀錄** | POST | `/records/<id>/delete`| — | 刪除指定的工作紀錄，重導向至 `/records` |
| **設定頁面** | GET | `/settings` | `templates/settings.html` | 顯示並修改目前工作設定（時薪等） |
| **更新設定** | POST | `/settings/update` | — | 接收表單更新 `job_settings`，重導向至 `/settings` |
| **匯出報表** | GET | `/export/<year>/<month>`| — | 將該月紀錄轉為 CSV 檔案下載 |

---

## 2. 每個路由的詳細說明

### `GET /` (首頁)
- **邏輯**：查詢 `WorkRecord` 今天的紀錄。
- **輸出**：如果沒有今日紀錄，顯示「上班打卡」按鈕。如果有上班但沒下班，顯示「下班打卡」按鈕與經過時間。如果已下班，顯示今日總工時與薪資。渲染 `index.html`。

### `POST /clock-in`
- **邏輯**：建立今日的 `WorkRecord`，`clock_in` 設為當前時間。
- **輸出**：`redirect(url_for('main.index'))`

### `POST /clock-out`
- **邏輯**：更新今日 `WorkRecord` 的 `clock_out` 為當前時間。呼叫 `utils` 計算工時與加班費（讀取 `job_settings` 時薪）。更新資料庫。
- **輸出**：`redirect(url_for('main.index'))`

### `GET /calendar`
- **邏輯**：獲取目前的年份與月份（預設為當月，也可吃 GET 參數 `?y=2026&m=6`），撈出該月所有 `work_records` 與 `leave_records`。
- **輸出**：渲染 `calendar.html`。

### `GET /settings` 與 `POST /settings/update`
- **邏輯**：讀取或更新 `job_settings` 表。
- **輸出**：渲染 `settings.html`。更新後閃現成功訊息並重導向。

---

## 3. Jinja2 模板清單

所有的模板都將繼承自 `base.html`，以保持一致的導覽列與版面配置。

- `base.html`：包含 HTML5 骨架、匯入 `style.css`、全站導覽列 (Navbar) 與頁尾 (Footer)。
- `index.html`：打卡專用的大按鈕面板。
- `calendar.html`：以格子狀顯示當月每天的狀態。
- `records.html`：資料表 (Table) 呈現詳細紀錄。
- `settings.html`：設定時薪的表單。

（預計實作在 `app/templates/` 內）
