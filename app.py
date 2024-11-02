from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def wrapper(*args, **kwargs):
        name = function(*args, **kwargs)
        return f"<b>{name}<b/>"

    return wrapper


@app.route("/bye")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/<path:name>/<int:age>")
@make_bold
def say_world(name, age):
    return f"<p>You re {name} and you are {age} years old...</p>"


if __name__ == "__main__":
    app.run(debug=True)
