from flask import Flask

from config import settings


app = Flask(__name__)


@app.get('/')
def root():
    return {
        'settings': dict(settings)
    }


if __name__ == '__main__':
    app.run(debug=True, port=8181)
