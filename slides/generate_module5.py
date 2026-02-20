"""generate_module5.py — 模組 5：進階技巧  (18 slides)

Usage:
    cd slides && uv run python generate_module5.py
"""
from shared import (
    new_prs, blank, set_bg, txbox, rect, header_bar, save_pptx,
    cover_slide, objectives_slide, content_slide, table_slide,
    two_col_slide, cta_slide, alert_slide,
    card_grid_slide, dialogue_step_slide,
    SW, PRIMARY, SECONDARY, LIGHT_BG, DARK_BG, WHITE, MUTED,
    SUCCESS, WARNING, DANGER, ACCENT, CODE_BG, CODE_FG,
    Inches, PP_ALIGN,
)


def build() -> None:
    prs = new_prs()

    # ── 1. Cover ─────────────────────────────────────────────────────────────
    cover_slide(
        prs, "5", "進階技巧",
        "多輪對話・迭代優化・常見錯誤・持續學習",
        "1 分鐘（導言）",
    )

    # ── 2. 開場鉤子 ───────────────────────────────────────────────────────────
    sl = blank(prs)
    set_bg(sl, DARK_BG)
    rect(sl, Inches(0), Inches(0), Inches(0.22), Inches(7.5), SECONDARY)

    txbox(sl,
          "您已經學了 RTFC，\n但有時候第一次的回應就是不夠好——\n那不是您的問題，也不是 AI 的問題。",
          Inches(0.55), Inches(1.0), Inches(11.5), Inches(2.5),
          size=28, bold=True, color=WHITE)

    txbox(sl,
          "這個模組要教您：如何透過「多輪對話」\n讓 AI 越改越好，\n還有使用 AI 時最常犯的三個錯誤。",
          Inches(0.55), Inches(3.8), Inches(11.5), Inches(1.8),
          size=22, color=SECONDARY)

    # ── 3. 學習目標 ───────────────────────────────────────────────────────────
    objectives_slide(prs, [
        "透過多輪對話，逐步把 AI 回應從「還可以」改到「直接可用」",
        "識別並避免三個最常見的 AI 使用錯誤",
        "知道三個學完本課後可以繼續精進的免費資源",
    ])

    # ── 4. 多輪對話說明 ───────────────────────────────────────────────────────
    content_slide(prs, "什麼時候需要多輪對話？", [
        "第一次回應不夠完整或不符期望",
        "需要 AI 修改特定部分",
        "想要調整語氣、長度或格式",
        "複雜任務需要分步進行",
        "關鍵技巧：不要重新開始新對話——在同一對話中繼續告訴 AI 哪裡需要調整",
        "  AI 會保留之前的理解，產出更符合期望的結果",
    ])

    # ── 5-8. 四輪對話範例（衛教文宣迭代） ───────────────────────────────────
    dialogue_step_slide(prs, 1, 4,
        "第一輪：初始請求",
        "你是疾管署衛教專家。\n"
        "請撰寫一篇登革熱預防衛教文宣，給一般民眾，300字以內。",
        "AI 回應了一份文字說明，但語氣比較正式……"
    )

    dialogue_step_slide(prs, 2, 4,
        "第二輪：調整語氣",
        "語氣可以再親切一點嗎？像是鄰居阿姨在提醒你的感覺。",
        "AI 把語氣改得更口語了，但您想加入具體的預防口訣……"
    )

    dialogue_step_slide(prs, 3, 4,
        "第三輪：增加內容",
        "請在預防措施加入「巡、倒、清、刷」口訣的說明。",
        "AI 加入了口訣說明，最後再調整一下呈現方式……"
    )

    dialogue_step_slide(prs, 4, 4,
        "第四輪：調整格式",
        "請把重點用條列式呈現，方便民眾閱讀。",
        "四輪對話後，得到一份符合需求、格式清楚、語氣親切的衛教文宣！"
    )

    # ── 9. 迭代優化常用指令表 ───────────────────────────────────────────────
    table_slide(prs, "迭代優化的常用指令",
        ["調整需求", "可以這樣說"],
        [
            ["調整語氣", "「語氣再正式一點」「改得更親切」「活潑一點」"],
            ["增減內容", "「請加入…」「請移除…」「請縮短/擴充…」"],
            ["調整格式", "「請改成條列式」「請加入標題」「整理成表格」"],
            ["修正錯誤", "「這部分不對，應該是…」「數字有誤，應為…」"],
            ["聚焦特定部分", "「第二段請重寫」「只修改結尾」"],
        ],
        col_widths=[Inches(2.8), Inches(9.3)],
    )

    # ── 10. 常見錯誤 1：個資 ─────────────────────────────────────────────────
    sl = blank(prs)
    set_bg(sl, LIGHT_BG)
    rect(sl, Inches(0), Inches(0), SW, Inches(1.15), DANGER)
    txbox(sl, "常見錯誤 1：輸入個人資料（最嚴重！）",
          Inches(0.4), Inches(0.2), Inches(12.5), Inches(0.75),
          size=26, bold=True, color=WHITE)

    # Bad example
    rect(sl, Inches(0.5), Inches(1.4), Inches(5.8), Inches(2.5), CODE_BG)
    txbox(sl,
          "✗  錯誤做法\n\n"
          "「請幫我整理這份疫調報告：\n"
          " 患者姓名：王大明\n"
          " 身分證字號：A123456789\n"
          " 地址：台北市…」",
          Inches(0.7), Inches(1.55), Inches(5.4), Inches(2.2),
          size=15, color=CODE_FG)

    rect(sl, Inches(0.5), Inches(4.1), Inches(5.8), Inches(0.8), DANGER)
    txbox(sl, "⚠  嚴重違反資安規範！可能導致個資外洩",
          Inches(0.7), Inches(4.15), Inches(5.4), Inches(0.7),
          size=15, bold=True, color=WHITE)

    # Good example
    rect(sl, Inches(7.0), Inches(1.4), Inches(5.8), Inches(2.5), SUCCESS)
    txbox(sl,
          "✓  正確做法（去識別化）\n\n"
          "「請幫我整理這份疫調報告格式：\n"
          " 患者 A，50 歲男性，北部地區居民，\n"
          " 發病日期：2024/10/15…」",
          Inches(7.2), Inches(1.55), Inches(5.4), Inches(2.2),
          size=15, color=WHITE)

    rect(sl, Inches(7.0), Inches(4.1), Inches(5.8), Inches(0.8), ACCENT)
    txbox(sl, "✓  移除個資後，可以使用 AI 協助",
          Inches(7.2), Inches(4.15), Inches(5.4), Inches(0.7),
          size=15, bold=True, color=WHITE)

    txbox(sl, "原則：不確定能不能輸入，那就不要輸入。",
          Inches(0.5), Inches(5.2), Inches(12.3), Inches(0.6),
          size=18, bold=True, italic=True, color=DANGER, align=PP_ALIGN.CENTER)

    # ── 11. 常見錯誤 2：Prompt 模糊 ──────────────────────────────────────────
    sl = blank(prs)
    set_bg(sl, LIGHT_BG)
    rect(sl, Inches(0), Inches(0), SW, Inches(1.15), WARNING)
    txbox(sl, "常見錯誤 2：Prompt 模糊不清",
          Inches(0.4), Inches(0.2), Inches(12.5), Inches(0.75),
          size=26, bold=True, color=DARK_BG)

    bad_prompts = [
        ("幫我處理這個", "AI 不知道「這個」是什麼"),
        ("寫點東西",     "什麼東西？多長？什麼主題？"),
        ("改好一點",     "什麼叫「好一點」？標準在哪？"),
    ]
    for i, (prompt, reason) in enumerate(bad_prompts):
        top = Inches(1.5) + i * Inches(1.75)
        rect(sl, Inches(0.5), top, Inches(4.5), Inches(1.5), CODE_BG)
        txbox(sl, f"✗  「{prompt}」",
              Inches(0.7), top + Inches(0.2), Inches(4.1), Inches(0.65),
              size=16, bold=True, color=DANGER)
        rect(sl, Inches(5.3), top, Inches(7.5), Inches(1.5),
             WARNING)
        txbox(sl, f"問題：{reason}\n\n解決：套用 RTFC 框架，描述角色、任務、格式、限制",
              Inches(5.5), top + Inches(0.2), Inches(7.1), Inches(1.2),
              size=15, color=DARK_BG)

    txbox(sl, "回到模組 2 的 RTFC 框架：角色、任務、格式、限制",
          Inches(0.5), Inches(6.8), Inches(12.3), Inches(0.4),
          size=15, italic=True, color=PRIMARY, align=PP_ALIGN.CENTER)

    # ── 12. 常見錯誤 3：完全信任 AI ──────────────────────────────────────────
    sl = blank(prs)
    set_bg(sl, LIGHT_BG)
    rect(sl, Inches(0), Inches(0), SW, Inches(1.15), DANGER)
    txbox(sl, "常見錯誤 3：完全信任 AI 輸出",
          Inches(0.4), Inches(0.2), Inches(12.5), Inches(0.75),
          size=26, bold=True, color=WHITE)

    rect(sl, Inches(0.5), Inches(1.4), Inches(12.3), Inches(1.0), CODE_BG)
    txbox(sl, "✗  「AI 說的一定對！直接複製貼上發布！」",
          Inches(0.7), Inches(1.55), Inches(11.9), Inches(0.7),
          size=18, bold=True, color=DANGER)

    risks = [
        "AI 可能有「幻覺」，編造看似合理但錯誤的數字或資訊",
        "AI 的知識有截止日期，無法得知最新疫情數據",
        "AI 可能誤解您的需求，產出不符合疾管署規範的內容",
    ]
    for i, risk in enumerate(risks):
        txbox(sl, "⚠  " + risk,
              Inches(0.7), Inches(2.65) + i * Inches(0.85),
              Inches(12.0), Inches(0.7),
              size=18, color=DANGER)

    rect(sl, Inches(0.5), Inches(5.5), Inches(12.3), Inches(1.1), SUCCESS)
    txbox(sl,
          "✓  正確做法：AI 的輸出是「草稿」，不是「定稿」。\n"
          "   每份 AI 產出都要經過人工審核確認後才能使用。",
          Inches(0.7), Inches(5.6), Inches(11.9), Inches(0.9),
          size=18, bold=True, color=WHITE)

    # ── 13. 正確使用心態（4 卡片） ───────────────────────────────────────────
    card_grid_slide(prs, "使用 AI 的正確心態",
        [
            (PRIMARY,  "AI 是助手，不是主管",
             "最終決策權在您手上\nAI 只是提供草稿和建議"),
            (SUCCESS,  "審核是必要步驟",
             "所有 AI 產出都要\n經過人工審核確認"),
            (DANGER,   "資安永遠第一",
             "有疑慮就不要輸入\n寧可保守，不要冒險"),
            (ACCENT,   "持續學習優化",
             "每次使用都是學習機會\n累積經驗，越用越好"),
        ])

    # ── 14. 官方學習資源 ─────────────────────────────────────────────────────
    table_slide(prs, "持續學習資源：官方",
        ["資源", "說明"],
        [
            ["Anthropic Academy",  "Claude 官方課程，含 Claude 101 入門"],
            ["Anthropic Learn",    "Claude 學習資源與使用指南"],
            ["OpenAI 教學",        "ChatGPT 官方使用說明"],
        ],
        col_widths=[Inches(3.8), Inches(8.4)],
    )

    # ── 15. 免費平台學習資源 ─────────────────────────────────────────────────
    table_slide(prs, "持續學習資源：免費平台（強力推薦）",
        ["資源", "說明"],
        [
            ["Learn Prompting",      "最完整的免費 Prompt 課程，4.8 星 ⭐"],
            ["Google AI Essentials", "職場 AI 應用，5 模組約 10 小時"],
            ["Anthropic 互動教學",   "9 章節互動練習，含 Playground"],
            ["IBM Prompt Engineering","Coursera 免費旁聽，結構化教學"],
            ["Prompt Engineering Guide","GitHub 開源指南，深入技術細節"],
        ],
        col_widths=[Inches(3.8), Inches(8.4)],
    )

    # ── 16. 課程總結回顧 ─────────────────────────────────────────────────────
    sl = blank(prs)
    set_bg(sl, LIGHT_BG)
    header_bar(sl, "六個模組，您學了什麼？")

    summaries = [
        (PRIMARY,   "模組 0", "帳號設定 + 課前準備"),
        (ACCENT,    "模組 1", "AI 能力、幻覺、四條資安原則"),
        (SUCCESS,   "模組 2", "RTFC 框架：角色、任務、格式、限制"),
        (WARNING,   "模組 3", "公文、會議紀錄、Email"),
        (SECONDARY, "模組 4", "Excel 公式、摘要、圖表說明"),
        (DANGER,    "模組 5", "多輪對話、三個常見錯誤"),
    ]
    for i, (clr, mod, desc) in enumerate(summaries):
        col = i % 3
        row = i // 3
        left = Inches(0.4) + col * Inches(4.25)
        top  = Inches(1.35) + row * Inches(2.55)
        rect(sl, left, top, Inches(4.0), Inches(2.3), clr)
        txbox(sl, mod,
              left + Inches(0.2), top + Inches(0.2),
              Inches(3.6), Inches(0.6),
              size=18, bold=True, color=WHITE)
        txbox(sl, desc,
              left + Inches(0.2), top + Inches(0.85),
              Inches(3.6), Inches(1.2),
              size=15, color=WHITE)

    # ── 17. 結業說明 ─────────────────────────────────────────────────────────
    sl = blank(prs)
    set_bg(sl, PRIMARY)
    rect(sl, Inches(0), Inches(0), Inches(0.22), Inches(7.5), SECONDARY)

    txbox(sl, "結業測驗",
          Inches(0.55), Inches(1.0), Inches(11.5), Inches(0.8),
          size=22, color=SECONDARY)
    txbox(sl,
          "10 題綜合測驗，涵蓋全部六個模組重點",
          Inches(0.55), Inches(1.9), Inches(11.5), Inches(0.7),
          size=24, color=WHITE)

    txbox(sl, "結業條件",
          Inches(0.55), Inches(3.0), Inches(11.5), Inches(0.7),
          size=22, color=SECONDARY)
    conditions = [
        "✓  完成所有模組的單元測驗",
        "✓  結業測驗成績 ≥ 80%",
        "✓  即可前往領取結業證書",
    ]
    for i, c in enumerate(conditions):
        txbox(sl, c,
              Inches(0.55), Inches(3.8) + i * Inches(0.82),
              Inches(11.5), Inches(0.65),
              size=22, color=WHITE)

    # ── 18. 結業 CTA ─────────────────────────────────────────────────────────
    sl = blank(prs)
    set_bg(sl, DARK_BG)
    rect(sl, Inches(0), Inches(0), SW, Inches(0.25), SECONDARY)
    rect(sl, Inches(0), Inches(7.25), SW, Inches(0.25), SECONDARY)

    txbox(sl, "🎓",
          Inches(5.5), Inches(0.5), Inches(2.5), Inches(1.5),
          size=60, align=PP_ALIGN.CENTER, color=WHITE)

    txbox(sl,
          "恭喜完成 AI 應用基礎班！",
          Inches(0.5), Inches(2.1), Inches(12.3), Inches(1.2),
          size=38, bold=True, color=WHITE, align=PP_ALIGN.CENTER)

    txbox(sl,
          "記得善用 Prompt 食譜庫與學習資源，持續精進。",
          Inches(0.5), Inches(3.5), Inches(12.3), Inches(0.7),
          size=20, color=SECONDARY, align=PP_ALIGN.CENTER)

    rect(sl, Inches(3.0), Inches(4.5), Inches(7.3), Inches(0.9), SECONDARY)
    txbox(sl, "▶  前往結業測驗，領取結業證書",
          Inches(3.0), Inches(4.5), Inches(7.3), Inches(0.9),
          size=22, bold=True, color=DARK_BG, align=PP_ALIGN.CENTER)

    txbox(sl, "疾病管制署  AI 應用基礎班",
          Inches(0.5), Inches(6.6), Inches(12.3), Inches(0.4),
          size=14, color=MUTED, align=PP_ALIGN.CENTER)

    save_pptx(prs, "module5_進階技巧.pptx")


if __name__ == "__main__":
    build()

