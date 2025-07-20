from pyrogram import Client
from pyrogram.types import ChatMemberUpdated
import os
from dotenv import load_dotenv

load_dotenv()

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_USER_ID = int(os.getenv("ADMIN_USER_ID"))

app = Client("leave_tracker", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_chat_member_updated()
async def on_leave(client: Client, update: ChatMemberUpdated):
    if update.left_chat_member:
        user = update.left_chat_member
        chat = update.chat
        text = (
            f"👤 کاربر لفت داد:\n"
            f"نام: {(user.first_name or '')} {(user.last_name or '')}\n"
            f"یوزرنیم: @{user.username or 'ندارد'}\n"
            f"آیدی عددی: `{user.id}`\n"
            f"از کانال: {chat.title}"
        )
        await app.send_message(ADMIN_USER_ID, text)

if __name__ == "__main__":
    app.run()
