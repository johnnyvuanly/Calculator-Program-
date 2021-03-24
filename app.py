from flask import Flask, render_template, request, session
from flask_socketio import SocketIO, send

app = Flask(__name__)

# Define secret key which is required for maintaining the sessions in the class
app.config['SECRET_KEY'] = 'secret'
socketio = SocketIO(app)

# This listens for particular event that I specify
@socketio.on('message') 
def handleMessage(msg):
    send(msg, broadcast=True) # When a message comes in, broadcast it to everyone connected to the server at the moment
    
""" Home page which is our index file """
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

""" Form submission route """
@app.route('/operation_result', methods=['POST'])
def operation_result():
    error = None
    result = None
    
    # request.form looks for:
    # html tags with matching "name="
    num1 = request.form['num1']
    num2 = request.form['num2']
    operation = request.form['operation']

    try:
        input1 = float(num1)
        input2 = float(num2)

        if operation == "+":
            result = input1 + input2
        elif operation == "-":
            result = input1 - input2
        elif operation == "/":
            result = input1 / input2
        else:
            operation = "*"
            result = input1 * input2

        return render_template(
            'index.html',
            input1=input1,
            input2=input2,
            operation=operation,
            result=result,
            calculation_success=True
        )
    except ZeroDivisionError:
        return render_template(
            'index.html',
            input1=input1,
            input2=input2,
            operation=operation,
            result="Bad Input",
            calculation_success=False,
            error="You cannot divide by zero"
        )
    except ValueError:
        return render_template(
            'index.html',
            input1=num1,
            input2=num2,
            operation=operation,
            result="Bad Input",
            calculation_success=False,
            error="Cannot perform numeric operations with provided input"
        )

if __name__ == '__main__':
    app.debug = True # Turned on developer mode, shows us actual errors when they pop up
    socketio.run(app) # socketio takes the Flask app, wraps around it and adds to the flask server