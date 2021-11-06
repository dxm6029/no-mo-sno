create table users (
   id SERIAL NOT NULL PRIMARY KEY,
   fname text NOT NULL,
   lname text NOT NULL,
   location text NOT NULL,
   rating DECIMAL(3, 2),
   numRating INT
);

CREATE TABLE comment (
       commentId SERIAL NOT NULL PRIMARY KEY,
       workerId INT NOT NULL,
       customerId INT NOT NULL,
       description VARCHAR(5000) NOT NULL
);