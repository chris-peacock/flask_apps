from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    n = request.args.get('n', default=10, type=int)  # default to 8 wedges
    return render_template('index.html', n=n)

if __name__ == '__main__':
    app.run(debug=True)