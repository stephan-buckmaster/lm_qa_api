class BaseHandler:
    def __init__(self, request):
        self.request = request

    def model(self):
        return self.request.model
