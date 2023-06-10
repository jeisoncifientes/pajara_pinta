from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve
from Controladores.ControladorCliente import ControladorCliente

app=Flask(__name__)
cors=CORS(app)
miControladorCliente=ControladorCliente()

def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data

@app.route("/",methods=['GET'])
def test():
    json = {}
    json["message"]="Servidor corriendo ..."
    return jsonify(json)

################## Cliente ##########################

@app.route("/clientes",methods=['GET'])
def getclientes():
    json=miControladorCliente.index()

    return jsonify(json)

@app.route("/clientes",methods=['POST'])
def crearCliente():
    data = request.get_json()
    print("hola")
    print(data)
    json=miControladorCliente.create(data)
    return jsonify(json)

@app.route("/clientes/<string:id>",methods=['GET'])
def getCliente(id):
    json=miControladorCliente.show(id)
    return jsonify(json)

@app.route("/clientes/<string:id>",methods=['PUT'])
def modificarCliente(id):
    data = request.get_json()
    json=miControladorCliente.update(id,data)
    return jsonify(json)

@app.route("/clientes/<string:id>",methods=['DELETE'])
def eliminarCliente(id):
    json=miControladorCliente.delete(id)
    return jsonify(json)

if __name__ == "__main__":
    dataConfig = loadFileConfig()
    print("Server running : "+"http://"+dataConfig["url-backend"]+":"+str(dataConfig["port"]))
    serve(app,host=dataConfig["url-backend"],port=dataConfig["port"])


