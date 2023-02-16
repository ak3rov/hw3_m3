import state
from  aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filtres.state import State, StatesGroup
from aiogram.types import message


class UserForm(StatesGroup):
    name = State()
    age = State()

async def start_user_dialog(massage: types.Message):
    UserForm.name.set()
    await message.answer('what is your name?')


async def process_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    UserForm.next()
    await message.answer('how old are you?')


async def process_age(message: types.Message, state: FSMContext):
    age = message.text
    if not age.is_numeric():
        await message.answer('enter only nums!')
    else:
        async with state.proxy() as data:
            data['age'] = age
            print(data)

await state.finish()

await message.answer('thanks for using us bot!')