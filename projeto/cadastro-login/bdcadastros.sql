CREATE DATABASE HELPOCEAN;
USE HELPOCEAN;

CREATE TABLE Cadastro (
    id 				INT auto_increment 		PRIMARY KEY,
    nome 			VARCHAR(20),
    email 			VARCHAR(20),
    senha			VARCHAR(10),
    telefone 		VARCHAR(15)
);