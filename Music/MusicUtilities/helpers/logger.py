
from Music.config import LOG_GROUP_ID
from Music import app
)
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

async def LOG_CHAT(message, what):
    if message.chat.username:
        chatusername = (f"@{message.chat.username}")
    else:
        chatusername = ("Private Group")
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    mention = "["+user_name+"](tg://user?id="+str(user_id)+")" 
    logger_text = f"""
**🤖 New {what}**

**📮 Chat:** {message.chat.title}
**📮 Chat ID: `{message.chat.id}`
**📮 Name:** {mention}
**📮 Username:** @{message.from_user.username}
**📮 User ID:** `{message.from_user.id}`
**📮 Chat Link:** {chatusername}
**📮 Query:** {message.text}"""
    await app.send_message(LOG_GROUP_ID, f"{logger_text}", disable_web_page_preview=True)
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Support", url=f"message.from_user.first_name"
                    )
                ]
            ]
        )
    )
