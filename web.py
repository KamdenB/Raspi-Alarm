from flask import Flask, render_template, request
import platform

if(platform.architecture()[0] == "32bit"): #Import full light control or dummy class depending if its 32 or 64 bit os
    from LightControl import LightControl
else:
    from LightControlDummy import LightControl

lc = LightControl(1,1)

app = Flask(__name__)

# with app.app_context():
#     url_for('static', filename="style.css")
@app.route('/')
def alarm():
    return render_template('alarm.html')

@app.route('/api/<action>', methods=['GET', 'POST'])
def api(action):
    if request.method == 'POST':
        if action == 'Light On':
            lc.on()
            return "lightOn"
        if action == 'Light Off':
            lc.off()
            return "lightOff"
        if action == "newAlarm":
            return 'new alarm'
        if action == "deleteAlarm":
            return 'delete alarm'
        if action == "editAlarm":
            return 'edit alarm'
        elif action == None:
            return "api"
    else:
        return 'get'

@app.route('/test/')
def test():
    return lc.flash(.5, 5)


@app.errorhandler(404)
def page_not_found(error):
    return '404 not found', 404


if __name__ == "__main__":
    app.run()