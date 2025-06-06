DROP DATABASE clinica_saude;

CREATE DATABASE clinica_saude;

DROP IF EXISTS pacientes, medicos, prontuarios;

CREATE TABLE pacientes (
    id_paciente INT IDENTITY(1,1) NOT NULL,
    nome        NVARCHAR(45),
    endereco    NVARCHAR(60),
    idade       INT,
    sangue      CHAR(1) CHECK (sangue IN ('0','A','B')),
    CONSTRAINT pk_pacientes PRIMARY KEY (id_paciente)
);
GO

CREATE TABLE medicos (
    crm           INT IDENTITY(1,1) NOT NULL,
    nome          NVARCHAR(45),
    especialidade NVARCHAR(20) CHECK (especialidade IN (
                      'Cardiologista',
                      'Pneumologista',
                      'Plástica',
                      'Geral'
                   )),
    desde         INT,
    CONSTRAINT pk_medicos PRIMARY KEY (crm)
);
GO

CREATE TABLE prontuarios (
    id_paciente INT NOT NULL,
    crm         INT NOT NULL,
    dia         DATE,
    tipo        NVARCHAR(10) CHECK (tipo IN ('SUS','Convenio')),
    CONSTRAINT pk_prontuarios PRIMARY KEY (id_paciente, crm),
    CONSTRAINT fk_prontuarios_paciente FOREIGN KEY (id_paciente)
        REFERENCES pacientes(id_paciente),
    CONSTRAINT fk_prontuarios_medico FOREIGN KEY (crm)
        REFERENCES medicos(crm)
);
GO