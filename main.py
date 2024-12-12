from aiogram import Bot, Dispatcher
from config_data.config import bot_token 
from handlers.user_handlers import router


bot = Bot(bot_token)
dp = Dispatcher()

dp.include_router(router)

# Запуск новосного бота 


if __name__ == '__main__':
    dp.run_polling(bot)