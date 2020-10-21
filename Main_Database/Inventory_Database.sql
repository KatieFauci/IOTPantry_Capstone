/*
IOT Pantry Capstone 2
By:
Katherine Fauci
Erik Rodriguez
Keshawn The Goat
Fall 2020
*/

DROP DATABASE IF EXISTS Inventory; /*Deletes database*/
CREATE DATABASE Inventory; /*Creates new database*/
USE Inventory; /*Brings focus to Inventory database*/

 /*Creates new table for schema*/
CREATE TABLE Items (
  item_id BIGINT(255) NOT NULL,
  type_id BIGINT(255) NOT NULL,
  product_name VARCHAR(128) NOT NULL,
  barcode_num BIGINT(255) NOT NULL,
  UID VARCHAR(128) NOT NULL,
  input_date VARCHAR(25) NOT NULL,
  expiration_date VARCHAR(11) NOT NULL,
  num_items SMALLINT(20) NOT NULL,
  food_group VARCHAR(50) NOT NULL,
  PRIMARY KEY (item_id, type_id)
);

/* Field will be used for sorting items in the inventory */
CREATE TABLE Food_type (
  type_id BIGINT(255) NOT NULL,
  type VARCHAR (128) NOT NULL,
  PRIMARY KEY (type_id)
);

CREATE TABLE Shopping_List (
  list_id BIGINT(255) NOT NULL,
  item_id BIGINT(255) NOT NULL,
  type_id BIGINT(255) NOT NULL,
  product_name VARCHAR(128) NOT NULL,
  food_group VARCHAR(50) NOT NULL,
  amount VARCHAR(128) NOT NULL,
  PRIMARY KEY (list_id, item_id, type_id)
);

CREATE TABLE recipe (
  recipe_id BIGINT(255) NOT NULL,
  recipe_name VARCHAR(128) NOT NULL,
  recipe_time VARCHAR(128) NOT NULL,
  PRIMARY KEY (recipe_id)
);

CREATE TABLE steps (
  recipe_id BIGINT(255) NOT NULL,
  step_id SMALLINT(50) NOT NULL,
  step VARCHAR(1024) NOT NULL,
  PRIMARY KEY (recipe_id, step_id)
);

CREATE TABLE ingrediants (
  recipe_id BIGINT(255) NOT NULL,
  ingrediant_id SMALLINT(50) NOT NULL,
  item_id BIGINT(255) NOT NULL,
  amount VARCHAR(128) NOT NULL,
  PRIMARY KEY(recipe_id, ingrediant_id, item_id)
)

/* Sample Data
INSERT INTO Items VALUES ("Tylonol", CURRENT_TIMESTAMP, "08/2020", "32,213,205,74", 100029185, 1, "Medicine");
*/
