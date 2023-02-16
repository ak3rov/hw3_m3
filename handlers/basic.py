from aiogram import types
import random
from config import bot

kb = types.InlineKeyboardMarkup()
kb.add(types.InlineKeyboardButton(
    text="Вакансии",
    callback_data="jobs"
))
kb.add(types.InlineKeyboardButton(
    text="О нас",
    callback_data="about"
))


# @dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message):
    await message.answer(
        f"""
            Доброго времени {message.from_user.full_name}!
        Мы HR компания puma !
        """,
        reply_markup=kb
    )
    await message.delete()

# @dp.message_handler(commands=["help"])
async def cmd_help(message: types.Message):
    await message.answer(
        f"""
        /start - приветствует по имени
        /help - показывает список команд
        /myinfo - отправляет пользователю его данные(id, first_name, username)
        /picture - отправляет слуайную картинку
        """
    )


# @dp.message_handler(commands=["myinfo"])
async def cmd_myinfo(message: types.Message):
    await message.answer(
        f"ID         {message.from_user.id}\n"
        f"FIRST_NAME {message.from_user.first_name}\n"
        f"USER_NAME  {message.from_user.username}\n"
    )


# @dp.message_handler(commands=["picture"])
async def cmd_picture(message: types.Message):
    img = ["watch.png", "watch.png", "70119eba3b9c1aaf0cc490012ccdf90a.jpg"]
    photo = open(random.choice(img), "rb")
    await message.answer_photo(
        photo
    )