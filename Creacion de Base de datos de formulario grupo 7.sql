CREATE DATABASE estudiantes_db;
use estudiantes_db;
CREATE TABLE estudiantes_db.respuestas_ia(
ID_RESPUESTA INT PRIMARY KEY AUTO_INCREMENT,
nombre VARCHAR(100) NOT NULL,
correo VARCHAR(100) NOT NULL,
p1 TEXT NOT NULL,
p2  TEXT NOT NULL,
p3 TEXT NOT NULL,
p4 TEXT NOT NULL,
p5 TEXT NOT NULL
);

drop table estudiantes;

select * from estudiantes_db.respuestas_ia;