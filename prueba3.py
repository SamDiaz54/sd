import telebot
import time
bot =telebot.TeleBot("641328257:AAEOdPPO5paJwqgE95fu9QFex4UokUEL9pw")
medicina=time.strftime("24:05:00")
medicina2=time.strftime("24:10:00")
hora=time.strftime("%X")
timer=0
inicio=False
def horas():
	global timer,corre
	chatid2=682154940
	bot.send_message(chatid2,"Recordatorio, toma tus medicamentos")
	bot.send_message(chatid2,"envia el comando /confirmar para confirmar")
	timer=0
while True:
	hora=time.strftime("%X")
	timer=timer+1
	time.sleep(1)
	print inicio
	print ("cronometro "+str(timer))
	print ("tiempo "+str(hora))
	if hora==medicina or hora==medicina2:
		horas()



