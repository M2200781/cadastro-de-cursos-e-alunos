#Importando SQLite3
import sqlite3 as lite

#criando conexão

try:
    con =lite.connect('cadastro_alunos.db')
    print('Conexao com o banco de dados realizado com sucesso!')
except lite.Error as e:
    print('Erro ao conectar ao banco de dados:', e)
    
    
# Talela cursos-------------------------------------------------
#CRUD

# criar Cursos (Create C)RUD
def criar_curso(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Cursos(nome, duracao, preco) VALUES(?,?,?)"
        cur.execute(query, i)
        
#criar_curso(['Python', 'Semanas', 50])

#Ver todos os cursos (Read R)UD

def ver_cursos():
    lista = []
    with con:
        cur = con.cursor()
        cur.execute('SELECT * FROM Cursos')
        linha = cur.fetchall()
        
        for i in linha:
            lista.append(i)
    return lista
#print(ver_cursos())

#Atualizar os cursos(Update U)D
def atualizar_curso(i):
    with con:
        cur = con.cursor()
        query = "UPDATE Cursos SET nome=?, duracao=?, preco=? WHERE id=?"
        cur.execute(query, i)            
    
#atualizar_curso(l)


#Deletar cursos(Delete D)
def deletar_curso(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM Cursos WHERE id=?"
        cur.execute(query, i)
#deletar_curso([1])


# Talela Turmas-------------------------------------------------

#Criar Turmas
def criar_turma(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Turmas(nome, curso_nome, data_inicio) VALUES(?, ?, ?)"
        cur.execute(query, i)
        

#Ver todas as turmas (Read R)UD

def ver_turmas():
    lista = []
    with con:
        cur = con.cursor()
        cur.execute('SELECT * FROM turmas')
        linha = cur.fetchall()
        
        for i in linha:
            lista.append(i)
    return lista
#print(ver_turmas())       


#Atualizar as turmas(Update U)D
def atualizar_turma(i):
    with con:
        cur = con.cursor()
        query = "UPDATE turmas SET nome=?, curso_nome=?, data_inicio=? WHERE id=?"
        cur.execute(query, i)          
        
        
#Deletar turma(Delete D)
def deletar_turma(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM Turmas WHERE id=?"
        cur.execute(query, i)
        
        
# Talela Alunos-------------------------------------------------

# criar Alunos (Create C)RUD
def criar_alunos(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Alunos(nome, email, telefone, sexo, imagem, data_nascimento, cpf, turma_nome) VALUES(?, ?, ?, ?, ?, ?, ?, ?)"
        cur.execute(query, i)
        
        
#Ver Alunos (Read R)UD
def ver_alunos():
    lista = []
    with con:
        cur = con.cursor()
        cur.execute('SELECT * FROM alunos')
        linha = cur.fetchall()
        
        for i in linha:
            lista.append(i)
    return lista


#Atualizar Alunos(Update U)D
def atualizar_aluno(i):
    with con:
        cur = con.cursor()
        query = "UPDATE alunos SET nome=?, email=?, telefone=?, sexo=?, imagem=?, data_nascimento=?, cpf=?, turma_nome=? WHERE id=?"
        cur.execute(query, i)
        
        
#Deletar Aluno(Delete D)
def deletar_aluno(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM alunos WHERE id=?"
        cur.execute(query, i)




