from flask import Flask, render_template, request, redirect
app = Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html", name = 'Zach')

@app.route('/server', methods=['POST'])
def server():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    print first_name, last_name
    return redirect('/')
app.run(debug=True)
