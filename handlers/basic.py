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


# @db.message_handler(commands=["start"])
async def cmd_start(message: types.Message):
    await message.answer(
        f"""
            Доброго времени {message.from_user.full_name}!
        Мы HR компания BAUMAN !
        """,
        reply_markup=kb
    )
    await message.delete()

# @db.message_handler(commands=["help"])
async def cmd_help(message: types.Message):
    await message.answer(
        f"""
        /start - приветствует по имени
        /help - показывает список команд
        /myinfo - отправляет пользователю его данные(id, first_name, username)
        /picture - отправляет слуайную картинку
        """
    )


# @db.message_handler(commands=["myinfo"])
async def cmd_myinfo(message: types.Message):
    await message.answer(
        f"ID         {message.from_user.id}\n"
        f"FIRST_NAME {message.from_user.first_name}\n"
        f"USER_NAME  {message.from_user.username}\n"
    )


# @db.message_handler(commands=["picture"])
async def cmd_picture(message: types.Message):
    img = ["img/img_1.png", "img/img_2.png", "img/img_3.png"]
    photo = open(random.choice(img), "rb")
    await message.answer_photo(
        photo
    )