-- Crear la base de datos
CREATE DATABASE esquema_estudiantes_cursos;
USE esquema_estudiantes_cursos;

-- Crear la tabla cursos
CREATE TABLE cursos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Crear la tabla estudiantes
CREATE TABLE estudiantes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    edad INT NOT NULL,
    curso_id INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    -- Definir la clave foránea hacia la tabla cursos
    FOREIGN KEY (curso_id) REFERENCES cursos(id)
);

-- Cambiar el nombre de la clave foránea a 'curso_id'
ALTER TABLE estudiantes
DROP FOREIGN KEY estudiantes_ibfk_1;  -- Este nombre depende de cómo lo genere automáticamente MySQL Workbench

-- Añadir nuevamente la clave foránea con el nombre 'curso_id'
ALTER TABLE estudiantes
ADD CONSTRAINT fk_curso FOREIGN KEY (curso_id) REFERENCES cursos(id);
