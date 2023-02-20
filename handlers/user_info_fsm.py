from aiogram import types
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery


class UserForm(StatesGroup):
    name = State()
    age = State()
    address = State()
    day = State()


async def start_user_dialog(message: types.Message):
    await UserForm.name.set()
    await message.answer("whats ur name?")


async def process_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        # сохраяем данные о имени
        data['name'] = message.text

    await UserForm.next()
    await message.answer("how old a u?")


async def process_age(message: types.Message, state: FSMContext):
    age = message.text
    if not age.isnumeric():
        await message.reply("only nums")
    else:
        async with state.proxy() as data:
            # сохраняем данные о возрасте
            data['age'] = age

    await UserForm.next()
    await message.answer("ur addres?")


async def process_address(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        # сохраяем данные о адресе
        data['address'] = message.text
        kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buttons = ["mon", "tus", "wen", "thurs", "fri", "sut"]
        kb.add(*buttons)

    await UserForm.next()
    await message.answer("when you can come to us?\n"
                         "we working at: mon-sat, sunday is day off", reply_markup=kb)


async def process_day(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        # сохраяем данные о дне недели для получения товара
        data['day'] = message.text
        buttons = [
            types.InlineKeyboardButton(text='да', callback_data='да'),
            types.InlineKeyboardButton(text='нет', callback_data='нет')
        ]
        kb = types.InlineKeyboardMarkup(row_width=2)
        kb.add(*buttons)
        print(data)

    await state.finish()
    await message.answer("thanks for using our cervise, u want to sand message?",
                         reply_markup=kb)


async def mail(callback: CallbackQuery):
    """
    обработчик, чтоб принять сообщение
    """
    await callback.answer()
    message = callback.message
    await message.bot.send_message(
        text=f'{callback.from_user.first_name} we send your message to admin!',
        chat_id=message.chat.id
    )


async def not_mail(callback: CallbackQuery):
    """
    обработчик, чтоб попращаться
    """
    await callback.answer()
    message = callback.message
    await message.bot.send_message(
        text=f'{callback.from_user.first_name} good bye!',
        chat_id=message.chat.id
    )