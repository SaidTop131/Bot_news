from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from lexicon.lexicon_ru import LEXICON_RU
from keyboards.keyboard import keyboard
from asyncio import sleep
import json
from parsers.parser_news import pars

router = Router()

@router.message(CommandStart())
async def start_news(message: Message):
    pars('test')
    await message.answer('Получаю новости футбола')
    await sleep(3)
    await message.answer('Новости загружены', reply_markup=keyboard)
    
@router.message(Command(commands='help'))
async def help(message: Message):
    await message.answer('Основные команды: \n'
                         'Загрузить все новости - /all_news\n')
    
@router.message(F.text == LEXICON_RU['but1'])
async def get_news(message: Message):
    with open('test.json','r',encoding='utf-8') as file:
        new_dict = json.load(file)
        for key, val in new_dict.items():
            news = f'{val["article_time"]}\n'\
                f'{val["article_url"]}\n'\
                    f'{val["article_title"]}\n'\
                        f'{val["article_desc"]}\n'\
                
            await message.answer(news)
 
@router.message(F.text == LEXICON_RU['but3'])
async def get_5_news(message: Message):
    with open('test.json','r',encoding='utf-8') as file:
        new_dict = json.load(file)
        for key, val in sorted(new_dict.items())[-5:]:
            news = f'{val["article_time"]}\n'\
                f'{val["article_url"]}\n'\
                    f'{val["article_title"]}\n'\
                        f'{val["article_desc"]}\n'\
            
            await message.answer(news)                
    
 
   
   

@router.message(F.text == LEXICON_RU["but2"])
async def fresh_news(message: Message):
    pars('new')
    list_id = []
    with open('new.json', 'r', encoding='utf-8') as file:
        new_dict = json.load(file)
    with open('test.json', 'r', encoding='utf-8') as file1:
        old_dict = json.load(file1)
    for news_id in new_dict.keys():
        if news_id not in old_dict.keys():
            list_id.append(news_id)
    if len(list_id) > 0:
        with open('test.json', 'w', encoding='utf-8') as file:
            json.dump(new_dict, file, indent = 4, ensure_ascii=False)
        for news_id in sorted(list_id):
            news = f'{new_dict[news_id]["article_time"]}\n'\
                   f'{new_dict[news_id]["article_url"]}\n'
            await message.answer(news)
        await message.answer("Новости добавлены в базу")
    else:
        await message.answer("Свежих новостей нет, попробуйте позже") 
                    
