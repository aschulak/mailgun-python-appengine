import urllib
import base64

from google.appengine.api import urlfetch

class Mailgun(object):

    def __init__(self, url, api_key, deadline=5):
        self.url = url
        self.api_key = api_key
        self.deadline = deadline

    def send_mail(self, sender, to, subject, text, html=None, campaign=None):
        payload = {}
        payload['from'] = sender
        payload['to'] = to
        payload['subject'] = subject
        payload['text'] = text
        if html:
            payload['html'] = html
        if campaign:
            payload['o:campaign'] = campaign
        encoded_payload = urllib.urlencode(payload)
        base64string = base64.encodestring('api:' + self.api_key).replace('\n', '')
        headers = {}
        headers['Authorization'] = "Basic %s" % base64string
        result = urlfetch.fetch(self.url, deadline=self.deadline, payload=encoded_payload, method=urlfetch.POST, headers=headers)
        return result