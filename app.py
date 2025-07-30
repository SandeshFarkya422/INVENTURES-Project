
from flask import Flask, request, render_template, redirect, url_for
from datetime import datetime

app = Flask(__name__)
notes = []

@app.route('/')
def home():
    return render_template('addnote.html')

@app.route('/addnote', methods=['POST'])
def add_note():
    title = request.form.get('title')
    content = request.form.get('content')

    if not title or not content:
        return "Title is required", 400

    note = {
        'title': title,
        'content': content,
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    notes.append(note)
    return redirect(url_for('get_notes'))

@app.route('/get_notes')
def get_notes():
    return render_template('notes.html', notes=notes)

if __name__ == '__main__':
    app.run(debug=True)


