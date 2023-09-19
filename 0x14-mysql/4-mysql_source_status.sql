-- Prints Source MySQL Status
-- Record File and Position to use in Replica setup
-- Run: sudo mysql --table < script.sql

FLUSH TABLES WITH READ LOCK;
SHOW MASTER STATUS;
UNLOCK TABLES;
