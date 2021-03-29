from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.properties import ListProperty
from kivy.graphics import Color, Ellipse, Rectangle

from client import Client
from threading import *

class Gerenciador(ScreenManager):
	...

class Opcoes(Screen):
	def adiciona(self, nome, preco, i):
		self.ids.box.add_widget(Opcao(nome, preco, i))
		
		
class Opcao(ButtonBehavior, BoxLayout):
	def __init__(self, nome, preco, i):
		super(Opcao, self).__init__()
		self.i = i
		
		self.ids.titulo.text = nome
		self.ids.preco.text = preco


class Viagem(Screen):
	'''
	def __init__(self):
		super(Viagem, self).__init__()
		self.opcao = 1'''
				
	def on_pre_enter(self):
		thread = Client('192.168.0.104', 50004)
		thread.start()
		
		thread.Envia('L')
		thread.Recebe(32)
		
		from time import sleep
		thread.Recebe(int(thread.buffer.decode()))
		dados = eval(thread.buffer.decode())
		
		sleep(1)
		
		print(dados, thread.buffer)	
	
class Botao(ButtonBehavior, Label):
    cor = ListProperty([0.1,0.5,0.7,1])
    cor2 = ListProperty([0.1,0.1,0.1,1])

    def __init__(self,**kwargs):
        super(Botao,self).__init__(**kwargs)
        self.atualizar()

    def on_pos(self,*args):
        self.atualizar()

    def on_size(self,*args):
        self.atualizar()


    def atualizar(self,*args):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(rgba=self.cor)
            Ellipse(size=(self.height,self.height),
                    pos=self.pos)
            Ellipse(size=(self.height,self.height),
                    pos=(self.x+self.width-self.height,self.y))
            Rectangle(size=(self.width-self.height,self.height),
                      pos=(self.x+self.height/2.0,self.y))


class MainApp(App):
	def build(self):
		inst = Gerenciador()
		
		thread = Client('192.168.0.104', 50004)
		thread.start()
		
		thread.Envia('L')
		thread.Recebe(32)
		
		from time import sleep
		thread.Recebe(int(thread.buffer.decode()))
		dados = eval(thread.buffer.decode())
		
		sleep(1)
		
		print(dados, thread.buffer)
		
		for cria in range(len(dados)):
			inst.get_screen('opcoes').adiciona(
			*dados[cria], cria)
		
		return inst
		
MainApp().run()