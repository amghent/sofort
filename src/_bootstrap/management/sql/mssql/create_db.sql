USE master
GO

DROP DATABASE IF EXISTS sofort
GO

CREATE DATABASE sofort
GO

USE sofort
GO

CREATE USER sofort
    FOR LOGIN sofort
GO

CREATE SCHEMA sofort_dev
GO

ALTER USER sofort
    WITH DEFAULT_SCHEMA = sofort_dev
GO

GRANT ALTER, CONTROL, REFERENCES
    ON DATABASE ::sofort TO sofort
GO

GRANT ALTER, CONTROL, CREATE SEQUENCE, DELETE, INSERT, REFERENCES, SELECT, UPDATE
    ON SCHEMA ::sofort_dev TO sofort
GO

USE master
GO