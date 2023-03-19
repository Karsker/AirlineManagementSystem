DROP TABLE IF EXISTS users;

CREATE TABLE users {
    userId INTEGER PRIMARY KEY;
    userName TEXT NOT NULL;
    contact INTEGER NOT NULL;
    userEmail TEXT; 
};