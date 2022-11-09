from aiogram import types
from aiogram.dispatcher import FSMContext

from db import reports
from app import dp, bot
from utils import buttons, messages
import handlers.frequent_cases as fq
from utils.states import Report
from random import randint


async def get_random_name():
    s = ''
    for i in range(16):
        s = s + str(randint(0, 9))
    return s


async def write_file(message):
    file_info = await bot.get_file(message.document.file_id)
    downloaded_file = await bot.download_file(file_info.file_path)
    src = '../db/files/' + await get_random_name()
    with open(src, 'wb') as new_file:
        new_file.write(downloaded_file.read())
    return src


@dp.message_handler(lambda m: m.text == buttons.create_new_order_btn.text)
async def create_order_command(message: types.Message):
    await message.reply(messages.SEND_DOCUMENT, reply_markup=buttons.back_to_menu_btn)
    await Report.set_file.set()


@dp.message_handler(state=Report.set_file, content_types=['document', 'photo', 'text'])
async def add_document_command(message: types.Message, state: FSMContext):
    await message.answer(str(message))  # in future comment this
    if message.text == buttons.back_to_menu_btn.text:
        await state.finish()
        return await fq.welcome_command(message)
    src = await write_file(message)
    async with state.proxy() as data:
        data["set_file"] = src
    await message.answer(messages.WRITE_DESCRIPTION)
    await Report.set_description.set()


@dp.message_handler(state=Report.set_description)
async def add_description_command(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        information = data.as_dict()
    reports.add_new(user_id=message.from_user.id, path=information['set_file'], description=message.text)
    await state.finish()
    await message.answer(messages.UPDATED)
    await fq.welcome_command(message)
