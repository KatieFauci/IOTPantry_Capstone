from flask import Flask
import os
# import Main_Application --> Will be importing the main application file that will be going here
# Main app needs to run in the background


app = Flask(__name__)
@app.route('/')
def run_script():
    file = '/home/ubuntu/Capstone/IOTPantry_Capstone/Main_Application/IOTPantry/IOTPantry.py'
    os.startfile(file)

if __name__ == '__main__':
    app.run(debug=True)