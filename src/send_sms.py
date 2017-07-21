import urllib2

def send(config):
	api_url = config['sms']['api_url']
	recipient = config['sms']['to']
	message = config['sms']['message']
	
	try:
		res = urllib2.urlopen(api_url + '&recipient=' + recipient + '&message=' + message).read()
	except: 
		return False
	finally:
		return res