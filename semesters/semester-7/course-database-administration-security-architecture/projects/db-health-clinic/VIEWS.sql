-- 4) pacientes com idade OU sangue nulos

CREATE VIEW view_pacientes_nulos AS
SELECT id_paciente, nome, idade, sangue
FROM pacientes
WHERE idade IS NULL
   OR sangue IS NULL;
GO

-- 5) INNER JOIN pacientes + prontuarios

CREATE VIEW view_pacientes_prontuarios_inner AS
SELECT
  p.id_paciente,
  p.nome,
  p.endereco,
  p.idade,
  p.sangue,
  pr.crm,
  pr.dia,
  pr.tipo
FROM pacientes AS p
INNER JOIN prontuarios AS pr
  ON p.id_paciente = pr.id_paciente;
GO

-- 6) LEFT JOIN pacientes + prontuarios

CREATE VIEW view_pacientes_prontuarios_left AS
SELECT
  p.id_paciente,
  p.nome,
  p.endereco,
  p.idade,
  p.sangue,
  pr.crm,
  pr.dia,
  pr.tipo
FROM pacientes AS p
LEFT JOIN prontuarios AS pr
  ON p.id_paciente = pr.id_paciente;
GO

-- 7) RIGHT JOIN pacientes + prontuarios

CREATE VIEW view_pacientes_prontuarios_right AS
SELECT
  p.id_paciente,
  p.nome,
  p.endereco,
  p.idade,
  p.sangue,
  pr.crm,
  pr.dia,
  pr.tipo
FROM pacientes AS p
RIGHT JOIN prontuarios AS pr
  ON p.id_paciente = pr.id_paciente;
GO

-- 8) LEFT JOIN pacientes + medicos
-- (exemplo didático cruzando id_paciente=com crm)

CREATE VIEW view_pacientes_medicos_left AS
SELECT
  p.id_paciente,
  p.nome         AS paciente_nome,
  p.endereco,
  p.idade,
  p.sangue,
  m.crm,
  m.nome         AS medico_nome,
  m.especialidade,
  m.desde
FROM pacientes AS p
LEFT JOIN medicos AS m
  ON p.id_paciente = m.crm;
GO

-- 9) RIGHT JOIN pacientes + medicos

CREATE VIEW view_pacientes_medicos_right AS
SELECT
  p.id_paciente,
  p.nome         AS paciente_nome,
  p.endereco,
  p.idade,
  p.sangue,
  m.crm,
  m.nome         AS medico_nome,
  m.especialidade,
  m.desde
FROM pacientes AS p
RIGHT JOIN medicos AS m
  ON p.id_paciente = m.crm;
GO