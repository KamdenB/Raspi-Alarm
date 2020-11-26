from flask import Flask, render_template
app = Flask(__name__)

# with app.app_context():
#     url_for('static', filename="style.css")

@app.route('/')
def alarm(alarmStatus=None):
    return render_template('alarm.html', alarmStatus=alarmStatus)

@app.route('/api/', methods=['GET', 'POST'])
def api():
    if request.method == 'POST':
        return 'post'
    else:
        return 'get'


if __name__ == "__main__":
    app.run()