# python -m pip install --upgrade pip
# pip install pytelegrambotapi

# №1
# ЭХО-БОТ

# import telebot
# from datetime import date
#
# # # Создаем бота
# bot = telebot.TeleBot('...')
#
#
# @bot.message_handler(commands=['start'])
# def send_welcome(message):
# 	bot.send_message(
# 		message.chat.id,
# 		f'''
# Привет, {message.from_user.first_name} {message.from_user.last_name}!
# Напиши что-нибудь!
# '''
# 	)
#
# @bot.message_handler(content_types=["text"])
# def say_echo(message):
# 	bot.send_message(message.chat.id, f'Ты написал мне: {message.text}!')
#
#
# bot.polling(none_stop=True)

#######################################################################
# homework
# Создать телеграм-бот (можно редактировать существующий).
# Бот при команде /start просит ввести число и проверяет, нечётное оно или чётное.
# Затем, выводит сообщение:
#
# (Число, которое ввел пользователь) - это число нечётное (или чётное)!

# import telebot
#
# # # Создаем бота
# bot = telebot.TeleBot('5245877443:AAGm7Gtt76CMg6RENHkm3xlos8RbiFTbub8')
#
#
# @bot.message_handler(commands=['start'])
# def send_welcome(message):
# 	bot.send_message(
# 		message.chat.id,
# 		f'''
# Привет, {message.from_user.first_name} {message.from_user.last_name}!
# Напиши число, а я скажу, чётное оно или нет!
# '''
# 	)
#
# @bot.message_handler(content_types=["text"])
# def is_parity(message):
# 	try:
# 		value = int(message.text)
# 		if value % 2 != 0:
# 			text = 'нечетное'
# 		else:
# 			text = 'четное'
# 		bot.send_message(message.chat.id, f'{value} - это число {text}!')
#
# 	except:
# 		bot.send_message(message.chat.id, 'Ты ввел не число!')
#
#
# bot.polling(none_stop=True)

#######################################################################
#######################################################################

# Set Age Bot
# import telebot
# from datetime import date
#
# # # Создаем бота
# bot = telebot.TeleBot('5245877443:AAGm7Gtt76CMg6RENHkm3xlos8RbiFTbub8')
#
#
# @bot.message_handler(commands=['start'])
# def send_welcome(message):
#     bot.send_message(
#         message.chat.id,
#         f'''
# Привет, {message.from_user.first_name} {message.from_user.last_name}!
# Напиши год своего рождения и я скажу, сколько тебе лет!
# '''
#     )
#
# @bot.message_handler(content_types=["text"])
# def set_age(message):
#     try:
#         age = date.today().year - int(message.text)
#         last_number = str(age)[-1]
#         penultimate_number = str(age)[-2]
#
#         if age > 0:
#             bot.send_message(message.chat.id, f'Тебе: {age} лет!')
#         else:
#             bot.send_message(message.chat.id, 'Ты ввел неправильный год рождения!')
#     except:
#         bot.send_message(message.chat.id, 'Я тебя не понимаю)')
#
#
# bot.polling(none_stop=True)

######################################################################
# homework
# Редактировать бота, устанавливающего возраст пользователя.
# Он должен использовать правильные окончания предложения.
# Например, 12 лет или 32 года. Предусмотреть все варианты возраста.

##################################################################
# import telebot
# from datetime import date
#
# # # Создаем бота
# bot = telebot.TeleBot('5245877443:AAGm7Gtt76CMg6RENHkm3xlos8RbiFTbub8')
#
#
# @bot.message_handler(commands=['start'])
# def send_welcome(message):
# 	bot.send_message(
# 		message.chat.id,
# 		f'''
# Привет, {message.from_user.first_name} {message.from_user.last_name}!
# Напиши год своего рождения и я скажу, сколько тебе лет!
# '''
# 	)
#
# @bot.message_handler(content_types=["text"])
# def set_age(message):
# 	try:
# 		age = date.today().year - int(message.text)
# 		last_number = str(age)[-1]
# 		penultimate_number = str(age)[-2]
#
# 		if age > 0:
# 			if penultimate_number == '1':
# 				text = 'лет'
# 			else:
# 				if last_number == '1':
# 					text = 'год'
# 				elif last_number == '2' or last_number == '3' or last_number == '4':
# 					text = 'года'
# 				else:
# 					text = 'лет'
# 			bot.send_message(message.chat.id, f'Тебе: {age} {text}!')
# 		else:
# 			bot.send_message(message.chat.id, 'Ты ввел неправильный год рождения!')
#
# 	except:
# 		bot.send_message(message.chat.id, 'Я тебя не понимаю)')
#
#
# bot.polling(none_stop=True)
#######################################################################
#######################################################################

