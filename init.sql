CREATE USER IF NOT EXISTS'demo'@'localhost' IDENTIFIED BY 'pwd';
GRANT ALL PRIVILEGES ON *.* TO 'demo'@'localhost' WITH GRANT OPTION;
FLUSH PRIVILEGES;

CREATE DATABASE IF NOT EXISTS portefeuille_db;
USE portefeuille_db;
CREATE TABLE IF NOT EXISTS referentielfonds (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS referentielinstruments (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS positions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    instrument_id INT,
    poids DECIMAL(5,2),
    FOREIGN KEY (instrument_id) REFERENCES referentielinstruments(id)
);
