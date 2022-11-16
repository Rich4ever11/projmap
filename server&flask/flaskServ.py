from flask import Flask
from getDB import DBSearch

app = Flask(__name__)

@app.route("/<name>")
def PROJMAP():
    tester = DBSearch()
    tester.start()
    find = tester.findAll("weapon")
    glizzys = 0
    for i in find:
        if i == 'FIREARM' or i == 'HANDGUN':
            glizzys= +1

    return "hi"


if __name__ == '__main__':
    app.run()