import socketserver
import os
import json

class Server(socketserver.BaseRequestHandler):
	"""docstring for Server"""

	def handle(self):
		try:
			# O atributo request se refere a conexão
			dado_recebido = self.request.recv(32)
			dado = dado_recebido.decode().upper()

			# Os dados que vão ser enviados
			dados = []

			diretorios = os.listdir("data_server")
				

			if dado == 'L': # Se for requisitado a listagem

				for info in diretorios:
					arq = open(f'data_server/{info}/list.json', 'r')
					dados_aux = arq.read()

					dicio = json.loads(dados_aux)
					dados.append([dicio['local'], dicio['preco']])

					arq.close()

				
			if dado == 'I': # Se for requisitado informações básicas
				
				for info in diretorios:
					arq = open(f'data_server/{info}/list.json', 'r')
					dados_aux = arq.read()

					dicio = json.loads(dados_aux)
					dados.append([dicio['imagem'], dicio['local'], dicio['nome']])

					arq.close()


			self.request.send(str(dados).encode())

		except Exception as E:
			print('Conexão falha', E)

		finally:
			self.request.close()




if __name__ == '__main__':
	host, port = ('localhost', 50002)

	server = socketserver.ThreadingTCPServer(
		(host, port), Server
		)

	server.serve_forever()
		