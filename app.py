from flask import Flask, render_template_string, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Секретный ключ для сессий

# ✅ Список пользователей (логин: пароль)
users = {
    'dnkarpenko@gmail.com': '20F001N',
    'user2': 'pass2',
    'user3': 'pass3',
    'user4': 'pass4',
    'user5': 'pass5',
    'user6': 'pass6',
    'user7': 'pass7',
    'user8': 'pass8',
    'user9': 'pass9',
    'user10': 'pass10'
}

# ✅ Главная страница (черный фон)
@app.route('/')
def home():
    if 'username' in session:
        return redirect(url_for('dashboard'))  # Если вошел – сразу на дашборд

    main_page = '''
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <title>Главная страница</title>
        <style>
            body {
                margin: 0;
                height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                background-color: #000;
            }
            .clickable-image {
                cursor: pointer;
                width: 400px;
                border-radius: 15px;
                transition: transform 0.3s ease;
                box-shadow: 0 4px 8px rgba(255, 255, 255, 0.2);
            }
            .clickable-image:hover {
                transform: scale(1.1);
            }
        </style>
    </head>
    <body>
        <a href="/login">
            <img src="https://raw.githubusercontent.com/igazser/glavnaya/main/image.jpeg" alt="Нажмите для авторизации" class="clickable-image">
        </a>
    </body>
    </html>
    '''
    return render_template_string(main_page)

# ✅ Страница логина (черный фон)
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users and users[username] == password:
            session['username'] = username
            return redirect(url_for('dashboard'))
        else:
            return '<h2 style="color:red;">❌ Неверный логин или пароль. <a href="/login" style="color:green;">Попробуйте снова</a></h2>'

    login_form = '''
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <title>Авторизация</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #000;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
                color: #fff;
            }
            .login-container {
                background-color: #222;
                padding: 30px 40px;
                border-radius: 10px;
                box-shadow: 0 4px 8px rgba(255,255,255,0.1);
                width: 300px;
                text-align: center;
            }
            h2 {
                margin-bottom: 20px;
                color: #4CAF50;
            }
            input[type="text"], input[type="password"] {
                width: 100%;
                padding: 10px;
                margin: 10px 0;
                border: 1px solid #4CAF50;
                border-radius: 5px;
                background-color: #333;
                color: #fff;
            }
            input[type="submit"] {
                background-color: #4CAF50;
                color: white;
                padding: 12px;
                border: none;
                border-radius: 5px;
                cursor: pointer;
                width: 100%;
            }
            input[type="submit"]:hover {
                background-color: #45a049;
            }
        </style>
    </head>
    <body>
        <div class="login-container">
            <h2>🔑 Авторизация</h2>
            <form method="POST">
                <input type="text" name="username" placeholder="Email" required><br>
                <input type="password" name="password" placeholder="Пароль" required><br>
                <input type="submit" value="Войти">
            </form>
        </div>
    </body>
    </html>
    '''
    return render_template_string(login_form)

# ✅ Дашборд (черный фон, имя пользователя исправлено)
@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect(url_for('login'))  # Если не авторизован, перекидываем на логин

    username = session['username']  # Исправлено, чтобы корректно показывало имя

    dashboard_page = '''
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <title>Материалы</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #000;
                color: #fff;
                margin: 0;
                padding: 20px;
            }
            .container {
                display: flex;
                flex-wrap: wrap;
                justify-content: center;
            }
            .card {
                background: #111;
                padding: 20px;
                margin: 10px;
                width: 250px;
                border-radius: 10px;
                text-align: center;
                transition: transform 0.3s ease;
            }
            .card:hover {
                transform: scale(1.05);
            }
            img {
                width: 100%;
                border-radius: 10px;
            }
            a {
                text-decoration: none;
                color: #4CAF50;
            }
        </style>
    </head>
    <body>
        <h1>Добро пожаловать, <span style="color:#4CAF50;">{{ username }}</span>!</h1>
        <p>Выберите материал:</p>
        <div class="container">
            {% for i in range(12) %}
            <div class="card">
                <img src="https://raw.githubusercontent.com/igazser/glavnaya/main/image.jpeg" alt="Материал">
                <h3>Материал {{ i+1 }}</h3>
                <a href="#">Подробнее</a>
            </div>
            {% endfor %}
        </div>
        <br>
        <a href="/logout" style="color:red;">Выйти</a>
    </body>
    </html>
    '''
    return render_template_string(dashboard_page, username=username)

# ✅ Выход из системы
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)

