from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Ciao, mondo!"

@app.route('/saluto/<nome>')
def saluto(nome):
    return jsonify({'messaggio' : f'ciao {nome}'})

if __name__ == '__main__':
    app.run()
