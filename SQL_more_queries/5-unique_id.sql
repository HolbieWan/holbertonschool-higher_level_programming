-- Script to create the table unique_id:
CREATE TABLE if not EXISTS unique_id (
    id INT DEFAULT 1,
    name VARCHAR(256),
    PRIMARY KEY (id)
);
