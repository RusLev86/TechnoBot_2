import telebot

# Вставьте свой токен
TOKEN = ''
bot = telebot.TeleBot(TOKEN)

# Удаляем вебхук
bot.remove_webhook()

# Запускаем опрос
bot.polling(none_stop=True)

import asyncio
import logging

from maxapi import Bot, Dispatcher, F
from maxapi.types import MessageCreated

logging.basicConfig(level=logging.INFO)

bot = Bot()
dp = Dispatcher()


@dp.message_created(F.message.body.text)
async def echo(event: MessageCreated):
    await event.message.answer(f"Повторяю за вами: {event.message.body.text}")


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
