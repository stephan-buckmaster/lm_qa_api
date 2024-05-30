from base_handler import BaseHandler

class EchoModelHandler(BaseHandler):
    def complete(self):
            return "Your model is " + self.model() + ";  that's just about it."
