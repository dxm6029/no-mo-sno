show databases;
use dxm6029;
show tables;

DROP TABLE IF EXISTS `user` ;

CREATE TABLE IF NOT EXISTS `user` (
  id INT NOT NULL AUTO_INCREMENT,
  fname VARCHAR(50) NOT NULL,
  lname VARCHAR(50) NOT NULL,
  location VARCHAR(4000) NOT NULL,
  rating DECIMAL(3, 2),
  numRating INT,
  PRIMARY KEY (id)
);
 
 DROP TABLE IF EXISTS `comment` ;

CREATE TABLE IF NOT EXISTS `comment` (
  commentId INT NOT NULL AUTO_INCREMENT,
  workerId INT NOT NULL,
  customerId VARCHAR(50) NOT NULL,
  `comment` VARCHAR(50) NOT NULL,
  PRIMARY KEY (commentId)
);
  