from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

users = {}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        users[email] = password
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if email in users and users[email] == password:
            return "Login Success ✅"
        else:
            return "Invalid ❌"
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)