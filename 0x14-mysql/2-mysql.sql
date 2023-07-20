-- SQL Script to create a databases and table.
-- Run this script on web-01 and web-02 servers.

-- Create a new database.
CREATE DATABASE IF NOT EXISTS tyrell_corp;
USE tyrell_corp;

-- Create new table.
DROP TABLE IF EXISTS nexus6;
CREATE TABLE nexus6 (
	id INT PRIMARY KEY,
	name VARCHAR(256) NOT NULL
);

INSERT INTO nexus6 (id, name) VALUES (1, 'Leon');
