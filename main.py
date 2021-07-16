from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


# @app.route('/', methods=['POST', 'GET'])
# def http_methods():
#     return request.method

@app.route('/')
def log():
    return render_template('login1.html')


@app.route('/dictionary')
def dictionary():
    dict_items = {'Godwin': 47, 'Karabo': 22, "Thabo": 17, 'Malik': 30, 'Zaid': 19}
    return jsonify(dict_items)


@app.route('/login', methods=['POST'])
def login():
    uname = request.form['username']
    passwrd = request.form['userpass']
    if uname == "Abdul-Malik" and passwrd == "0000":
        return "Welcome %s" % uname  # + request.method
    else:
        return "Error in logging in"  # + request.method


if __name__ == '__main__':
    app.debug = True
    app.run()
