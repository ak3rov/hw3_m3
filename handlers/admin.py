from aiogram import types

import config


async def on_user_joined(message: types.Message):
    await message.delete()

async def filter_messages(message: types.Message):
    if "Bad word" in message.text:
        await message.delete()

async def cmd_ban(message: types.Message):
    if not message.reply_to_message:
        await message.reply('this command needs to be a reply!')
        return
    await message.bot.delete_message(chat_id=config.GROUP_ID)
    await message.bot.kick_chat_member(chat_id=config.GROUP_ID,user_id=message.reply_to_message.from_user.id)

    await message.reply_to_message.reply('user is banned!')