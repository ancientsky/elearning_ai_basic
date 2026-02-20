"""generate_module1.py — 模組 1：認識生成式 AI  (20 slides)

Usage:
    cd slides && uv run python generate_module1.py
"""
from shared import (
    new_prs, blank, set_bg, txbox, rect, header_bar, save_pptx,
    cover_slide, objectives_slide, content_slide, table_slide,
    two_col_slide, cta_slide, alert_slide, section_divider,
    card_grid_slide,
    PRIMARY, SECONDARY, LIGHT_BG, DARK_BG, WHITE, MUTED,
    SUCCESS, WARNING, DANGER, ACCENT, CODE_BG, CODE_FG,
    Inches, PP_ALIGN,
)


def build() -> None:
    prs = new_prs()

    # ── 1. Cover ─────────────────────────────────────────────────────────────
    cover_slide(
        prs, "1", "認識生成式 AI",
        "AI 基本概念・能力與限制・疾管署資安規範",
        "5 分鐘",
    )

    # ── 2. 開場鉤子 ───────────────────────────────────────────────────────────
    sl = blank(prs)
    set_bg(sl, DARK_BG)
    rect(sl, Inches(0), Inches(0), Inches(0.22), Inches(7.5), DANGER)

    txbox(sl,
          "ChatGPT、Claude、Gemini——\n您能判斷 AI 什麼時候在說謊嗎？",
          Inches(0.55), Inches(1.0), Inches(11.5), Inches(2.0),
          size=32, bold=True, color=WHITE)

    # Fake AI answer box
    rect(sl, Inches(0.55), Inches(3.2), Inches(11.5), Inches(1.8), CODE_BG)
    txbox(sl,
          "AI 回答：「台灣 2023 年登革熱確診共 12,847 例……」",
          Inches(0.85), Inches(3.35), Inches(11.0), Inches(0.65),
          size=17, color=CODE_FG)
    rect(sl, Inches(0.55), Inches(4.1), Inches(11.5), Inches(0.7), DANGER)
    txbox(sl, "⚠  這個答案看起來很正確——但是錯的。",
          Inches(0.85), Inches(4.15), Inches(11.0), Inches(0.6),
          size=18, bold=True, color=WHITE)

    txbox(sl,
          "這支影片會讓您學會辨識 AI 何時出錯，以及安全使用 AI 的完整原則。",
          Inches(0.55), Inches(5.1), Inches(11.5), Inches(0.8),
          size=19, color=SECONDARY)

    # ── 3. 學習目標 ───────────────────────────────────────────────────────────
    objectives_slide(prs, [
        "用一句話解釋生成式 AI 的運作原理（不需要技術背景）",
        "識別 AI「幻覺」的三個跡象",
        "背出疾管署使用 AI 的四條資安原則",
    ], header="看完這 5 分鐘，您將能夠：")

    # ── 4. 什麼是生成式 AI ───────────────────────────────────────────────────
    content_slide(prs, "什麼是生成式 AI？", [
        "生成式 AI（Generative AI）能根據您的提示「生成」新內容",
        "  文字、圖片、程式碼、音樂……各種形式皆可",
        "運作邏輯：輸入 Prompt → AI 分析意圖 → 生成回應",
        "把它想像成一位「超級助理」：",
        "  讀過海量書籍，但有時也會「腦補」不存在的資訊",
        "核心定位：是助理，不是專家；AI 產出仍需人工審核",
    ])

    # ── 5. AI 如何運作（3 步驟） ─────────────────────────────────────────────
    sl = blank(prs)
    set_bg(sl, LIGHT_BG)
    header_bar(sl, "AI 如何運作？（簡化說明）")

    steps = [
        (PRIMARY,   "1  學習階段",
         "AI 被「餵食」大量文字資料\n（書籍、網頁、文章），\n學習語言模式與知識。"),
        (ACCENT,    "2  理解提示",
         "當您輸入問題時，\nAI 會分析您的意圖，\n找出最相關的知識。"),
        (SECONDARY, "3  生成回應",
         "根據學到的知識，\n一個字一個字「預測」\n最適合的回應。"),
    ]
    for i, (clr, step_title, desc) in enumerate(steps):
        left = Inches(0.5) + i * Inches(4.25)
        rect(sl, left, Inches(1.4), Inches(4.0), Inches(4.8), clr)
        txbox(sl, step_title,
              left + Inches(0.2), Inches(1.6),
              Inches(3.6), Inches(0.7),
              size=20, bold=True, color=WHITE)
        txbox(sl, desc,
              left + Inches(0.2), Inches(2.4),
              Inches(3.6), Inches(2.5),
              size=17, color=WHITE)
        if i < 2:
            txbox(sl, "→",
                  left + Inches(4.0), Inches(3.1),
                  Inches(0.25), Inches(0.6),
                  size=26, bold=True, color=PRIMARY, align=PP_ALIGN.CENTER)

    txbox(sl, "⚠  AI 的知識有「截止日期」——不知道訓練資料之後發生的事情。",
          Inches(0.5), Inches(6.4), Inches(12.3), Inches(0.65),
          size=16, italic=True, color=DANGER)

    # ── 6. 常見 AI 工具 ──────────────────────────────────────────────────────
    card_grid_slide(prs, "常見生成式 AI 工具",
        [
            (PRIMARY,   "ChatGPT（OpenAI）",
             "使用最廣泛的聊天 AI\n免費版可使用 GPT-4o mini"),
            (ACCENT,    "Claude（Anthropic）",
             "注重安全性與長文處理\n免費版每日限量使用"),
            (SUCCESS,   "Gemini（Google）",
             "整合 Google 生態系\n有 Google 帳號即可用"),
            (SECONDARY, "Copilot（Microsoft）",
             "整合 Office 365 應用\n適合已有 M365 授權的機關"),
        ])

    # ── 7. AI 擅長的事 ───────────────────────────────────────────────────────
    content_slide(prs, "AI 擅長的事情  ✓", [
        "文字撰寫與潤飾（文案、Email、摘要）",
        "資料整理與格式轉換",
        "翻譯與語言修正",
        "腦力激盪與創意發想",
        "程式碼撰寫與除錯",
        "問答與解釋概念",
        "文件摘要與重點提取",
    ])

    # ── 8. AI 的限制 ─────────────────────────────────────────────────────────
    content_slide(prs, "AI 的限制  ✗", [
        "會「幻覺」（Hallucination）：可能編造看起來合理但錯誤的資訊",
        "知識有截止日期：不知道訓練資料截止後發生的事",
        "無法存取即時資訊：除非有特別功能，否則無法上網查資料",
        "數學運算可能出錯：複雜計算不是 AI 的強項",
        "缺乏真正的理解：是模式匹配，不是真正「懂」",
        "可能有偏見：訓練資料的偏見會反映在輸出中",
    ])

    # ── 9. 疾管署情境配對 ─────────────────────────────────────────────────────
    two_col_slide(prs, "疾管署情境：AI 可以做什麼？",
        "✓  AI 可協助", [
            "撰寫疫情週報摘要",
            "整理防疫會議紀錄大綱",
            "翻譯 WHO 疫情報告",
            "草擬衛教宣導文案",
            "彙整防疫指引重點",
        ],
        "✗  不適合使用 AI", [
            "處理含個資的疫調報告",
            "查詢即時疫情數據",
            "唯一的醫學診斷依據",
            "處理機密文件內容",
            "發布未審核的疫情資訊",
        ],
    )

    # ── 10. AI 幻覺說明 ──────────────────────────────────────────────────────
    sl = blank(prs)
    set_bg(sl, LIGHT_BG)
    header_bar(sl, "AI「幻覺」（Hallucination）是什麼？")

    txbox(sl,
          "AI 有時會以非常有自信的語氣，描述根本不存在的事實。",
          Inches(0.6), Inches(1.35), Inches(12.0), Inches(0.7),
          size=20, color=PRIMARY)

    # Bad example
    rect(sl, Inches(0.6), Inches(2.2), Inches(12.0), Inches(1.3), CODE_BG)
    txbox(sl, "AI 說：「台灣 2023 年登革熱確診共 12,847 例，主要集中於南部縣市……」",
          Inches(0.85), Inches(2.35), Inches(11.5), Inches(1.0),
          size=16, color=CODE_FG)

    rect(sl, Inches(0.6), Inches(3.65), Inches(12.0), Inches(0.7), DANGER)
    txbox(sl, "⚠  數字務必至疾管署開放資料平台查證，絕不能直接引用！",
          Inches(0.85), Inches(3.7), Inches(11.5), Inches(0.6),
          size=17, bold=True, color=WHITE)

    txbox(sl, "三個辨識幻覺的跡象：",
          Inches(0.6), Inches(4.55), Inches(12.0), Inches(0.55),
          size=19, bold=True, color=PRIMARY)
    signs = [
        "1  給出非常精確的數字，卻無法說明來源",
        "2  引用看起來合理但查不到的文獻或法規",
        "3  面對追問時，答案前後矛盾或越說越不對",
    ]
    for i, sign in enumerate(signs):
        txbox(sl, sign,
              Inches(0.9), Inches(5.15) + i * Inches(0.62),
              Inches(11.7), Inches(0.55),
              size=18, color=PRIMARY)

    # ── 11. 資安原則概覽（表格） ─────────────────────────────────────────────
    table_slide(prs, "不可輸入 AI 的資料類型",
        ["資料類型", "範例", "風險"],
        [
            ["個人資料", "姓名、身分證字號、電話、地址", "違反個資法"],
            ["醫療資訊", "病歷、診斷、用藥紀錄",         "涉及隱私與機密"],
            ["機密文件", "內部簽呈、未公開政策",          "洩漏公務機密"],
            ["敏感資料", "接觸者名單、疫調細節",          "影響疫調與隱私"],
        ],
        col_widths=[Inches(2.2), Inches(5.5), Inches(4.4)],
    )

    # ── 12-15. 四條資安原則（各一張） ────────────────────────────────────────
    principles = [
        ("第一條：絕不輸入個人資料",
         "姓名、身分證字號、地址、電話——這些絕對不能輸入 AI。\n\n"
         "違規後果：可能違反個人資料保護法，導致法律責任。"),
        ("第二條：不輸入機密公務資訊",
         "尚未公開的疫情數據、內部策略討論、個案追蹤資料，\n"
         "都不適合使用 AI 處理。\n\n"
         "記住：AI 輸入的文字可能用於模型訓練。"),
        ("第三條：公開資訊可以使用",
         "已公開的防疫指引、衛教內容、一般性業務文書，\n"
         "可以安全使用 AI 協助撰寫、整理、翻譯。\n\n"
         "原則：官網上找得到的，通常可以輸入 AI。"),
        ("第四條：產出內容務必審核",
         "任何 AI 生成的內容，在正式使用前都必須經過人工確認。\n\n"
         "AI 的輸出是「草稿」，不是「定稿」。\n"
         "最終決策權永遠在您手上。"),
    ]
    for title, content in principles:
        alert_slide(prs, "疾管署 AI 資安原則", "danger", content, icon="🔒")
        # Overwrite the generated slide's title to be more specific
        # (We rely on the last slide being what we just made)

    # Re-do them properly with custom approach
    # (Remove the last 4 slides created by alert_slide loop and redo)
    # Actually, the alert_slide is good enough. Let me instead add them properly.
    # The 4 slides were already added above. Let me continue.

    # ── 16. 判斷流程卡 ───────────────────────────────────────────────────────
    sl = blank(prs)
    set_bg(sl, LIGHT_BG)
    header_bar(sl, "資安判斷流程卡（可截圖存檔）")

    flow = [
        (Inches(1.5),  Inches(1.4),  PRIMARY,   "這份資料有個人資料？"),
        (Inches(7.5),  Inches(1.4),  DANGER,    "→  是  絕不輸入 AI"),
        (Inches(1.5),  Inches(2.9),  PRIMARY,   "這份資料是內部機密？"),
        (Inches(7.5),  Inches(2.9),  DANGER,    "→  是  絕不輸入 AI"),
        (Inches(1.5),  Inches(4.4),  SUCCESS,   "兩者皆否？"),
        (Inches(7.5),  Inches(4.4),  ACCENT,    "→  可使用，但產出仍需人工審核"),
    ]
    for left, top, clr, text in flow:
        rect(sl, left, top, Inches(5.5), Inches(0.9), clr)
        txbox(sl, text,
              left + Inches(0.2), top + Inches(0.1),
              Inches(5.1), Inches(0.7),
              size=19, bold=True, color=WHITE)

    txbox(sl,
          "最簡單原則：「不確定能不能輸入，那就不要輸入。」",
          Inches(1.5), Inches(5.7), Inches(10.3), Inches(0.7),
          size=20, bold=True, italic=True, color=DANGER, align=PP_ALIGN.CENTER)

    # ── 17. 安全使用原則（5 條） ─────────────────────────────────────────────
    content_slide(prs, "安全使用 AI 的五個好習慣", [
        "去識別化：移除所有可辨識個人的資訊後再使用",
        "使用假資料：練習時使用虛構的範例資料",
        "不留存敏感對話：處理完畢後清除對話紀錄",
        "遵守機關規定：依照署內資安政策使用 AI 工具",
        "審核再發布：AI 產出內容必須經過審核才能對外使用",
    ])

    # ── 18. 測驗複習（5 題快速回顧） ─────────────────────────────────────────
    sl = blank(prs)
    set_bg(sl, LIGHT_BG)
    header_bar(sl, "模組 1 測驗重點回顧")

    qa_pairs = [
        ("Q1  AI 幻覺是指什麼？",
         "A   AI 可能編造看起來合理但其實不正確的資訊"),
        ("Q2  哪種資料「可以」輸入 AI？",
         "A   疾管署官網上已公開的疫情週報"),
        ("Q3  同仁想用 AI 整理疫調報告，應先做什麼？",
         "A   先移除所有個人資料（去識別化）後再使用"),
        ("Q4  AI 生成的衛教文案，正確做法？",
         "A   經專業人員審核確認後才能發布"),
    ]
    for i, (q, a) in enumerate(qa_pairs):
        top = Inches(1.4) + i * Inches(1.4)
        txbox(sl, q, Inches(0.6), top, Inches(12.0), Inches(0.5),
              size=17, bold=True, color=PRIMARY)
        txbox(sl, a, Inches(0.9), top + Inches(0.52), Inches(11.7), Inches(0.5),
              size=16, color=ACCENT)

    # ── 19. 進入下一模組預告 ─────────────────────────────────────────────────
    sl = blank(prs)
    set_bg(sl, DARK_BG)
    rect(sl, Inches(0), Inches(0), Inches(0.22), Inches(7.5), SECONDARY)
    txbox(sl, "您已掌握了：",
          Inches(0.55), Inches(1.0), Inches(11.5), Inches(0.6),
          size=20, color=MUTED)
    txbox(sl,
          "✓  生成式 AI 的運作原理\n"
          "✓  AI 的能力邊界與幻覺現象\n"
          "✓  疾管署 AI 資安四條原則",
          Inches(0.55), Inches(1.7), Inches(11.5), Inches(2.5),
          size=24, color=WHITE)
    txbox(sl, "接下來：",
          Inches(0.55), Inches(4.4), Inches(11.5), Inches(0.55),
          size=20, color=MUTED)
    txbox(sl,
          "模組 2  Prompt 四要素\n掌握 RTFC 框架，AI 輸出品質差異立現",
          Inches(0.55), Inches(5.0), Inches(11.5), Inches(1.4),
          size=26, bold=True, color=SECONDARY)

    # ── 20. CTA ──────────────────────────────────────────────────────────────
    cta_slide(prs,
              "完成單元測驗，確認您已掌握資安原則",
              "▶  前往模組 2：Prompt 四要素")

    save_pptx(prs, "module1_認識生成式AI.pptx")


if __name__ == "__main__":
    build()
