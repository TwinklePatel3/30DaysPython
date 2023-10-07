from flask import Flask, render_template, redirect, request, url_for
import os
import ast

app = Flask(__name__)


@app.route('/')
def home():
    techs = ['HTML', 'CSS', 'Flask', 'Python']
    name = '30 Days Of Python Programming'
    return render_template('home.html', techs=techs, name=name, title="Home")


@app.route("/about")
def about():
    name = '30 Days Of Python Programming'
    return render_template('about_us.html', name=name, title='About Us')


@app.route('/result')
def result():
    data = request.args.to_dict()
    headers = ["WORD", "WORD COUNT"]
    tableData = request.args.getlist("words")
    table = [i for i in ast.literal_eval(tableData[0])]
    return render_template('result.html', data=data, headers=headers, tableData=sorted(table, reverse=True))


@app.route('/post', methods=['GET', 'POST'])
def post():
    name = 'Text Analyzer'
    if request.method == 'GET':
        return render_template('post.html', name=name, title=name)
    if request.method == 'POST':
        content = request.form['content']
        text = content.lower().split()
        num_of_char = len(content)
        total_words = len(text)
        freq_words = [(text.count(x), x) for x in text]
        freq_word = (max(freq_words, key=lambda x: x[0]))[1]
        word_variety = (len(set(freq_words)) / total_words * 100)
        data = {"num_of_char": num_of_char,
                "total_words": total_words, "freq_word": freq_word, "word_variety": "{:.1f}".format(word_variety)}
        return redirect(url_for('result', **data, words=set(freq_words)))


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
