from socket import *

serverHost = 'localhost'
serverPort = 30800

mensagem = [ b'nao vai ter como jogar CS, minha internet esta ruim por ter criado um servidor']


sockobj = socket(AF_INET, SOCK_STREAM)
sockobj.connect ((serverHost,serverPort))

for linha in mensagem:
    sockobj.send(linha)
    data = sockobj.recv(1024)
    print('Mensagem do servidor: ', data)
sockobj.close()