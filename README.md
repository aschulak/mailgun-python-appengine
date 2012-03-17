# mailgun-python-appengine

`mailgun-python-appengine` is a python appengine client for [Mailgun][]. Mailgun is a set of 
powerful APIs that allow you to send, receive, track and store email effortlessly.

  [mailgun]: http://www.mailgun.net

## Usage
	import mailgun
	
	url = '<your mailgun url>'
	api_key = '<your mailgun api key>'
	deadline = 5 # optional urlfetch timeout in seconds
	mailgun_client = mailgun.Mailgun(url, api_key, deadline=deadline)
	result = mailgun_client.send_mail(sender, to, subject, body, html=body, campaign='optional_campaign_code')