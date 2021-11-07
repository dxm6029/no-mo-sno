BEGIN;

create table users (
   id SERIAL NOT NULL PRIMARY KEY,
   fname text NOT NULL,
   lname text NOT NULL,
   username text NOT NULL UNIQUE,
   hashed_password text NOT NULL,
   location text NOT NULL,
   shovel_rating decimal,
   num_shovel_rating INT DEFAULT 0,
   house_rating decimal,
   num_house_rating INT DEFAULT 0,
   token text
);
CREATE TABLE comments (
       commentId SERIAL NOT NULL PRIMARY KEY,
       postUser INT NOT NULL,
       workerId INT NOT NULL,
       customerId INT NOT NULL,
       description text NOT NULL,
       CONSTRAINT comments_worker_exists FOREIGN KEY (workerId) REFERENCES users,
       CONSTRAINT comments_customer_exists FOREIGN KEY (customerId) REFERENCES users
);

create table jobs (
                       jobId SERIAL NOT NULL PRIMARY KEY,
                       customerId int NOT NULL,
                       workerId int NOT NULL,
                       location text NOT NULL,
                       price int not null,
                       rating decimal -- of customer --
);

COMMIT;