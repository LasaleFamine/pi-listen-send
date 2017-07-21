import urllib2
import urllib

def send(config):
	api_url = config['sms']['api_url']
	recipient = config['sms']['to']
	message = config['sms']['message']

	query_string = urllib.urlencode({ 'recipient' : recipient, 'message' : message})
	
	try:
		res = urllib2.urlopen(api_url + '&' query_string).read()
	except: 
		return False
	finally:
		return res