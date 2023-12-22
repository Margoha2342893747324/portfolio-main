#Импорт
from flask import Flask, render_template,request, redirect



app = Flask(__name__)

#Запуск страницы с контентом
@app.route('/')
def index():
    return render_template('index.html')


#Динамичные скиллы
@app.route('/', methods=['POST'])
def process_form():
    button_python = request.form.get('button_python')
    return render_template('index.html', button_python=button_python)

def process_form():
    discord = request.form.get('discord')
    return render_template ('index.html',discord=discord)

def process_form():
    profile = request.form.get('profile')
    return render_template ('index.html',profile=profile)

def process_form():
    html = request.form.get('html')
    return render_template ('index.html',html=html)





if __name__ == "__main__":
    app.run(debug=True)