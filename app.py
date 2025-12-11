from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/codigo-fuente')
def codigo_fuente():
    return '<h1>¡Tu aplicación funciona!</h1>'

if __name__ == '__main__':
    app.run(debug=True)
