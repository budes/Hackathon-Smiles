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

				# Cada elemento na string tem 1 byte, logo, a soma de todos os
				# elementos === peso do que vai enviar
				peso = len(str(dados))

				self.request.send(str(peso).encode())

				
			if 'I' in dado: # Se for requisitado informações básicas
				
				indice = int(dado[1:])

				info = diretorios[indice]

				arq = open(f'data_server/{info}/info.json', 'r')
				dados_aux = arq.read()

				dicio = json.loads(dados_aux)

				# A imagem a enviar é obtida em bytes
				imagem = open(f'data_server/{info}/imagem.jpg', 'rb')
				img_enviar = imagem.read()
				imagem.close()

				dados = [img_enviar, dicio['local'], dicio['nome']]

				arq.close()

				# Repito o mesmo processo acima para descobrir o peso do arquivo
				peso = len(str(dados))
				self.request.send(str(peso).encode())


			self.request.send(str(dados).encode())


		finally:
			self.request.close()




if __name__ == '__main__':
	host, port = ('localhost', 50003)

	server = socketserver.ThreadingTCPServer(
		(host, port), Server
		)

	server.serve_forever()
		