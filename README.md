# mailgun-python-appengine

`mailgun-python-appengine` is a python appengine client for [Mailgun][]. Mailgun is a set of 
powerful APIs that allow you to send, receive, track and store email effortlessly.

  [mailgun]: http://www.mailgun.net

## Usage

    exceptional = Exceptional('YOUR_API_KEY_HERE')
    try:
        1/0
    except Exception, e:
        exceptional.submit(e)
        raise