# №3
# WIKIPEDIA-БОТ
# pip install wikipedia

# import telebot, wikipedia
#
# # # Создаем бота
# bot = telebot.TeleBot('5245877443:AAGm7Gtt76CMg6RENHkm3xlos8RbiFTbub8')
#
# # Устанавливаем русский язык
# wikipedia.set_lang("ru")
#
# def get_page(page):
#     try:
#         resp = wikipedia.page(page)
#
#         # Получаем первую тысячу символов
#         page_text = resp.content[:1000]
#
#         # Разделяем по точкам
#         page_list = page_text.split('.')
#
#         # Отбрасываем всЕ после последней точки
#         page_list = page_list[:-1]
#
#         # Фильтруем от '==' (заголовки)
#         page_list = list(filter(lambda x: not ('==' in x), page_list))
#
#         # Преобразуем к строке
#         str = '.'.join(page_list)
#
#         # Возвращаем строку
#         return str
#
#     # Обрабатываем исключение, которое мог вернуть модуль wikipedia при запросе
#     except:
#         return 'В Википедии об этом ничего нет('
#
#
# @bot.message_handler(commands=['start'])
# def send_welcome(message):
# 	bot.reply_to(message, "Отправь мне любое слово, и я найду его значение в Википедии!")
#
#
# # Получение сообщений от пользователя
# @bot.message_handler(content_types=["text"])
# def handle_text(message):
#     bot.send_message(message.chat.id, get_page(message.text))
#
#
# bot.infinity_polling()


#########################################################
#########################################################

# Game-bot

# import telebot, random
# from telebot import types
#
# bot = telebot.TeleBot('5245877443:AAGm7Gtt76CMg6RENHkm3xlos8RbiFTbub8')
#
# def build_menu(buttons, n_cols,
#                header_buttons=None,
#                footer_buttons=None):
#     menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
#     if header_buttons:
#         menu.insert(0, [header_buttons])
#     if footer_buttons:
#         menu.append([footer_buttons])
#     return menu
#
#
# button_list = [
# 	types.InlineKeyboardButton(text='1', callback_data='1'),
# 	types.InlineKeyboardButton(text='2', callback_data='2'),
# 	types.InlineKeyboardButton(text='3', callback_data='3'),
# 	types.InlineKeyboardButton(text='4', callback_data='4'),
# 	types.InlineKeyboardButton(text='5', callback_data='5'),
# ]
#
#
# def play_again(call):
# 	bot.send_message(
# 		call.message.chat.id,
# 		'Если хочешь играть ещё раз, нажми кнопку /game!'
# 	)
# 	value = random.randint(1, 5)
#
# @bot.message_handler(commands=['start'])
# def start(message):
# 	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
# 	markup.add(types.KeyboardButton("/game"))
# 	bot.send_message(
# 		chat_id=message.chat.id,
# 		text=f'''Привет, {message.from_user.first_name} {message.from_user.last_name}!
# Если хочешь поиграть, нажми на кнопку /game!''',
# 		reply_markup=markup
# 	)
#
# @bot.message_handler(commands=["game"])
# def game(message):
# 	markup = types.InlineKeyboardMarkup(build_menu(button_list, n_cols=2))
#
# 	bot.send_message(
# 		chat_id=message.chat.id,
# 		text="Я загадал число от 1 до 5, а ты попробуй его отгадать!",
# 		reply_markup=markup
# 	)
#
#
# @bot.callback_query_handler(func=lambda call: True)
# def callback_inline(call):
# 	value = random.randint(1, 5)
#
# 	if int(call.data) == value:
# 		bot.send_message(call.message.chat.id, 'Ты отгадал!)')
# 		play_again(call)
# 	else:
# 		bot.send_message(
# 			call.message.chat.id,
# 			f'Ты не отгадал. я загадал число {value}'
# 		)
# 		play_again(call)
#
#
# bot.polling(none_stop=True)


################################################
################################################
