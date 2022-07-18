from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters

import click
import os


def unknown(update: Update, _):
    update.message.reply_text(
        f"The command {update.message.text} is just wrong, bruh :/\n")


def start(update: Update, _):
    update.message.reply_text(
        "gimmi ur books bro"
    )


def choose_book(update: Update, _):
    update.message.reply_text(
        "choosing"
    )


def add_new_book(update: Update, _):
    update.message.reply_text(
        "adding"
    )


def delete_book(update: Update, _):
    update.message.reply_text(
        "deleting"
    )


def add_pages(update: Update, _):
    update.message.reply_text(
        "deleting"
    )

# https://www.google.com/search?q=telegram+python+make+button&rlz=1C1CHBF_deDE902DE902&oq=telegram+python+make+button&aqs=chrome..69i57j33i160l2j33i22i29i30l6.5566j0j7&sourceid=chrome&ie=UTF-8#kpvalbx=_tI3QYt2MIOLjsAfR8biYCQ20


@click.command()
@click.option('--local', is_flag=True)
def main(local):
    """Simple program that greets NAME for a total of COUNT times."""
    if local:
        with open("TELEGRAM_TOKEN.env", "r") as f:
            token = f.readline()
    else:
        token = os.environ['TELEGRAM_TOKEN']

    updater = Updater(token, use_context=True)
    commands = [start, add_new_book, add_pages, choose_book, delete_book]
    for c in commands:
        updater.dispatcher.add_handler(CommandHandler(c.__name__, c))
    updater.dispatcher.add_handler(MessageHandler(
        Filters.command, unknown))  # Filters out unknown commands
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
