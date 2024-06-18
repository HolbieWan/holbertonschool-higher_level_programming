-- Script that creates the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa)
CREATE DATABASE if not EXISTS hbtn_0d_usa;
CREATE TABLE if not EXISTS states in database hbtn_0d_usa (
    id INT auto generated unique not null,
    name VARCHAR(256) not null,
    PRIMARY KEY (id)
);
