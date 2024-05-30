from base_handler import BaseHandler

class DefaultHandler(BaseHandler):
    def complete(self):
            return "Unkown model provided >>" + self.model() + "<<"
