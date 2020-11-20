/*DROP DATABASE IF EXISTS ref_database; /*Deletes database*/
/*CREATE DATABASE ref_database; /*Creates new database*/
/*USE ref_database; /*Brings focus to Inventory database*/


/* Field will be used for sorting items in the inventory */
CREATE TABLE items (
  code_id BIGINT(255) NOT NULL,
  name VARCHAR(255) NOT NULL,
  food_group VARCHAR(255) NOT NULL,
  exp_date VARCHAR(255),
  barcode VARCHAR (128) NOT NULL,
  RFIDcode VARCHAR (128) NOT NULL,
  PRIMARY KEY (code_id)
);

INSERT INTO items VALUES(1,"Ground Cinnamon",
                           "Herbs & Spices",
                           "Jan 20 22",
                           "052100038216",
                           "48,215,205,74");

INSERT INTO items VALUES(2,"Rosemary Leaves",
                           "Herbs & Spices",
                           "1/28/2023",
                           "604485002414",
                           "48,207,205,74");

INSERT INTO items VALUES(3, "Granulated Garlic",
                            "Herbs & Spices",
                            "6/20/2023",
                            "604485016336",
                            "48,183,205,74");

INSERT INTO items VALUES(4, "White Sesame Seed",
                            "Seeds & Nuts",
                            "Jun 24 21",
                            "011152066004",
                            "16,189,203,74");

INSERT INTO items VALUES(5, "Ground Sage",
                            "Herbs & Spices",
                            "3/21/2021",
                            "604485002759",
                            "48,191,205,74");

INSERT INTO items VALUES(6, "Ground Cardomon",
                            "Herbs & Spices",
                            "0ct 09 22",
                            "05228810",
                            "224,160,204,74");

INSERT INTO items VALUES(7, "Corn Starch",
                            "Dry Goods",
                            "nov 01 2020",
                            "688267070365",
                            "0,100,204,74");

INSERT INTO items VALUES(8, "Hershey's Cocoa Special Dark 100% Cocao",
                            "Dry Goods",
                            "12 2020",
                            "034000053001",
                            "0,92,204,74");

INSERT INTO items VALUES(9, "Quaker Oats Steel Cut",
                            "Dry Goods",
                            "sep 04 2021",
                            "030000320938",
                            "0,137,204,74");

INSERT INTO items VALUES(10,"4C Bread Crumbs Seasoned with Pecorino Romano Cheese",
                            "Dry Goods",
                            "feb 11 2021",
                            "041387406467",
                            "0,129,204,74");

INSERT INTO items VALUES(11,"Sun Dried Tomatoes",
                            "Cans & Jars",
                            "12/12/19",
                            "00098724",
                            "0,116,204,74");

INSERT INTO items VALUES(12,"Pitted Kalamata Olives",
                            "Cans & Jars",
                            "09/04/2021",
                            "00362993",
                            "0,108,204,74");

INSERT INTO items VALUES(13,"Herb Ox Chicken Bouillon Cubes",
                            "Herbs & Spices",
                            "jul 2021",
                            "033600000118",
                            "16,181,203,74");

INSERT INTO items VALUES(14,"Ronzoni Spaghetti",
                            "Dry Goods",
                            "sep 16 2023",
                            "071300000083",
                            "48,199,205,74");

INSERT INTO items VALUES(15,"Carolina Basmati Rice",
                            "Dry Goods",
                            "jun 09 2022",
                            "017400106683",
                            "0,175,203,74");

INSERT INTO items VALUES(16,"Mountain Ridge Orange Blossom Honey",
                            "Cans & Jars",
                            "01 01 24",
                            "073209003202",
                            "204,152,204,74");

INSERT INTO items VALUES(17,"Pastene Pine Nuts",
                            "Seeds & Nuts",
                            "NOV 19 2021",
                            "066086140900",
                            "32,169,203,74");

INSERT INTO items VALUES(18,"Skippy Creamy Peanut Butter",
                            "Cans & Jars",
                            "OCT 09 21",
                            "037600223324",
                            "96,121,204,74");

INSERT INTO items VALUES(19,"Gold Medal All Purpose Flour",
                            "Dry Goods",
                            "23 JAN 2022",
                            "016000502697",
                            "0,162,203,74");

INSERT INTO items VALUES(20,"Kame Wide Lo Mein Noodles",
                            "Dry Goods",
                            "DEC282021",
                            "070844004755",
                            "16,154,203,74");

INSERT INTO items VALUES(21,"Jack Rabbit Brand Navy Beans",
                            "Dry Goods",
                            "23MAR21",
                            "070620001015",
                            "16,146,203,74");

INSERT INTO items VALUES(22,"Goya Black Beans",
                            "Cans & Jars",
                            "05/24/24",
                            "041331124669",
                            "16,138,203,74");

INSERT INTO items VALUES(23,"Muir Glen Organic Diced Tomatoes",
                            "Cans & Jars",
                            "16APR2022",
                            "725342260713",
                            "0,124,203,74");

INSERT INTO items VALUES(24,"Thai Kitchen Lite Coconut Milk",
                            "Cans & Jars",
                            "MAY152022",
                            "737628011605",
                            "0,145,204,74");

INSERT INTO items VALUES(25,"Wellsley Farms Blueberry Cereal Bars",
                            "Other",
                            "04/01/2021",
                            "888670045459",
                            "0,132,203,74");
