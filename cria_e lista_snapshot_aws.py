#coding: utf-8

print 'Bem vindo ao sistema de rotatividade de snapshots na aws'
print ''
print 'Opção 1 - Cadastrar volume para ser deletado'
print 'Opção 2 - Listar volumes cadastrados atualmente'

option = str(raw_input("Digite qual a opção desejada: 1 ou 2: "))

if option == '1':


	volumes = open("volumes.txt", "a")

	vol = str(raw_input("Insira o nome do volume: "))
	desc = str(raw_input("Insira a descricao do volume: "))
	ret = int(raw_input("Insira a qtde de dias de retenção: "))

	volumes.write("%s:%s:%s:\n" %(vol, desc, ret))

	volumes.close()

if option == '2':

	volumes = open("volumes.txt", "r")
	line = volumes.read()
	print line