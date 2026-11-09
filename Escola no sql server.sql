-- comando pra cria o banco de dados
Create database escola;

-- comando pra usa o banco de dados
use escola;

-- tabela alunos
create table alunos 
(
	id int identity(1,1) primary key, -- identity (1,1) significa que o id vai começar em 1 e vai incrementar de 1 em 1
	nome varchar(100) not null,
	idade int not null,
	email varchar(100) unique not null,
	cpf varchar(11) unique not null, -- unique significa que não pode ter dois alunos com o mesmo cpf
	docentes_id int, -- chave estrangeira para a tabela docentes
	salas_id int, -- chave estrangeira para a tabela salas
    foreign key (docentes_id) references docentes(id), --  relacionamento
    foreign key (salas_id) references salas(id) -- relacionamento
);

alter table alunos drop column professor_id; -- removendo a coluna professor_id da tabela alunos
select * from alunos;

-- fazendo as inserções na tabela alunos
insert into alunos (nome, idade, email, cpf, docentes_id, salas_id) values ('João Silva', 20, 'joao.silva@email.com', '12345678901', 1, 1);
insert into alunos (nome, idade, email, cpf, docentes_id, salas_id) values ('Maria Oliveira', 22, 'maria.oliveira@email.com', '12345678902', 2, 2);
insert into alunos (nome, idade, email, cpf, docentes_id, salas_id) values ('Pedro Santos', 21, 'pedro.santos@email.com', '12345678903', 3, 3);
insert into alunos (nome, idade, email, cpf, docentes_id, salas_id) values ('Ana Costa', 23, 'ana.costa@email.com', '12345678904', 4, 4);
insert into alunos (nome, idade, email, cpf, docentes_id, salas_id) values ('Carlos Pereira', 24, 'carlos.pereira@email.com', '12345678905', 5, 5);

--add column docentes_id relacionamento varios alunos 1 docente
alter table alunos add docentes_id int; -- adicionando a coluna docentes_id na tabela alunos
alter table alunos add foreign key (docentes_id) references docentes(id); -- criando o relacionamento entre a tabela alunos e a tabela docentes

--add column salas_id relacionamento varios alunos 1 sala
alter table alunos add salas_id int;
alter table alunos add foreign key (salas_id) references salas(id);

-- tabela cursos
create table cursos 
(
	id int identity(1,1) primary key,
	nome varchar(100) not null,
	descricao varchar(255) not null
);

-- fazendo as inserções na tabela cursos
insert into cursos (nome, descricao) values ('Curso de Matemática', 'Curso de Matemática para iniciantes');
insert into cursos (nome, descricao) values ('Curso de Física', 'Curso de Física para iniciantes');
insert into cursos (nome, descricao) values ('Curso de Química', 'Curso de Química para iniciantes');
insert into cursos (nome, descricao) values ('Curso de Biologia', 'Curso de Biologia para iniciantes');
insert into cursos (nome, descricao) values ('Curso de História', 'Curso de História para iniciantes');

-- tabela n-n de cursos com alunos
create table alunos_cursos 
(
	id int identity(1,1) primary key,
	aluno_id int not null,
	curso_id int not null,
	foreign key (aluno_id) references alunos(id),
	foreign key (curso_id) references cursos(id)
);

-- fazendo as inserções na tabela alunos_cursos
insert into alunos_cursos (aluno_id, curso_id) values (1, 1);
insert into alunos_cursos (aluno_id, curso_id) values (2, 2);
insert into alunos_cursos (aluno_id, curso_id) values (3, 3);
insert into alunos_cursos (aluno_id, curso_id) values (4, 4);
insert into alunos_cursos (aluno_id, curso_id) values (5, 5);

-- tabela disciplinas
create table disciplinas 
(
	id int identity(1,1) primary key,
	nome varchar(100) not null,
	carga_horaria int not null,
	curso_id int not null, -- chave estrangeira para a tabela cursos
	foreign key (curso_id) references cursos(id) -- relacionamento
);

-- fazendo as inserções na tabela disciplinas
insert into disciplinas (nome, carga_horaria, curso_id) values ('Matemática Básica', 60, 1);
insert into disciplinas (nome, carga_horaria, curso_id) values ('Física Básica', 60, 2);
insert into disciplinas (nome, carga_horaria, curso_id) values ('Química Básica', 60, 3);
insert into disciplinas (nome, carga_horaria, curso_id) values ('Biologia Básica', 60, 4);
insert into disciplinas (nome, carga_horaria, curso_id) values ('História Básica', 60, 5);

-- tabela notas
create table notas 
(
	id int identity(1,1) primary key,
	aluno_id int not null, -- chave estrangeira para a tabela alunos
	disciplina_id int not null, -- chave estrangeira para a tabela disciplinas
	docente_id int not null, -- chave estrangeira para a tabela docentes
	nota decimal(5,2) not null,
	foreign key (aluno_id) references alunos(id), -- relacionamento
	foreign key (disciplina_id) references disciplinas(id), -- relacionamento
	foreign key (docente_id) references docentes(id) -- relacionamento
);

-- ver os relacionamentos da tabela notas
select
    fk.name as nome_relacionamento,
    OBJECT_NAME(fk.parent_object_id) as tabela_origem,
    COL_NAME(fkc.parent_object_id, fkc.parent_column_id) as coluna_origem,
    OBJECT_NAME(fk.referenced_object_id) as tabela_referenciada,
    COL_NAME(fkc.referenced_object_id, fkc.referenced_column_id) as coluna_referenciada
from sys.foreign_keys fk
inner join sys.foreign_key_columns fkc
    on fk.object_id = fkc.constraint_object_id
where OBJECT_NAME(fk.parent_object_id) = 'notas'
   OR OBJECT_NAME(fk.referenced_object_id) = 'notas';

