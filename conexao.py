# importa a função do sql pro python
from mssql_python import connect

# cria a conexão com o banco da minha preferencia
conexao = connect("Server=localhost;Database=escola;Trusted_Connection=yes;TrustServerCertificate=yes;")

# cria o cursor que executa comandos sql no python
cursor = conexao.cursor()

while True:
    print("\n")
    print("=== BANCO DE DADOS ESCOLA ===")
    print("1 - Consultar alunos")
    print("2 - Cadastrar aluno")
    print("3 - Alterar aluno")
    print("4 - Excluir aluno")
    print("5 - Sair")

    opcao = int(input("Escolha uma opção: "))

    match opcao:
        case 1:
            print("\n")
            print("Você escolheu consultar alunos!\n")
            # essa linha mostra todos os dados da entidade alunos do banco escola
            cursor.execute("select * from alunos")

            # fetchall() significa basicamente: pegue todos os resultados encontrados.
            # td isso foi pro resultado
            resultado = cursor.fetchall()

            # mostrando: para cada aluno que tiver no resultado: mostre aluno
            for aluno in resultado:
                print(aluno)
        case 2:
            print("\n")
            print("Você escolheu cadastrar aluno!\n")
            nome = input("Digite o nome do aluno: ")
            idade = int(input("Digite a idade do aluno: "))

            email = input("Digite o email do aluno: ")
            # verifica se o email já existe
            while True:
                # no (email,) a virgula faz com q possa ser todos os email que tem na tabela alunos, 
                # se for so (email) so vai passa um email inves de todos
                cursor.execute("select id from alunos where email = ?", (email,))

                if not cursor.fetchone():
                    break

                print("Email já cadastrado!")
                email = input("Digite outro email: ")

            cpf = input("Digite o CPF do aluno: ")
            # verificando se o cpf é valido
            while True:
                cursor.execute("select id from alunos where cpf = ?", (cpf,))

                if not cursor.fetchone():
                    break

                print("CPF já cadastrado!")
                cpf = input("Digite outro CPF: ")

            # pedindo pra inserir o id do docente
            docentes_id = int(input("Digite o ID do docente: "))

            # verifica se o docente existe
            while True:
                cursor.execute("select id from docentes where id = ?", (docentes_id,))

                if cursor.fetchone():
                    break

                print("Docente não encontrado!")
                docentes_id = int(input("Digite novamente o ID do docente: "))


            # pedindo pra inserir o id da sala
            salas_id = int(input("Digite o ID da sala: "))

            # verifica se a sala existe
            while True:
                cursor.execute("select id from salas where id = ?", (salas_id,))

                if cursor.fetchone():
                    break

                print("Sala não encontrada!")
                salas_id = int(input("Digite novamente o ID da sala: "))

            # insere os dados na tabela alunos, os "?" sao substituidos pelas variaveis que tao dps dos parenteses
            cursor.execute("""insert into alunos (nome, idade, email, cpf, docentes_id, salas_id) values (?, ?, ?, ?, ?, ?)
                """, (nome, idade, email, cpf, docentes_id, salas_id))
            # confirma a inserção
            conexao.commit()
            print("Aluno cadastrado com sucesso!")

        case 3:
            print("\n")
            print("Você escolheu alterar aluno!\n")

            # pedindo pra inserir o id
            aluno_id = int(input("Digite o ID do aluno: "))

            # verifica se o id do aluno existe
            while True:
                cursor.execute("select id from alunos where id = ?", (aluno_id,))

                # fetchone significa: nao achei nd
                if cursor.fetchone():
                    break

                print("Aluno não encontrado!")

                # pedindo pra inserir denovo
                aluno_id = int(input("Digite novamente o ID do aluno: "))

            nome = input("Digite o novo nome: ")
            idade = int(input("Digite a nova idade: "))
            email = input("Digite o novo email: ")
            # verifica se o email já pertence a outro aluno
            while True:
                cursor.execute("select id from alunos where email = ? and id != ?", (email, aluno_id))

                if not cursor.fetchone():
                    break

                print("Email já cadastrado para outro aluno!")
                email = input("Digite outro email: ")

            cpf = input("Digite o novo CPF: ")
                # verifica se o cpf já pertence a outro aluno
            while True:
                cursor.execute(
                "select id from alunos where cpf = ? and id != ?",
                (cpf, aluno_id)
                )

                if not cursor.fetchone():
                    break

                print("CPF já cadastrado para outro aluno!")
                cpf = input("Digite outro CPF: ")

            # pedindo pra inserir o id do docente
            docentes_id = int(input("Digite o ID do docente: "))

            # verifica se o docente existe
            while True:
                cursor.execute("select id from docentes where id = ?", (docentes_id,))

                if cursor.fetchone():
                    break

                print("Docente não encontrado!")
                docentes_id = int(input("Digite novamente o ID do docente: "))


            # pedindo pra inserir o id da sala
            salas_id = int(input("Digite o ID da sala: "))

            # verifica se a sala existe
            while True:
                cursor.execute("select id from salas where id = ?", (salas_id,))

                if cursor.fetchone():
                    break

                print("Sala não encontrada!")
                salas_id = int(input("Digite novamente o ID da sala: "))

            # atualiza todos os dados do aluno
            cursor.execute("""UPDATE alunos SET nome = ?, idade = ?, email = ?, cpf = ?, docentes_id = ?, salas_id = ? WHERE id = ?
                """, (nome, idade, email, cpf, docentes_id, salas_id, aluno_id))

            # confirma a alteração
            conexao.commit()

            print("Aluno atualizado com sucesso!")
        case 4:
            print("\n")
            print("Você escolheu excluir aluno!\n")

            aluno_id = int(input("Digite o ID do aluno que deseja excluir: "))
            # verifica se o aluno existe
            while True:
                cursor.execute("select id from alunos where id = ?", (aluno_id,))

                if cursor.fetchone():
                    break

                print("Aluno não encontrado!")
                aluno_id = int(input("Digite novamente o ID do aluno: "))

            # exclui o aluno
            cursor.execute("delete from alunos where id = ?", (aluno_id,))

            # confirma a exclusão
            conexao.commit()
            print("Aluno excluído com sucesso!")

        case 5:
            print("Até logo...")
            break
        case _:
            print("Opção inválida")