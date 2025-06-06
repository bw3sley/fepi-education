USE exercicio_8;
GO

INSERT INTO fornecedores (cnpj, nome, endereco, tipo)
VALUES
  ('00000000000001', 'Fornecedor Bebidas', 'Rua A', 'Bebidas'),
  ('00000000000002', 'Fornecedor Carne', 'Rua B', 'Carne'),
  ('00000000000003', 'Fornecedor Diversos', 'Rua Halls', 'Diversos');
GO

INSERT INTO entregadores (nome, endereco, tipo)
VALUES
  ('Entregador A', 'Av. A', 'Moto'),
  ('Entregador B', 'Av. B', 'Bicicleta');
GO

INSERT INTO caixas (cpf, nome, endereco, salario)
VALUES
  ('11111111111', 'Caixa A', 'Rua Caixa A', 1500.00),
  ('22222222222', 'Caixa B', 'Rua Caixa B', 2000.00);
GO

INSERT INTO controle_entregas (cpf, cnpj, cod_entregador, destino)
VALUES
  ('11111111111', '00000000000002', 1, 'Destino A'),
  ('22222222222', '00000000000003', 2, 'Destino B');
GO

INSERT INTO clientes (nome, endereco, desde)
VALUES
  ('Cliente 1', 'Rua Cliente 1', '2022-01-10'),
  ('Cliente 2', 'Rua Cliente 2', '2022-05-20');
GO

INSERT INTO produtos (nome, preco, estoque)
VALUES
  ('Cerveja', 8.50, 100),
  ('Chocolate', 5.00, 50),
  ('Carne', 20.00, 30),
  ('Suco', 3.50, 75);
GO

INSERT INTO fornecimentos (cnpj, cod_produto, entrega)
VALUES
  ('00000000000002', 3, '2020-05-15'),
  ('00000000000001', 1, '2019-03-10'),
  ('00000000000001', 2, '2018-11-30'),
  ('00000000000003', 4, '2021-07-20');
GO

INSERT INTO vendidos (cod, cpf, data_venda, nome)
VALUES
  (1, '11111111111', '2023-08-10', 'Cerveja'),
  (3, '22222222222', '2023-08-11', 'Carne');
GO
