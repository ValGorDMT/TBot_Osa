from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import CallbackQuery, Message, ReplyKeyboardRemove
import app.keyboards as kb
#from app.keyboards import main это импорт конкретной переменой, а выше импорт всех переменных и сокращение ее пути до 2х символов


router = Router()

# answer - отправить сообщение
# reply - ответить на сообщение
#AgACAgIAAxkBAAICj2cTzKzLm9nG8VZpAAEP6-7dKzVt8QAC798xG3vboEj9-yeNNvUhQgEAAwIAA3kAAzYE
#AgACAgIAAxkBAAIBvWcS97hpbwubFRxWzic-NGTaUgq6AAIq5TEbe9uYSNBxOTRg7iupAQADAgADeQADNgQ

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer_photo(photo='AgACAgIAAxkBAAIBvWcS97hpbwubFRxWzic-NGTaUgq6AAIq5TEbe9uYSNBxOTRg7iupAQADAgADeQADNgQ', #Этот айдишник получил с помощью команды ниже
                              caption=f'Привет {message.from_user.first_name}! Твой ID: {message.from_user.id}',
                              reply_markup=kb.startkb)
    
@router.callback_query(F.data == 'startkb')
async def cmd_menu(callback: CallbackQuery):
    await callback.message.delete()
    await callback.answer()
    await callback.message.answer_photo(photo='AgACAgIAAxkBAAICj2cTzKzLm9nG8VZpAAEP6-7dKzVt8QAC798xG3vboEj9-yeNNvUhQgEAAwIAA3kAAzYE',
                                        caption='И так', 
                                        reply_markup=kb.main)

@router.message(Command('clear'))
async def clear(message: Message):
    await message.answer('удалено', reply_markup=ReplyKeyboardRemove(),)

@router.message(F.photo)
async def id_foto(message: Message):
    await message.answer(f'ID: {message.photo[-1].file_id}')

@router.message(Command('help'))
async def get_help(message: Message):
    await message.answer('Помощь')

@router.message(F.text=='Как дела')
async def hau(message: Message):
    await message.answer('Норм')

@router.callback_query(F.data == "add_to_list")
async def add_to_list(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer("Добавлено")

@router.callback_query(F.data == "delete_to_list")
async def delete_to_list(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer("Удалено")

@router.callback_query(F.data == "my_list")
async def my_list(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer("Вот твой список")

