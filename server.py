from flask import Flask

app = Flask(__name__)

@app.route('/data.html')
def data():
    with open('/home/pi/Gyroscope_Project/data.csv') as fin:
        data= fin.readline()
        text_td= " "
        for line in fin:
            Gx,Gy,Gz,Ax,Ay,Az= line.split(",")

            text_td+="<tr> <td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td> </tr>".format(Gx,Gy,Gz,Ax,Ay,Az)
           
        text_data= """
        <table> 

        <tr>
        <th scope="col">Gx</th>
        <th scope="col">Gy</th>
        <th scope="col">Gz</th>
        <th scope="col">Ax</th>
        <th scope="col">Ay</th>
        <th scope="col">Az</th>

        </tr>
        <tr>
        {}
        </tr>
        </table>
        """.format(text_td)
        return text_data
            
if __name__ == '__main__':
    app.run(host="0.0.0.0")