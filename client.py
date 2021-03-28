import socket

class Client(object):
	"""docstring for Client"""
	def __init__(self, host, port):

		# Cria uma conexão TCP/IP com o servidor
		self.sockobj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.sockobj.connect((host, port))

		self.buffer = None
	def Envia(self, entrada:str):
		self.sockobj.send(entrada.encode())
		
	def Recebe(self, tamanho):
		self.sockobj.recv(tamanho)
		
if __name__ == '__main__':
	inst = Client('localhost', 50002)

	inst.Envia()
