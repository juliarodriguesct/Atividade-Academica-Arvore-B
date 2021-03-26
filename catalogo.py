# -*- coding: utf-8 -*-

class Catalogo():

	def abrirAlunos(self):
		caminhoDosAlunos = 't/Alunos.txt'
		return caminhoDosAlunos			
	def abrirCursos(self):
		caminhoDosCursos = 't/Cursos.txt'
		return caminhoDosCursos
	def abrirDisciplinas(self):
		caminhoDasDisciplinas = 't/Disciplinas.txt'
		return caminhoDasDisciplinas
	def abrirDisciplinasHistorico(self):
		caminhoDosHistoricos = 't/DisciplinaHistorico.txt'
		return caminhoDosHistoricos
	def abrirHash(self):
		caminhoDaHash = 't/hash.txt'
		return caminhoDaHash
	def abrirNested(self):
		caminhoDaNested = 't/nested.txt'
		return caminhoDaNested	
	def abrirSelecao(self):
		caminhoDaSelecao = 't/selecao.txt'
		return caminhoDaSelecao	
	def abrirProjecao(self):
		caminhoDaProjecao = 't/projecao.txt'
		return caminhoDaProjecao
	
	def leitura(self, escolha):
		if escolha == 1:
			objeto = self.abrirAlunos()
			with open(objeto) as entradaAluno:
				linhas = entradaAluno.read().splitlines()
				return linhas
		elif escolha == 2:
			objeto = self.abrirCursos()
			with open(objeto) as entradaCurso:
				linhas = entradaCurso.read().splitlines()
			return linhas
		elif escolha == 3:
			objeto = self.abrirDisciplinas() 
			with open(objeto) as entradaDisciplinas:
				linhas = entradaDisciplinas.read().splitlines()
			return linhas
		elif escolha == 4:
			objeto = self.abrirDisciplinasHistorico()
			with open(objeto) as entradaDisciplinaHistorico:
				linhas = entradaDisciplinaHistorico.read().splitlines()
			return linhas	
		elif escolha == 5:
			objeto = self.abrirHash() 
			with open(objeto) as entradaHash:
				linhas = entradaHash.read().splitlines()
			return linhas
		elif escolha == 6:
			objeto = self.abrirNested() 
			with open(objeto) as entradaNested:
				linhas = entradaNested.read().splitlines()
			return linhas
		elif escolha == 7:
			objeto = self.abrirSelecao() 
			with open(objeto) as entradaSelecao:
				linhas = entradaSelecao.read().splitlines()
			return linhas	
		else:
			objeto = self.abrirProjecao()
			with open(objeto) as entradaProjecao:
				linhas = entradaProjecao.read().splitlines()
			return linhas	
'''
def main():	
	C = Catalogo()
	escolha = input("Digite de 1 a 4: ")
	print(C.leitura(int(escolha)))

main()
				for linha in linhas:
					linhaEmPartes = linha.split()
					cursos['id_curso'] = linhaEmPartes[0]
					cursos['nome'] = " ".join(linhaEmPartes[1:])
					resultado.append(cursos)
					cursos = {}'''