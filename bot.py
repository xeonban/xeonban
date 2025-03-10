from pyrogram import Client, filters
import logging
from dotenv import load_dotenv
import os
from flask import Flask
import threading
import time

# Load environment variables from .env file
load_dotenv()

API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
PORT = int(os.getenv("PORT", 5000))

# Configure logging with emojis
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - 💀🔫¸ %(message)s')

bot_app = Client("Autoclr", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Flask app for web server
flask_app = Flask(__name__)

@flask_app.route('/')
def home():
    return "Bot is running!"

@flask_app.route('/ping')
def ping():
    return "pong"

def run_web():
    flask_app.run(host='0.0.0.0', port=PORT)

def keep_alive():
    server = threading.Thread(target=run_web)
    server.start()

# Delete join messages
@bot_app.on_message(filters.new_chat_members)
async def delete_join_message(client, message):
    try:
        await message.delete()
        logging.info(f"🗑️ Deleted join message in {message.chat.title}")
    except Exception as e:
        logging.error(f"⚠️ Error deleting join message: {e}")

# Delete leave messages
@bot_app.on_message(filters.left_chat_member)
async def delete_leave_message(client, message):
    try:
        await message.delete()
        logging.info(f"🗑️ Deleted leave message in {message.chat.title}")
    except Exception as e:
        logging.error(f"⚠️ Error deleting leave message: {e}")

# Ping command
@bot_app.on_message(filters.command("ping"))
async def ping_command(client, message):
    start_time = time.time()
    await message.reply_text("pong")
    end_time = time.time()
    response_time = int((end_time - start_time) * 1000)
    await message.reply_text(f"Response time: {response_time} ms")
    logging.info(f"🏓 Ping command received and replied with pong in {response_time} ms")

if __name__ == "__main__":
    keep_alive()
    bot_app.run()