-- fazendo as inserções na tabela notas
insert into notas (aluno_id, disciplina_id, docente_id, nota) values (1, 1, 1, 8.5);
insert into notas (aluno_id, disciplina_id, docente_id, nota) values (2, 2, 2, 7.5);
insert into notas (aluno_id, disciplina_id, docente_id, nota) values (3, 3, 3, 9.0);
insert into notas (aluno_id, disciplina_id, docente_id, nota) values (4, 4, 4, 8.0);
insert into notas (aluno_id, disciplina_id, docente_id, nota) values (5, 5, 5, 7.0);

-- tabela docentes
create table docentes 
(
	id int identity(1,1) primary key,
	nome varchar(100) not null,
	idade int not null,
	email varchar(100) unique not null,
	cpf varchar(11) unique not null
);

-- fazendo as inserções na tabela docentes
insert into docentes (nome, idade, email, cpf) values ('Carlos Silva', 40, 'carlos.silva@email.com', '12345678901');
insert into docentes (nome, idade, email, cpf) values ('Maria Oliveira', 35, 'maria.oliveira@email.com', '12345678902');
insert into docentes (nome, idade, email, cpf) values ('Pedro Santos', 45, 'pedro.santos@email.com', '12345678903');
insert into docentes (nome, idade, email, cpf) values ('Ana Costa', 30, 'ana.costa@email.com', '12345678904');
insert into docentes (nome, idade, email, cpf) values ('Carlos Pereira', 50, 'carlos.pereira@email.com', '12345678905');

-- remover relacionamento
alter table docentes drop constraint FK__docentes__notas___6D0D32F4;

-- tira a coluna notas_id da tabela docentes
alter table docentes drop column notas_id;

--add column notas_id relacionamento varias notas 1 docente
alter table docentes add notas_id int;
alter table docentes add foreign key (notas_id) references notas(id);

-- ver todos os bancos de dados criados
select name from sys.databases;

-- ver todas as tabelas criadas
select name from sys.tables;

-- tabela funcionarios
create table funcionarios 
(
	id int identity(1,1) primary key,
	nome varchar(100) not null,
	idade int not null,
	email varchar(100) unique not null,
	cpf varchar(11) unique not null
);

-- fazendo as inserções na tabela funcionarios
insert into funcionarios (nome, idade, email, cpf) values ('João Silva', 30, 'joao.silva@email.com', '12345678901');
insert into funcionarios (nome, idade, email, cpf) values ('Maria Oliveira', 25, 'maria.oliveira@email.com', '12345678902');
insert into funcionarios (nome, idade, email, cpf) values ('Pedro Santos', 35, 'pedro.santos@email.com', '12345678903');
insert into funcionarios (nome, idade, email, cpf) values ('Ana Costa', 28, 'ana.costa@email.com', '12345678904');
insert into funcionarios (nome, idade, email, cpf) values ('Carlos Pereira', 40, 'carlos.pereira@email.com', '12345678905');

-- tabela n-n de funcionarios com salas
create table funcionarios_salas 
(
	id int identity(1,1) primary key,
	funcionario_id int not null,
	sala_id int not null,
	foreign key (funcionario_id) references funcionarios(id),
	foreign key (sala_id) references salas(id)
);

-- fazendo as inserções na tabela funcionarios_salas
insert into funcionarios_salas (funcionario_id, sala_id) values (1, 1);
insert into funcionarios_salas (funcionario_id, sala_id) values (2, 2);
insert into funcionarios_salas (funcionario_id, sala_id) values (3, 3);
insert into funcionarios_salas (funcionario_id, sala_id) values (4, 4);
insert into funcionarios_salas (funcionario_id, sala_id) values (5, 5);

--tabela n-n de docentes com salas
create table docentes_salas 
(
	id int identity(1,1) primary key,
	docente_id int not null,
	sala_id int not null,
	foreign key (docente_id) references docentes(id),
	foreign key (sala_id) references salas(id)
);

-- fazendo as inserções na tabela docentes_salas
insert into docentes_salas (docente_id, sala_id) values (1, 1);
insert into docentes_salas (docente_id, sala_id) values (2, 2);
insert into docentes_salas (docente_id, sala_id) values (3, 3);
insert into docentes_salas (docente_id, sala_id) values (4, 4);
insert into docentes_salas (docente_id, sala_id) values (5, 5);

-- tabela salas
create table salas 
(
	id int identity(1,1) primary key,
	nome varchar(100) not null
);

-- fazer inserções na tabela salas, 5 salas criadas, primeiro foi efetuado na tabela salas pq ela nao tem chave estrangeira e nao depende de nenhuma tabela diferente das outras tabelas
insert into salas (nome) values ('Sala 1');
insert into salas (nome) values ('Sala 2');
insert into salas (nome) values ('Sala 3');
insert into salas (nome) values ('Sala 4');
insert into salas (nome) values ('Sala 5');

--tabela n-n de cursos com alunos
create table matriculas 
(
	id int identity(1,1) primary key,
	aluno_id int not null,
	curso_id int not null,
	data_matricula date not null,
	foreign key (aluno_id) references alunos(id),
	foreign key (curso_id) references cursos(id)
); 

insert into matriculas (aluno_id, curso_id, data_matricula) values (1, 1, '2024-01-01');
insert into matriculas (aluno_id, curso_id, data_matricula) values (2, 2, '2024-01-02');
insert into matriculas (aluno_id, curso_id, data_matricula) values (3, 3, '2024-01-03');
insert into matriculas (aluno_id, curso_id, data_matricula) values (4, 4, '2024-01-04');
insert into matriculas (aluno_id, curso_id, data_matricula) values (5, 5, '2024-01-05');