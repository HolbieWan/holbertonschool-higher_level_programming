-- Command to create a new user and give it the SELECT privilege on the database hbtn_0d_2:
CREATE USER if not EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;
