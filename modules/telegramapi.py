import requests
import os
from dotenv import load_dotenv
load_dotenv()

bot_message = os.getlogin()
bot_token = os.getenv('BOT_TOKEN')
bot_chatID = os.getenv('BOT_CHATID')
send_text = 'https://api.telegram.org/bot' + str(bot_token) + '/sendMessage?chat_id=' + str(bot_chatID) + '&parse_mode=Markdown&text=' + bot_message

response = requests.get(send_text)
# print(response.json())