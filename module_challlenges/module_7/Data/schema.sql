CREATE TABLE card_holder (
    id int Primary Key,  
    name varchar(30)
);

CREATE TABLE credit_card (
    card varchar(20) Primary Key,
    cardholder_id int references card_holder(id)
);

CREATE TABLE merchant_category (
    id int Primary Key,
    name varchar(50)
);

CREATE TABLE merchant (
    id int Primary Key,
    name varchar(50),
    id_merchant_category int references merchant_category(id)
);

CREATE TABLE transaction(
    id int Primary Key,
    date timestamp,
    amount int,
    card varchar(20) references credit_card(card), 
    id_merchant int references merchant(id) 
);