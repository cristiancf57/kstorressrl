CREATE DATABASE if NOT EXISTS kstorres_db;
USE kstorres_db;

CREATE TABLE if NOT EXISTS profesiones(
	id VARCHAR(5) PRIMARY KEY NOT NULL,
	profesion VARCHAR(60) NOT NULL,
	abreviado VARCHAR(5)
);

CREATE TABLE if NOT EXISTS roles(
	id VARCHAR(5) PRIMARY KEY NOT NULL,
	cargo VARCHAR(50)
);

CREATE TABLE if NOT EXISTS usuarios(
	id INT(10) PRIMARY KEY AUTO_INCREMENT,
	nombre VARCHAR(50) NOT NULL,
	apellido VARCHAR(50) NOT NULL,
	foto TEXT,
	telefono INT(9),
	salario FLOAT(15.2),
	obs TEXT,
	id_profesion VARCHAR(5),
	id_rol VARCHAR(5),
	FOREIGN KEY (id_profesion) REFERENCES profesiones (id),
	FOREIGN KEY (id_rol) REFERENCES roles (id)
);

CREATE TABLE if NOT EXISTS users(
	id INT PRIMARY KEY AUTO_INCREMENT,
	username VARCHAR(30),
	passwd TEXT,
	id_usuario INT(10),
	FOREIGN KEY (id_usuario) REFERENCES usuarios (id)
);

CREATE TABLE if NOT EXISTS proyectos(
	id INT PRIMARY KEY AUTO_INCREMENT,
	proyecto TEXT NOT NULL,
	caracteristica TEXT,
	superficie INT(15),
	ubicacion VARCHAR(80),
	fecha_inicio DATE,
	fecha_fin DATE,
	estado VARCHAR(20),
	presupuesto INT(15),
	id_usuario INT(10),
	FOREIGN KEY (id_usuario) REFERENCES usuarios (id)
);

CREATE TABLE if NOT EXISTS fotos(
	id INT PRIMARY KEY AUTO_INCREMENT,
	detalle TEXT,
	id_proyecto INT,
	FOREIGN KEY (id_proyecto) REFERENCES proyectos (id)
);

CREATE TABLE if NOT EXISTS inventarios(
	id INT PRIMARY KEY AUTO_INCREMENT,
	material TEXT,
	cantidad INT(10),
	unidad VARCHAR(20),
	costo_unit FLOAT(10,2),
	total REAL(15,2),
	id_proyecto INT,
	FOREIGN KEY (id_proyecto) REFERENCES proyectos (id)
);

CREATE TABLE if NOT EXISTS gastos(
	id INT PRIMARY KEY AUTO_INCREMENT,
	monto REAL(15,2),
	concepto TEXT,
	nro_factura INT,
	fecha DATE,
	id_proyecto INT,
	FOREIGN KEY (id_proyecto) REFERENCES proyectos (id)
);


INSERT INTO profesiones (id,profesion,abreviado) 
VALUES
('ADME','Administrador de Empresas','Lic'),
('INGC','Ingeniero Civil','Ing'),
('ARQU','Arquitecto','Arq'),
('CONT','Contador','Lic'),
('ECON','Economista','Lic'),
('INGF','Ingeniero Financiero','Ing'),
('INGS','Ingeniero de Sistemas','Ing'),
('INFO','Informatica','Lic'),
('TECN','Tecnico','Tec');

INSERT INTO roles(id,cargo)
VALUES
('ROOT','Super administrador'),
('ADM','Administrador'),
('SUP','Supervisor'),
('PER','Personal'),
('USR','Usuario');