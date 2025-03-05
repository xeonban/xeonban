# Autoclr Bot

Autoclr Bot is a Telegram bot built using Pyrogram that automatically deletes join and leave messages in a chat. It also includes a simple Flask web server to keep the bot running.

## Requirements

- Python 3.6+
- Telegram Bot Token
- API ID and API Hash from [my.telegram.org](https://my.telegram.org)

## Installation

1. Clone the repository:

    ```sh
    git clone  https://github.com/xeonban/xeonban
    cd xeonban
    ```

2. Install the required packages:

    ```sh
    pip install -r requirements.txt
    ```

3. Create a [.env] file in the root directory and add your bot token, API ID, API Hash, and port:

    ```env
    BOT_TOKEN=your_bot_token
    API_HASH=your_api_hash
    API_ID=your_api_id
    PORT=5000
    ```

## Usage

1. Run the bot:

    ```sh
    python bot.py
    ```

2. The bot will start and automatically delete join and leave messages in the chat.

## Files

- [bot.py]: Main bot script.
- [requirements.txt]: List of required Python packages.
- [.env]: Environment variables file.

## License

This project is licensed under the MIT License.