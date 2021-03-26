from juncao import *

# -*- coding: utf-8 -*-

class Operacoes():
	
	def selecao(self, tabela, index, arg):

		file = open("t/selecao.txt", "w")

		for s in tabela:
			linha1 = s.split("\t")
			if linha1[index] == arg:
				file.write("\t".join(linha1) + "\n")
	def projecao(self, tabela, index , outroIndex):			

		file = open("t/projecao.txt", "w")

		for s in tabela:
			linha1 = s.split("\t")
			file.write(linha1[index] +"\t"+  linha1[outroIndex] + "\n") 

'''def main():
	o = Operacoes()
	c = Catalogo()
	o.selecao(c.leitura(4), 1, 'SERVICO SOCIAL')
	o.projecao(c.leitura(5), 4, 5)
main()'''		