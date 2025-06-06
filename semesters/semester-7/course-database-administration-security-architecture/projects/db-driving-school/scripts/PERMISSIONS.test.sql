USE db_driving_school;
GO

--  TESTES PARA ADMINISTRATOR (admin_user)
PRINT '--- Testando role: administrator (admin_user) ---';
EXECUTE AS USER = 'admin_user';

-- Deve conseguir INSERT em exams
BEGIN TRY
    INSERT INTO exams (student_id, score) VALUES (1, 88.0);
    PRINT 'OK: administrator pode INSERT em exams';
END TRY
BEGIN CATCH
    PRINT 'ERRO: administrator não conseguiu INSERT em exams: ' + ERROR_MESSAGE();
END CATCH;

-- Deve conseguir SELECT em questions
BEGIN TRY
    SELECT TOP 1 * FROM questions;
    PRINT 'OK: administrator pode SELECT em questions';
END TRY
BEGIN CATCH
    PRINT 'ERRO: administrator não conseguiu SELECT em questions: ' + ERROR_MESSAGE();
END CATCH;

-- Deve falhar SELECT em students (não concedido)
BEGIN TRY
    SELECT TOP 1 * FROM students;
    PRINT 'ERRO: administrator inesperadamente conseguiu SELECT em students';
END TRY
BEGIN CATCH
    PRINT 'OK: administrator não tem SELECT em students (esperado): ' + ERROR_MESSAGE();
END CATCH;

REVERT;
GO

--------------------------------------------------------------------------------
--  TESTES PARA INSTRUCTOR (instructor_user)
--------------------------------------------------------------------------------
PRINT '--- Testando role: instructor (instructor_user) ---';
EXECUTE AS USER = 'instructor_user';

-- Deve conseguir INSERT em lessons
BEGIN TRY
    INSERT INTO lessons (instructor_id, title, content)
    VALUES (1, 'Teste de Lesson', 'Conteúdo de teste');
    PRINT 'OK: instructor pode INSERT em lessons';
END TRY
BEGIN CATCH
    PRINT 'ERRO: instructor não conseguiu INSERT em lessons: ' + ERROR_MESSAGE();
END CATCH;

-- Deve conseguir SELECT em exams
BEGIN TRY
    SELECT TOP 1 * FROM exams;
    PRINT 'OK: instructor pode SELECT em exams';
END TRY
BEGIN CATCH
    PRINT 'ERRO: instructor não conseguiu SELECT em exams: ' + ERROR_MESSAGE();
END CATCH;

-- Deve falhar DELETE em exams
BEGIN TRY
    DELETE FROM exams WHERE id = -1;
    PRINT 'ERRO: instructor inesperadamente conseguiu DELETE em exams';
END TRY
BEGIN CATCH
    PRINT 'OK: instructor não tem DELETE em exams (esperado): ' + ERROR_MESSAGE();
END CATCH;

REVERT;
GO

--------------------------------------------------------------------------------
--  TESTES PARA STUDENT (student_user)
--------------------------------------------------------------------------------
PRINT '--- Testando role: student (student_user) ---';
EXECUTE AS USER = 'student_user';

-- Deve conseguir INSERT em exams
BEGIN TRY
    INSERT INTO exams (student_id, score) VALUES (1, 92.0);
    PRINT 'OK: student pode INSERT em exams';
END TRY
BEGIN CATCH
    PRINT 'ERRO: student não conseguiu INSERT em exams: ' + ERROR_MESSAGE();
END CATCH;

-- Deve conseguir SELECT em lessons
BEGIN TRY
    SELECT TOP 1 * FROM lessons;
    PRINT 'OK: student pode SELECT em lessons';
END TRY
BEGIN CATCH
    PRINT 'ERRO: student não conseguiu SELECT em lessons: ' + ERROR_MESSAGE();
END CATCH;

-- Deve falhar UPDATE em questions
BEGIN TRY
    UPDATE questions SET statement = 'Teste' WHERE id = -1;
    PRINT 'ERRO: student inesperadamente conseguiu UPDATE em questions';
END TRY
BEGIN CATCH
    PRINT 'OK: student não tem UPDATE em questions (esperado): ' + ERROR_MESSAGE();
END CATCH;

REVERT;
GO

--------------------------------------------------------------------------------
--  TESTES PARA REVIEWER (reviewer_user)
--------------------------------------------------------------------------------
PRINT '--- Testando role: reviewer (reviewer_user) ---';
EXECUTE AS USER = 'reviewer_user';

-- Deve conseguir INSERT em questions
BEGIN TRY
    INSERT INTO questions (statement) VALUES ('Pergunta do revisor');
    PRINT 'OK: reviewer pode INSERT em questions';
END TRY
BEGIN CATCH
    PRINT 'ERRO: reviewer não conseguiu INSERT em questions: ' + ERROR_MESSAGE();
END CATCH;

-- Deve conseguir UPDATE em questions
BEGIN TRY
    UPDATE questions SET statement = 'Alteração do revisor' WHERE id = 1;
    PRINT 'OK: reviewer pode UPDATE em questions';
END TRY
BEGIN CATCH
    PRINT 'ERRO: reviewer não conseguiu UPDATE em questions: ' + ERROR_MESSAGE();
END CATCH;

-- Deve falhar SELECT em students
BEGIN TRY
    SELECT * FROM students;
    PRINT 'ERRO: reviewer inesperadamente conseguiu SELECT em students';
END TRY
BEGIN CATCH
    PRINT 'OK: reviewer não tem SELECT em students (esperado): ' + ERROR_MESSAGE();
END CATCH;

REVERT;
GO

--------------------------------------------------------------------------------
--  TESTES PARA DATA_ANALYST (data_analyst_user)
--------------------------------------------------------------------------------
PRINT '--- Testando role: data_analyst (data_analyst_user) ---';
EXECUTE AS USER = 'data_analyst_user';

-- Deve conseguir SELECT em vw_student_performance
BEGIN TRY
    SELECT TOP 1 * FROM vw_student_performance;
    PRINT 'OK: data_analyst pode SELECT em vw_student_performance';
END TRY
BEGIN CATCH
    PRINT 'ERRO: data_analyst não conseguiu SELECT em vw_student_performance: ' + ERROR_MESSAGE();
END CATCH;

-- Deve falhar INSERT em exams
BEGIN TRY
    INSERT INTO exams (student_id, score) VALUES (1, 50.0);
    PRINT 'ERRO: data_analyst inesperadamente conseguiu INSERT em exams';
END TRY
BEGIN CATCH
    PRINT 'OK: data_analyst não tem INSERT em exams (esperado): ' + ERROR_MESSAGE();
END CATCH;

REVERT;
GO

PRINT '--- FIM DOS TESTES DE ROLE ---';
