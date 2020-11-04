DROP DATABASE IF EXISTS test_inventory; /*Deletes database*/
CREATE DATABASE test_inventory; /*Creates new database*/
USE test_inventory; /*Brings focus to Inventory database*/


/* Field will be used for sorting items in the inventory */
CREATE TABLE barcode (
  code_id BIGINT(255) NOT NULL,
  barcode VARCHAR (128) NOT NULL,
  PRIMARY KEY (code_id)
);

INSERT INTO barcode VALUES(1,"122422433");
INSERT INTO barcode VALUES(2,"363453456");
