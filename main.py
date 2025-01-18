# Get toke from the environment variable
import os
from telegram import Bot
token = os.getenv("TOKEN")

bot = Bot(token)
# updates = bot.get_updates()
# print(updates.update_id)
# message = bot.send_message(chat_id=6824726862, text="Hello, world!")
f='C:/Users/user/Desktop/image.png'
photo = bot.send_photo(chat_id=6824726862, photo=f )
# print(bot.send_document(chat_id=6824726862, document='README.md'))
# print(bot.send_audio(chat_id=6824726862, audio='C:/Users/user/Desktop/A2 lesson 6. Ex 2.mp3'))
# print(bot.send_video(chat_id=6824726862, video='"BAACAgIAAxkBAAOWZrSm8TZXdqnOVtS38kJ-c9XupRwAAu1RAAJosplJg9GyueFNFKg1BA"'))
# print(bot.send_voice(chat_id=6824726862, voice='AwACAgIAAxkBAAICe2eKQ510Ccj7jpJNwPJPFhX2uRGFAAKLVAACwdjYSbZrmrqpJ5-VNgQ'))




