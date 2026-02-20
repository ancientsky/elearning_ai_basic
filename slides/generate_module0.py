"""generate_module0.py — 模組 0：學前準備  (17 slides)

Usage:
    cd slides && uv run python generate_module0.py
"""
from shared import (
    new_prs, blank, set_bg, txbox, rect, header_bar, save_pptx,
    cover_slide, objectives_slide, content_slide, table_slide,
    two_col_slide, cta_slide, alert_slide, section_divider,
    PRIMARY, SECONDARY, LIGHT_BG, DARK_BG, WHITE, MUTED,
    SUCCESS, WARNING, DANGER, ACCENT,
    Inches, PP_ALIGN,
)


def build() -> None:
    prs = new_prs()

    # ── 1. Cover ─────────────────────────────────────────────────────────────
    cover_slide(
        prs, "0", "學前準備",
        "課程介紹・帳號設定・課前自我檢測",
        "3 分鐘",
    )

    # ── 2. 開場鉤子 ───────────────────────────────────────────────────────────
    sl = blank(prs)
    set_bg(sl, DARK_BG)
    rect(sl, Inches(0), Inches(0), Inches(0.22), Inches(7.5), SECONDARY)
    txbox(sl,
          "您知道在疾管署，\n哪些事情 AI 能幫您做——\n哪些又絕對不能輸入嗎？",
          Inches(0.6), Inches(1.2), Inches(11.5), Inches(3.0),
          size=32, bold=True, color=WHITE)
    txbox(sl,
          "很多人開始用 AI，卻不確定邊界在哪裡。\n\n"
          "這門課，30 分鐘讓您從零開始，安全又有效地用 AI 工作。",
          Inches(0.6), Inches(4.4), Inches(11.5), Inches(1.8),
          size=21, color=SECONDARY)

    # ── 3. 學習目標 ───────────────────────────────────────────────────────────
    objectives_slide(prs, [
        "說出 AI 的三項能力與兩個絕對禁止事項",
        "用 RTFC 框架寫出有效的 Prompt",
        "在公文、資料整理等五種業務情境中，實際套用 AI 協助",
    ])

    # ── 4. 課程全覽地圖（文字版）─────────────────────────────────────────────
    sl = blank(prs)
    set_bg(sl, LIGHT_BG)
    header_bar(sl, "課程架構：六個模組")

    modules = [
        ("0", "學前準備",      "確認 AI 工具帳號設定完成",         "10 min"),
        ("1", "認識生成式 AI", "了解能做什麼、不能做什麼，及資安規範", "15 min"),
        ("2", "Prompt 四要素", "掌握 R-T-F-C 核心框架",           "20 min"),
        ("3", "文書處理應用",   "公文、會議紀錄、Email",            "20 min"),
        ("4", "資料整理應用",   "Excel 公式、摘要、圖表說明",       "25 min"),
        ("5", "進階技巧",      "多輪對話、常見錯誤、持續學習",       "15 min"),
    ]
    clrs = [SECONDARY, PRIMARY, ACCENT, SUCCESS, WARNING, DANGER]
    for i, (num, title, desc, dur) in enumerate(modules):
        col = i % 2
        row = i // 2
        left = Inches(0.4) + col * Inches(6.5)
        top  = Inches(1.35) + row * Inches(2.0)
        rect(sl, left, top, Inches(6.1), Inches(1.7), clrs[i])
        txbox(sl, f"模組 {num}  {title}",
              left + Inches(0.2), top + Inches(0.15),
              Inches(5.7), Inches(0.6),
              size=18, bold=True, color=WHITE)
        txbox(sl, desc,
              left + Inches(0.2), top + Inches(0.75),
              Inches(4.5), Inches(0.55),
              size=15, color=WHITE)
        txbox(sl, dur,
              left + Inches(4.8), top + Inches(0.75),
              Inches(1.1), Inches(0.55),
              size=14, color=WHITE, align=PP_ALIGN.RIGHT)

    # ── 5. 模組 0 重點說明 ───────────────────────────────────────────────────
    content_slide(prs, "本模組包含三個單元", [
        "單元 0.1  課程介紹與學習目標",
        "  觀看 3 分鐘影片，了解整體課程架構",
        "單元 0.2  AI 工具帳號設定",
        "  ChatGPT / Claude / Gemini 三擇一，完成帳號設定",
        "單元 0.3  課前自我檢測",
        "  5 題輕鬆測驗，了解目前 AI 認識程度（不計分）",
    ])

    # ── 6. 如何使用這個平台 ──────────────────────────────────────────────────
    content_slide(prs, "如何使用這個平台", [
        "點擊左側「單元導覽」，依序或跳躍學習",
        "每個單元有互動練習，完成自動記錄進度",
        "Prompt 食譜庫：直接複製可用的 Prompt 模板",
        "行動裝置友善，可隨時隨地學習",
        "建議：先完成線上自學，實體課更能深入討論",
    ])

    # ── 7. AI 工具比較表 ─────────────────────────────────────────────────────
    table_slide(prs, "三大 AI 工具比較",
        ["工具", "開發商", "免費方案", "特點"],
        [
            ["ChatGPT",  "OpenAI",     "有（GPT-4o mini）",  "使用最廣泛、功能豐富"],
            ["Claude",   "Anthropic",  "有（每日限量）",      "長文處理佳、注重安全"],
            ["Gemini",   "Google",     "有（Google 帳號）",   "整合 Google 生態系"],
            ["Copilot",  "Microsoft",  "有（Bing 整合）",     "整合 Office 365 應用"],
        ],
        col_widths=[Inches(2.0), Inches(2.2), Inches(2.8), Inches(5.1)],
    )

    # ── 8. ChatGPT 帳號設定 ──────────────────────────────────────────────────
    content_slide(prs, "ChatGPT 帳號設定步驟", [
        "前往 chat.openai.com",
        "點擊「Sign up」（註冊）",
        "使用 Email 或 Google / Microsoft 帳號註冊",
        "完成電子郵件驗證",
        "登入後即可使用免費版",
        "  💡  免費版即足夠本課程所有練習，無需付費升級",
    ])

    # ── 9. Claude 帳號設定 ───────────────────────────────────────────────────
    content_slide(prs, "Claude 帳號設定步驟", [
        "前往 claude.ai",
        "點擊「Start for free」",
        "使用 Email 或 Google 帳號註冊",
        "完成手機號碼驗證",
        "登入後即可使用",
        "  💡  免費版每日有訊息數量限制，足夠一般練習使用",
    ])

    # ── 10. Gemini 帳號設定 ──────────────────────────────────────────────────
    content_slide(prs, "Gemini 帳號設定步驟", [
        "前往 gemini.google.com",
        "使用您的 Google 帳號登入",
        "同意使用條款",
        "即可開始使用",
        "  💡  如果您已有 Google 帳號，無需額外註冊",
    ])

    # ── 11. 帳號設定檢核清單 ─────────────────────────────────────────────────
    sl = blank(prs)
    set_bg(sl, LIGHT_BG)
    header_bar(sl, "帳號設定檢核清單")

    items = [
        "已選擇至少一個 AI 工具並完成註冊",
        "已成功登入並看到對話介面",
        "已嘗試送出一則測試訊息（如「你好」）",
        "已確認 AI 能正常回覆",
    ]
    for i, item in enumerate(items):
        top = Inches(1.5) + i * Inches(1.1)
        rect(sl, Inches(0.5), top, Inches(0.75), Inches(0.75), SUCCESS)
        txbox(sl, "☑", Inches(0.5), top, Inches(0.75), Inches(0.75),
              size=26, bold=True, color=WHITE, align=PP_ALIGN.CENTER)
        txbox(sl, item,
              Inches(1.45), top + Inches(0.05),
              Inches(11.2), Inches(0.65),
              size=20, color=PRIMARY)

    # ── 12. 資安提醒（重要） ─────────────────────────────────────────────────
    alert_slide(prs, "重要資安提醒", "danger",
                "使用 AI 工具時，請勿輸入任何機密資料、個資或敏感資訊。\n\n"
                "• 個人資料（姓名、身分證字號、電話、地址）\n"
                "• 機密公務文件\n"
                "• 尚未公開的疫情數據\n\n"
                "詳細資安規範將在模組 1 完整說明。",
                icon="🔒")

    # ── 13-17. 課前自我檢測 5 題（每題一張） ─────────────────────────────────
    quiz_items = [
        ("什麼是「生成式 AI」？",
         "能夠根據提示產生文字、圖片等新內容的 AI",
         "不是：搜尋引擎、是非題程式、電腦病毒"),
        ("「Prompt」（提示詞）指的是什麼？",
         "我們輸入給 AI 的指令或問題",
         "不是：AI 的品牌、AI 的回覆、程式語言"),
        ("以下哪項「不應該」輸入 AI？",
         "包含民眾姓名與身分證字號的個案資料",
         "可以輸入：公開文字、翻譯、無敏感內容的大綱"),
        ("使用 AI 輔助工作時，哪個做法最正確？",
         "AI 產出的內容需要審核與確認後才能使用",
         "錯誤：完全相信 AI、完全不能信任 AI"),
        ("哪種 Prompt 寫法比較好？",
         "「請撰寫一篇 300 字的登革熱預防衛教文章，對象是一般民眾」",
         "差：「寫一篇文章」「幫我做事」「登革熱」"),
    ]
    for i, (q, correct, note) in enumerate(quiz_items):
        sl = blank(prs)
        set_bg(sl, LIGHT_BG)
        header_bar(sl, f"課前自我檢測  第 {i+1} 題／共 5 題")

        txbox(sl, q,
              Inches(0.6), Inches(1.35), Inches(12.0), Inches(1.2),
              size=22, bold=True, color=PRIMARY)

        rect(sl, Inches(0.6), Inches(2.7), Inches(12.0), Inches(1.5), SUCCESS)
        txbox(sl, "✓  " + correct,
              Inches(0.85), Inches(2.85), Inches(11.5), Inches(1.2),
              size=20, bold=True, color=WHITE)

        rect(sl, Inches(0.6), Inches(4.4), Inches(12.0), Inches(1.1), MUTED)
        txbox(sl, note,
              Inches(0.85), Inches(4.5), Inches(11.5), Inches(0.9),
              size=17, color=WHITE)

        # Progress dots
        for d in range(5):
            clr = SECONDARY if d == i else PRIMARY
            rect(sl, Inches(5.8) + d * Inches(0.55),
                 Inches(6.85), Inches(0.38), Inches(0.38), clr)

    # ── 17. CTA ──────────────────────────────────────────────────────────────
    cta_slide(prs,
              "帳號設定好了嗎？\n準備好就前往模組 1！",
              "▶  前往模組 1：認識生成式 AI")

    save_pptx(prs, "module0_學前準備.pptx")


if __name__ == "__main__":
    build()
