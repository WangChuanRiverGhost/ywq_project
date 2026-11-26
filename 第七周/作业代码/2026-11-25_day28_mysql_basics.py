# 库操作
"""
查库：
mysql> SHOW DATABASES;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| phpmyadmin         |
| sys                |
| test               |
| user_management_db |
+--------------------+
7 rows in set (0.00 sec)

进入库：
mysql> USE user_management_db
Database changed

查表：
mysql> SHOW TABLES;
+------------------------------+
| Tables_in_user_management_db |
+------------------------------+
| user                         |
+------------------------------+
1 row in set (0.00 sec)
"""
# 表操作
"""
建表：
CREATE TABLE user (
  id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
  user_name varchar(8) NOT NULL,
  user_id int(11) NOT NULL,
  accout varchar(11) NOT NULL,
  password varchar(15) NOT NULL,
  email varchar(255) DEFAULT NULL,
  create_time datetime DEFAULT CURRENT_TIMESTAMP
) 

查表结构：
mysql> DESC user
    -> ;
+-------------+--------------+------+-----+---------------------+----------------+
| Field       | Type         | Null | Key | Default             | Extra          |
+-------------+--------------+------+-----+---------------------+----------------+
| id          | int(11)      | NO   | PRI | NULL                | auto_increment |
| user_name   | varchar(8)   | NO   |     | NULL                |                |
| user_id     | int(11)      | NO   |     | NULL                |                |
| accout      | varchar(11)  | NO   |     | NULL                |                |
| password    | varchar(15)  | NO   |     | NULL                |                |
| email       | varchar(255) | YES  |     | NULL                |                |
| create_time | datetime     | YES  |     | current_timestamp() |                |
+-------------+--------------+------+-----+---------------------+----------------+

删除表：
mysql> DROP TABLE user
    -> ;
Query OK, 0 rows affected (0.03 sec)

mysql> SHOW TABLES;
Empty set (0.00 sec)
"""
# 数据操作
"""
插入数据：
mysql> INSERT INTO user(user_name,user_id,accout,password,email)
    -> VALUE("李四",2,"lisi2020777","wwwww","ccc@outlook.com")
    -> ;
Query OK, 1 row affected (0.02 sec)
"""

"""
查数据：
mysql> SELECT * FROM user
    -> ;
+----+--------------+---------+-------------+---------------+----------------------+---------------------+
| id | user_name    | user_id | accout      | password      | email                | create_time         |
+----+--------------+---------+-------------+---------------+----------------------+---------------------+
|  1 | 张三         |       1 | zhangsan200 | qqqqq         | aaa@163.com          | 2026-11-26 10:08:33 |
|  2 | 李四         |       2 | lisi2020777 | wwwww         | ccc@outlook.com      | 2026-11-26 10:18:47 |
|  3 | 张三         |       1 | zhangsan200 | qqqqq         | aaa@163.com          | 2026-11-26 10:08:33 |
|  4 | 李四         |       2 | lisi2020777 | wwwww         | ccc@outlook.com      | 2026-11-26 10:18:47 |
|  5 | 王五         |       3 | wangwu_888  | 123456        | NULL                 | 2026-11-27 09:00:00 |
|  6 | 赵六         |       4 | zhaoliu99   | password      | zhaoliu@qq.com       | 2026-11-27 14:30:15 |
|  7 | 欧阳娜娜     |       5 | ouyang_nana | nana123456789 | nana@gmail.com       | 2026-11-28 08:15:22 |
|  8 | 孙悟空       |       6 | sunwukong   | wukong666     | swk@163.com          | 2026-11-28 11:45:00 |
|  9 | Alice        |       7 | alice_in_wo | alicepass     | NULL                 | 2026-11-29 16:20:10 |
| 10 | Bob          |       8 | bob_builder | bob2026       | bob@outlook.com      | 2026-11-29 18:00:00 |
| 11 | 周杰伦       |       9 | jay_chou    | jaychou1      | jay.chou@foxmail.com | 2026-11-25 10:00:00 |
| 12 | 林俊杰       |      10 | jj_lin      | jj_lin2026    | jj@qq.com            | 2026-11-25 22:30:45 |
+----+--------------+---------+-------------+---------------+----------------------+---------------------+
12 rows in set (0.00 sec)

WHERE查id大于等于6的数据：
mysql> SELECT user_name FROM user WHERE id>=6;
+--------------+
| user_name    |
+--------------+
| 赵六         |
| 欧阳娜娜     |
| 孙悟空       |
| Alice        |
| Bob          |
| 周杰伦       |
| 林俊杰       |
+--------------+
7 rows in set (0.00 sec)

WHERE查id大于等于6的数据并ORDER BY逆序排序：
mysql> SELECT * FROM user WHERE id>=6 ORDER BY id DESC;
+----+--------------+---------+-------------+---------------+----------------------+---------------------+
| id | user_name    | user_id | accout      | password      | email                | create_time         |
+----+--------------+---------+-------------+---------------+----------------------+---------------------+
| 12 | 林俊杰       |      10 | jj_lin      | jj_lin2026    | jj@qq.com            | 2026-11-25 22:30:45 |
| 11 | 周杰伦       |       9 | jay_chou    | jaychou1      | jay.chou@foxmail.com | 2026-11-25 10:00:00 |
| 10 | Bob          |       8 | bob_builder | bob2026       | bob@outlook.com      | 2026-11-29 18:00:00 |
|  9 | Alice        |       7 | alice_in_wo | alicepass     | NULL                 | 2026-11-29 16:20:10 |
|  8 | 孙悟空       |       6 | sunwukong   | wukong666     | swk@163.com          | 2026-11-28 11:45:00 |
|  7 | 欧阳娜娜     |       5 | ouyang_nana | nana123456789 | nana@gmail.com       | 2026-11-28 08:15:22 |
|  6 | 赵六         |       4 | zhaoliu99   | password      | zhaoliu@qq.com       | 2026-11-27 14:30:15 |
+----+--------------+---------+-------------+---------------+----------------------+---------------------+
7 rows in set (0.00 sec)

WHERE查id大于等于6的数据并ORDER BY逆序排序后LIMIT获取前三条数据：
mysql> SELECT * FROM user WHERE id>=6 ORDER BY id DESC LIMIT 3;
+----+-----------+---------+-------------+------------+----------------------+---------------------+
| id | user_name | user_id | accout      | password   | email                | create_time         |
+----+-----------+---------+-------------+------------+----------------------+---------------------+
| 12 | 林俊杰    |      10 | jj_lin      | jj_lin2026 | jj@qq.com            | 2026-11-25 22:30:45 |
| 11 | 周杰伦    |       9 | jay_chou    | jaychou1   | jay.chou@foxmail.com | 2026-11-25 10:00:00 |
| 10 | Bob       |       8 | bob_builder | bob2026    | bob@outlook.com      | 2026-11-29 18:00:00 |
+----+-----------+---------+-------------+------------+----------------------+---------------------+
3 rows in set (0.00 sec)
"""

