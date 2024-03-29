0x0D-SQL_introduction

Learning Objectives

    • What’s a database
    • What’s a relational database
    • What does SQL stand for
    • What’s MySQL
    • How to create a database in MySQL
    • What does DDL and DML stand for
    • How to CREATE or ALTER a table
    • How to SELECT data from a table
    • How to INSERT, UPDATE or DELETE data
    • What are subqueries
    • How to use MySQL functions

Files:

    1. 0-list_databases.sql - a script that lists all databases of your MySQL server.
    2. 1-create_database_if_missing.sql - a script that creates the database hbtn_0c_0 in your MySQL server
        ◦ If the database hbtn_0c_0 already exists, your script should not fail
        ◦ You are not allowed to use the SELECT or SHOW statements
    3. 2-remove_database.sql - a script that deletes the database hbtn_0c_0 in your MySQL server.
    4. 3-list_tables.sql - a script that lists all the tables of a database in your MySQL server.
    5. 4-first_table.sql - a script that creates a table called first_table in the current database in your MySQL server.
    6. 5-full_table.sql - a script that prints the full description of the table first_table from the database hbtn_0c_0 in your MySQL server.
    7. 6-list_values.sql - a script that lists all rows of the table first_table from the database hbtn_0c_0 in your MySQL server.
    8. 7-insert_value.sql - a script that inserts a new row in the table first_table (database hbtn_0c_0) in your MySQL server.
    9. 8-count_89.sql - a script that displays the number of records with id = 89 in the table first_table of the database hbtn_0c_0 in your MySQL server.
    10. 9-full_creation.sql - a script that creates a table second_table in the database hbtn_0c_0 in your MySQL server and add multiples rows.
    11. 10-top_score.sql - a script that lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server.
    12. 11-best_score.sql - a script that lists all records with a score >= 10 in the table second_table of the database hbtn_0c_0 in your MySQL server.
    13. 12-no_cheating.sql - a script that updates the score of Bob to 10 in the table second_table.
    14. 13-change_class.sql - a script that removes all records with a score <= 5 in the table second_table of the database hbtn_0c_0 in your MySQL server.
    15. 14-average.sql - a script that computes the score average of all records in the table second_table of the database hbtn_0c_0 in your MySQL server.
    16. 15-groups.sql - a script that lists the number of records with the same score in the table second_table of the database hbtn_0c_0 in your MySQL server.
    17. 16-no_link.sql - a script that lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server.
    18. 100-move_to_utf8.sql - a script that converts hbtn_0c_0 database to UTF8 (utf8mb4, collate utf8mb4_unicode_ci) in your MySQL server.
    19. 101-avg_temperatures.sql - Import in hbtn_0c_0 database this table dump: download (https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/272/temperatures.sql). Write a script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending).
    20. 102-top_city.sql - Import in hbtn_0c_0 database this table dump: download[https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/272/temperatures.sql] (same as Temperatures #0)Write a script that displays the top 3 of cities temperature during July and August ordered by temperature (descending)
    21. 103-max_state.sql - Import in hbtn_0c_0 database this table dump: download [https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/272/temperatures.sql](same as Temperatures #0). Write a script that displays the max temperature of each state (ordered by State name).

