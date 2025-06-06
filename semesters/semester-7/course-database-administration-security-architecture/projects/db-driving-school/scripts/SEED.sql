-- Inserindo dados iniciais para a tabela students
INSERT INTO students (name, email, password, birth_date) VALUES
('Alice Johnson', 'alice.johnson@email.com', HASHBYTES('SHA2_256', 'password123'), '2000-05-15'),
('Bob Smith', 'bob.smith@email.com', HASHBYTES('SHA2_256', 'password123'), '1999-09-22'),
('Charlie Brown', 'charlie.brown@email.com', HASHBYTES('SHA2_256', 'password123'), '2001-03-10');

-- Inserindo dados iniciais para a tabela instructors
INSERT INTO instructors (name, email, password) VALUES
('David Adams', 'david.adams@email.com', HASHBYTES('SHA2_256', 'password123')),
('Eve Taylor', 'eve.taylor@email.com', HASHBYTES('SHA2_256', 'password123'));

-- Inserindo dados iniciais para a tabela administrators
INSERT INTO administrators (name, email, password) VALUES
('Admin User', 'admin@email.com', HASHBYTES('SHA2_256', 'adminpass'));

-- Inserindo dados iniciais para a tabela reviewers
INSERT INTO reviewers (name, email, password) VALUES
('Review Expert', 'reviewer@email.com', HASHBYTES('SHA2_256', 'reviewpass'));

-- Inserindo dados iniciais para a tabela data_analysts
INSERT INTO data_analysts (name, email, password) VALUES
('Data Analyst', 'analyst@email.com', HASHBYTES('SHA2_256', 'datapass'));

-- Inserindo dados iniciais para a tabela lessons
INSERT INTO lessons (instructor_id, title, content) VALUES
(1, 'Basic Traffic Rules', 'Introduction to traffic rules and regulations'),
(2, 'Advanced Driving Techniques', 'Tips and techniques for advanced driving maneuvers');

-- Inserindo dados iniciais para a tabela exams
INSERT INTO exams (student_id, realization_date, score) VALUES
(1, '2024-03-01', 85.5),
(2, '2024-03-02', 70.0),
(3, '2024-03-03', 90.0);

-- Inserindo dados iniciais para a tabela questions
INSERT INTO questions (statement) VALUES
('What is the maximum speed limit in a residential area?'),
('When should you use a turn signal?');

-- Inserindo dados iniciais para a tabela answers
INSERT INTO answers (question_id, alternative, correct) VALUES
(1, '30 km/h', 1),
(1, '50 km/h', 0),
(2, 'Before making a turn', 1),
(2, 'Only if there are other vehicles around', 0);

-- Inserindo dados iniciais para a tabela exams_history
INSERT INTO exams_history (student_id, exam_id, score, realization_date) VALUES
(1, 1, 85.5, '2024-03-01'),
(2, 2, 70.0, '2024-03-02'),
(3, 3, 90.0, '2024-03-03');

-- Inserindo dados iniciais para a tabela students_lessons
INSERT INTO students_lessons (student_id, lesson_id, visualization_date) VALUES
(1, 1, '2024-03-04'),
(2, 2, '2024-03-05');
