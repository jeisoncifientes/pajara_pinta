from Modelos.Cliente import Cliente
from Repositorios.RepositorioCliente import RepositorioCliente

class ControladorCliente():
    def __init__(self):
        self.repositorioCliente = RepositorioCliente()

    def index(self):
        return self.repositorioCliente.findAll()

    def create(self,infoCliente):
        nuevoCliente = Cliente(infoCliente)
        return self.repositorioCliente.save(nuevoCliente)

    def show(self,id):
        elCliente = Cliente(self.repositorioCliente.findById(id))
        return elCliente.__dict__

    def update (self,id,infoCliente):
        ClienteActual = Cliente(self.repositorioCliente.findById(id))
        ClienteActual.telefono= infoCliente["telefono"]
        ClienteActual.nombre = infoCliente["nombre"]
        ClienteActual.apellido = infoCliente["apellido"]
        ClienteActual.correo = infoCliente["correo"]
        ClienteActual.comentario = infoCliente["comentario"]
        return self.repositorioCliente.save(ClienteActual)

    def delete (self,id):
        return self.repositorioCliente.delete(id)


