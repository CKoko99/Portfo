from flask import Flask, render_template, request

app = Flask(__name__)



@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == "POST":
        data = request.form.to_dict()
        print(data)
    else:
        print("something went wrong :(")
    return render_template('submitted.html')
