from flask import Flask
from flask import render_template
import json

app = Flask(__name__)

@app.route('/')
def root():
    return render_template('table.html')

@app.route('/get_data.json')
def get_data():
    response= {"data": []}
    with open('data/data.csv') as fin:
        data= fin.readline()
        text_td= " "
        for line in fin:
            Gx, Gy, Gz, Ax, Ay, Az= line.rstrip("\n").split(",")
            response['data'].append([Gx, Gy, Gz, Ax, Ay, Az])
        jsonStr = json.dumps(response)
        return jsonStr
            
if __name__ == '__main__':
    app.run(host="0.0.0.0")