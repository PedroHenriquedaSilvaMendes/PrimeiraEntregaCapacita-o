import sqlite3, time

id = 0
t = 0
connect = sqlite3.connect('bancodedados.db')
c = connect.cursor()

def bddcreate():
    c.execute('CREATE TABLE IF NOT EXISTS lista (id integer, nome text, doacao integer, total integer)')
try:
    bddcreate()
except:
    print('Erro na criacao do banco de dados')
else:
    print('Banco de dados criado com sucesso')

def cadastro( n, d, t):
    i = id
    c.execute('INSERT INTO lista VALUES(?, ?, ?, ?)', (i, n, d, t))
    id += 1
    connect.commit()

def consulta(c):
    sql = 'SELECT * FROM lista WHERE nome = ?'
    for row in c.execute(sql, (c,)):
        print (row[0], row[1], row[2])

def consultavalortotal(c):
    sql = 'SELECT * FROM lista WHERE nome = ?'
    for row in c.execute(sql, (c,)):
        print(row[3])

escolha = int(input('1-Cadastrar nova doacao\n2-Consultar a lista de doacoes\nQual o comando?'))

if escolha == 1:

    try:
        print('Nova doacao!!')
        time.sleep(3)
        n = str(input('Digite o nome: '))
        d = int(input('Digite o valor inteiro da doacao: '))
        t += d
        cadastro(n,d,t)
    except:
        print('Erro ao cadastrar!')
    else:
        print('Cadastrado com sucesso!')
elif escolha == 2:
    print('Ferramenta de consulta, carregando...')
    time.sleep(1)
    c = str(input('Digite o nome que quer buscar: '))
    consulta(c)
elif escolha == 3:
    print('Ferramenta de consulta, carregando...')
    time.sleep(1)
    c = str(input('Digite o nome da pessoa para saber o valor total de doacoes no momento do cadastro dela: '))
    consultavalortotal(c)
else:
    print('Valor nao valido, execute novamente o programa!')