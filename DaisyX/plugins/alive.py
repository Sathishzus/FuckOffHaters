from pyrogram import Filters
from DaisyX import app

@app.on_message(Filters.regex("^.alive"))
def amialivedad(event):
    chat = event.chat.id 
    message = " Master ! I am alive :)"
    app.edit_message_text(chat_id=chat, message_id="me", text=message)
