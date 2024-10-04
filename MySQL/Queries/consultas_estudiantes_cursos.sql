
-- 1. Crear 3 cursos nuevos
INSERT INTO cursos (nombre, created_at, updated_at)
VALUES ('Matemáticas', NOW(), NOW()),
       ('Historia', NOW(), NOW()),
       ('Ciencias', NOW(), NOW());

-- 2. Eliminar los 3 cursos que creaste
DELETE FROM cursos WHERE nombre IN ('Matemáticas', 'Historia', 'Ciencias');

-- 3. Crear otros 3 cursos nuevos
INSERT INTO cursos (nombre, created_at, updated_at)
VALUES ('Literatura', NOW(), NOW()),
       ('Física', NOW(), NOW()),
       ('Química', NOW(), NOW());

-- 4. Crear 3 estudiantes que estén inscritos en el primer curso
INSERT INTO estudiantes (nombre, apellido, edad, curso_id, created_at, updated_at)
VALUES ('Juan', 'Pérez', 20, 1, NOW(), NOW()),
       ('Ana', 'Gómez', 22, 1, NOW(), NOW()),
       ('Luis', 'Martínez', 19, 1, NOW(), NOW());

-- 5. Crear 3 estudiantes que estén inscritos en el segundo curso
INSERT INTO estudiantes (nombre, apellido, edad, curso_id, created_at, updated_at)
VALUES ('María', 'Rodríguez', 21, 2, NOW(), NOW()),
       ('Pedro', 'Fernández', 23, 2, NOW(), NOW()),
       ('Laura', 'López', 20, 2, NOW(), NOW());

-- 6. Crear 3 estudiantes que estén inscritos en el tercer curso
INSERT INTO estudiantes (nombre, apellido, edad, curso_id, created_at, updated_at)
VALUES ('Carlos', 'Sánchez', 24, 3, NOW(), NOW()),
       ('Elena', 'Morales', 22, 3, NOW(), NOW()),
       ('Jorge', 'Díaz', 21, 3, NOW(), NOW());

-- 7. Recuperar todos los estudiantes que estén inscritos en el primer curso
SELECT * FROM estudiantes WHERE curso_id = 1;

-- 8. Recuperar todos los estudiantes que estén inscritos en el último curso
SELECT * FROM estudiantes WHERE curso_id = 3;

-- 9. Recuperar el curso del último estudiante
SELECT c.nombre
FROM estudiantes e
JOIN cursos c ON e.curso_id = c.id
ORDER BY e.id DESC
LIMIT 1;