"""
修改id大于11的用户名字为已注销：
mysql> UPDATE user SET user_name="已注销" WHERE id>11;
Query OK, 1 row affected (0.02 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> SELECT * FROM user
    -> ;
+----+--------------+---------+-------------+---------------+----------------------+---------------------+
| id | user_name    | user_id | accout      | password      | email                | create_time         |
+----+--------------+---------+-------------+---------------+----------------------+---------------------+
|  1 | 张三         |       1 | zhangsan200 | qqqqq         | aaa@163.com          | 2026-11-26 10:08:33 |
|  2 | 李四         |       2 | lisi2020777 | wwwww         | ccc@outlook.com      | 2026-11-26 10:18:47 |
|  3 | 张三         |       1 | zhangsan200 | qqqqq         | aaa@163.com          | 2026-11-26 10:08:33 |
|  4 | 李四         |       2 | lisi2020777 | wwwww         | ccc@outlook.com      | 2026-11-26 10:18:47 |
|  5 | 王五         |       3 | wangwu_888  | 123456        | NULL                 | 2026-11-27 09:00:00 |
|  6 | 赵六         |       4 | zhaoliu99   | password      | zhaoliu@qq.com       | 2026-11-27 14:30:15 |
|  7 | 欧阳娜娜     |       5 | ouyang_nana | nana123456789 | nana@gmail.com       | 2026-11-28 08:15:22 |
|  8 | 孙悟空       |       6 | sunwukong   | wukong666     | swk@163.com          | 2026-11-28 11:45:00 |
|  9 | Alice        |       7 | alice_in_wo | alicepass     | NULL                 | 2026-11-29 16:20:10 |
| 10 | Bob          |       8 | bob_builder | bob2026       | bob@outlook.com      | 2026-11-29 18:00:00 |
| 11 | 周杰伦       |       9 | jay_chou    | jaychou1      | jay.chou@foxmail.com | 2026-11-25 10:00:00 |
| 12 | 已注销       |      10 | jj_lin      | jj_lin2026    | jj@qq.com            | 2026-11-25 22:30:45 |
+----+--------------+---------+-------------+---------------+----------------------+---------------------+
12 rows in set (0.00 sec)
"""

"""
删除已注销的用户：
mysql> DELETE FROM user WHERE user_name="已注销";
Query OK, 1 row affected (0.02 sec)

mysql> SELECT * FROM user
    -> ;
+----+--------------+---------+-------------+---------------+----------------------+---------------------+
| id | user_name    | user_id | accout      | password      | email                | create_time         |
+----+--------------+---------+-------------+---------------+----------------------+---------------------+
|  1 | 张三         |       1 | zhangsan200 | qqqqq         | aaa@163.com          | 2026-11-26 10:08:33 |
|  2 | 李四         |       2 | lisi2020777 | wwwww         | ccc@outlook.com      | 2026-11-26 10:18:47 |
|  3 | 张三         |       1 | zhangsan200 | qqqqq         | aaa@163.com          | 2026-11-26 10:08:33 |
|  4 | 李四         |       2 | lisi2020777 | wwwww         | ccc@outlook.com      | 2026-11-26 10:18:47 |
|  5 | 王五         |       3 | wangwu_888  | 123456        | NULL                 | 2026-11-27 09:00:00 |
|  6 | 赵六         |       4 | zhaoliu99   | password      | zhaoliu@qq.com       | 2026-11-27 14:30:15 |
|  7 | 欧阳娜娜     |       5 | ouyang_nana | nana123456789 | nana@gmail.com       | 2026-11-28 08:15:22 |
|  8 | 孙悟空       |       6 | sunwukong   | wukong666     | swk@163.com          | 2026-11-28 11:45:00 |
|  9 | Alice        |       7 | alice_in_wo | alicepass     | NULL                 | 2026-11-29 16:20:10 |
| 10 | Bob          |       8 | bob_builder | bob2026       | bob@outlook.com      | 2026-11-29 18:00:00 |
| 11 | 周杰伦       |       9 | jay_chou    | jaychou1      | jay.chou@foxmail.com | 2026-11-25 10:00:00 |
+----+--------------+---------+-------------+---------------+----------------------+---------------------+
11 rows in set (0.00 sec)
"""
# 聚合函数
"""
使用COUNT查看表的行数：
mysql> SELECT COUNT(*) FROM user
    -> ；
    -> ;
+----------+
| COUNT(*) |
+----------+
|       11 |
+----------+
1 row in set (0.00 sec)
"""