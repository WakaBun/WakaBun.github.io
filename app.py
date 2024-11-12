from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/data_visualization')
def index():
    return render_template('data_visualization.html')

if __name__ == '__main__':
    # init_db()
    app.run(debug=True)