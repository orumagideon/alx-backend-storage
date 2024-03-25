# alx-backend-storage

## Repository: alx-backend-storage
## Directory: 0x00-MySQL_Advanced

### 0x00. MySQL advanced

This repository contains MySQL advanced tasks and their solutions. Each task is aimed at practicing various MySQL concepts and commands.

---

### Tasks

#### 0. We are all unique!
- **Objective**: Write a SQL script that creates a table users following specific requirements.
- **File**: [0-uniq_users.sql](0x00-MySQL_Advanced/0-uniq_users.sql)

#### 1. In and not out
- **Objective**: Write a SQL script that creates a table users following specific requirements.
- **File**: [1-country_users.sql](0x00-MySQL_Advanced/1-country_users.sql)

#### 2. Best band ever!
- **Objective**: Write a SQL script that ranks country origins of bands, ordered by the number of (non-unique) fans.
- **File**: [2-fans.sql](0x00-MySQL_Advanced/2-fans.sql)

#### 3. Old school band
- **Objective**: Write a SQL script that lists all bands with Glam rock as their main style, ranked by their longevity.
- **File**: [3-glam_rock.sql](0x00-MySQL_Advanced/3-glam_rock.sql)

#### 4. Buy buy buy
- **Objective**: Write a SQL script that creates a trigger that decreases the quantity of an item after adding a new order.
- **Files**: [4-init.sql](0x00-MySQL_Advanced/4-init.sql), [4-store.sql](0x00-MySQL_Advanced/4-store.sql), [4-main.sql](0x00-MySQL_Advanced/4-main.sql)

#### 5. Email validation to sent
- **Objective**: Write a SQL script that creates a trigger that resets the attribute valid_email only when the email has been changed.
- **Files**: [5-init.sql](0x00-MySQL_Advanced/5-init.sql), [5-valid_email.sql](0x00-MySQL_Advanced/5-valid_email.sql), [5-main.sql](0x00-MySQL_Advanced/5-main.sql)

#### 6. Add bonus
- **Objective**: Write a SQL script that creates a stored procedure AddBonus that adds a new correction for a student.
- **Files**: [6-init.sql](0x00-MySQL_Advanced/6-init.sql), [6-bonus.sql](0x00-MySQL_Advanced/6-bonus.sql), [6-main.sql](0x00-MySQL_Advanced/6-main.sql)

#### 7. Average score
- **Objective**: Write a SQL script that creates a stored procedure ComputeAverageScoreForUser that computes and stores the average score for a student.
- **Files**: [7-init.sql](0x00-MySQL_Advanced/7-init.sql), [7-average_score.sql](0x00-MySQL_Advanced/7-average_score.sql), [7-main.sql](0x00-MySQL_Advanced/7-main.sql)

#### 8. Optimize simple search
- **Objective**: Write a SQL script that creates an index idx_name_first on the table names and the first letter of name.
- **File**: [8-index_my_names.sql](0x00-MySQL_Advanced/8-index_my_names.sql)

#### 9. Optimize search and score
- **Objective**: Write a SQL script that creates an index idx_name_first_score on the table names and the first letter of name and the score.
- **File**: [9-index_name_score.sql](0x00-MySQL_Advanced/9-index_name_score.sql)

#### 10. Safe divide
- **Objective**: Write a SQL script that creates a function SafeDiv that divides the first by the second number or returns 0 if the second number is equal to 0.
- **Files**: [10-init.sql](0x00-MySQL_Advanced/10-init.sql), [10-div.sql](0x00-MySQL_Advanced/10-div.sql)

#### 11. No table for a meeting
- **Objective**: Write a SQL script that creates a view need_meeting that lists all students that have a score under 80 (strict) and no last_meeting or more than 1 month.
- **Files**: [11-init.sql](0x00-MySQL_Advanced/11-init.sql), [11-need_meeting.sql](0x00-MySQL_Advanced/11-need_meeting.sql), [11-main.sql](0x00-MySQL_Advanced/11-main.sql)

---

### Resources

#### Read or watch:
- MySQL cheatsheet
- MySQL Performance: How To Leverage MySQL Database Indexing
- Stored Procedure
- Triggers
- Views
- Functions and Operators
- Trigger Syntax and Examples
- CREATE TABLE Statement
- CREATE PROCEDURE and CREATE FUNCTION Statements
- CREATE INDEX Statement
- CREATE VIEW Statement

---

### Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google
