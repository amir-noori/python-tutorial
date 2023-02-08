
# Postgres

## start database
    cd #postgres_bin
    ./postgres -D #data_directory

## connect to database
    ./psql -U postgres

## create database
    create database testdb;

## connect to schema
    \c testdb;


create table tbl_account
(
    account_id INT,
    account_name varchar(100)
);


## insert data

insert into tbl_account (account_id, account_name) values (1, 'test');



# ORM (Object Relational Mapping)

Table -> Entity
tbl_acount -> Account


# task:

    with "sql alchemy":
        1- create two tables:
            account
            user -> each user has many accounts
        2- fetch data from database












