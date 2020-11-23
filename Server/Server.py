from flask import Flask
from flask import render_template
import Main_Application.IOTPantry
# import Main_Application --> Will be importing the main application file that will be going here
# Main app needs to run in the background


app = Flask(__name__)
@app.route('/')
def run_script():
    file = open(r'/home/ubuntu/Flask-project/IOTPantry_Capstone/Main_Application/Main_Application.py', 'r').read()
    return exec(file)

if __name__ == '__main__':
    app.run(debug=True)