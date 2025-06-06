-- Enfermeiras e suas alas
SELECT
  e.id       AS enfermeira_id,
  e.cre      AS cre,
  e.nome     AS enfermeira,
  a.id       AS ala_id,
  a.especialidade
FROM enfermeiras e
INNER JOIN alas a 
	ON e.id_ala = a.id;
GO

-- Chefes de ala
SELECT
  a.id              AS ala_id,
  a.especialidade,
  e.id               AS chefe_id,
  e.cre             AS chefe_cre,
  e.nome            AS chefe_nome
FROM alas a
INNER JOIN enfermeiras e 
	ON a.id_enfermeira = e.id;
GO

-- 6.3) Médicos e seus atendimentos
SELECT
  m.id             AS medico_id,
  m.crm,
  m.nome           AS medico,
  p.id             AS paciente_id,
  p.nome           AS paciente,
  at.data_hora
FROM atendimentos a
INNER JOIN medicos m   
	ON a.id_medico   = m.id
INNER JOIN pacientes p 
	ON a.id_paciente = p.id
ORDER BY a.data_hora;
GO

-- 6.4) Pacientes e seus planos de saúde
SELECT
  p.id       AS paciente_id,
  p.nome     AS paciente,
  ps.id      AS plano_id,
  ps.nome    AS plano,
  ps.tipo,
  ps.telefone
FROM pacientes p
JOIN planos_saude ps 
	ON p.id_plano = ps.id;
GO

-- Médicos credenciados em cada plano
SELECT
  m.id       AS medico_id,
  m.nome     AS medico,
  ps.id      AS plano_id,
  ps.nome    AS plano,
  ps.tipo
FROM medicos_planos mp
INNER JOIN medicos m       
	ON mp.id_medico = m.id
INNER JOIN planos_saude ps 
	ON mp.id_plano  = ps.id
ORDER BY m.nome, ps.nome;
GO