import smtplib
import email.utils
from email.mime.text import MIMEText

def send(config):
	user = config['server']['username']
	password = config['server']['password']
	smtpServer = config['server']['smpt_server']
	sender = config['mail']['sender']
	sender_name = config['mail']['sender_name']
	recipient = config['mail']['to']
	subject = config['mail']['subject']
	text = config['mail']['text']

	msg = MIMEText(text)
	msg.set_unixfrom('author')
	msg['To'] = email.utils.formataddr(('Recipient', recipient))
	msg['From'] = email.utils.formataddr((sender_name, sender))
	msg['Subject'] = subject

	server = smtplib.SMTP(smtpServer)
	try:
		server.set_debuglevel(True)

		# identify ourselves, prompting server for supported features
		server.ehlo()

		# If we can encrypt this session, do it
		if server.has_extn('STARTTLS'):
			server.starttls()
			# re-identify ourselves over TLS connection
			server.ehlo() 

		server.login(user, password)
		server.sendmail(sender, [recipient], msg.as_string())
	except: 
		return False
	finally:
		server.quit()
		return True
