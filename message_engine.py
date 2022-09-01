import requests
import pywhatkit
import datetime
from datetime import timedelta


def casper_alert(bot_alert):
   bot_token = '5679912803:AAFNf9EHAxJnqpTmzHBr0ZuaeqeLtFx1oc8'
   my_chatID = '1813981055'
   send_alert = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + my_chatID + '&parse_mode=Markdown&text=' + "*" + bot_alert + "*"

   response = requests.get(send_alert)
   return response.json()

def telegram_text(send):
   bot_token = '5679912803:AAFNf9EHAxJnqpTmzHBr0ZuaeqeLtFx1oc8'
   my_chatID = '1813981055'
   send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + my_chatID + '&parse_mode=Markdown&text=' + send

   response = requests.get(send_text)
   return response.json()

def whatsapp_text(send):
   hour = int(datetime.datetime.now().strftime("%H"))
   print(hour)

   now_m = datetime.datetime.now().strftime("%M") 
   dt = datetime.datetime.now().strptime(now_m, '%M')
   add_m = str(dt + timedelta(minutes=1))

   a = add_m.replace('1900-01-01 ', '')
   b = a.replace(':00', '')
   min = b.replace('00:', '')
   print(min)

   min = int(min)
   pywhatkit.sendwhatmsg('+94741040292', send, hour, min)


   # https://web.whatsapp.com/send?phone=+94741040292&text=this%20is%20a%20test














