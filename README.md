pyng
====

Pyng is a bare-bones uptime monitor relying on a Telegram bot for notifications.

It requires Python 3 and the [requests](docs.python-requests.org/) module.

Getting started
---------------

In order to use pyng, you first need to vitit [telegram.me/botfather](telegram.me/botfather) and type `/newbot` to create a bot. You should get a reply that asks you to choose a name for your bot. You can name it whatever you want. BotFather will then ask you to pick a username for your bot. Bot usernames have to end in `bot`. From now on I'll refer to it as `<your-bot-username>` BotFather will now send you a "Congratulations" message, including your bot's token. I'll refer to that as `<your-bot-token>`.

Visit `t.me/<your-bot-username>`, or search for `@<your-bot-username>` in any Telegram client to start a conversation with your bot. Press the `/start` button at the bottom of the chat window.

Now visit `https://api.telegram.org/bot<your-bot-token>/getUpdates`. Try to locate this section of the JSON-formatted text:

    "chat":{"id":XXXXXXXXX,

I'll refer to that number as `<your-chat-id>`.

Now open `pyng.py` with your favorite editor and replace the string after these constants:

*   `SITE = '<url-of-the-site-you-want-to-monitor>'`
*   `TOKEN = '<your-bot-token>'`
*   `CHAT_ID = '<your-chat-id>'`

That's it! Now you need to find a way to run pyng periodically. I've scheduled a cron job to run it every minute, like this:

    * * * * * python3 /path/to/pyng/pyng.py

Now pyng will inform you every time your site goes down and when it comes back up!
