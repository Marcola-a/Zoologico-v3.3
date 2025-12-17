drop database if exists zoologico;
create database zoologico;

use zoologico;

drop table if exists animal;
drop table if exists usuario;

create table usuario (
	usuario_id integer primary key auto_increment not null,
    
    nome varchar(30) not null,
	senha varchar(20) not null,
    
	email varchar(35),
    constraint email check (email like "%@%.%"),
    
	admin boolean not null
);

create table animal(
	id_animal integer primary key not null auto_increment,
    
	apelido varchar(20),
	especie varchar(35) not null,
	nome_cientifico varchar(35) not null,
	peso float not null,
	data_nascimento date not null,
	data_chegada date not null,
	dieta varchar(35) not null,
	rotina_limpeza varchar(50) not null,
	recinto varchar(35) not null,
	
	ativo boolean not null
);


INSERT INTO animal (apelido, especie, nome_cientifico, peso, data_nascimento, data_chegada, dieta, rotina_limpeza, recinto, ativo) 
VALUES
	("Luna", "Leão Africano", "Panthera leo", 184.5, "2018-04-12", "2020-06-18", "Carnívoro", "Limpeza diária", "Sabana A1", true),
	("Tico", "Tigre de Bengala", "Panthera tigris tigris", 220.3, "2017-02-05", "2019-09-21", "Carnívoro", "Limpeza diária", "Floresta T2", true),
	("Babu", "Chimpanzé", "Pan troglodytes", 54.2, "2015-10-10", "2018-03-12", "Onívoro", "Limpeza a cada 2 dias", "Selva P3", true),
	("Nina", "Girafa", "Giraffa camelopardalis", 780.0, "2016-11-07", "2017-12-01", "Herbívoro", "Limpeza semanal", "Planície G4", true),
	("Spike", "Hiena", "Crocuta crocuta", 65.4, "2019-03-15", "2021-02-20", "Carnívoro", "Limpeza a cada 2 dias", "Sabana H5", true),
	("Zuzu", "Zebra", "Equus quagga", 310.7, "2018-08-02", "2019-05-30", "Herbívoro", "Limpeza semanal", "Planície Z6", true),
	("Kiko", "Crocodilo-do-Nilo", "Crocodylus niloticus", 430.1, "2010-01-14", "2012-07-22", "Carnívoro", "Limpeza mensal", "Lago C7", true),
	("Pudim", "Panda-vermelho", "Ailurus fulgens", 6.4, "2020-03-19", "2021-01-08", "Herbívoro", "Limpeza semanal", "Bambu P8", true),
	("Rocky", "Urso-pardo", "Ursus arctos", 350.0, "2014-09-25", "2016-08-07", "Onívoro", "Limpeza semanal", "Montanha U9", true),
	("Milo", "Lobo-cinzento", "Canis lupus", 45.8, "2018-12-11", "2020-04-13", "Carnívoro", "Limpeza a cada 2 dias", "Floresta L10", true),
	("Tarta", "Tartaruga-gigante", "Chelonoidis nigra", 240.5, "1980-06-03", "1999-10-18", "Herbívoro", "Limpeza mensal", "Ilhas T11", true),
	("Dori", "Arara-azul", "Anodorhynchus hyacinthinus", 1.2, "2021-05-07", "2022-02-12", "Herbívoro", "Limpeza semanal", "Aviário A12", true),
	("Flash", "Guepardo", "Acinonyx jubatus", 72.0, "2019-07-21", "2020-10-02", "Carnívoro", "Limpeza diária", "Sabana G13", true),
	("Pingo", "Pinguim-de-Magalhães", "Spheniscus magellanicus", 4.6, "2020-11-01", "2021-06-22", "Carnívoro", "Limpeza diária", "Gelo P14", true),
	("Toto", "Capivara", "Hydrochoerus hydrochaeris", 54.9, "2017-04-30", "2018-09-14", "Herbívoro", "Limpeza semanal", "Lago C15", true),
	("Lola", "Lêmure-de-cauda-anelada", "Lemur catta", 3.2, "2019-01-23", "2020-03-10", "Herbívoro", "Limpeza a cada 2 dias", "Selva L16", true),
	("Bolt", "Antílope", "Antilope cervicapra", 41.3, "2018-02-18", "2019-07-02", "Herbívoro", "Limpeza semanal", "Planície A17", true),
	("Rex", "Hipopótamo", "Hippopotamus amphibius", 1500.0, "2012-05-09", "2014-12-25", "Herbívoro", "Limpeza semanal", "Rio H18", true),
	("Snow", "Raposa-do-ártico", "Vulpes lagopus", 6.9, "2021-02-14", "2022-01-16", "Carnívoro", "Limpeza a cada 2 dias", "Gelo R19", true),
	("Pipoca", "Coala", "Phascolarctos cinereus", 7.1, "2020-09-29", "2021-11-03", "Herbívoro", "Limpeza semanal", "Eucalipto C20", true);

insert into usuario (nome, senha, email, admin) values
	("DEV", "1234", "dev_marco@gmail.com", True);
    
select * from usuario;

-- Usados no python:
-- 		animal.py
-- select * from animal where ativo = true;
-- 		usuario.py
-- select * from usuario where nome = "variável nome" AND senha = "variável senha"
-- insert into usuario (nome, senha, email, admin) values (%s, %s, %s, %s)