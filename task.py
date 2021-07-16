from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route('/')
def shopping_list():
    return render_template('shopping_list.html')


@app.route('/show_items', methods=['POST', 'GET'])
def items():
    result = request.form
    return render_template('show_items.html', result=result)


if __name__ == '__main__':
    app.debug = True
    app.run()

