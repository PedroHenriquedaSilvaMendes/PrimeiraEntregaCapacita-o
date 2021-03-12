from socket import *

meuHost = 'localhost'
minhaPort = 30800

sockobj = socket(AF_INET, SOCK_STREAM)
sockobj.bind ((meuHost,minhaPort))
sockobj.listen (5)

while True:
    conexao, endereco = sockobj.accept()
    print ('O servidor foi conectado pelo endereço', endereco, ' e ele chamou para jogar CS')
    while True:
        data = conexao.recv(1024)
        if not data:
            break
        conexao.send( data)
    conexao.close()