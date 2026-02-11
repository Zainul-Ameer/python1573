from flask import Flask, request
from flask_mail import Mail, Message

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'za378r@gmail.com'
app.config['MAIL_PASSWORD'] = 'kkksnylyhnvlirjm'
app.config['MAIL_DEFAULT_SENDER'] = 'za378r@gmail.com'

mail = Mail(app)

@app.route('/send', methods=['POST'])
def send_email():
    user_email = request.form.get('email')  # email from form

    msg = Message(
        subject='Welcome!',
        recipients=['alameeragency@gmail.com'],
        body='Thank you for registering.'
    )

    mail.send(msg)
    return "Email Sent Successfully!"