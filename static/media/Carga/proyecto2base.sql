-- create database proyecto2 DEFAULT CHARACTER SET utf8 ;

DROP DATABASE proyecto2_general;
CREATE DATABASE proyecto2_general DEFAULT CHARACTER SET utf8;

-- use proyecto2;
-- use proyecto2_general;

set  FOREIGN_KEY_CHECKS=0;

CREATE TABLE IF NOT EXISTS Permiso (
Permiso INT NOT NULL,
Descripcion VARCHAR(250) NOT NULL,
PRIMARY KEY (Permiso))
;

CREATE TABLE IF NOT EXISTS Permiso_Usuario (
  Permiso INT NOT NULL,
  Usuario INT NOT NULL,
  PRIMARY KEY (Permiso, Usuario),
  FOREIGN KEY (Permiso) REFERENCES Permiso (Permiso) ON DELETE cascade ON UPDATE cascade,
  FOREIGN KEY (Usuario) REFERENCES proyecto_usuario(id)ON DELETE cascade ON UPDATE cascade)
;

CREATE TABLE IF NOT EXISTS Modulo (
   Modulo INT NOT NULL,
  Nombre VARCHAR(45) NOT NULL,
  PRIMARY KEY (Modulo))
;

CREATE TABLE IF NOT EXISTS Proceso (
  Proceso INT NOT NULL,
  Modulo INT NOT NULL,
  PRIMARY KEY (Proceso),
  FOREIGN KEY (Modulo)REFERENCES Modulo (Modulo) ON DELETE cascade ON UPDATE cascade
  );


CREATE TABLE IF NOT EXISTS Tipo (
  Tipo INT NOT NULL,
  Descripcion VARCHAR(45) NOT NULL,
  PRIMARY KEY (Tipo));

CREATE TABLE IF NOT EXISTS Etapa (
  Etapa INT NOT NULL,
  Nombre VARCHAR(45) NOT NULL,
  Proceso INT NOT NULL,
  Tipo INT NOT NULL,
  PRIMARY KEY (Etapa),
    FOREIGN KEY (Proceso )REFERENCES Proceso (Proceso)ON DELETE cascade ON UPDATE cascade,
    FOREIGN KEY (Tipo)REFERENCES Tipo (Tipo)ON DELETE cascade ON UPDATE cascade)
;

CREATE TABLE IF NOT EXISTS Condicion (
  Condicion INT NOT NULL,
  Descripcion VARCHAR(45) NOT NULL,
  PRIMARY KEY (Condicion))
;


CREATE TABLE IF NOT EXISTS Enlace (
  Etapa_Actual INT NOT NULL,
  Etapa_Destino INT NOT NULL,
  Condicion INT NOT NULL,
  PRIMARY KEY (Etapa_Actual, Etapa_Destino, Condicion),
    FOREIGN KEY (Etapa_Actual)REFERENCES Etapa (Etapa)ON DELETE cascade ON UPDATE cascade,
    FOREIGN KEY (Etapa_Destino)REFERENCES Etapa (Etapa)ON DELETE cascade ON UPDATE cascade,
    FOREIGN KEY (Condicion)REFERENCES Condicion (Condicion)ON DELETE cascade ON UPDATE cascade)
;

CREATE TABLE IF NOT EXISTS Estado (
  Estado INT NOT NULL,
  Descripcion VARCHAR(45) NOT NULL,
  PRIMARY KEY (Estado))
;

CREATE TABLE IF NOT EXISTS Gestion (
  Gestion INT NOT NULL,
  Proceso INT NOT NULL,
  PRIMARY KEY (Gestion),
  FOREIGN KEY (Proceso) REFERENCES Proceso(Proceso)ON DELETE cascade ON UPDATE cascade
  );


CREATE TABLE IF NOT EXISTS Info (
  Info INT NOT NULL,
  Descripcion VARCHAR(250) NOT NULL,
  Estado INT NOT NULL,
  Gestion INT NOT NULL,
  PRIMARY KEY (Info),
    FOREIGN KEY (Estado)REFERENCES Estado (Estado)ON DELETE cascade ON UPDATE cascade,
    FOREIGN KEY (Gestion)REFERENCES Gestion (Gestion)ON DELETE cascade ON UPDATE cascade)
;

CREATE TABLE IF NOT EXISTS Notificacion (
  Usuario INT NOT NULL,
  Etapa INT NOT NULL,
  Info INT NOT NULL,
  Gestion INT NOT NULL,
  Condicion INT NOT NULL,
  Contestado boolean NULL,
  PRIMARY KEY (Usuario,Etapa,Info,Gestion,Condicion),
    FOREIGN KEY (Usuario)REFERENCES proyecto_usuario(id)ON DELETE cascade ON UPDATE cascade,
    FOREIGN KEY (Etapa)REFERENCES Etapa(Etapa)ON DELETE cascade ON UPDATE cascade,
    FOREIGN KEY (Info)REFERENCES Info (Info)ON DELETE cascade ON UPDATE cascade,
    FOREIGN KEY (Gestion)REFERENCES Gestion (Gestion)ON DELETE cascade ON UPDATE cascade,
    FOREIGN KEY (Condicion)REFERENCES Condicion (Condicion)ON DELETE cascade ON UPDATE cascade)
;

insert into permiso values(1,"Generar Reportes");
insert into permiso values(2,"Crear Procesor");
insert into permiso values(3,"Atender Gestion");
insert into permiso values(4,"Logueo");
insert into permiso values(5,"Inicio Gestion");
insert into permiso values(6,"Eliminar Gestion");
insert into permiso values(7,"Modificar Proceso");
insert into permiso values(8,"Eliminar Proceso");