INSERT INTO hospitais (nome, cpnj) VALUES
  ('Hospital Central', '12.345.678/0001-90');
GO

INSERT INTO alas (especialidade, id_hospital) VALUES
  ('Cardiologia', 1),
  ('Pediatria',   1);
GO

INSERT INTO enfermeiras (cre, nome, id_ala) VALUES
  ('CRE101', 'Ana Souza',    1),
  ('CRE102', 'Beatriz Lima', 2);
GO

UPDATE alas
  SET id_enfermeira = 1
  WHERE id = 1;

UPDATE alas
  SET id_enfermeira = 2
  WHERE id = 2;
GO

INSERT INTO planos_saude (nome, tipo, telefone) VALUES
  ('Unimed',        'convenio_empresa', '0800-123-456'),
  ('ParticularTop','particular',       '0800-987-654');
GO

INSERT INTO pacientes (nome, id_plano) VALUES
  ('Carlos Pereira', 1),
  ('Fernanda Rocha', 2);
GO

INSERT INTO medicos (crm, nome, especialidade) VALUES
  (201, 'Dr. João Silva',   'Cardiologista'),
  (202, 'Dra. Maria Costa', 'Pediatra');
GO

INSERT INTO atendimentos (id_medico, id_paciente, data_hora) VALUES
  (1, 1, '2025-05-20 09:00:00'),
  (2, 2, '2025-05-21 10:30:00'),
  (1, 2, '2025-05-22 14:15:00');
GO

INSERT INTO medicos_planos (id_plano, id_medico) VALUES
  (1, 1),
  (2, 1),
  (1, 2);
GO