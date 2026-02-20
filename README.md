# AI 應用基礎班 — 線上自學平台

為台灣疾病管制署（CDC）同仁設計的互動式 AI 應用自學課程，從基礎概念到實務應用，幫助學員掌握生成式 AI 工具，提升工作效率。

## 課程模組

| 模組 | 主題 | 說明 |
|------|------|------|
| 模組 0 | 學前準備 | 環境設定與學習指引 |
| 模組 1 | 認識生成式 AI | AI 基本概念與原理 |
| 模組 2 | Prompt 四要素 | 撰寫有效 Prompt 的方法 |
| 模組 3 | 文書處理應用 | AI 輔助日常文書工作 |
| 模組 4 | 資料整理應用 | AI 輔助資料分析與整理 |
| 模組 5 | 進階技巧 | 多輪對話、迭代優化、常見錯誤與避坑指南 |

## 功能特色

- **教學影片** — 每個模組嵌入對應 YouTube 教學影片，支援全螢幕播放
- **投影片下載** — 每部影片下方提供 PDF 投影片下載連結
- **互動式測驗** — 單選、多選、拖曳排序、填空等多種題型
- **Prompt 食譜** — 20+ 可直接複製使用的 Prompt 範本
- **學習進度追蹤** — 自動記錄各模組完成狀態（LocalStorage）
- **學習地圖** — 視覺化呈現整體學習進度
- **結業證書** — 完成所有模組且期末測驗達 80% 即可取得
- **響應式設計** — 支援桌機、平板、手機瀏覽（RWD）

## 技術架構

純靜態網站，零依賴、無需建置步驟。

```
├── index.html              # 首頁（學習地圖、模組總覽）
├── certificate.html        # 結業證書頁面
├── modules/
│   └── module0-5.html      # 6 個課程模組（含嵌入式 YouTube 影片）
├── recipes/
│   └── prompt-recipes.html # Prompt 食譜
├── resources/
│   └── links.html          # 延伸學習資源
├── css/
│   └── style.css           # 全站樣式（CSS Custom Properties、RWD 斷點）
├── js/
│   └── main.js             # 全站互動邏輯
├── slides/
│   ├── shared.py           # 品牌常數與共用投影片函數
│   ├── generate_module0-5.py  # 6 個模組投影片腳本（python-pptx）
│   ├── generate_all.py     # 批次執行入口
│   └── output/
│       ├── *.pptx          # 6 份 PowerPoint 投影片（115 張）
│       └── pdf/            # PDF 版投影片（供下載）
└── docs/
    └── 影片腳本.md          # 教學影片腳本
```

## 快速開始

用任意靜態伺服器啟動：

```bash
# Python
python -m http.server 8000

# Node.js
npx serve .
```

然後開啟 http://localhost:8000 即可。也可以直接在瀏覽器開啟 `index.html`。

### 重新生成投影片（選用）

需要先安裝 [uv](https://docs.astral.sh/uv/)：

```bash
cd slides
uv run python generate_all.py
# 輸出至 slides/output/（6 份 .pptx，共 115 張）
```

## License

MIT
