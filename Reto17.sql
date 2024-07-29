--- 17. Creación de tabla: Escribe una consulta SQL para crear una tabla Usuarios con columnas id y nombre. ---

CREATE TABLE Usuarios(
id_usuarios NOT NULL UNIQUE PRIMARY KEY,
nombre_usuarios VARCHAR(50) NOT NULL, 
);
