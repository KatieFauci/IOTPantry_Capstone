/*
IOT Pantry Capstone 2
By:
Katherine Fauci
Erik Rodriguez
Keshawn The Goat
Fall 2020
*/

drop database if exists Inventory; /*Deletes database*/
create database Inventory; /*Creates new database*/
use Inventory; /*Brings focus to Inventory database*/

 /*Creates new table for schema*/
create table Items (
  type_id bigint(255) not null,
  product_name varchar(128) not null,
  input_date varchar(25) not null,
  expiration_date varchar(11) not null,
  UID varchar(128) not null,
  barcode_num bigint(255) not null,
  num_items smallint(20) not null,
  food_group varchar(50) not null,
  primary key (barcode_num, type_id)
);

create table Food_type (
  type_id bigint(255) not null,
  type varchar (128) not null,
  primary key (type_id)
);

create table Shopping_List (
  item_id bigint(255) not null,
  product_name varchar(128) not null,
  food_group varchar(50), not null,
  amount varchar(128) not null,
  primary key (item_id, product_name, amount)
);

create table recipe (
  recipe_id bigint(255) not null,
  recipe_name varchar(128) not null,
  recipe_time varchar(128) not null,
  primary key (recipe_id)
);

create table steps (
  recipe_id bigint(255) not null,
  step_id smallint(50) not null,
  step varchar(1024) not null,
  primary key (recipe_id, step_id)
);

create table ingrediants (
  recipe_id bigint(255) not null,
  ingrediant_id smallint(50) not null,
  item_id bigint(255) not null,
  amount varchar(128) not null,
  primary key(recipe_id, ingrediant_id, item_id)
)

INSERT INTO Items VALUES ("Tylonol", CURRENT_TIMESTAMP, "08/2020", "32,213,205,74", 100029185, 1, "Medicine");
