CREATE PROCEDURE _sp_register_student
@name VARCHAR(100),
@email VARCHAR(100),
@password VARBINARY(256),
@birth_date DATE
AS
BEGIN
    BEGIN TRY
        INSERT INTO students (name, email, password, birth_date)
        VALUES (@name, @email, @password, @birth_date);
    END TRY

    BEGIN CATCH
       PRINT 'Error inserting user';
    END CATCH
END;
GO

CREATE PROCEDURE _sp_register_exam
@studentID INT,
@score FLOAT
AS
BEGIN
    BEGIN TRY
        INSERT INTO exams (student_id, realization_date, score)
        VALUES (@studentID, GETDATE(), @score);
    END TRY

    BEGIN CATCH
        PRINT 'Error inserting exam';
    END CATCH
END;
GO

CREATE PROCEDURE _sp_update_question
@questionId INT,
@newStatement VARCHAR(255)
AS
BEGIN
    BEGIN TRY
        UPDATE questions
        SET statement = @newStatement
        WHERE id = @questionId;
    END TRY

    BEGIN CATCH
        PRINT 'Error updating question';
    END CATCH
END;
GO

CREATE PROCEDURE _sp_filter_students
@name NVARCHAR(100) = NULL,
@email NVARCHAR(100) = NULL,
@birth_date DATE = NULL
AS
BEGIN
    BEGIN TRY
        DECLARE @sql NVARCHAR(MAX);
        SET @sql = 'SELECT * FROM students WHERE 1=1';
        
        IF @name IS NOT NULL
            SET @sql = @sql + ' AND name LIKE ''%' + @name + '%''';
        
        IF @email IS NOT NULL
            SET @sql = @sql + ' AND email = ''' + @email + '''';
        
        IF @birth_date IS NOT NULL
            SET @sql = @sql + ' AND birth_date = ''' + CONVERT(NVARCHAR, @birth_date, 23) + '''';
        
        EXEC sp_executesql @sql;
    END TRY

    BEGIN CATCH
        PRINT 'Error executing dynamic student filter query';
    END CATCH
END;
GO

CREATE PROCEDURE _sp_bulk_insert_students
@file_path NVARCHAR(255)
AS
BEGIN
    BEGIN TRY
        DECLARE @sql NVARCHAR(MAX);

        SET @sql = N'
            BULK INSERT students
            FROM ''' + @file_path + N'''
            WITH (
                FORMAT = ''CSV'',
                FIRSTROW = 2,
                FIELDTERMINATOR = '','',
                ROWTERMINATOR = ''\n'',
                CODEPAGE = ''65001'', -- UTF-8
                TABLOCK
            );';

        EXEC sp_executesql @sql;
    END TRY
    BEGIN CATCH
        PRINT 'Error performing bulk insert';
    END CATCH
END;
GO