# importa a função do sql pro python
from mssql_python import connect

# importa o tipo date
from datetime import datetime

# cria a conexão com o banco da minha preferencia
conexao = connect("Server=localhost;Database=escola;Trusted_Connection=yes;TrustServerCertificate=yes;")

# cria o cursor que executa comandos sql no python
cursor = conexao.cursor()

while True:
    print("\n")
    print("=== BANCO DE DADOS ESCOLA ===")
    print("1 - Consultar alunos")
    print("2 - Cadastrar alunos")
    print("3 - Alterar alunos")
    print("4 - Excluir alunos")
    print("5 - Consultar Tabelas")
    print("6 - Consultar funcionarios")
    print("7 - Cadastrar funcionarios")
    print("8 - Alterar funcionarios")
    print("9 - Excluir funcionarios")
    print("10 - Consultar cursos")
    print("11 - Cadastrar cursos")
    print("12 - Alterar cursos")
    print("13 - Excluir cursos")
    print("14 - Consultar docentes")
    print("15 - Cadastrar docentes")
    print("16 - Alterar docentes")
    print("17 - Excluir docentes")
    print("18 - Consultar matriculas")
    print("19 - Cadastrar matriculas")
    print("20 - Alterar matriculas")
    print("21 - Excluir matriculas")
    print("22 - Consultar salas")
    print("23 - Cadastrar salas")
    print("24 - Alterar salas")
    print("25 - Excluir salas")
    print("26 - Consultar disciplinas")
    print("27 - Cadastrar disciplinas")
    print("28 - Alterar disciplinas")
    print("29 - Excluir disciplinas")
    print("40 - Sair")

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

                # o not é pra se nao achar nenhum outro email alem do inserido no momento,
                # basicamente o not é pro valor dps da virgula: (email, )
                # o email é o inserido na hora, dps da virgula é os outros q ele vai procura
                if not cursor.fetchone():
                    break

                print("Email já cadastrado!")
                email = input("Digite outro email: ")
            print("\n")
            cpf = input("Digite o CPF do aluno: ")
            # verificando se o cpf é valido
            while True:
                cursor.execute("select id from alunos where cpf = ?", (cpf,))

                if not cursor.fetchone():
                    break

                print("CPF já cadastrado!")
                cpf = input("Digite outro CPF: ")
            print("\n")
            # pedindo pra inserir o id do docente
            docentes_id = int(input("Digite o ID do docente: "))

            # verifica se o docente existe
            while True:
                cursor.execute("select id from docentes where id = ?", (docentes_id,))

                if cursor.fetchone():
                    break

                print("Docente não encontrado!")
                docentes_id = int(input("Digite novamente o ID do docente: "))
            print("\n")

            # pedindo pra inserir o id da sala
            salas_id = int(input("Digite o ID da sala: "))

            # verifica se a sala existe
            while True:
                cursor.execute("select id from salas where id = ?", (salas_id,))

                if cursor.fetchone():
                    break

                print("Sala não encontrada!")
                salas_id = int(input("Digite novamente o ID da sala: "))
            print("\n")
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
            print("\n")
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
            print("\n")
            cpf = input("Digite o novo CPF: ")
            # verifica se o cpf já pertence a outro aluno
            while True:
                cursor.execute("select id from alunos where cpf = ? and id != ?", (cpf, aluno_id))

                if not cursor.fetchone():
                    break

                print("CPF já cadastrado para outro aluno!")
                cpf = input("Digite outro CPF: ")
            print("\n")
            # pedindo pra inserir o id do docente
            docentes_id = int(input("Digite o ID do docente: "))

            # verifica se o docente existe
            while True:
                cursor.execute("select id from docentes where id = ?", (docentes_id,))

                if cursor.fetchone():
                    break

                print("Docente não encontrado!")
                docentes_id = int(input("Digite novamente o ID do docente: "))
            print("\n")

            # pedindo pra inserir o id da sala
            salas_id = int(input("Digite o ID da sala: "))

            # verifica se a sala existe
            while True:
                cursor.execute("select id from salas where id = ?", (salas_id,))

                if cursor.fetchone():
                    break

                print("Sala não encontrada!")
                salas_id = int(input("Digite novamente o ID da sala: "))
            print("\n")
            # atualiza todos os dados do aluno
            cursor.execute("""update alunos set nome = ?, idade = ?, email = ?, cpf = ?, docentes_id = ?, salas_id = ? where id = ?
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
            print("\n")
            # exclui o aluno
            cursor.execute("delete from alunos where id = ?", (aluno_id,))

            # confirma a exclusão
            conexao.commit()
            print("Aluno excluído com sucesso!")
        case 5:
            print("\n")
            print("Você escolheu consultar as tabelas do banco!\n")

            # executando o comando pra ve as tabelas do banco
            cursor.execute("select name from sys.tables")

            # guardando os resultados na variavel resultado
            resultado = cursor.fetchall()
            print("Aqui estão as tabelas do banco Escola:")

            # mostrando uma tabela de cada vez com o for
            for tables in resultado:
                print(tables)
        case 6:
            print("\n")
            print("Você escolheu consultar os funcionarios!\n")

            # essa linha mostra todos os dados da entidade funcionarios do banco escola
            cursor.execute("select * from funcionarios")

            # fetchall() significa basicamente: pegue todos os resultados encontrados.
            # td isso foi pro resultado
            resultado = cursor.fetchall()

            # mostrando: para cada aluno que tiver no resultado: mostre aluno
            for funcionarios in resultado:
                print(funcionarios)
        case 7:
            print("\n")
            print("Você escolehu cadastrar os funcionarios!\n")

            nome = input("Informe o nome do funcionario: ")
            idade = int(input("Informe a idade do funcionario: "))

            email = input("Digite o email do funcionario: ")
            # verifica se o email já existe
            while True:
                # no (email,) a virgula faz com q possa ser todos os email que tem na tabela funcionarios, 
                # se for so (email) so vai passa um email inves de todos
                cursor.execute("select id from funcionarios where email = ?", (email,))

                if not cursor.fetchone():
                    break

                print("Email já cadastrado!")
                email = input("Digite outro email: ")
            print("\n")
            cpf = input("Digite o CPF do funcionario: ")
            # verificando se o cpf é valido
            while True:
                cursor.execute("select id from funcionarios where cpf = ?", (cpf,))

                if not cursor.fetchone():
                    break

                print("CPF já cadastrado!")
                cpf = input("Digite outro CPF: ")
            print("\n")
            # insere os dados na tabela alunos, os "?" sao substituidos pelas variaveis que tao dps dos parenteses
            cursor.execute("""insert into funcionarios (nome, idade, email, cpf) values (?, ?, ?, ?)
                """, (nome, idade, email, cpf))
            # confirma a inserção
            conexao.commit()
            print("\n")
            print("Funcionario cadastrado com sucesso!")
        case 8:
            print("\n")
            print("Você escolheu alterar os dados de um funcionario!\n")
            # pedindo pra inserir o id
            funcionario_id = int(input("Digite o ID do funcionario: "))

            # verifica se o id do aluno existe
            while True:
                cursor.execute("select id from funcionarios where id = ?", (funcionario_id,))

                # fetchone significa: nao achei nd
                if cursor.fetchone():
                    break

                print("Funcionario não encontrado!")

                # pedindo pra inserir denovo
                funcionario_id = int(input("Digite novamente o ID do funcionario: "))
            print("\n")
            nome = input("Informe o novo nome: ")
            idade = int(input("Informe a nova idade: "))
            email = input("Digite o novo email: ")
            # verifica se o email já pertence a outro aluno
            while True:
                cursor.execute("select id from funcionarios where email = ? and id != ?", (email, funcionario_id))

                if not cursor.fetchone():
                    break

                print("Email já cadastrado para outro funcionario!")
                email = input("Digite outro email: ")
            print("\n")
            cpf = input("Digite o novo CPF: ")
                # verifica se o cpf já pertence a outro aluno
            while True:
                cursor.execute("select id from funcionarios where cpf = ? and id != ?", (cpf, funcionario_id))

                if not cursor.fetchone():
                    break

                print("CPF já cadastrado para outro funcionario!")
                cpf = input("Digite outro CPF: ")
            print("\n")

            # atualiza todos os dados do aluno
            cursor.execute("""update funcionarios set nome = ?, idade = ?, email = ?, cpf = ? where id = ?
                """, (nome, idade, email, cpf, funcionario_id))

            # confirma a alteração
            conexao.commit()
            print("\n")
            print("Funcionario atualizado com sucesso!")
        case 9:
            print("\n")
            print("Você escolheu excluir um funcionario!\n")
            funcionario_id = int(input("Digite o ID do funcionario que deseja excluir: "))
            # verifica se o funcionario existe
            while True:
                cursor.execute("select id from funcionarios where id = ?", (funcionario_id,))

                if cursor.fetchone():
                    break

                print("Funcionario não encontrado!")
                funcionario_id = int(input("Digite novamente o ID do funcionario: "))
            print("\n")
            # exclui o funcionario
            conexao.execute("delete from funcionarios where id = ?", (funcionario_id,))

            # confirma a exclusão
            conexao.commit()
            print("Funcionario excluído com sucesso!")
        case 10:
            print("\n")
            print("Você escolheu consultar os cursos!\n")
            # essa linha mostra todos os dados da entidade cursos do banco escola
            cursor.execute("select * from cursos")

            # fetchall() significa basicamente: pegue todos os resultados encontrados.
            # td isso foi pro resultado
            resultado = cursor.fetchall()

            # mostrando: para cada aluno que tiver no resultado: mostre curso
            for cursos in resultado:
                print(cursos)
        case 11:
            print("\n")
            print("Você escolheu cadastrar um curso!\n")
            # pedindo os dados
            nome = input("Informe o nome do curso: ")
            descricao = input("Informe a descrição do curso: ")
            # inserindo
            cursor.execute("""insert into cursos (nome, descricao) values (?, ?)""", (nome, descricao))
            # confirmando e mostrando
            conexao.commit()
            print("\n")
            print("Curso cadastrado com sucesso!")
        case 12:
            print("\n")
            print("Você escolheu atualizar os cursos!\n")

            cursos_id = int(input("Informe o ID: "))
            while True:
                cursor.execute("select id from cursos where id = ?", (cursos_id,))
                if cursor.fetchone():
                    break
                print("Aluno não encontrado!\n")
                cursos_id = int(input("Informe o ID do curso existente: "))
            print("\n")
            nome = input("Informe o novo nome: ")
            descricao = input("Informe a nova descrição: ")
            cursor.execute("""update cursos set nome = ?, descricao = ? where id = ?""", (nome, descricao, cursos_id))
            conexao.commit()
            print("\n")
            print("Curso atualizado com sucesso!\n")
        case 13:
            print("\n")
            print("Você escolheu excluir um curso!\n")

            cursos_id = int(input("Informe o ID: "))

            while True:
                cursor.execute("select id from cursos where id = ?", (cursos_id,))
                if cursor.fetchone():
                    break
                print("Curso nao encontrado!")
                cursos_id = int(input("Informe o ID existente: "))
            print("\n")
            cursor.execute("delete from cursos where id = ?", (cursos_id,))
            conexao.commit()
            print("\n")
            print("Curso excluido com sucesso!")
        case 14:
            print("\n")
            print("Você escolheu consultar docentes!\n")

            cursor.execute("select * from docentes")
            resultado = cursor.fetchall()

            for docentes in resultado:
                print(docentes)
        case 15:
            print("\n")
            print("Você escolheu cadastrar docentes!\n")
            nome = input("Informe o nome: ")
            idade = int(input("Informe a idade: "))
            email = input("Informe o e-mail: ")
            while True:
                cursor.execute("select id from docentes where email = ?", (email,))
                if not cursor.fetchone():
                    break
                email = input("Informe um e-mail que nao seja repetido: ")
            print("\n")
            cpf = input("Informe o cpf: ")
            while True:
                cursor.execute("select id from docentes where cpf = ?", (cpf, ))
                if not cursor.fetchone():
                    break
                cpf = input("Informe um cpf que nao seja repetido: ")
            cursor.execute("""insert into docentes (nome, idade, email, cpf) values (?, ?, ?, ?)""", (nome, idade, email, cpf))
            conexao.commit()
            print("Docente cadastrado com sucesso!")
        case 16:
            print("\n")
            print("Você escolheu alterar os dados de um docente!\n")
            id_docentes = int(input("Informe o ID do docente: "))
            while True:
                cursor.execute("select id from docentes where id = ?", (id_docentes,))
                if cursor.fetchone():
                    break
                print("Docente não encontrado!")
                id_docentes = int(input("Informe um docente existente: "))
            print("\n")
            nome = input("Informe o novo nome: ")
            idade = int(input("Informe a nova idade: "))
            email = input("Informe o novo e-mail: ")
            while True:
                cursor.execute("select id from docentes where email = ? and id != ?", (email, id_docentes))
                if not cursor.fetchone():
                    break
                print("E-mail repetido!")
                email = input("Informe o novo e-mail que não seja repetido: ")
            print("\n")
            cpf = input("Informe o novo cpf: ")
            while True:
                cursor.execute("select id from docentes where cpf = ? and id != ?", (cpf, id_docentes))
                if not cursor.fetchone():
                    break
                print("CPF repetido!")
                cpf = input("Informe o novo cpf que não seja repetido: ")
            print("\n")
            cursor.execute("""update docentes set nome = ?, idade = ?, email = ?, cpf = ? where id = ?
                """, (nome, idade, email, cpf, id_docentes))
            conexao.commit()
            print("Docente atualizado com sucesso!")
        case 17:
            print("\n")
            print("Você escolheu excluir um docente!\n")
            id_docentes = int(input("Informe o ID do docente: "))
            while True:
                cursor.execute("select id from docentes where id = ?", (id_docentes,))
                if cursor.fetchone():
                    break
                print("Docente nao encontrado!")
                id_docentes = int(input("Informe o ID de um docente existente: "))
            print("\n")
            cursor.execute("delete from docentes where id = ?", (id_docentes,))
            conexao.commit()
            print("Docente excluído com sucesso!")
        case 18:
            print("\n")
            print("Você escolheu consultar uma matricula!\n")
            cursor.execute("select * from matriculas")
            resultado = cursor.fetchall()
            for matriculas in resultado:
                # por data de matricula ser do tipo date o python recebe automaticamente datetime, e precisa converte pra mostra
                # primeiro transforma td que ta na matricula em lista:
                matriculas = list(matriculas)
                # dps pega o terceiro dado e converte em texto com dia, mes e ano
                matriculas[3] = matriculas[3].strftime("%d-%m-%Y")

                # tuple vai fazer o contrario do list, vai deixa em: ex:(1, 1, 1, 10-01-2021)
                print(tuple(matriculas))
        case 19:
            print("\n")
            print("Você escolheu cadastrar matricula!\n")
            aluno_id = int(input("Informe o ID do aluno: "))
            while True:
                cursor.execute("select id from alunos where id = ?", (aluno_id,))
                if cursor.fetchone():
                    break
                print("Aluno não existente!")
                aluno_id = int(input("Informe o ID de um aluno existente: "))
            print("\n")
            curso_id = int(input("Informe o ID do curso: "))
            while True:
                cursor.execute("select id from cursos where id = ?", (curso_id,))
                if cursor.fetchone():
                    break
                print("Curso não existe!")
                curso_id = int(input("Informe o ID do curso existente: "))
            print("\n")
            # pedindo pra inserir um dado do tipo datetime pq no python nao tem so date, pra inserir é assim, 
            # pra consultar é diferente
            data_matricula = input("Informe a data da matricula: ")
            data_matricula = datetime.strptime(data_matricula, "%d-%m-%Y").date()

            cursor.execute("""insert into matriculas (aluno_id, curso_id, data_matricula) values (?, ?, ?)
                """, (aluno_id, curso_id, data_matricula))
            conexao.commit()
            print("Matricula cadastrada com sucesso!")
        case 20:
            print("\n")
            print("Você escolheu alterar uma matricula!\n")

            id = int(input("Informe o ID da matricula: "))
            while True:
                cursor.execute("select id from matriculas where id = ?", (id, ))
                if cursor.fetchone():
                    break
                print("Matricula não existente!")
                id = int(input("Informe o ID de uma matricula existente: "))
            print("\n")
            aluno_id = int(input("Informe o ID do aluno: "))
            while True:
                cursor.execute("select id from alunos where id = ?", (aluno_id, ))
                if cursor.fetchone():
                    break
                print("Aluno não existente!")
                aluno_id = int(input("Informe o ID de uma aluno existente: "))
            print("\n")
            curso_id = int(input("Informe o ID do curso: "))
            while True:
                cursor.execute("select id from cursos where id = ?", (curso_id, ))
                if cursor.fetchone():
                    break
                print("Curso não existente!")
                curso_id = int(input("Informe o ID de uma cursos existente: "))
            print("\n")
            data_matricula = input("Informe a nova data da matricula: ")
            data_matricula = datetime.strptime(data_matricula, "%d-%m-%Y").date()
            cursor.execute("""update matriculas set aluno_id = ?, curso_id = ?, data_matricula = ? where id = ?
                """, (aluno_id, curso_id, data_matricula, id))
            conexao.commit()
            print("Matricula altera com sucesso!")
        case 21:
            print("\n")
            print("Você escolheu excluir uma matricula!\n")
            id = int(input("Informe o ID da matricula: "))
            while True:
                cursor.execute("select id from matriculas where id = ?", (id, ))
                if cursor.fetchone():
                    break
                print("Matricula não encontrada!")
                id = int(input("Informe o ID de uma matricula existente: "))
            print("\n")
            cursor.execute("delete from matriculas where id = ?", id)
            conexao.commit()
            print("Matricula excluida com sucesso!")
        case 22:
            print("\n")
            print("Você escolheu consultar uma sala!\n")
            cursor.execute("select * from salas")
            resultado = cursor.fetchall()
            for salas in resultado:
                print(salas)
        case 23:
            print("\n")
            print("Você escolheu cadastrar uma sala!\n")
            nome = input("Informe o nome da sala: ")

            cursor.execute("""insert into salas (nome) values (?)""", (nome))
            conexao.commit()
            print("Sala cadastrada com sucesso!")
        case 24:
            print("\n")
            print("Você escolheu alterar uma sala!\n")
            salas_id = int(input("Informe o ID da sala: "))
            while True:
                cursor.execute("select id from salas where id = ?", (salas_id, ))
                if cursor.fetchone():
                    break
                print("Sala não encontrada!")
                salas_id = int(input("Informe o ID de uma sala existente: "))
            print("\n")
            nome = input("Informe o novo nome da sala: ")
            cursor.execute("""update salas set nome = ? where id = ?""", (nome, salas_id))
            conexao.commit()
            print("Sala alterada com sucesso!")
        case 25:
            print("\n")
            print("Você escolheu excluir uma sala!\n")
            salas_id = int(input("Informe o ID da sala: "))
            while True:
                cursor.execute("select id from salas where id = ?", (salas_id, ))
                if cursor.fetchone():
                    break
                print("Sala não encontrada!")
                salas_id = int(input("Informe o ID de uma sala existente: "))
            print("\n")
            cursor.execute("delete from salas where id = ?", (salas_id))
            conexao.commit()
            print("Sala excluida com sucesso!")
        case 26:
            print("\n")
            print("Você escolheu consultar as disciplinas!\n")
            cursor.execute("select * from disciplinas")
            resultado = cursor.fetchall()
            for disciplina in resultado:
                print(disciplina)

        case 27:
            print("\n")
            print("Você escolheu cadastrar uma disciplina!\n")
            nome = input("Informe o nome da disciplina do curso: ")
            carga_horaria = int(input("Informe a carga horaria da disciplina: "))
            curso_id = int(input("Informe o ID do curso: "))
            while True:
                cursor.execute("select id from cursos where id = ?", (curso_id, ))
                if cursor.fetchone():
                    break
                print("Curso não encontrado!")
                curso_id = int(input("Informe o ID de um curso existente: "))
            print("\n")
            cursor.execute("""insert into disciplinas (nome, carga_horaria, curso_id) values (?,?,?)
                """, (nome, carga_horaria, curso_id))
            conexao.commit()
            print("Disciplina cadastrada com sucesso!")
        case 28:
            print("\n")
            print("Você escolheu alterar uma disciplina!\n")

            id = int(input("Informe o ID da disciplina: "))
            while True:
                cursor.execute("select id from disciplinas where id = ?", (id, ))
                if cursor.fetchone():
                    break
                print("Disciplina não encontrada!")
                id = int(input("Informe o ID de uma disciplina existente: "))
            print("\n")
            nome = input("Informe o novo nome: ")
            carga_horaria = int(input("Informe a nova carga horária: "))
            curso_id = int(input("Informe o novo ID do curso: "))
            while True:
                cursor.execute("select id from cursos where id = ?", (curso_id, ))
                if cursor.fetchone():
                    break
                print("Curso não encontrado!")
                curso_id = int(input("Informe o ID de um curso existente: "))
            print("\n")

            cursor.execute("""update disciplinas set nome = ?, carga_horaria = ?, curso_id = ? where id = ?
                """, (nome, carga_horaria, curso_id, id))
            conexao.commit()
            print("Disciplina alterada com sucesso!")
        case 29:
            print("\n")
            print("Você escolheu excluir uma disciplina!")
            id = int(input("Informe o ID da disciplina: "))
            while True:
                cursor.execute("select id from disciplinas where id = ?", (id, ))
                if cursor.fetchone():
                    break
                print("Disciplina não encontrada!")
                id = int(input("Informe o ID de uma disciplina existente: "))
            print("\n")
            cursor.execute("delete from disciplinas where id = ?", (id))
            conexao.commit()
            print("Disciplina excluída com sucesso!")
        case 40:
            print("Até logo...")
            break
        case _:
            print("Opção inválida")