# mailgun-python-appengine

`mailgun-python-appengine` is a python appengine client for [Mailgun]. Mailgun is a set of 
powerful APIs that allow you to send, receive, track and store email effortlessly.

This client only does send at the moment. Feel free to add extra goodness.

  [mailgun]: http://www.mailgun.net
  
The URL you will need to supply is the URL to send messages for your Mailgun domain - it will look something like `https://api.mailgun.net/v2/yourdomain/messages`.

## Usage
	import mailgun
	
	url = '<your mailgun url>'
	api_key = '<your mailgun api key>'
	mailgun_client = mailgun.Mailgun(url, api_key, deadline=optional_urlfetch_deadline_in_seconds)
	result = mailgun_client.send_mail(sender, to, subject, body, html=optional_html_body, campaign='optional_campaign_code')
	if result.status_code == 200:
		# hooray!
		pass
	else:
		# boo
		pass
