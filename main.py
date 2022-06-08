from flask import Flask , render_template
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!' 


@app.route('/dojo')
def dojo():
    return 'Dojo!'


@app.route('/say/<name>')
def welcome(name):
    return f"Hi {name}!"


@app.route('/repeat/<int:num>/<message>')
def grating(num,message):
    return render_template('index.html',num=num,message=message)

@app.errorhandler(404)
def test(e):
    return " sorry page not found"



if __name__ == "__main__":
    app.run(debug=True)
