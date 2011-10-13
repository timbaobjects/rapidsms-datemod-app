Datemod
=======

Datemod is a reusable RapidSMS application that allows reporters to explicitly set the date a message should carry directly from the text message. This is useful in cases where the dates in SMS reports are stored and used.

This app tracks messages that have something that looks like a date at the end of the message and uses that to set the date on the message.

E.g.

	br report 200412 b 1 2 3 4 g 1 2 3 4 12/7/2011

This app sees ``12/7/2011`` and automatically recognizing that it's a date, parses that and sets the date on the message accordingly.

It supports dates in the format ``dd/mm/yyyy``, ``dd/mm`` with the delimiter being either a ``/`` or  ``-``.

Installation
============

	git clone https://github.com/timbaobjects/rapidsms-datemod-app.git datemod

Then add ``datemod`` to your INSTALLED_APPS setting in your settings.py

Dependencies
============
* `python-dateutil <http://pypi.python.org/pypi/python-dateutil>`_