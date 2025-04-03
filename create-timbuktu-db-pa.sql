-- Pythonanywhere
-- Drop the existing tables if they exist
DROP TABLE IF EXISTS announcements;
DROP TABLE IF EXISTS journeys;
DROP TABLE IF EXISTS events;
DROP TABLE IF EXISTS users;


CREATE TABLE `users` (
  `user_id` INT NOT NULL AUTO_INCREMENT, -- It generates a unique integer ID for each added new user
  `username` VARCHAR(20) NOT NULL,
  `password_hash` CHAR(60) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL COMMENT 'Bcrypt Password Hash and Salt (60 bytes)',
  `email` VARCHAR(320) NOT NULL COMMENT 'Maximum email address length according to RFC5321 section 4.5.3.1 is 320 characters (64 for local-part, 1 for at sign, 255 for domain)',
  `first_name` VARCHAR(50),
  `last_name` VARCHAR(50),
  `location` VARCHAR(50),
  `profile_image` VARCHAR(255),
  `profile_description` TEXT,
  `role` ENUM('traveller', 'editor', 'admin') NOT NULL,
  `status` ENUM('active', 'blocked', 'banned') NOT NULL,
  PRIMARY KEY (`user_id`),
  UNIQUE KEY `username` (`username`)
);

CREATE TABLE `announcements` (
  `announcement_id` INT NOT NULL AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `announcement_title` VARCHAR(255) NOT NULL,
  `announcement_description` TEXT NOT NULL,
  `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP, -- Automatically sets the creation timestamp
  PRIMARY KEY (`announcement_id`),
  FOREIGN KEY (`user_id`) REFERENCES `users`(`user_id`)
);

CREATE TABLE `journeys` (
  `journey_id` INT NOT NULL AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `journey_title` VARCHAR(255) NOT NULL,
  `journey_description` TEXT NOT NULL,
  `start_date` date NOT NULL, 
  `status` ENUM('private', 'public', 'hidden') NOT NULL,
  PRIMARY KEY (`journey_id`),
  FOREIGN KEY (`user_id`) REFERENCES `users`(`user_id`)
);

CREATE TABLE `events` (
  `event_id` INT NOT NULL AUTO_INCREMENT,
  `journey_id` INT NOT NULL,
  `event_title` VARCHAR(255) NOT NULL,
  `event_description` TEXT,
  `start_date` TIMESTAMP NOT NULL,
  `end_date` TIMESTAMP,
  `event_location` VARCHAR(50) NOT NULL,
  `event_image` VARCHAR(255),
  PRIMARY KEY (`event_id`),
  FOREIGN KEY (`journey_id`) REFERENCES `journeys`(`journey_id`)
);