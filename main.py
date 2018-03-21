from flask import Flask

from route.bye_world import ByeWorld
from route.hello_world import HelloWorld
from route.main_view import MainView

app = Flask(__name__)

routes = [
    MainView(),
    HelloWorld(),
    ByeWorld()
]

for route in routes:
    app.add_url_rule(route.get_route(), view_func=route.as_view(route.get_route()))

app.run()