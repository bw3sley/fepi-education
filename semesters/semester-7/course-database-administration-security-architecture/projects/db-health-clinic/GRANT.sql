-- 1) CRIAR LOGIN E USER “restrito”
USE master;
GO

-- 1.a) TENTATIVA COM SENHA FRACA (vai falhar se CHECK_POLICY estiver ON)
IF EXISTS (
w
)
  DROP LOGIN [restrito];
GO

CREATE LOGIN [restrito]
  WITH PASSWORD         = 'teste123',  -- senha fraca para teste
       CHECK_POLICY     = ON,          -- ativa complexidade de senha
       CHECK_EXPIRATION = ON;          -- ativa expiração de senha
GO

-- 1.b) CRIAÇÃO COM SENHA FORTE
IF EXISTS (
  SELECT 1
    FROM sys.server_principals
   WHERE name = N'restrito'
)
  DROP LOGIN [restrito];
GO

CREATE LOGIN [restrito]
  WITH PASSWORD         = 'Str0ngP@ssw0rd!',
       CHECK_POLICY     = ON,
       CHECK_EXPIRATION = ON;
GO

USE clinica_saude;
GO

CREATE USER [restrito]
  FOR LOGIN [restrito]
  WITH DEFAULT_SCHEMA = dbo;
GO

-- 2) DAR APENAS SELECT EM dbo.prontuarios PARA restrito
GRANT SELECT
  ON dbo.prontuarios
  TO restrito;
GO

-- 3) LISTAR PERMISSÕES DO USUARIO restrito
SELECT
  princ.name        AS principal,
  perm.state_desc   AS estado,
  perm.permission_name,
  ISNULL(obj.name, '(DATABASE)') AS objeto
FROM sys.database_permissions AS perm
JOIN sys.database_principals AS princ
  ON perm.grantee_principal_id = princ.principal_id
LEFT JOIN sys.objects AS obj
  ON perm.major_id = obj.object_id
WHERE princ.name = 'restrito';
GO

-- 5) CONCEDER INSERT e DELETE em dbo.pacientes COM GRANT OPTION
GRANT INSERT, DELETE
  ON dbo.pacientes
  TO restrito
  WITH GRANT OPTION;
GO

-- EXECUTE AS USER = 'restrito';
--   SELECT * FROM fn_my_permissions('dbo.pacientes','OBJECT');
-- REVERT;

-- 6) INSERIR E DELETAR EM dbo.pacientes (como restrito)
INSERT INTO dbo.pacientes (nome,endereco,idade,sangue)
VALUES ('João Teste','Rua Exemplo, 123',1980,'A');

DELETE FROM dbo.pacientes
WHERE nome = 'João Teste';
-- OK: INSERT e DELETE permitidos

-- 7) CONCEDER SELECT em dbo.pacientes E RETESTAR DELETE
GRANT SELECT
  ON dbo.pacientes
  TO restrito;
GO

-- 8) TESTAR UPDATE em dbo.medicos (vai falhar), DEPOIS DAR UPDATE
UPDATE dbo.medicos
SET nome = 'Dr. Alterado'
WHERE crm = 1;

GRANT UPDATE
  ON dbo.medicos
  TO restrito;
GO

-- 9) DAR PERMISSÃO TOTAL NO BANCO E CHECAR
EXEC sp_addrolemember  
  'db_owner',  
  'restrito';  
GO

SELECT
  dp.name      AS role_name,
  member_principal_id,
  princ.name   AS member_name
FROM sys.database_role_members AS rm
JOIN sys.database_principals AS dp
  ON rm.role_principal_id = dp.principal_id
JOIN sys.database_principals AS princ
  ON rm.member_principal_id = princ.principal_id
WHERE princ.name = 'restrito';
GO

-- 10) DAR CRIAR VIEW E CRIAR view_pacientes_prontuarios
GRANT CREATE VIEW
  TO restrito;
GO

CREATE VIEW dbo.view_pacientes_prontuarios AS
SELECT
  p.id_paciente,
  p.nome       AS paciente,
  p.idade,
  pr.crm,
  pr.dia,
  pr.tipo
FROM dbo.pacientes AS p
INNER JOIN dbo.prontuarios AS pr
  ON p.id_paciente = pr.id_paciente;
GO

-- 11) REVOKE TUDO (um a um) E CHECAR
REVOKE SELECT
  ON dbo.prontuarios
  FROM restrito;


REVOKE INSERT, DELETE, SELECT, UPDATE
  ON dbo.pacientes
  FROM restrito
  CASCADE;

REVOKE UPDATE
  ON dbo.medicos
  FROM restrito;

REVOKE CREATE VIEW
  TO restrito;

EXEC sp_droprolemember
  'db_owner',
  'restrito';
GO

SELECT
  princ.name,
  perm.state_desc,
  perm.permission_name,
  ISNULL(obj.name,'(DATABASE)') AS objeto
FROM sys.database_permissions AS perm
JOIN sys.database_principals AS princ
  ON perm.grantee_principal_id = princ.principal_id
LEFT JOIN sys.objects AS obj
  ON perm.major_id = obj.object_id
WHERE princ.name = 'restrito';
GO

-- 12) DROPAR O USER E O LOGIN restrito
USE clinica_saude;
GO
DROP USER restrito;
GO

USE master;
GO
DROP LOGIN restrito;
GO