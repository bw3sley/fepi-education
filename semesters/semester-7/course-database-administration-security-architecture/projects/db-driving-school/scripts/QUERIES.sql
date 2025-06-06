SELECT * FROM students;

SELECT * FROM exams WHERE score >= 70;

SELECT 
    instructors.name, 
    COUNT(lessons.id) AS total_lessons 
    
FROM instructors 
    JOIN lessons 
        ON instructors.id = lessons.instructor_id 
        
GROUP BY instructors.name;

SELECT 
    students.name, 
    AVG(exams_history.score) AS average_score 
    
FROM students 
    JOIN exams_history 
        ON students.id = exams_history.student_id 
    
GROUP BY students.name;

SELECT 
    lessons.title, 
    COUNT(students_lessons.id) AS total_views 

FROM lessons 
    JOIN students_lessons 
        ON lessons.id = students_lessons.lesson_id 
        
GROUP BY 
    lessons.title 

ORDER BY total_views DESC;