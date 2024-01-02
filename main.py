from flask import Flask
from flask import *
from flask import request
from markupsafe import escape
import Dijkstra 

app = Flask(__name__)

@app.route('/')
@app.route('/welcome/')
def index():
    return render_template("welcome.html")

@app.route('/app/machinery', methods=['POST'] )
def machinery():
    
    tanggal = int(request.form['tanggal'])
    bulan = int(request.form['bulan'])
    tahun = int(request.form['tahun'])
    lokasi = int(request.form['lokasi'])

    data = Dijkstra.inputMachinery(lokasi, tanggal, bulan, tahun)
    data['req'] = request.form
    return data



app.run()