import RPi.GPIO as GPIO

import send_mail
import send_sms
import config

cfg = config.get_config()
pin = cfg['raspberry']['pin']

def pi_listen(callback):
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(pin, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
	GPIO.add_event_detect(pin, GPIO.RISING, callback = callback, bouncetime = 300)

def handler_reponses(mail, sms):
	if mail:
		print ('EMAIL sent.')
	else:
		print ('An error occured: EMAIL')

	if sms:
		print ('SMS sent. -> ' + sms)
	else:
		print ('An error occured: SMS')


def handler_listen(channel):
	if GPIO.input(pin):
		print('Movement!')
		email = send_mail.send(cfg)
		message = send_sms.send(cfg)
		handler_reponses(email, message)
		

def main():
	pi_listen(handler_listen)
	while True:
			pass

main()