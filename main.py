from aiogram import executor, types
from aiogram.dispatcher.filters import Text
from config import dp
from handlers.user_info_fsm import (
  UserForm,
  srart_user_dialog,
  process_name,
  process_age
)

from handlers.admin import (
    on_user_joined,
    filter_messages,
    cmd_ban
)
from handlers.filters import IsAdminFilter





if __name__ == "__main__":
    dp.filters_factory.bind(IsAdminFilter)
    dp.register_message_handlers(on_user_joined, content_types=["new_chat_members"])
    dp.register_message_handler(filter_messages)
    dp.register_message_handler(cmd_ban, is_admin=True, commands=['ban'], commands_prefix='!/')
    print('hello')
    executor.start_polling(dp)

