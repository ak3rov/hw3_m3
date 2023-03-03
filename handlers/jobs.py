from aiogram import types

from const import (
COURIER,
COLLECTOR,
MERCHANDISER
)


kb = types.ReplyKeyboardMarkup()
kb.add(
    types.KeyboardButton("Курьером")
)
kb.add(
    types.KeyboardButton("Сборщиком")
)
kb.add(
    types.KeyboardButton("товароведом")
)

# async def show_jobs(message: types.Message):
#     chat_id = message.from_user.id
#     await bot.send_message(
#         chat_id=chat_id,
#         text="Доброго времени суток кем вы хотите работать ? ",
#         reply_markup=kb
#     )


async def show_jobs(call: types.CallbackQuery):
    await call.message.answer(
        text="Мы можем вам подобрать работу",
        reply_markup=kb
    )


async def show_courier(message: types.Message):
    await message.reply(COURIER)


async def show_collector(message: types.Message):
    await message.reply(COLLECTOR)


async def show_merchandiser(message: types.Message):
    await message.reply(MERCHANDISER)