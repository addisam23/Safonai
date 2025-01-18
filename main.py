#Author: Arman Idrisi

import telebot
import google.generativeai as genai

genai.configure(api_key="AIzaSyAl9GwPb6uL3ds5XcfpCAPomQGw-0qGECw")
model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("Explain how AI works")
print(response.text)



#Bot Api Token
API_TOKEN = '7597773357:AAGOUlb2EfugOAOK-2SFMqYc0JLiGWUgZrI'




bot = telebot.TeleBot(API_TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
	 # bot.send_message(message.chat.id,message.text)
	   bot.send_message(message.chat.id, """\
Hi there, I am A Ai ChatBot.

I am here to Give Answers Of Your Question.

I Am Created Using Chatgpt Api ! 

Use /ask  To Ask Questions\
""")

#Handle The '/ask'
@bot.message_handler(commands=['ask'])
def first_process(message):
	bot.send_message(message.chat.id,"Send Me your Question")
	bot.register_next_step_handler(message,second_process)
def again_send(message):
  bot.register_next_step_handler(message,second_process)
def second_process(message):
  bot.send_message(message.chat.id,get_response(message.text))
  again_send(message)

 
bot.infinity_polling()

