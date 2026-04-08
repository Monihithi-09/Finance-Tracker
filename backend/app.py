from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

user_category = None

users = {}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # 🔴 ADD THIS CHECK
        if email in users:
            return "Account already exists ❌"

        # ✅ THEN STORE
        users[email] = password
        return '''
            <!DOCTYPE html>
            <html>
            <head>
                <title>Success</title>
                <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
                <style>
                    body {
                        background: linear-gradient(to right, #4facfe, #00f2fe);
                    }
                </style>
            </head>

            <body class="d-flex justify-content-center align-items-center vh-100">

            <div class="card p-5 shadow text-center" style="max-width: 400px;">
                <h3>Account Created Successfully ✅</h3>
                <a href="/login" class="btn btn-success mt-4">Go to Login</a>
            </div>

            </body>
            </html>
            '''

    return render_template('register.html')
@app.route('/check_email', methods=['POST'])
def check_email():
    email = request.form['email']
    if email in users:
        return "exists"
    return "available"

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if email in users and users[email] == password:
            return redirect(url_for('dashboard'))
        else:
            return "Invalid Credentials ❌"
    return render_template('login.html')

@app.route('/forgot_password', methods=['GET','POST'])
def forgot_password():
    if request.method == 'POST':
        email = request.form['email']
        new_password = request.form['new_password']

        if email not in users:
            return "Account doesn't exist ❌"

        users[email] = new_password
        return "Password updated successfully ✅"

    return render_template('forgot_password.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/income', methods=['POST'])
def income():
    income = int(request.form['income'])

    if income <= 20000:
        category = "low"
    elif income <= 50000:
        category = "medium"
    else:
        category = "high"

    # store temporarily (for now)
    global user_category
    user_category = category

    return redirect(url_for('dashboard'))

if __name__ == '__main__':
    app.run(debug=True)