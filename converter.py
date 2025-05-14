import html2text                                           # :contentReference[oaicite:0]{index=0}
import telegramify_markdown as tgmd                        # :contentReference[oaicite:1]{index=1}


# ─── your bot token and chat/group ID ────────────────────────────────────────
TOKEN   = "YOUR_BOT_TOKEN_HERE"
CHAT_ID = 123456789

def html_to_markdown_v2(html: str) -> str:
    """
    1) Parse & convert HTML → CommonMark via html2text.HTML2Text
    2) Escape that Markdown → Telegram-safe MarkdownV2 via telegramify_markdown.markdownify()
    """
    h = html2text.HTML2Text()   # use the class, not the standalone function
    h.body_width = 0            # disable wrapping
    # h.protect_links = True    # optional: avoid line-break wraps around [text](url)
    common_md = h.handle(html)  # :contentReference[oaicite:3]{index=3}

    # Convert raw Markdown → Telegram MarkdownV2
    return tgmd.markdownify(common_md)

html = """
<p>Уважаемые сотрудники группы компаний DAACDigital!</p><p>Система Doctrina вновь готова помогать развивать персональные компетенции, знакомить вас с внутренними регламентами и приказами, а также обеспечивать проверку ключевых профессиональных знаний, необходимых для выполнения своих обязанностей. Система обновилась и приобрела новый язык интерфейса - румынский. Doctrina доступна по ссылке <a href="https://doc.daacdigital.com/">doc.daacdigital.com</a>, или через Telegram бот (ссылка на бот размещена на первой странице после входа в приложение).</p><p>Следите за обновлениями и новыми возможностями – перед нами большие задачи, и вместе мы сможем достичь больших результатов!</p><p>Желаем успехов.</p> 
"""
print(html_to_markdown_v2(html))

