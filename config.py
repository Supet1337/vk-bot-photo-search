vk_token = 'vk1.a.HkZsS9LOXaf_0JpgKcwXyq8H7Bf1YB8bBEmUR0LQEIx0nD3NVArqlKspXS8EjIoHw4YSEFs95iCuZgwod_ufOSUgEz0a-ogkULbY1mBEC9pOpMN908IEGeu7bI-Qd4DjQZyDg4tymh9dKowX8ONeeTYoFpjoWpYWK3UBjHXMd6f69SF-ac0z9jp8Y66vb0YNAJjSK1ioIzZx9xp8G6prZA'
bot_token = '5870749218:AAFIZ_JVleg1G_ioXlpU0VthydsXN8GsM7o'



# @bot.message_handler(content_types='text')
# def get_photo(message):
#     if message.text == "Хочу фото!" or message.text == "Хочу ещё" or message.text == "Ещё?":
#         msg = bot.send_message(message.chat.id, "Так, а теперь скажи какое фото тебе прислать")
#         bot.register_next_step_handler(msg, send_photo)
#     else:
#         bot.send_message(message.chat.id, "Я тебя не очень понимаю")
#
# def send_photo(message):
#     try:
#         url_photos_info = f'https://api.vk.com/method/photos.search?q={message.text}о&count=100&access_token={vk_token}&v=5.131'
#         req_url_photos_info = requests.get(url_photos_info)
#         jsn_photos = req_url_photos_info.json()
#
#         bot.send_message(message.chat.id, "Лови")
#         bot.send_photo(message.chat.id, jsn_photos['response']['items'][random.randint(0, 100)]['sizes'][3]['url'])
#
#         markup = types.InlineKeyboardMarkup()
#         markup.add(types.InlineKeyboardButton(text='Ещё?', callback_data='again'))
#         markup.add(types.InlineKeyboardButton(text='Покажи похожие', callback_data='more'))
#         bot.send_message(message.chat.id, "Что дальше?",  reply_markup=markup)
#
#     except:
#         bot.send_message(message.chat.id, "Что-то пошло не так!")
#
# @bot.callback_query_handler(func=lambda call: True)
# def callback_inline(call):
#     if call.message:
#         if call.data == "again":
#             bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Окей")
#             get_photo(call.message)
#         if call.data == "more":
#             bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Окей")
#             send_photo(call.message)
#
# bot.infinity_polling()