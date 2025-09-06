from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    names = []

    if request.method == 'POST':
        raw_names = request.form.get('names', '')
        # Split by newline or comma, strip whitespace
        names = [name.strip() for name in raw_names.replace(',', '\n').split('\n') if name.strip()]
        if not names:
            return render_template('index.html', names=[], error="Please enter at least one name.")
        return render_template('index.html', names=names)

    return render_template('index.html', names=[])

if __name__ == '__main__':
    app.run(debug=True)