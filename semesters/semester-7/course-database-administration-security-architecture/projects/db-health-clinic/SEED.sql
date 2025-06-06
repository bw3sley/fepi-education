INSERT INTO pacientes (nome,endereco,idade,sangue) VALUES
  ('Ana Plástica',        'Rua do Botox',                  1989,'A'),
  ('Emanuel Coxa Bamba',  'Rua da Canela',                 2000,'0'),
  ('Zilda Apneia',        'Rua do Sono',                   1993,'B'),
  ('Francisco Boldo',     'Rua da Balalaika',              1998,'B'),
  ('Silvana Feliciana',   'Avenida Calmaria',              2004,'A'),
  ('Antonio Costa',       'Rua Bico do Papagaio',          1994,'0'),
  ('Senhor Nulo',         'Rua Bico do NULL',              NULL,'0'),
  ('Dona Anula',          'Rua NULL',                      1994, NULL);
GO

INSERT INTO medicos (nome,especialidade,desde) VALUES
  ('Dr. Nárcio MacDonalds','Cardiologista',2003),
  ('Dra. Cristina Tabaco', 'Pneumologista',2005),
  ('Dr. Godofredo Pelanca','Plástica',     2008),
  ('Dra. Adele Gerais',    'Geral',        2006),
  ('Dra. Nu Shibata',      'Geral',        NULL),
  ('Zilda Apneia',         'Cardiologista',2003),
  ('Silvana Feliciana',    'Pneumologista',2005);
GO

INSERT INTO prontuarios (id_paciente, crm, dia)
VALUES
  (1, 4, '2019-02-01'),
  (1, 2, '2018-10-03'),
  (2, 3, '2021-10-03'),
  (3, 4, '2020-08-05'),
  (4, 5, '2019-02-03'),
  (5, 6, '2018-02-15'),
  (6, 7, '2018-11-03'),
  (7, 2, '2020-03-07');
GO