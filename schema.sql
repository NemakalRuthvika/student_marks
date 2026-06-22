CREATE DATABASE IF NOT EXISTS student_db;

USE student_db;

CREATE TABLE IF NOT EXISTS students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    roll VARCHAR(50),
    sub1 FLOAT,
    sub2 FLOAT,
    sub3 FLOAT,
    sub4 FLOAT,
    sub5 FLOAT,
    total FLOAT,
    average FLOAT,
    percentage FLOAT,
    grade VARCHAR(10),
    status VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
