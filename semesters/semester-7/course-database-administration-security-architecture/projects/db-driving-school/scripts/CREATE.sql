DROP DATABASE IF EXISTS db_driving_school;
GO

CREATE DATABASE db_driving_school;
GO

USE db_driving_school;
GO

CREATE TABLE students (
    id INT IDENTITY PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARBINARY(256) NOT NULL,
    birth_date DATE NOT NULL
);

CREATE TABLE instructors (
    id INT IDENTITY PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARBINARY(256) NOT NULL
);

CREATE TABLE administrators (
    id INT IDENTITY PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARBINARY(256) NOT NULL
);

CREATE TABLE reviewers (
    id INT IDENTITY PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARBINARY(256) NOT NULL
);

CREATE TABLE data_analysts (
    id INT IDENTITY PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARBINARY(256) NOT NULL
);

CREATE TABLE exams (
    id INT IDENTITY PRIMARY KEY,
    student_id INT NOT NULL,
    realization_date DATETIME DEFAULT GETDATE(),
    score FLOAT,
    FOREIGN KEY (student_id) REFERENCES students(id) ON DELETE CASCADE
);

CREATE TABLE questions (
    id INT IDENTITY PRIMARY KEY,
    statement VARCHAR(255) NOT NULL
);

CREATE TABLE answers (
    id INT IDENTITY PRIMARY KEY,
    question_id INT NOT NULL,
    alternative VARCHAR(255) NOT NULL,
    correct BIT NOT NULL,
    FOREIGN KEY (question_id) REFERENCES questions(id) ON DELETE CASCADE
);

CREATE TABLE lessons (
    id INT IDENTITY PRIMARY KEY,
    instructor_id INT NOT NULL,
    title VARCHAR(255) NOT NULL,
    content TEXT NOT NULL,
    FOREIGN KEY (instructor_id) REFERENCES instructors(id) ON DELETE CASCADE
);

CREATE TABLE exams_history (
    id INT IDENTITY PRIMARY KEY,
    student_id INT NOT NULL,
    exam_id INT NOT NULL,
    score FLOAT NOT NULL,
    realization_date DATETIME DEFAULT GETDATE(),
    FOREIGN KEY (student_id) REFERENCES students(id) ON DELETE CASCADE,
    FOREIGN KEY (exam_id) REFERENCES exams(id) ON DELETE NO ACTION -- Evita ciclo
);

CREATE TABLE students_lessons (
    id INT IDENTITY PRIMARY KEY,
    student_id INT NOT NULL,
    lesson_id INT NOT NULL,
    visualization_date DATETIME DEFAULT GETDATE(),
    FOREIGN KEY (student_id) REFERENCES students(id) ON DELETE CASCADE,
    FOREIGN KEY (lesson_id) REFERENCES lessons(id) ON DELETE CASCADE
);
