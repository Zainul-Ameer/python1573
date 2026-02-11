from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)

# Gmail configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'za378r@gmail.com'
app.config['MAIL_PASSWORD'] = 'kkksnylyhnvlirjm'
app.config['MAIL_DEFAULT_SENDER'] = 'za378r@gmail.com'

mail = Mail(app)

@app.route('/send')

def send_email():
    msg = Message(
        subject='Hello from Flask',
        recipients=['zainulameer@hotmail.com'],
        body='This email was sent using Flask and Gmail - 2.30pm!'
    )

    mail.send(msg)
    return "Email Sent Successfully!"

if __name__ == '__main__':
    app.run(debug=True)





#..........................................
