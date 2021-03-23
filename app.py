from flask import Flask, render_template, request

app = Flask(__name__)

""" Home page which is our index file """
@app.route('/')
def home_page():
    return render_template('index.html')

""" Form submission route """
@app.route('/send', methods=['POST'])
def send(sum=sum):
    if request.method == 'POST':
        # Start pulling data from Form input
        num1 = request.form['num1']
        num2 = request.form['num2']
        operation = request.form['operation']
        # Calculation IF Statements
        if operation == 'add':
            sum = float(num1) + float(num2)
            return render_template('index.html', sum=sum) # basically passing in a prop like in Vue
        elif operation == 'subtract':
            sum = float(num1) - float(num2)
            return render_template('index.html', sum=sum)
        elif operation == 'multiply':
            sum = float(num1) * float(num2)
            return render_template('index.html', sum=sum)
        elif operation == 'divide':
            sum = float(num1) / float(num2)
            return render_template('index.html', sum=sum)
        else:
            return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True) # Turned on developer mode, shows us actual errors when they pop up