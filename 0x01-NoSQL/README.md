# 0x01. NoSQL

## Introduction

This repository contains solutions to various tasks related to NoSQL databases, specifically MongoDB, as part of the ALX Software Engineering program.

## General Information

- Start Date: March 25, 2024, 6:00 AM
- End Date: March 27, 2024, 6:00 AM
- Checker Release Date: March 25, 2024, 6:00 PM
- Auto Review Deadline: March 27, 2024, 6:00 AM
- Weight: 1

## Resources

- [NoSQL Databases Explained](https://www.youtube.com/watch?v=GGpGGQiI2Mc)
- [What is NoSQL?](https://www.mongodb.com/nosql-explained)
- [MongoDB with Python Crash Course - Tutorial for Beginners](https://www.youtube.com/watch?v=E-1xI85Zog8)
- [MongoDB Tutorial 2: Insert, Update, Remove, Query](https://www.youtube.com/watch?v=YnbFt0PFaQY)
- [Aggregation](https://docs.mongodb.com/manual/aggregation/)
- [Introduction to MongoDB and Python](https://realpython.com/introduction-to-mongodb-and-python/)
- [mongo Shell Methods](https://docs.mongodb.com/manual/reference/mongo-shell/)
- [Mongosh](https://docs.mongodb.com/mongosh/)

## Learning Objectives

By the end of this project, you should be able to explain the following concepts without the help of Google:

- What NoSQL means
- Difference between SQL and NoSQL
- ACID properties
- Document storage
- Types of NoSQL databases
- Benefits of using a NoSQL database
- Querying information from a NoSQL database
- Inserting, updating, and deleting information from a NoSQL database
- How to use MongoDB

## Requirements

### MongoDB Command File

- All files should be interpreted/compiled on Ubuntu 18.04 LTS using MongoDB version 4.2
- Files should end with a new line
- The first line of all files should be a comment: `// my comment`
- A `README.md` file is mandatory and should be placed at the root of the project folder

### Python Scripts

- All files should be interpreted/compiled on Ubuntu 18.04 LTS using Python3 (version 3.7) and PyMongo (version 3.10)
- Files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/env python3`
- A `README.md` file is mandatory and should be placed at the root of the project folder
- Code should follow the `pycodestyle` style (version 2.5.*)
- All modules and functions should have documentation
- Code should not be executed when imported (use `if __name__ == "__main__":`)

### MongoDB Installation

Follow the official installation guide to install MongoDB 4.2 on Ubuntu 18.04 LTS. Below are the basic steps:

```bash
$ wget -qO - https://www.mongodb.org/static/pgp/server-4.2.asc | apt-key add -
$ echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.2 multiverse" > /etc/apt/sources.list.d/mongodb-org-4.2.list
$ sudo apt-get update
$ sudo apt-get install -y mongodb-org
$ sudo service mongod status
$ mongo --version
$ pip3 install pymongo
Tasks
0. List all databases
Task details

1. Create a database
Task details

2. Insert document
Task details

3. All documents
Task details

4. All matches
Task details

5. Count
Task details

6. Update
Task details

7. Delete by match
Task details

8. List all documents in Python
Task details

9. Insert a document in Python
Task details

10. Change school topics
Task details

11. Where can I learn Python?
Task details

12. Log stats
Task details

13. Regex filter
Task details

14. Top students
Task details

15. Log stats - new version
Task details

Author
GIDEON ORUMA - Initial work
