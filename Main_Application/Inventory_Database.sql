/*
IOT Pantry Capstone 2
By:
Katherine Fauci
Erik Rodriguez
Keshawn Smith
Fall 2020
*/
/*
DROP DATABASE IF EXISTS Inventory; /*Deletes database*/
/*CREATE DATABASE Inventory; /*Creates new database*/
/*USE Inventory; /*Brings focus to Inventory database*/


/* Field will be used for sorting items in the inventory */
CREATE TABLE food_type (
  type_id BIGINT(255) NOT NULL,
  type VARCHAR (128) NOT NULL,
  PRIMARY KEY (type_id)
);

 /*Creates new table for schema*/
CREATE TABLE items (
  item_id BIGINT(255) NOT NULL,
  type_id BIGINT(255) NOT NULL,
  product_name VARCHAR(128) NOT NULL,
  barcode_num BIGINT(255) NOT NULL,
  UID VARCHAR(128) NOT NULL,
  input_date VARCHAR(25) NOT NULL,
  expiration_date VARCHAR(11) NOT NULL,
  num_items SMALLINT(20) NOT NULL,
  PRIMARY KEY (item_id, type_id)
);

/*Creates new table for items being added to shopping list*/
CREATE TABLE shopping_list (
  list_id BIGINT(255) NOT NULL,
  item_id BIGINT(255) NOT NULL,
  type_id BIGINT(255) NOT NULL,
  product_name VARCHAR(128) NOT NULL,
  food_group VARCHAR(50) NOT NULL,
  amount VARCHAR(128) NOT NULL,
  PRIMARY KEY (list_id, item_id, type_id)
);

/*Creates new table for recipes*/
CREATE TABLE recipe (
  recipe_id BIGINT(255) NOT NULL,
  recipe_name VARCHAR(128) NOT NULL,
  recipe_time VARCHAR(128) NOT NULL,
  PRIMARY KEY (recipe_id)
);

/*Creates new table for steps of the recipes*/
CREATE TABLE steps (
  recipe_id BIGINT(255) NOT NULL,
  step_id SMALLINT(50) NOT NULL,
  step VARCHAR(1024) NOT NULL,
  PRIMARY KEY (recipe_id, step_id)
);

/*Creates new table for ingrediants in recipes*/
CREATE TABLE ingredients (
  recipe_id BIGINT(255) NOT NULL,
  ingredient_id SMALLINT(50) NOT NULL,
  item_id BIGINT(255) NOT NULL,
  amount VARCHAR(128) NOT NULL,
  PRIMARY KEY(recipe_id, ingredient_id, item_id)
);

/*Inserting food groups into food type columb*/
INSERT INTO food_type VALUES(1,"Fruits");
INSERT INTO food_type VALUES(2,"Vegtables");
INSERT INTO food_type VALUES(3,"Canned Goods");
INSERT INTO food_type VALUES(4,"Dried Goods");
INSERT INTO food_type VALUES(5,"Medicine");

/*Sample Data*/
INSERT INTO items VALUES (1, 5, "Tylonol", 100029185, "32,213,205,74", CURRENT_TIMESTAMP, "08/2020", 1);
INSERT INTO Items VALUES ("Tylonol", CURRENT_TIMESTAMP, "08/2020", "32,213,205,74", 100029185, 1, "Medicine");
