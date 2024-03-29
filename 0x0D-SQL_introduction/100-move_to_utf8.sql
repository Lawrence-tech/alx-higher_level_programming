-- Script that converts hbtn_0c_0 database to UTF8 (utf8mb4, collate utf8mb4_unicode_ci)

-- Database hbtn_0c_0
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Use the hbtn_0c_0 database
USE hbtn_0c_0;

-- Table first_table
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Field name in first_table
ALTER TABLE first_table MODIFY `name` VARCHAR(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE first_table MODIFY `score` int(11);
