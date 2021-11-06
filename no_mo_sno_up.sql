BEGIN;

create table users (
   id SERIAL NOT NULL PRIMARY KEY,
   fname text NOT NULL,
   lname text NOT NULL,
   username text NOT NULL,
   hashed_password text NOT NULL,
   location text NOT NULL,
   shovel_rating decimal,
   num_shovel_rating INT,
   house_rating decimal,
   num_house_rating INT
);

CREATE TABLE comment (
       commentId SERIAL NOT NULL PRIMARY KEY,
       workerId INT NOT NULL,
       customerId INT NOT NULL,
       description VARCHAR(5000) NOT NULL
);

COMMIT;