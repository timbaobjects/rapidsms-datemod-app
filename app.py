import re
from rapidsms.apps.base import AppBase
try:
	from dateutil.parser import *
except ImportError:
	raise ImportError("python-dateutil is requirement for this app")

class App(AppBase):
	def start(self):
		self.pattern = re.compile(r"(?P<date>(\d+[\/\-]\d+|\d+[\/\-]\d+[\/\-]\d+))$")

	def parse(self, msg):
		'''The purpose of this method is to look for any strings resembling a date string
		e.g. 7/12/2009, 7/12, 7-12-2009, 7-12 and use that to set the date of the message.
		This is essentially to cater for reports that may come in late.'''
		last_token = re.split('\s+', msg.text.strip())[-1]

		if (self.pattern.match(last_token)):
			msg_date_string = self.pattern.match(last_token).group(1)
			msg_date = parse(msg_date_string, dayfirst=True)

			if (msg_date):
				if msg_date > msg_date.now():
					msg_date = msg_date.replace(year=msg_date.year-1)
				msg.received_at = msg_date

				# strip message of date string
				msg.text = " ".join(re.split("\s+", msg.text.strip())[0:-1])
