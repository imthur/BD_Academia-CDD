import mysql.connector

def menu():
    print("=" * 35)
    print(" MENU DE ADMINISTRAÇÃO DA ACADEMIA")
    print("=" * 35)
    print("[1] Inserir")
    print("[2] Remover")
    print("[3] Procurar")
    print("[0] Sair")
    print("=" * 35)

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="ARTHUUR132",
    database="desafioacademia"
)
mycursor = mydb.cursor()
loop = True
while loop:
    menu()
    choice = input("Digite o dígito da operação que deseja efetuar: ")
    #Tipo de Dado
    if choice != "0":
        while True:
            print("=" * 35)
            print("Qual será o tipo de dado?")
            print("=" * 35)
            print("[1] Aluno")
            print("[2] Funcionário")
            print("[3] Modalidade")
            print("[4] Personal")
            print("=" * 35)
            type = int(input("Digite aqui: "))
            if type == 1:
                table = "alunos"
                break
            if type == 2:
                table = "funcionarios"
                break
            if type == 3:
                table = "modalidades"
                break
            if type == 4:
                table = "personal"
                break
            else:
                print("Insira um dígito válido.")
    #Inserir
    if choice == "1":
        if table == "alunos":
            nome = input("Digite o nome do aluno: ")
            telefone = input(f"Digite o telefone do aluno {nome}: ")
            endereco = input(f"Digite o endereço do aluno {nome}: ")
            cpf = input(f"Digite o CPF do aluno {nome}: ")
            email = input(f'Digite o email do aluno {nome}: ')
            val = (nome, telefone, endereco, cpf, email)
            sql = "INSERT INTO alunos (NOME, TELEFONE, ENDEREÇO, CPF, EMAIL) VALUES (%s, %s, %s, %s, %s)"
            mycursor.execute(sql, val)
            mydb.commit()
            print("=" * 35)
            print(" ALUNO ADICIONADO COM SUCESSO!")
        if table == "personal":
            nome = input("Digite o nome do personal: ")
            cpf = input(f"Digite o CPF do personal {nome}: ")
            cref = input(f"Digite o CREF do personal {nome}: ")
            telefone = input(f"Digite o telefone do personal {nome}: ")
            endereco = input(f"Digite o endereço do personal {nome}: ")
            val = (cpf, cref, nome, telefone, endereco)
            sql = "INSERT INTO personal (CPF, CREF, NOME, TELEFONE, ENDEREÇO) VALUES (%s, %s, %s, %s, %s)"
            mycursor.execute(sql, val)
            mydb.commit()
            print("=" * 35)
            print("PERSONAL ADICIONADO COM SUCESSO!")
        if table == "funcionarios":
            nome = input("Digite o nome do funcionario: ")
            cpf = input(f"Digite o CPF do funcionario {nome}: ")
            salario = input(f"Digite o salario do funcionario {nome}: ")
            val = (nome, cpf, salario)
            sql = "INSERT INTO funcionarios (NOME, CPF, SALARIO) VALUES (%s, %s, %s)"
            mycursor.execute(sql, val)
            mydb.commit()
            print("=" * 35)
            print("FUNCIONÁRIO ADICIONADO COM SUCESSO!")
        if table == "modalidades":
            nome = input("Digite o nome da modalidade: ")
            desc = input(f"Digite a descrição da modalidade {nome}:")
            duracao = input(f"Digite a duração da modalidade {nome}: ")
            val = (nome, desc, duracao)
            sql = "INSERT INTO modalidades (NOME, DESCRICAO, DURACAO) VALUES (%s, %s, %s)"
            mycursor.execute(sql, val)
            mydb.commit()
            print("=" * 35)
            print("MODALIDADE ADICIONADA COM SUCESSO!")
    #Remover
    elif choice == "2":
        if table == "alunos":
            valor = input("Digite a matrícula do aluno que deseja remover: ")
            val = (valor, )
            sql = f"DELETE FROM {table} WHERE id = %s"
            mycursor.execute(sql, val)
            mydb.commit()
            print("=" * 35)
            print("ALUNO REMOVIDO COM SUCESSO!")
        if table == "personal":
            valor = input("Digite o CREF do personal que deseja remover: ")
            val = (valor, )
            sql = f"DELETE FROM {table} WHERE id = %s"
            mycursor.execute(sql, val)
            mydb.commit()
            print("=" * 35)
            print("PERSONAL REMOVIDO COM SUCESSO!")
        if table == "funcionarios":
            valor = input("Digite o ID do funcionário que deseja remover: ")
            val = (valor, )
            sql = f"DELETE FROM {table} WHERE id = %s"
            mycursor.execute(sql, val)
            mydb.commit()
            print("=" * 35)
            print("FUNCIONÁRIO REMOVIDO COM SUCESSO!")
        if table == "modalidades":
            valor = input("Digite o ID da modalidade que deseja remover: ")
            val = (valor, )
            sql = f"DELETE FROM {table} WHERE id = %s"
            mycursor.execute(sql, val)
            mydb.commit()
            print("=" * 35)
            print("MODALIDADE REMOVIDA COM SUCESSO!")
    #Procurar
    elif choice == "3":
        if table == "alunos":
            mycursor.execute(f"SELECT * FROM {table}")
            resultado = mycursor.fetchall()

            for aluno in resultado:
                print("=" * 35)
                print(f"MATRÍCULA: {aluno[0]}")
                print(f"NOME: {aluno[1]}")
                print(f"TELEFONE: {aluno[2]}")
                print(f"ENDEREÇO: {aluno[3]}")
                print(f"CPF: {aluno[4]}")
                print(f"EMAIL: {aluno[5]}")
                print("=" * 35)
        if table == "personal":
            mycursor.execute(f"SELECT * FROM {table}")
            resultado = mycursor.fetchall()

            for personal in resultado:
                print("=" * 35)
                print(f"NOME: {personal[0]}")
                print(f"CPF: {personal[1]}")
                print(f"CREF: {personal[2]}")
                print(f"TELEFONE: {personal[3]}")
                print(f"ENDEREÇO: {personal[4]}")
                print("=" * 35)
        if table == "modalidades":
            mycursor.execute(f"SELECT id, nome, descricao, duracao FROM {table}")
            resultado = mycursor.fetchall()

            for modalidade in resultado:
                print("=" * 35)
                print(f"ID: {modalidade[0]}")
                print(f"NOME: {modalidade[1]}")
                print(f"DESCRIÇÃO: {modalidade[2]}")
                print(f"DURAÇÃO: {modalidade[3]}")
                print("=" * 35)
        if table == "funcionarios":
            mycursor.execute(f"SELECT id, nome, cpf, salario FROM {table}")
            resultado = mycursor.fetchall()

            for funcionario in resultado:
                print("=" * 35)
                print(f"ID: {funcionario[0]}")
                print(f"NOME: {funcionario[1]}")
                print(f"CPF: {funcionario[2]}")
                print(f"SALÁRIO: {funcionario[3]}")
                print("=" * 35)
    #Sair
    elif choice == "0":
        while True:
            doubt = input("DIGITE 1 PARA ENCERRAR OU 2 PARA VOLTAR AO MENU: ")
            if doubt != "1" and doubt != "2":
                print("Insira um dígito válido.")
            else:
                break
        if doubt == "1":
            break
        if doubt == "2":
            ...
print("Programa finalizado!")
