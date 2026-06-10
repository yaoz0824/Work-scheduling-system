# 紀錄上班時數小程式 - 系統架構設計

## 1. 技術架構說明

本系統為輕量級的網頁應用程式，我們將採用以下技術棧進行開發：

- **後端框架：Python + Flask**
  Flask 是一個輕量、靈活的 Web 框架，非常適合用來快速開發中小型應用。
- **前端與渲染：HTML/CSS/JS + Jinja2**
  為了簡化開發流程與降低維護成本，我們不採用前後端分離，而是透過 Flask 內建的 Jinja2 模板引擎，將資料夾帶入 HTML 直接在伺服器端渲染後回傳給瀏覽器。並會手刻高質感的 CSS (Vanilla CSS) 以確保優雅的視覺體驗。
- **資料庫：SQLite**
  因為資料主要供個人使用（儲存打卡紀錄、設定等），不需要複雜的大型資料庫。SQLite 檔案型資料庫輕巧且不需額外安裝服務器，非常符合需求。可以使用 SQLAlchemy (或純 sqlite3) 進行存取。

### MVC 架構模式對應
- **Model (模型)**：負責定義資料結構（如：`Job`, `WorkRecord`, `LeaveRecord`）並與 SQLite 互動。
- **View (視圖)**：Jinja2 的 HTML 模板，負責畫面的呈現與邏輯判斷（如：如果超時顯示加班圖示）。
- **Controller (控制器)**：Flask 的 Route 函式，負責接收來自瀏覽器的 Request，呼叫 Model 取得/寫入資料，最後將資料傳遞給 View 渲染。

---

## 2. 專案資料夾結構

以下為建議的專案資料夾結構與用途說明：

```text
Work-scheduling-system/
├── app/
│   ├── __init__.py      # Flask 應用程式初始化
│   ├── models.py        # 資料庫模型定義 (SQLite / SQLAlchemy)
│   ├── routes.py        # 所有的 Controller (網址路由與商業邏輯)
│   ├── utils.py         # 共用函式 (如：加班費計算邏輯、時數轉換)
│   ├── static/          # 靜態資源 (CSS, JS, 圖片)
│   │   ├── css/
│   │   │   └── style.css # 全域樣式 (定義色彩計畫、動畫等)
│   │   └── js/
│   │       └── main.js  # 前端互動邏輯 (如：圖表渲染、日期選擇)
│   └── templates/       # HTML (Jinja2) 模板
│       ├── base.html    # 共用版型 (包含導覽列、頁尾)
│       ├── index.html   # 首頁 (打卡、當日狀態)
│       ├── calendar.html # 月曆視圖與統計
│       ├── records.html # 歷史工時紀錄列表
│       └── settings.html # 工作設定 (時薪、加班費規則)
├── instance/
│   └── database.db      # SQLite 資料庫檔案 (運行時產生，不加入版控)
├── docs/                # 文件資料夾 (PRD, 架構圖等)
├── .env                 # 環境變數設定檔
├── requirements.txt     # Python 依賴套件清單
└── run.py               # 程式進入點 (啟動 Flask Server)
```

---

## 3. 元件關係圖

### 基本請求與回應流程
```mermaid
graph LR
    Browser[瀏覽器 (使用者)] -- "1. HTTP Request (GET / POST)" --> Route[Flask Route (Controller)]
    Route -- "2. 查詢/修改" --> Model[Model (資料模型)]
    Model -- "3. 讀寫" --> SQLite[(SQLite 資料庫)]
    SQLite -- "4. 回傳資料" --> Model
    Model -- "5. 傳遞物件" --> Route
    Route -- "6. 渲染資料" --> Template[Jinja2 Template (View)]
    Template -- "7. 產生 HTML" --> Route
    Route -- "8. HTTP Response (HTML)" --> Browser
```

---

## 4. 關鍵設計決策

1. **伺服器端渲染 (SSR)**
   - **原因**：使用 Jinja2 渲染 HTML，而非 React/Vue 加上 REST API。因為此專案重點在於快速實作核心功能，單一伺服器渲染架構可免去處理 CORS、複雜的狀態管理與前端路由，能最快產出 MVP。
2. **共用工具模組 (`utils.py`)**
   - **原因**：工時與薪資計算（包含勞基法加班費率、不同假別的扣薪比例）邏輯較為複雜且可能頻繁調整。將這些純邏輯抽離至 `utils.py`，不要混在 Route 裡，有助於未來撰寫單元測試以確保算出來的薪水絕對精準。
3. **Vanilla CSS 打造質感介面**
   - **原因**：不依賴龐大的 UI 框架（如 Bootstrap 或 Tailwind），而是自己維護 `style.css`。這能讓我們更自由地使用現代 Web Design 技巧（例如：Glassmorphism、微動畫、動態漸層背景），給使用者「Wow」的優質體驗。
4. **預防浮點數誤差**
   - **原因**：在計算金錢（薪水）與時數時，應避免常見的浮點數誤差。設計時薪水計算應在最後一步才進行四捨五入，或是採用精確的 Decimal 型態進行處理。
