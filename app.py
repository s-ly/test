# главный модуль Админки

# render_template - генерирует HTML
# request - получает данные из формы в HTML
from flask import Flask, render_template, request

import func

app = Flask(__name__)

@app.route('/') 
def test():
    """Читает данные из файла, показывает их и форму ввода."""
    # func.read_db()
    # f = open('text.txt', 'r')
    # my_text = f.read()
    # f.close()  
    data = func.read_db()  
    # my_text = str(data)
    my_text = data
    return render_template('index.html', the_title = 'Админка', the_text = my_text)

@app.route('/text', methods=['POST']) 
def test2():
    """Принимает данные из формы (name="word") и записывает их в файл.
    methods=['POST'] - нужен для передачи данных."""
    
    text = request.form['word']    
    # func.write_db(text)
    # f = open('text.txt', 'w')
    # f.write(text)
    # f.close()
    data = func.write_db(text)
    text = data
    return render_template('text.html', the_title = 'Админка text', the_word = text)

@app.route('/img', methods=['POST']) 
def test3():
    """img"""
    
    # text = request.form['word']    
    # func.write_db(text)
    # f = open('text.txt', 'w')
    # f.write(text)
    # f.close()
    # data = func.write_db(text)
    # text = data
    # return render_template('text.html', the_title = 'Админка text', the_word = text)
    return render_template('img.html')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)