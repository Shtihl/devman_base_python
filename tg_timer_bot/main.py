import os
import ptbot
import random
from pytimeparse import parse


TG_TOKEN = os.environ['TG_TOKEN']


def render_progressbar(total, iteration, prefix='', suffix='', length=30, fill='█', zfill='░'):
    iteration = min(total, iteration)
    percent = "{0:.1f}"
    percent = percent.format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    pbar = fill * filled_length + zfill * (length - filled_length)
    return '{0} |{1}| {2}% {3}'.format(prefix, pbar, percent, suffix)


def notify(secs_left, chat_id, message_id, user_timer):
    bot.update_message(
        chat_id,
        message_id,
        "Осталось {} секунд!\n{}".format(
            secs_left,
            render_progressbar(user_timer, user_timer - secs_left)
        )
    )


def times_up(chat_id):
    bot.send_message(chat_id, "Время вышло")


def reply(chat_id, text):
    user_timer = parse(text)
    message_id = bot.send_message(chat_id, "Запуск таймера")
    bot.create_countdown(
        user_timer,
        notify,
        chat_id=chat_id,
        message_id=message_id,
        user_timer=user_timer
    )
    bot.create_timer(
        user_timer,
        times_up,
        chat_id=chat_id,
    )


if __name__ == "__main__":
    bot = ptbot.Bot(TG_TOKEN)
    bot.reply_on_message(reply)
    bot.run_bot() 