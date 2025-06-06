-- 1. CRIAÇÃO DAS ROLES (SE NÃO EXISTIREM)
IF NOT EXISTS (SELECT 1 FROM sys.database_principals WHERE name = 'administrator' AND type = 'R')
    CREATE ROLE administrator;

IF NOT EXISTS (SELECT 1 FROM sys.database_principals WHERE name = 'instructor' AND type = 'R')
    CREATE ROLE instructor;

IF NOT EXISTS (SELECT 1 FROM sys.database_principals WHERE name = 'student' AND type = 'R')
    CREATE ROLE student;

IF NOT EXISTS (SELECT 1 FROM sys.database_principals WHERE name = 'reviewer' AND type = 'R')
    CREATE ROLE reviewer;

IF NOT EXISTS (SELECT 1 FROM sys.database_principals WHERE name = 'data_analyst' AND type = 'R')
    CREATE ROLE data_analyst;

PRINT 'Roles criadas ou já existentes.';

-- 2. CRIAÇÃO DE LOGINS E USUÁRIOS

IF NOT EXISTS (SELECT name FROM sys.server_principals WHERE name = 'admin_login')
    CREATE LOGIN admin_login WITH PASSWORD = 'AdminSenha123!';

IF NOT EXISTS (SELECT name FROM sys.database_principals WHERE name = 'admin_user')
    CREATE USER admin_user FOR LOGIN admin_login;

IF NOT EXISTS (SELECT name FROM sys.server_principals WHERE name = 'instructor_login')
    CREATE LOGIN instructor_login WITH PASSWORD = 'InstrutorSenha123!';

IF NOT EXISTS (SELECT name FROM sys.database_principals WHERE name = 'instructor_user')
    CREATE USER instructor_user FOR LOGIN instructor_login;

IF NOT EXISTS (SELECT name FROM sys.server_principals WHERE name = 'student_login')
    CREATE LOGIN student_login WITH PASSWORD = 'AlunoSenha123!';

IF NOT EXISTS (SELECT name FROM sys.database_principals WHERE name = 'student_user')
    CREATE USER student_user FOR LOGIN student_login;

IF NOT EXISTS (SELECT name FROM sys.server_principals WHERE name = 'reviewer_login')
    CREATE LOGIN reviewer_login WITH PASSWORD = 'RevisorSenha123!';

IF NOT EXISTS (SELECT name FROM sys.database_principals WHERE name = 'reviewer_user')
    CREATE USER reviewer_user FOR LOGIN reviewer_login;

IF NOT EXISTS (SELECT name FROM sys.server_principals WHERE name = 'data_analyst_login')
    CREATE LOGIN data_analyst_login WITH PASSWORD = 'AnalistaSenha123!';

IF NOT EXISTS (SELECT name FROM sys.database_principals WHERE name = 'data_analyst_user')
    CREATE USER data_analyst_user FOR LOGIN data_analyst_login;

PRINT 'Logins e usuários criados ou já existentes.';

ALTER ROLE administrator ADD MEMBER admin_user;
ALTER ROLE instructor ADD MEMBER instructor_user;
ALTER ROLE student ADD MEMBER student_user;
ALTER ROLE reviewer ADD MEMBER reviewer_user;
ALTER ROLE data_analyst ADD MEMBER data_analyst_user;

PRINT 'Usuários adicionados às roles.';

-- ADMINISTRADOR
GRANT SELECT, INSERT, UPDATE, DELETE  ON SCHEMA::dbo TO administrator;
GRANT EXECUTE ON SCHEMA::dbo TO administrator;

-- INSTRUTOR
GRANT INSERT, UPDATE, DELETE ON dbo.lessons TO instructor;
GRANT SELECT ON dbo.exams TO instructor;
GRANT SELECT ON dbo.students TO instructor;

-- ALUNO
GRANT SELECT, INSERT ON dbo.exams TO student;
GRANT SELECT ON dbo.lessons TO student;
GRANT SELECT ON dbo.questions TO student;
GRANT SELECT ON dbo.student_results TO student;

-- AVALIADOR
GRANT INSERT, UPDATE, DELETE, SELECT ON dbo.questions TO reviewer;

-- ANALISTA DE DADOS
GRANT SELECT ON dbo.vw_student_performance TO data_analyst;

PRINT 'Permissões aplicadas com sucesso.';
    