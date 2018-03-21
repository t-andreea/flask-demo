from flask.views import MethodView

class MainView(MethodView):

    def __init__(self):
        pass

    @classmethod
    def _generate_response(cls, input_data=None):
       if input_data is None:
          resp = dict(status=1, content="Method Not Implemented!")
       else:
          resp = dict(status=0, content=input_data)
       return Response(json.dumps(resp))

    def get(self):
        return 'Hello from GET :P'

    def post(self):
        return 'Hello from POST :('

    def get_route(self) -> str:
        return "/"