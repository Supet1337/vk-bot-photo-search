import telebot
import requests
import random
from config import vk_token, bot_token
from telebot import types
bot = telebot.TeleBot(bot_token)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup()
    item1 = types.KeyboardButton("Хочу фото!")
    markup.add(item1)
    bot.send_message(message.chat.id, "Привет!\nЯ могу отправить тебе фото из вк по твоему запросу!\nСоздал Воронцов Пётр ИДБ-21-10.", reply_markup=markup)


@bot.message_handler(content_types='text')
def get_photo(message):
    if message.text == "Хочу фото!" or message.text == "Хочу ещё" or message.text == "Ещё?":
        msg = bot.send_message(message.chat.id, "Так, а теперь скажи какое фото тебе прислать")
        bot.register_next_step_handler(msg, send_photo)
    else:
        bot.send_message(message.chat.id, "Я тебя не очень понимаю")

def send_photo(message):
    try:
        url_photos_info = f'https://api.vk.com/method/photos.search?q={message.text}о&count=100&access_token={vk_token}&v=5.131'
        req_url_photos_info = requests.get(url_photos_info)
        jsn_photos = req_url_photos_info.json()

        bot.send_message(message.chat.id, "Лови")
        bot.send_photo(message.chat.id, jsn_photos['response']['items'][random.randint(0, 100)]['sizes'][3]['url'])

        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton(text='Давай по новой', callback_data='again'))
        bot.send_message(message.chat.id, "Ещё?",  reply_markup=markup)

    except:
        bot.send_message(message.chat.id, "Что-то пошло не так!")

@bot.callback_query_handler(lambda c: c.data == 'again')
def callback_inline(call):
    if call.message:
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Окей")
            get_photo(call.message)

bot.infinity_polling()