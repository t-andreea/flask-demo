from route.main_view import MainView

class HelloWorld(MainView):

    def __init__(self):
        super().__init__()

    @classmethod
    def _generate_response(cls, input_data=None):
        return super()._generate_response(input_data)

    def get(self):
        return 'Hello from the other side/GET'

    def post(self):
        return 'Hello from the other side/POST'

    def get_route(self) -> str:
        return "/hello"

