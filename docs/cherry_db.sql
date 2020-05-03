create database cherry_shop

-- CREATE TABLES

create table classifier(
  code INT PRIMARY KEY NOT NULL
)

create table warehouse(
  id_wh INT PRIMARY KEY IDENTITY(1,1) NOT NULL,
  code INT NOT NULL,
  supplier VARCHAR (40) NOT NULL,
  receipt_date DATE NOT NULL,
  value_product INT NOT NULL,
  price money NOT NULL,
  first_value INT NOT NULL,
  CONSTRAINT FK_code FOREIGN KEY (code) REFERENCES classifier (code)
)

create table supplier(
  id_sup INT PRIMARY KEY IDENTITY(1,1) NOT NULL,
  company_name VARCHAR (20) NOT NULL,
  bank VARCHAR (30) NOT NULL,
  account_number VARCHAR (12) NOT NULL,
  phone_number VARCHAR (20) NOT NULL,
  email VARCHAR (20) NULL,
  id_wh INT NOT NULL,
  CONSTRAINT FK_supp_to_warehouse FOREIGN KEY (id_wh) REFERENCES warehouse (id_wh)
)

create table seller(
  id_sell INT PRIMARY KEY IDENTITY(1,1) NOT NULL,
  status BIT NOT NULL,
  FIO VARCHAR (50) NOT NULL,
  value_product INT NOT NULL,
)

create table product(
  id_prod INT PRIMARY KEY IDENTITY(1,1) NOT NULL,
  value_product INT NOT NULL,
  date_sell DATE NOT NULL,
  price_prod MONEY NOT NULL,
  id_sell INT NOT NULL,
  id_wh INT NOT NULL,
  code INT NOT NULL,
  CONSTRAINT FK_prod_to_seller FOREIGN KEY (id_sell) REFERENCES seller (id_sell),
  CONSTRAINT FK_prod_to_warehouse FOREIGN KEY (id_wh) REFERENCES warehouse (id_wh),
  CONSTRAINT FK_prod_code FOREIGN KEY (code) REFERENCES classifier (code)
)



-- QUERIES

-- classifier
INSERT INTO classifier (code) VALUES (1)

SELECT code from classifier
SELECT code from classifier WHERE code = 1

UPDATE classifier SET code = 7 WHERE code = 6

DELETE FROM classifier WHERE code = 6



-- Warehouse
INSERT INTO warehouse (code, supplier, receipt_date, value_product, price, first_value) VALUES (1, 'supl 1', '20200427', 12, 1000, 1000);

SELECT * from warehouse
SELECT * from warehouse WHERE id_wh = 10
SELECT id_wh from warehouse

UPDATE warehouse SET code = 3, supplier = 'supl 34', receipt_date = '20200424', value_product = 15, price = 100, first_value = 2000 WHERE id_wh = 13

DELETE FROM warehouse WHERE id_wh = 10



-- Supplier
INSERT INTO supplier (company_name, bank, account_number, phone_number, email, id_wh) VALUES ('company_1', 'bank_1', 'acc_1', '+77771232123', 'a@g.com', 7);

SELECT * from supplier
SELECT * from supplier WHERE id_sup = 1
SELECT * from supplier WHERE id_wh = 7

UPDATE supplier SET company_name = '', bank = '', account_number = '', phone_number = '', email = '', id_wh = 1 WHERE id_sup = 1

DELETE FROM supplier WHERE id_sup = 10



-- Seller
INSERT INTO seller (status, FIO, value_product) VALUES (0, 'name_1', 20);



-- Product
INSERT INTO product (value_product, date_sell, price_prod, id_sell, id_wh, code) VALUES (100, '20200427', 20, 2, 7, 5);
