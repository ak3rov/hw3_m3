from aiogram.types import message
from aiogram import types
from config import schrduler, bot
from datetime import datetime

async def notify_command_handler(mesage: types.Message):
    schrduler.add_job(notify, 'interval', seconds=5, args=(message.from_user.id,))
    await message.answer('принято')

async  def notify_date_handler(message: types.Message):
    schrduler.add_job(notify, 'date', datetime(year=2023, month=3, day=1, hour=16), args=(message.from_user.id,))
    await  message.answer('принято')


async def notify_priodic_handler(message: types.Message):
    schrduler.add_job(notify, 'cron', args=(message.from_user.id, ))
    await  message.answer('принято')

async def notify(iser_id: int):
    await  bot.send_message(
        text='напоминалка',
        chat_id=iser_id
    )