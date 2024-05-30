from base_handler import BaseHandler
import time

class TimeOfDayHandler(BaseHandler):
    def complete(self):
            return "For all we know the current time is " + time.strftime('%a %b %d %H:%M:%S %Z %Y')
