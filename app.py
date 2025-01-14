from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)

app.config['MAIL_SERVER']= 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'hamza.ali@student.moringaschool.com'
app.config['MAIL_PASSWORD'] = 'lfwz smmo hrin ngog'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
mail = Mail(app)


@app.route("/")
def index():
    msg = Message(subject='Hello from the other side!', sender='hamza.ali@student.moringaschool.com', recipients=['david.kakhayanga@student.moringaschool.com',
    'Anne.muriuki@student.moringaschool.com',
    'robin.adhola@student.moringaschool.com'
     ])
    msg.body = "Hey team, sending you this email from my Flask app, lmk if it works."
    mail.send(msg)
    return "Message sent!"


if __name__ == '__main__':
    app.run(debug=True)