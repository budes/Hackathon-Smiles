import socket
from threading import *

class Client(Thread):
	"""docstring for Client"""
	def __init__(self, host, port):
		Thread.__init__(self)
		
		# Cria uma conexão TCP/IP com o servidor
		self.sockobj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.sockobj.connect((host, port))
		
		self.buffer = None

	def Envia(self, entrada:str):
		self.sockobj.send(entrada.encode())
		
	def Recebe(self, tamanho):
		self.buffer = self.sockobj.recv(tamanho)
		
		return self.buffer
		
if __name__ == '__main__':
	inst = Client('localhost', 50003)

	from time import sleep

	inst.Envia('L')

	valor = inst.Recebe(32)
	valor_usavel = valor.decode()

	info = inst.Recebe(int(valor_usavel))
	info.decode()

	print(info)

	inst = Client('localhost', 50003)

	inst.Envia('I0')

	valor = inst.Recebe(32)
	valor_usavel = valor.decode()

	info = inst.Recebe(int(valor_usavel))

	print(info.decode())