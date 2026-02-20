"""generate_module2.py — 模組 2：Prompt 四要素  (22 slides)

Usage:
    cd slides && uv run python generate_module2.py
"""
from shared import (
    new_prs, blank, set_bg, txbox, rect, header_bar, save_pptx,
    cover_slide, objectives_slide, content_slide, table_slide,
    two_col_slide, cta_slide, alert_slide, section_divider,
    rtfc_card_slide, code_slide,
    PRIMARY, SECONDARY, LIGHT_BG, DARK_BG, WHITE, MUTED,
    SUCCESS, WARNING, DANGER, ACCENT, CODE_BG, CODE_FG,
    ROLE_C, TASK_C, FORMAT_C, CONST_C,
    SW, Inches, PP_ALIGN,
)


def build() -> None:
    prs = new_prs()

    # ── 1. Cover ─────────────────────────────────────────────────────────────
    cover_slide(
        prs, "2", "Prompt 四要素",
        "角色・任務・格式・限制 — 撰寫有效 Prompt 的核心",
        "3 分鐘",
    )

    # ── 2. 開場對比（模糊 vs 清楚） ──────────────────────────────────────────
    sl = blank(prs)
    set_bg(sl, DARK_BG)
    rect(sl, Inches(0), Inches(0), Inches(0.22), Inches(7.5), SECONDARY)

    txbox(sl, "同樣的工具，為什麼差這麼多？",
          Inches(0.55), Inches(0.8), Inches(11.5), Inches(0.8),
          size=28, bold=True, color=WHITE)

    # Left (bad)
    rect(sl, Inches(0.55), Inches(1.8), Inches(5.8), Inches(4.0), CODE_BG)
    txbox(sl, "模糊 Prompt",
          Inches(0.55), Inches(1.8), Inches(5.8), Inches(0.6),
          size=16, bold=True, color=MUTED, align=PP_ALIGN.CENTER)
    txbox(sl, "幫我寫登革熱文宣",
          Inches(0.75), Inches(2.5), Inches(5.4), Inches(0.5),
          size=15, color=CODE_FG)
    txbox(sl, "AI 輸出：空洞通用段落，格式不確定，對象不明……",
          Inches(0.75), Inches(3.1), Inches(5.4), Inches(2.3),
          size=14, color=MUTED)

    # Arrow
    txbox(sl, "vs", Inches(6.5), Inches(3.6), Inches(0.5), Inches(0.5),
          size=22, bold=True, color=SECONDARY, align=PP_ALIGN.CENTER)

    # Right (good)
    rect(sl, Inches(7.1), Inches(1.8), Inches(5.8), Inches(4.0), ACCENT)
    txbox(sl, "RTFC 完整 Prompt",
          Inches(7.1), Inches(1.8), Inches(5.8), Inches(0.6),
          size=16, bold=True, color=WHITE, align=PP_ALIGN.CENTER)
    txbox(sl,
          "你是疾管署衛教專家。\n"
          "請撰寫登革熱預防衛教文宣，\n"
          "分三段，民眾易懂，300字以內。",
          Inches(7.3), Inches(2.5), Inches(5.4), Inches(1.5),
          size=14, color=WHITE)
    txbox(sl, "AI 輸出：精準、結構化、符合疾管署風格，直接可用",
          Inches(7.3), Inches(4.1), Inches(5.4), Inches(1.3),
          size=14, bold=True, color=WHITE)

    txbox(sl, "差別就在於 4 個要素。掌握了，效果至少提升 3 倍。",
          Inches(0.55), Inches(6.3), Inches(12.2), Inches(0.6),
          size=18, bold=True, color=SECONDARY, align=PP_ALIGN.CENTER)

    # ── 3. 學習目標 ───────────────────────────────────────────────────────────
    objectives_slide(prs, [
        "R — 設定角色，讓 AI 切換身份與專業度",
        "T — 描述任務，精準到 AI 不會猜錯",
        "F — 指定格式，輸出直接可用",
    ], header="這 3 分鐘結束後，您能做到：")

    # ── 4. 什麼是 Prompt ──────────────────────────────────────────────────────
    sl = blank(prs)
    set_bg(sl, LIGHT_BG)
    header_bar(sl, "什麼是 Prompt？")

    txbox(sl,
          "Prompt（提示詞）= 您輸入給 AI 的指令或問題",
          Inches(0.6), Inches(1.4), Inches(12.0), Inches(0.7),
          size=24, bold=True, color=PRIMARY)
    txbox(sl,
          "Prompt 就像是您給助理的工作指示：\n\n"
          "・指示模糊 → 助理做出不符期望的結果\n"
          "・指示清楚具體 → 更容易得到想要的成果\n\n"
          "Prompt 的品質，直接決定 AI 回應的品質。",
          Inches(0.6), Inches(2.3), Inches(12.0), Inches(3.5),
          size=20, color=PRIMARY)

    rect(sl, Inches(0.6), Inches(6.0), Inches(12.0), Inches(0.7), SECONDARY)
    txbox(sl, "四要素框架：角色（R）・任務（T）・格式（F）・限制（C）",
          Inches(0.6), Inches(6.0), Inches(12.0), Inches(0.7),
          size=18, bold=True, color=WHITE, align=PP_ALIGN.CENTER)

    # ── 5. RTFC 四色總覽卡 ────────────────────────────────────────────────────
    rtfc_card_slide(prs)

    # ── 6. R — Role 角色 ──────────────────────────────────────────────────────
    sl = blank(prs)
    set_bg(sl, LIGHT_BG)
    rect(sl, Inches(0), Inches(0), SW, Inches(1.15), ROLE_C)
    txbox(sl, "R  —  Role  角色",
          Inches(0.4), Inches(0.2), Inches(12.5), Inches(0.75),
          size=26, bold=True, color=WHITE)

    txbox(sl, "告訴 AI 它應該扮演什麼角色",
          Inches(0.6), Inches(1.4), Inches(12.0), Inches(0.6),
          size=22, color=PRIMARY)

    # Prompt example
    rect(sl, Inches(0.6), Inches(2.1), Inches(12.0), Inches(0.75), ROLE_C)
    txbox(sl, "「你是疾管署的衛教專家。」",
          Inches(0.8), Inches(2.15), Inches(11.6), Inches(0.65),
          size=20, bold=True, color=WHITE)

    txbox(sl, "設定角色可以：",
          Inches(0.6), Inches(3.1), Inches(12.0), Inches(0.55),
          size=19, bold=True, color=PRIMARY)
    effects = [
        "讓 AI 採用特定領域的專業知識與詞彙",
        "影響回應的語氣和風格",
        "獲得更符合實際工作需求的內容",
    ]
    for i, e in enumerate(effects):
        txbox(sl, "• " + e,
              Inches(0.9), Inches(3.75) + i * Inches(0.72),
              Inches(11.7), Inches(0.6),
              size=19, color=PRIMARY)

    # ── 7. 角色範例表 ─────────────────────────────────────────────────────────
    table_slide(prs, "疾管署常用角色設定",
        ["角色設定", "適用情境"],
        [
            ["疾管署衛教專家",    "撰寫衛教文宣、民眾溝通"],
            ["公共衛生專業人員",  "疫情分析、防疫策略"],
            ["政府公文撰寫專家",  "正式公文、函文"],
            ["會議記錄專員",     "整理會議紀錄"],
            ["資料分析師",       "統計資料解讀、圖表說明"],
        ],
        col_widths=[Inches(4.0), Inches(8.1)],
    )

    # ── 8. T — Task 任務 ──────────────────────────────────────────────────────
    sl = blank(prs)
    set_bg(sl, LIGHT_BG)
    rect(sl, Inches(0), Inches(0), SW, Inches(1.15), TASK_C)
    txbox(sl, "T  —  Task  任務",
          Inches(0.4), Inches(0.2), Inches(12.5), Inches(0.75),
          size=26, bold=True, color=WHITE)

    txbox(sl, "明確說明您要 AI 做什麼事",
          Inches(0.6), Inches(1.4), Inches(12.0), Inches(0.6),
          size=22, color=PRIMARY)

    rect(sl, Inches(0.6), Inches(2.1), Inches(12.0), Inches(0.75), TASK_C)
    txbox(sl, "「請撰寫一份流感疫苗接種宣導文案。」",
          Inches(0.8), Inches(2.15), Inches(11.6), Inches(0.65),
          size=20, bold=True, color=WHITE)

    txbox(sl, "任務描述的要訣：",
          Inches(0.6), Inches(3.1), Inches(12.0), Inches(0.55),
          size=19, bold=True, color=PRIMARY)
    tips = [
        "使用動詞開頭：撰寫、整理、翻譯、摘要、分析……",
        "具體明確：不要說「幫我做事」，而是說具體要做什麼",
        "說明目的：讓 AI 了解這項任務的用途",
        "提供背景：必要時說明相關情境",
    ]
    for i, t in enumerate(tips):
        txbox(sl, "• " + t,
              Inches(0.9), Inches(3.75) + i * Inches(0.72),
              Inches(11.7), Inches(0.6),
              size=19, color=PRIMARY)

    # ── 9. 疾管署常見任務類型 ─────────────────────────────────────────────────
    sl = blank(prs)
    set_bg(sl, LIGHT_BG)
    header_bar(sl, "疾管署常見任務類型")

    task_types = [
        (TASK_C,   "撰寫",  "公文、衛教文宣、Email"),
        (ACCENT,   "整理",  "會議紀錄、資料彙整"),
        (SUCCESS,  "摘要",  "報告、期刊、週報"),
        (PRIMARY,  "翻譯",  "英文文獻、WHO 報告"),
        (CONST_C,  "分析",  "數據解讀、趨勢說明"),
        (ROLE_C,   "修改",  "潤稿、格式調整"),
    ]
    for i, (clr, action, example) in enumerate(task_types):
        col = i % 3
        row = i // 3
        left = Inches(0.45) + col * Inches(4.25)
        top  = Inches(1.4) + row * Inches(2.5)
        rect(sl, left, top, Inches(4.0), Inches(2.1), clr)
        txbox(sl, action,
              left + Inches(0.2), top + Inches(0.2),
              Inches(3.6), Inches(0.7),
              size=26, bold=True, color=WHITE)
        txbox(sl, example,
              left + Inches(0.2), top + Inches(1.0),
              Inches(3.6), Inches(0.9),
              size=17, color=WHITE)

    # ── 10. F — Format 格式 ───────────────────────────────────────────────────
    sl = blank(prs)
    set_bg(sl, LIGHT_BG)
    rect(sl, Inches(0), Inches(0), SW, Inches(1.15), FORMAT_C)
    txbox(sl, "F  —  Format  格式",
          Inches(0.4), Inches(0.2), Inches(12.5), Inches(0.75),
          size=26, bold=True, color=WHITE)

    txbox(sl, "指定您希望的輸出格式，讓 AI 輸出直接可用",
          Inches(0.6), Inches(1.4), Inches(12.0), Inches(0.6),
          size=22, color=PRIMARY)

    rect(sl, Inches(0.6), Inches(2.1), Inches(12.0), Inches(0.75), FORMAT_C)
    txbox(sl,
          "「請分成三個段落：為什麼打疫苗、誰應優先接種、接種注意事項。」",
          Inches(0.8), Inches(2.15), Inches(11.6), Inches(0.65),
          size=18, bold=True, color=WHITE)

    formats = [
        "條列式：使用編號或項目符號",
        "表格：比較、整理資料時特別有用",
        "段落式：正式文章、報告",
        "公文格式：主旨、說明、辦法",
        "特定結構：如 SWOT、5W1H 等",
    ]
    for i, f in enumerate(formats):
        txbox(sl, "• " + f,
              Inches(0.9), Inches(3.1) + i * Inches(0.72),
              Inches(11.7), Inches(0.6),
              size=19, color=PRIMARY)

    # ── 11. 格式範例表 ────────────────────────────────────────────────────────
    table_slide(prs, "疾管署常用格式對應表",
        ["工作類型", "建議格式"],
        [
            ["公文",    "主旨、說明（條列）、辦法"],
            ["會議紀錄", "會議資訊、出席、討論、決議、待辦"],
            ["衛教單張", "症狀、預防、就醫時機（三段式）"],
            ["週報摘要", "本週重點、數據變化、後續關注"],
            ["資料比較", "表格形式"],
        ],
        col_widths=[Inches(3.0), Inches(9.1)],
    )

    # ── 12. C — Constraint 限制 ───────────────────────────────────────────────
    sl = blank(prs)
    set_bg(sl, LIGHT_BG)
    rect(sl, Inches(0), Inches(0), SW, Inches(1.15), CONST_C)
    txbox(sl, "C  —  Constraint  限制",
          Inches(0.4), Inches(0.2), Inches(12.5), Inches(0.75),
          size=26, bold=True, color=WHITE)

    txbox(sl, "設定邊界條件，控制輸出品質",
          Inches(0.6), Inches(1.4), Inches(12.0), Inches(0.6),
          size=22, color=PRIMARY)

    rect(sl, Inches(0.6), Inches(2.1), Inches(12.0), Inches(0.75), CONST_C)
    txbox(sl, "「使用民眾易懂的語言，字數 250 字以內。」",
          Inches(0.8), Inches(2.15), Inches(11.6), Inches(0.65),
          size=20, bold=True, color=WHITE)

    constraints = [
        "字數限制：「300 字以內」「不超過 500 字」",
        "語氣／風格：「正式」「親切」「專業」「活潑」",
        "目標對象：「給一般民眾」「給醫護人員」「給長者」",
        "排除項目：「不要使用專業術語」「不要列出參考資料」",
        "語言：「使用繁體中文」「避免使用簡體字詞」",
    ]
    for i, c in enumerate(constraints):
        txbox(sl, "• " + c,
              Inches(0.9), Inches(3.1) + i * Inches(0.72),
              Inches(11.7), Inches(0.6),
              size=19, color=PRIMARY)

    # ── 13. 限制範例表 ────────────────────────────────────────────────────────
    table_slide(prs, "疾管署常用限制範例",
        ["限制類型", "範例寫法"],
        [
            ["字數",  "300 字以內、約 500 字"],
            ["語氣",  "正式公文語氣、親切易懂"],
            ["對象",  "一般民眾、醫護人員、長者"],
            ["用語",  "避免專業術語、使用台灣常用詞彙"],
            ["內容",  "只討論預防措施、不涉及治療"],
        ],
        col_widths=[Inches(2.8), Inches(9.3)],
    )

    # ── 14. 完整 RTFC 範例（登革熱） ─────────────────────────────────────────
    code_slide(prs, "完整 Prompt 範例：登革熱衛教文宣",
        "【R 角色】\n"
        "你是疾管署的衛教專家。\n\n"
        "【T 任務】\n"
        "請撰寫一篇登革熱預防衛教文宣。\n\n"
        "【F 格式】\n"
        "分為三個段落：\n"
        "  1. 認識登革熱（什麼是登革熱、傳播方式）\n"
        "  2. 預防措施（居家清除積水容器、個人防護）\n"
        "  3. 就醫時機（出現哪些症狀要就醫）\n\n"
        "【C 限制】\n"
        "目標對象：一般民眾｜字數：300 字以內｜語氣：親切易懂｜使用繁體中文",
        caption="四個要素都包含了 → AI 輸出精準、結構化、直接可用"
    )

    # ── 15. 另一個完整範例（流感疫苗接種通知） ──────────────────────────────
    code_slide(prs, "完整 Prompt 範例：流感疫苗接種通知",
        "【R 角色】\n"
        "你是疾管署公文撰寫專家。\n\n"
        "【T 任務】\n"
        "請撰寫流感疫苗接種通知，發送給各單位同仁。\n\n"
        "【F 格式】\n"
        "公文格式：主旨、說明、辦法\n\n"
        "【C 限制】\n"
        "字數：200 字以內｜語氣：正式但友善",
        caption="從模組 3 開始，您將拿到每種業務的 Prompt 食譜，直接填入即可"
    )

    # ── 16. RTFC 逐行標色解析 ─────────────────────────────────────────────────
    sl = blank(prs)
    set_bg(sl, LIGHT_BG)
    header_bar(sl, "Prompt 四要素：標色解析")

    lines = [
        (ROLE_C,   "R  角色",  "你是疾管署的衛教專家。"),
        (TASK_C,   "T  任務",  "請撰寫一份流感疫苗接種宣導文案。"),
        (FORMAT_C, "F  格式",  "分為「為什麼要打疫苗」「誰應該優先接種」「接種注意事項」三段。"),
        (CONST_C,  "C  限制",  "使用民眾易懂的語言，字數 250 字以內。"),
    ]
    for i, (clr, label, text) in enumerate(lines):
        top = Inches(1.5) + i * Inches(1.35)
        rect(sl, Inches(0.5), top, Inches(1.5), Inches(1.1), clr)
        txbox(sl, label,
              Inches(0.5), top, Inches(1.5), Inches(1.1),
              size=16, bold=True, color=WHITE, align=PP_ALIGN.CENTER)
        rect(sl, Inches(2.2), top, Inches(10.6), Inches(1.1), LIGHT_BG,
             line=clr)
        txbox(sl, text,
              Inches(2.4), top + Inches(0.2),
              Inches(10.2), Inches(0.75),
              size=18, color=PRIMARY)

    txbox(sl, "四行組合在一起 = 一個完整、可直接使用的 Prompt",
          Inches(0.5), Inches(7.0), Inches(12.3), Inches(0.3),
          size=15, italic=True, color=MUTED, align=PP_ALIGN.CENTER)

    # ── 17. 記憶口訣 ─────────────────────────────────────────────────────────
    sl = blank(prs)
    set_bg(sl, PRIMARY)
    txbox(sl, "記憶口訣",
          Inches(1.5), Inches(0.8), Inches(10.3), Inches(0.7),
          size=22, color=SECONDARY, align=PP_ALIGN.CENTER)
    txbox(sl, "角 • 任 • 格 • 限",
          Inches(1.0), Inches(1.7), Inches(11.3), Inches(1.8),
          size=64, bold=True, color=WHITE, align=PP_ALIGN.CENTER)

    words = [
        (ROLE_C,   "角色\nRole"),
        (TASK_C,   "任務\nTask"),
        (FORMAT_C, "格式\nFormat"),
        (CONST_C,  "限制\nConstraint"),
    ]
    for i, (clr, word) in enumerate(words):
        left = Inches(0.8) + i * Inches(3.0)
        rect(sl, left, Inches(3.8), Inches(2.7), Inches(2.0), clr)
        txbox(sl, word, left, Inches(3.8), Inches(2.7), Inches(2.0),
              size=22, bold=True, color=WHITE, align=PP_ALIGN.CENTER)

    txbox(sl,
          "不是每個 Prompt 都需要四個要素，視情況靈活運用。\n"
          "但加上的要素越多，輸出越精準。",
          Inches(1.0), Inches(6.2), Inches(11.3), Inches(0.9),
          size=17, color=SECONDARY, align=PP_ALIGN.CENTER)

    # ── 18. 好 vs 差對比 ──────────────────────────────────────────────────────
    two_col_slide(prs, "Prompt 品質對比",
        "✗  模糊的 Prompt", [
            "「幫我寫衛教文章」",
            "「整理一下這個」",
            "「做個報告」",
        ],
        "✓  清楚的 Prompt（含 RTFC）", [
            "「你是衛教專家，請撰寫流感預防文宣，條列式，300字以內，對象一般民眾」",
            "「請將以下逐字稿整理成結構化會議紀錄，含決議與待辦」",
            "「你是資料分析師，請摘要週報重點供署長參閱，300字，條列式」",
        ],
    )

    # ── 19. 實際應用情境練習 ──────────────────────────────────────────────────
    sl = blank(prs)
    set_bg(sl, LIGHT_BG)
    header_bar(sl, "情境練習：組合 RTFC")

    txbox(sl,
          "情境：需要撰寫一份給各縣市衛生局的流感疫苗接種通知函",
          Inches(0.6), Inches(1.35), Inches(12.0), Inches(0.65),
          size=20, bold=True, color=PRIMARY)

    draft_lines = [
        (ROLE_C,   "你是", "疾管署公文撰寫專家。"),
        (TASK_C,   "請",   "撰寫流感疫苗接種通知函，發送給各縣市衛生局。"),
        (FORMAT_C, "格式", "公文格式（主旨、說明、辦法）。"),
        (CONST_C,  "限制", "200 字以內，正式公文語氣。"),
    ]
    for i, (clr, prompt_label, content) in enumerate(draft_lines):
        top = Inches(2.2) + i * Inches(1.05)
        rect(sl, Inches(0.5), top, Inches(1.4), Inches(0.8), clr)
        txbox(sl, prompt_label,
              Inches(0.5), top, Inches(1.4), Inches(0.8),
              size=18, bold=True, color=WHITE, align=PP_ALIGN.CENTER)
        txbox(sl, content,
              Inches(2.1), top + Inches(0.1),
              Inches(10.7), Inches(0.65),
              size=18, color=PRIMARY)

    txbox(sl, "→  把四行合在一起，就是一個完整的 Prompt，直接複製貼上使用！",
          Inches(0.6), Inches(6.55), Inches(12.0), Inches(0.65),
          size=17, bold=True, color=ACCENT)

    # ── 20. 測驗重點複習 ──────────────────────────────────────────────────────
    sl = blank(prs)
    set_bg(sl, LIGHT_BG)
    header_bar(sl, "模組 2 測驗重點回顧")

    qa_pairs = [
        ("Q1  Prompt 四要素是指？",
         "A   角色、任務、格式、限制"),
        ("Q2  「你是疾管署的衛教專家」屬於哪個要素？",
         "A   角色（Role）"),
        ("Q3  「請使用表格比較三種疾病」主要設定了哪個要素？",
         "A   格式（Format）"),
        ("Q4  「300 字以內，語氣親切，目標民眾」屬於？",
         "A   限制（Constraint）"),
        ("Q5  以下哪個 Prompt 四要素最完整？",
         "A   「你是衛教專家，請撰寫流感文章，條列式，300字以內，對象民眾」"),
    ]
    for i, (q, a) in enumerate(qa_pairs):
        top = Inches(1.35) + i * Inches(1.15)
        txbox(sl, q, Inches(0.6), top, Inches(12.0), Inches(0.5),
              size=17, bold=True, color=PRIMARY)
        txbox(sl, a, Inches(0.9), top + Inches(0.52), Inches(11.7), Inches(0.5),
              size=16, color=ACCENT)

    # ── 21. 下一步預告 ────────────────────────────────────────────────────────
    sl = blank(prs)
    set_bg(sl, DARK_BG)
    rect(sl, Inches(0), Inches(0), Inches(0.22), Inches(7.5), SECONDARY)
    txbox(sl, "您已掌握 RTFC 框架！",
          Inches(0.55), Inches(1.2), Inches(11.5), Inches(0.8),
          size=28, bold=True, color=WHITE)
    txbox(sl,
          "接下來的模組 3 和 4，\n"
          "您會拿到真實的疾管署業務情境 Prompt 食譜——\n"
          "不需要從頭想，填入資料直接使用。",
          Inches(0.55), Inches(2.2), Inches(11.5), Inches(2.5),
          size=22, color=SECONDARY)
    txbox(sl, "模組 3  文書處理應用",
          Inches(0.55), Inches(5.0), Inches(5.5), Inches(0.7),
          size=20, bold=True, color=WHITE)
    txbox(sl, "公文・會議紀錄・Email",
          Inches(0.55), Inches(5.75), Inches(5.5), Inches(0.5),
          size=17, color=MUTED)
    txbox(sl, "模組 4  資料整理應用",
          Inches(7.0), Inches(5.0), Inches(5.5), Inches(0.7),
          size=20, bold=True, color=WHITE)
    txbox(sl, "Excel 公式・摘要・圖表說明",
          Inches(7.0), Inches(5.75), Inches(5.5), Inches(0.5),
          size=17, color=MUTED)

    # ── 22. CTA ──────────────────────────────────────────────────────────────
    cta_slide(prs,
              "完成練習後，\n前往模組 3 拿您的第一份 Prompt 食譜！",
              "▶  前往模組 3：文書處理應用")

    save_pptx(prs, "module2_Prompt四要素.pptx")


if __name__ == "__main__":
    build()
