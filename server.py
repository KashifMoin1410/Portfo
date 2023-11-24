from flask import Flask, render_template, request, redirect
import csv 

app = Flask(__name__)

# default homepage.
@app.route('/')
def my_home():
    return render_template('index.html')

# switching between the pages. 
@app.route('/<string:page_name>')
def works(page_name):
    return render_template(page_name)

# function to store the data in database.txt. 
def write_to_file(data):
    with open('./WebServer/database.txt', mode='a') as database:
        email = data['email']
        message = data['message']
        subject = data['subject']
        file = database.write(f'\nemail: {email}, subject: {subject}, message: {message}')

# function to store the data in database.csv. 
def write_to_csv(data):
    with open('./WebServer/database.csv', mode='a',newline='') as database:
        email = data['email']
        message = data['message']
        subject = data['subject']
        csv_writer = csv.writer(database,delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])

# getting data from the form and store it in a variable.
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('thankyou.html')
        except:
            return 'Error. Did not save to the database.'
    else:
        return 'Something went wrong.'
    

# $env:FLASK_APP = "server"     
# flask run --debug