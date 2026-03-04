from flask import Flask
from Configs.Queries import *

app = Flask(__name__)


@app.route('/')
def index():
    names = retrieve_names()
    page_contents = ''
    for name in names:
        page_contents += f'<h1>{name}</h1><br>'
    return page_contents


if __name__ == '__main__':
    app.run()