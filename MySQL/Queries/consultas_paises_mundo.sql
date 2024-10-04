
-- 1. Obtener todos los países que hablan español, ordenados por porcentaje de habla en orden descendente
SELECT p.nombre AS pais, l.idioma, l.porcentaje
FROM paises p
JOIN idiomas l ON p.id = l.pais_id
WHERE l.idioma = 'Español'
ORDER BY l.porcentaje DESC;

-- 2. Mostrar el número total de ciudades de cada país, ordenados por el número de ciudades en orden descendente
SELECT p.nombre AS pais, COUNT(c.id) AS total_ciudades
FROM paises p
JOIN ciudades c ON p.id = c.pais_id
GROUP BY p.id
ORDER BY total_ciudades DESC;

-- 3. Obtener todas las ciudades de Chile con una población mayor a 200,000, ordenadas por población en orden descendente
SELECT c.nombre AS ciudad, c.poblacion
FROM ciudades c
JOIN paises p ON c.pais_id = p.id
WHERE p.nombre = 'Chile' AND c.poblacion > 200000
ORDER BY c.poblacion DESC;

-- 4. Obtener todos los idiomas en cada país con un porcentaje de habla mayor a 89%, ordenados por porcentaje de habla en orden descendente
SELECT p.nombre AS pais, l.idioma, l.porcentaje
FROM paises p
JOIN idiomas l ON p.id = l.pais_id
WHERE l.porcentaje > 89
ORDER BY l.porcentaje DESC;

-- 5. Obtener todos los países con un área de superficie menor a 501 y una población mayor a 100,000
SELECT nombre, area_superficie, poblacion
FROM paises
WHERE area_superficie < 501 AND poblacion > 100000;

-- 6. Obtener países donde el tipo de gobierno es "República", capital mayor a 2000 y esperanza de vida mayor a 78 años
SELECT nombre, tipo_gobierno, capital, esperanza_vida
FROM paises
WHERE tipo_gobierno = 'República' AND capital > 2000 AND esperanza_vida > 78;

-- 7. Obtener todas las ciudades de Colombia dentro del distrito de Valle con una población mayor a 200,000 habitantes
SELECT p.nombre AS pais, c.nombre AS ciudad, c.distrito, c.poblacion
FROM ciudades c
JOIN paises p ON c.pais_id = p.id
WHERE p.nombre = 'Colombia' AND c.distrito = 'Valle' AND c.poblacion > 200000;

-- 8. Resumir el número de países en cada región, ordenados por el número de países en orden descendente
SELECT region, COUNT(id) AS total_paises
FROM paises
GROUP BY region
ORDER BY total_paises DESC;
