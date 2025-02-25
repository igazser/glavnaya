from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "🚀 Привет! Ваш сайт работает на Heroku через GitHub."

if __name__ == '__main__':
    app.run(debug=True)
