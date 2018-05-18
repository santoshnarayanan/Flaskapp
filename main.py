from flask import Flask

app = Flask(__name__)

'''
This below line is not required as it is configuration parameter in flask version 1.02
'''
# app.config.from_object(DevConfig)


@app.route('/')
def hello_world():
    return 'Hello World!!!!'


if __name__ == '__main__':
    app.run()
