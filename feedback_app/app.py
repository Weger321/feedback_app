from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def feedback():
    if request.method == 'POST':
        name = request.form['name']
        message = request.form['message']
        
        # Сохранение отзыва в файл
        with open('feedback.txt', 'a', encoding='utf-8') as f:
            f.write(f'Имя: {name}\nСообщение: {message}\n\n')

        return render_template('feedback_form.html', thank_you=True)

    return render_template('feedback_form.html', thank_you=False)

if __name__ == '__main__':
    app.run(debug=True)
