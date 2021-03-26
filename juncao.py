from HashTable import *

# -*- coding: utf-8 -*-

class Juncao():

	
	def hashJoin(self, tabela1, tabela2):
		
		resultado = []
		
		hashing = HashTable(len(tabela1))
		
		file = open("t/hash.txt","w")

		for s in tabela2:
			linha = s.split("\t")
			hashing.insereHash(s)
		for i in tabela1:
			linha = i.split("\t")
			resultado = hashing.procuraHash(linha[1])
			if resultado is not None:
				file.write(resultado +"\t"+ "\t".join(linha) + "\n")

	def nestedLoopJoin(self, tabela1, tabela2):

		file = open("t/nested.txt","w")

		for s in tabela2:
			linha1 = s.split("\t")
			for r in tabela1:
				linha2 = r.split("\t")
				if linha1[0] == linha2[1]:						
					file.write("\t".join(linha1) +"\t"+ "\t".join(linha2) + "\n")

	def sortMergeJoin(self, tabela1, tabela2):

		file = open("t/mergesorted.txt","w")		
		contador = 0
		for s in tabela2:
			linha1 = s.split("\t")
			if contador == linha1[0]:
				for	r in tabela1:
					linha2 = r.split("\t")
					if linha1[0] == linha2[1]:						
						file.write("\t".join(linha1) +"\t"+ "\t".join(linha2) + "\n")
					
			else:
				contador += 1	


'''def main():

	c = Catalogo() 
	j = Juncao()

	f = lambda x, y, z: x[y] == z
	g = lambda x: f(x, y = 'id_curso', z = '5')
	h = lambda i: i['matricula']+ "\t" + i['nome']+"\n"

	i = lambda x, y, z: x[y] == z[y] 
	
	j.hashJoin(c.leitura(1), c.leitura(2))
	j.nestedLoopJoin(c.leitura(1), c.leitura(2))

main()'''	