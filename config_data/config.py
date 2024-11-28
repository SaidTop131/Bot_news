from environs import Env
URL = 'https://sport24.ru/football'
env = Env()
env.read_env()
bot_token = env('BOT_TOKEN')
