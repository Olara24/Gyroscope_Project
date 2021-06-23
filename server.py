from flask import Flask
import json

app = Flask(__name__)

@app.route('/data.html')
def data():
    base= """
    <!DOCTYPE html>
        <html>
        <head>
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
        <link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/1.10.25/css/jquery.dataTables.css">
        <script type="text/javascript" charset="utf8" src="https://cdn.datatables.net/1.10.25/js/jquery.dataTables.js"></script>

        <script>
        $(document).ready( function () {
            $('#table_id').DataTable();
            } );
        </script>
        </head>
        <body>
        %s
        </body>
        </html>
    """
    with open('/home/pi/Gyroscope_Project/data.csv') as fin:
        data= fin.readline()
        text_td= " "
        for line in fin:
            Gx,Gy,Gz,Ax,Ay,Az= line.split(",")

            text_td+="<tr> <td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td> </tr>".format(Gx,Gy,Gz,Ax,Ay,Az)
           
        text_data= """
        <table id="table_id" class="display">

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
        return base%(text_data)

@app.route('/get_data.json')
def get_data():
    response= []
    with open('/home/pi/Gyroscope_Project/data.csv') as fin:
        data= fin.readline()
        text_td= " "
        for line in fin:
            Gx,Gy,Gz,Ax,Ay,Az= line.split(",")
            response.append([Gx,Gy,Gz,Ax,Ay,Az])
        jsonStr = json.dumps(response)
        return jsonStr
            
if __name__ == '__main__':
    app.run(host="0.0.0.0")