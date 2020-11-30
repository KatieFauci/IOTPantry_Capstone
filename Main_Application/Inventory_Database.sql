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
  ingredient VARCHAR(255) NOT NULL,
  amount VARCHAR(128) NOT NULL,
  PRIMARY KEY(recipe_id, ingredient_id)
);

/*Inserting food groups into food type columb*/
INSERT INTO food_type VALUES(1,"Fruits");
INSERT INTO food_type VALUES(2,"Vegtables");
INSERT INTO food_type VALUES(3,"Canned Goods");
INSERT INTO food_type VALUES(4,"Dried Goods");
INSERT INTO food_type VALUES(5,"Medicine");

/*Sample Data*/
INSERT INTO items VALUES (1, 5, "Tylonol", 100029185, "32,213,205,74", CURRENT_TIMESTAMP, "08/2020", 1);
/*INSERT INTO Items VALUES ("Tylonol", CURRENT_TIMESTAMP, "08/2020", "32,213,205,74", 100029185, 1, "Medicine");

INSERT INTO ingredients VALUES (1,1,"Salted Butter *softened", "1 cup");
INSERT INTO ingredients VALUES (1,2,"white (granulated) sugar","1 cup");
INSERT INTO ingredients VALUES (1,3,"light brown sugar packed","1 cup");
INSERT INTO ingredients VALUES (1,4,"pure vanilla extract","2 tsp");
INSERT INTO ingredients VALUES (1,5,"Large Eggs","2");
INSERT INTO ingredients VALUES (1,6,"All-purpose Flour","2 tsp");
INSERT INTO ingredients VALUES (1,7,"Baking Soda","1 tsp");
INSERT INTO ingredients VALUES (1,8,"Sea Salt","1 tsp");
INSERT INTO ingredients VALUES (1,9,"Chocolate Chips","2 cups");

INSERT INTO recipe VALUES(2,"Pasta Aglio E Olio","20 minutes");
INSERT INTO ingredients VALUES (2,1,"garlic, separated and peeled", "1/2 head");
INSERT INTO ingredients VALUES (2,2,"flat-leaf parsley, rinsed and finely chopped","1/2 cup");
INSERT INTO ingredients VALUES (2,3,"good quality olive oil","1/2 cup");
INSERT INTO ingredients VALUES (2,4,"red pepper flakes","1 tsp");
INSERT INTO ingredients VALUES (2,5,"dry linguine","1/2 pound");
INSERT INTO ingredients VALUES (2,6,"lemon","1/2");
INSERT INTO steps VALUES(2,1,"Heavily salt a large pot of water, and bring to a boil. Cook pasta until slightly underdone while completing the steps below.");
INSERT INTO steps VALUES(2,2,"Slice the garlic cloves thinly, and set aside. Heat olive oil in a large sauté pan over medium heat until barely shimmering. Add sliced garlic, stirring constantly, until softened and turning golden on the edges. Add the red pepper flakes and lower the heat to medium-low.");
INSERT INTO steps VALUES(2,3,"Add the pasta, drained, with about 1/4 cup reserved pasta cooking water. Squeeze lemon juice over top, and mix into the pasta with the fresh parsley. If sauce is too watery, continue to cook for 1-3 minutes, until pasta has absorbed more liquid. Season with salt and pepper, and serve.");


