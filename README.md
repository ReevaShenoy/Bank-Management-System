# Bank-Management-System
This project is built upon the connectivity between Python (frontend) and MySQL (backend), and gives the user the freedom to perform simple bank operations such as deposit money, withdraw money, check balance, forgot password, etc.

The database used in this programme is REALPROJECT. The two tables CUST and BANKDETAILS, connected by a foreign key, contain the data.

## Structure of table CUST:

CREATE TABLE cust (
    account_no INT,
    cname VARCHAR(30),
    address VARCHAR(30),
    phone VARCHAR(12)
);


![image](https://github.com/user-attachments/assets/6692c7a9-7439-4ce8-8faa-45b7413fcfb4)

## Structure of table BANKDETAILS:

CREATE TABLE bankdetails (
    account_no INT NOT NULL PRIMARY KEY,
    account_type VARCHAR(20),
    amount INT,
    pin INT
);


![image](https://github.com/user-attachments/assets/9d7a9b64-a298-4992-8e91-06d25782518a)
