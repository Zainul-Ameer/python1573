from flask import Flask, request, render_template
from flask_mail import Mail, Message
import random

app = Flask(__name__)

# Gmail configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'za378r@gmail.com'
app.config['MAIL_PASSWORD'] = 'kkksnylyhnvlirjm'
app.config['MAIL_DEFAULT_SENDER'] = 'za378r@gmail.com'

mail = Mail(app)

# Temporary storage (for testing only)
generated_otp = None

"""
@app.route('/')
def home():
    return '''
        <form method="POST" action="/send_otp">
            <input type="email" name="email" placeholder="Enter your email" required>
            <button type="submit">Send OTP</button>
        </form>
    '''



"""
@app.route('/')
def home():
    return render_template("index.html")

@app.route('/send_otp', methods=['POST'])
def send_otp():
    global generated_otp

    user_email = request.form.get('email')

    # Generate 6-digit OTP
    generated_otp = str(random.randint(100000, 999999))

    msg = Message(
        subject='Your OTP Code',
        recipients=[user_email],
        body=f'Your OTP is: {generated_otp}'
    )

    mail.send(msg)

    return f"OTP sent to {user_email}"
    

if __name__ == '__main__':
    app.run(debug=True)
    