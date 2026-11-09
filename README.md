# Sistema de Gerenciamento Escolar – Python e SQL Server

## Sobre o projeto
Projeto desenvolvido em Python integrado ao SQL Server, com o objetivo de gerenciar as informações de uma instituição de ensino.

O sistema permite realizar operações CRUD (Create, Read, Update e Delete) em todas as tabelas do banco de dados, por meio de um menu interativo no terminal.

## Tecnologias utilizadas
- Python
- SQL Server
- Biblioteca `mssql-python`
- SQL

## Estrutura do banco de dados
O banco de dados `escola` possui 11 tabelas:
- alunos
- funcionarios
- docentes
- cursos
- disciplinas
- salas
- matriculas
- notas
- alunos_cursos
- funcionarios_salas
- docentes_salas

## Funcionalidades do programa
- Cadastro, consulta, atualização e exclusão de registros.
- Gerenciamento de alunos, funcionários, docentes, cursos, disciplinas e salas.
- Controle de matrículas e notas.
- Gerenciamento dos relacionamentos entre alunos, cursos, funcionários, docentes e salas.
- Listagem das tabelas disponíveis no banco de dados.
- Validação de informações, como e-mails, CPFs e IDs relacionados.
- Integração com o SQL Server para armazenar e consultar os dados.

## Objetivo
Aplicar conhecimentos de Python e SQL Server, desenvolvendo um sistema de gerenciamento escolar que utiliza operações CRUD e trabalha com banco de dados relacionais.
