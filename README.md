# MySQL Advanced

This repository contains SQL scripts that demonstrate advanced MySQL functionalities. Each task is outlined below with its respective SQL script and instructions for execution.

## Requirements

All scripts are designed to be executed on Ubuntu 18.04 LTS using MySQL 5.7 (version 5.7.30). Ensure that you have MySQL set up and running on your system before executing these scripts.

## General Instructions

- All SQL queries should have a comment just before them, detailing their purpose.
- Scripts should start with a comment describing the task.
- All SQL keywords should be in uppercase (e.g., SELECT, WHERE).
- The length of your files will be tested using wc.

## Setup

To set up the environment, you can use "container-on-demand" to run MySQL. Follow these steps:

1. Ask for a container with Ubuntu 18.04 and Python 3.7.
2. Connect to the container via SSH or WebTerminal.
3. Start MySQL service: `$ service mysql start`

## Task Overview

### 0. We are all unique!
- Create a table 'users' with specific attributes.
- Ensure email uniqueness.
- [File: 0-uniq_users.sql]

### 1. In and not out
- Create a table 'users' with specific attributes and an enumeration of countries.
- Ensure email uniqueness and country validation.
- [File: 1-country_users.sql]

### 2. Best band ever!
- Rank country origins of bands based on the number of fans.
- [File: 2-fans.sql]

### 3. Old school band
- List bands with Glam rock as their main style, ranked by longevity.
- [File: 3-glam_rock.sql]

### 4. Buy buy buy
- Create a trigger to decrease the quantity of an item after adding a new order.
- [Files: 4-init.sql, 4-store.sql, 4-main.sql]

### 5. Email validation to sent
- Create a trigger to reset the 'valid_email' attribute only when the email has been changed.
- [Files: 5-init.sql, 5-valid_email.sql, 5-main.sql]

### 6. Add bonus
- Create a stored procedure to add a new correction for a student.
- [Files: 6-init.sql, 6-bonus.sql, 6-main.sql]

### 7. Average score
- Create a stored procedure to compute and store the average score for a student.
- [Files: 7-init.sql, 7-average_score.sql, 7-main.sql]

### 8. Optimize simple search
- Create an index on the table 'names' for faster searching.
- [Files: names.sql, 8-index_my_names.sql]

### 9. Optimize search and score
- Create an index on the table 'names' for faster searching with score.
- [Files: names.sql, 9-index_name_score.sql]

### 10. Safe divide
- Create a function to safely divide two numbers.
- [Files: 10-init.sql, 10-div.sql]

### 11. No table for a meeting
- Create a view that lists students needing a meeting based on score and last meeting date.
- [Files: 11-init.sql, 11-need_meeting.sql, 11-main.sql]

### 12. Average weighted score (Advanced)
- Create a stored procedure to compute and store the average weighted score for a student.
- [Files: 100-init.sql]

## Repository Information

- **GitHub Repository:** [alx-backend-storage](https://github.com/orumagideon/alx-backend-storage)
- **Directory:** 0x00-MySQL_Advanced
