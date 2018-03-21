from route.main_view import MainView


class ByeWorld(MainView):

    def __init__(self):
        super().__init__()

    @classmethod
    def _generate_response(cls, input_data=None):
        return super()._generate_response(input_data)

    def post(self):
        return "Hello darkness, my old friend, I'm post"

    def get(self):
        return "Darkness, this is get"

    def get_route(self) -> str:
        return "/bye"