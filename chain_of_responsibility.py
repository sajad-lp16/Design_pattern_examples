from abc import abstractmethod


# Main Chain Of Responsibility
class AbstractHandler:

    def __init__(self, successor):
        self._successor = successor

    def handle(self, request):
        handled = self.process_request(request)
        if not handled:
            self._successor.handle(request)

    @abstractmethod
    def process_request(self, request):
        pass


# -------------------------------------------------------
class HandlerOne(AbstractHandler):
    def process_request(self, request):
        if 0 < request <= 10:
            print(f'This request was handled by HandlerOne {request}')
            return True


class HandlerTwo(AbstractHandler):
    def process_request(self, request):
        if 10 < request <= 20:
            print(f'This request was handled by HandlerTwo {request}')
            return True


class DefaultHandler(AbstractHandler):
    def process_request(self, request):
        print(f'This request was not able to been handled using normal handlers {request}')
        return True


# -----------------------------------------------------

def get_request():
    request = int(input('Enter the request: '))
    handler = HandlerOne(HandlerTwo(DefaultHandler(None)))
    handler.handle(request)


if __name__ == '__main__':
    get_request()
