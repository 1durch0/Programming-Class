# Log Analysis Report

## Summary
- **Total Log Entries:** 68
- **INFO Entries:** 2
- **WARNING Entries:** 61
- **ERROR Entries:** 5

## Security Issues
- **Forbidden Access:** 23 occurrences
- **SQL Injection:** 20 occurrences
- **Brute Force:** 18 occurrences

### Details of Security Issues
- **Timestamp:** 2025-11-20 12:01:01,201
  - **Type:** Forbidden Access
  - **IP Address:** 192.168.1.44
  - **Log Message:** Forbidden access attempt: 192.168.1.44 -> /admin

- **Timestamp:** 2025-11-20 12:01:01,202
  - **Type:** SQL Injection
  - **IP Address:** 88.23.91.14
  - **Log Message:** Potential SQL injection: 88.23.91.14 -> /login?user=admin'--

- **Timestamp:** 2025-11-20 12:01:01,303
  - **Type:** Brute Force
  - **IP Address:** 10.0.0.15
  - **Log Message:** Brute force attempt from 10.0.0.15 - 3 failed attempts

- **Timestamp:** 2025-11-20 12:01:01,401
  - **Type:** Forbidden Access
  - **IP Address:** 10.0.0.22
  - **Log Message:** Forbidden access attempt: 10.0.0.22 -> /etc/passwd

- **Timestamp:** 2025-11-20 12:01:01,501
  - **Type:** SQL Injection
  - **IP Address:** 193.14.55.21
  - **Log Message:** Potential SQL injection: 193.14.55.21 -> /products?id=4 UNION SELECT *

- **Timestamp:** 2025-11-20 12:01:01,601
  - **Type:** Forbidden Access
  - **IP Address:** 172.16.8.77
  - **Log Message:** Forbidden access attempt: 172.16.8.77 -> /root

- **Timestamp:** 2025-11-20 12:01:01,701
  - **Type:** Brute Force
  - **IP Address:** 10.0.0.15
  - **Log Message:** Brute force attempt from 10.0.0.15 - 4 failed attempts

- **Timestamp:** 2025-11-20 12:01:01,801
  - **Type:** SQL Injection
  - **IP Address:** 66.92.13.5
  - **Log Message:** Potential SQL injection: 66.92.13.5 -> /search?q=DROP TABLE users;

- **Timestamp:** 2025-11-20 12:01:01,901
  - **Type:** Forbidden Access
  - **IP Address:** 212.88.99.18
  - **Log Message:** Forbidden access attempt: 212.88.99.18 -> /admin/config

- **Timestamp:** 2025-11-20 12:01:02,001
  - **Type:** Brute Force
  - **IP Address:** 172.20.10.5
  - **Log Message:** Brute force attempt from 172.20.10.5 - 3 failed attempts

- **Timestamp:** 2025-11-20 12:01:02,102
  - **Type:** Forbidden Access
  - **IP Address:** 8.8.8.8
  - **Log Message:** Forbidden access attempt: 8.8.8.8 -> /private

- **Timestamp:** 2025-11-20 12:01:02,203
  - **Type:** SQL Injection
  - **IP Address:** 77.54.33.10
  - **Log Message:** Potential SQL injection: 77.54.33.10 -> /login?password=admin;--

- **Timestamp:** 2025-11-20 12:01:02,304
  - **Type:** Brute Force
  - **IP Address:** 172.20.10.5
  - **Log Message:** Brute force attempt from 172.20.10.5 - 4 failed attempts

- **Timestamp:** 2025-11-20 12:01:02,405
  - **Type:** Forbidden Access
  - **IP Address:** 145.33.76.22
  - **Log Message:** Forbidden access attempt: 145.33.76.22 -> /hidden

- **Timestamp:** 2025-11-20 12:01:02,506
  - **Type:** SQL Injection
  - **IP Address:** 201.22.11.1
  - **Log Message:** Potential SQL injection: 201.22.11.1 -> /products?category=select * from

- **Timestamp:** 2025-11-20 12:01:02,607
  - **Type:** Forbidden Access
  - **IP Address:** 33.12.44.10
  - **Log Message:** Forbidden access attempt: 33.12.44.10 -> /superuser

- **Timestamp:** 2025-11-20 12:01:02,708
  - **Type:** Brute Force
  - **IP Address:** 10.1.1.99
  - **Log Message:** Brute force attempt from 10.1.1.99 - 3 failed attempts

- **Timestamp:** 2025-11-20 12:01:02,809
  - **Type:** SQL Injection
  - **IP Address:** 91.15.23.48
  - **Log Message:** Potential SQL injection: 91.15.23.48 -> /items?filter=union all select

- **Timestamp:** 2025-11-20 12:01:02,910
  - **Type:** Forbidden Access
  - **IP Address:** 100.100.100.10
  - **Log Message:** Forbidden access attempt: 100.100.100.10 -> /admin/backup

- **Timestamp:** 2025-11-20 12:01:03,011
  - **Type:** Brute Force
  - **IP Address:** 10.1.1.99
  - **Log Message:** Brute force attempt from 10.1.1.99 - 4 failed attempts

- **Timestamp:** 2025-11-20 12:01:03,112
  - **Type:** SQL Injection
  - **IP Address:** 44.22.11.9
  - **Log Message:** Potential SQL injection: 44.22.11.9 -> /login?return_to=--DROP

- **Timestamp:** 2025-11-20 12:01:03,213
  - **Type:** Forbidden Access
  - **IP Address:** 10.20.30.40
  - **Log Message:** Forbidden access attempt: 10.20.30.40 -> /secure

- **Timestamp:** 2025-11-20 12:01:03,314
  - **Type:** Brute Force
  - **IP Address:** 192.168.1.15
  - **Log Message:** Brute force attempt from 192.168.1.15 - 3 failed attempts

- **Timestamp:** 2025-11-20 12:01:03,415
  - **Type:** SQL Injection
  - **IP Address:** 201.8.77.9
  - **Log Message:** Potential SQL injection: 201.8.77.9 -> /query?name=insert into users

- **Timestamp:** 2025-11-20 12:01:03,516
  - **Type:** Forbidden Access
  - **IP Address:** 55.44.33.22
  - **Log Message:** Forbidden access attempt: 55.44.33.22 -> /hidden/console

- **Timestamp:** 2025-11-20 12:01:03,617
  - **Type:** Brute Force
  - **IP Address:** 192.168.1.15
  - **Log Message:** Brute force attempt from 192.168.1.15 - 4 failed attempts

- **Timestamp:** 2025-11-20 12:01:03,718
  - **Type:** SQL Injection
  - **IP Address:** 88.77.66.55
  - **Log Message:** Potential SQL injection: 88.77.66.55 -> /test?value=select

- **Timestamp:** 2025-11-20 12:01:03,819
  - **Type:** Forbidden Access
  - **IP Address:** 9.9.9.9
  - **Log Message:** Forbidden access attempt: 9.9.9.9 -> /root/admin

- **Timestamp:** 2025-11-20 12:01:03,920
  - **Type:** Brute Force
  - **IP Address:** 192.168.2.22
  - **Log Message:** Brute force attempt from 192.168.2.22 - 3 failed attempts

- **Timestamp:** 2025-11-20 12:01:04,021
  - **Type:** SQL Injection
  - **IP Address:** 155.22.33.44
  - **Log Message:** Potential SQL injection: 155.22.33.44 -> /login?attempt=admin' OR 1=1

- **Timestamp:** 2025-11-20 12:01:04,122
  - **Type:** Forbidden Access
  - **IP Address:** 22.33.44.55
  - **Log Message:** Forbidden access attempt: 22.33.44.55 -> /settings/system

- **Timestamp:** 2025-11-20 12:01:04,223
  - **Type:** Brute Force
  - **IP Address:** 192.168.2.22
  - **Log Message:** Brute force attempt from 192.168.2.22 - 4 failed attempts

- **Timestamp:** 2025-11-20 12:01:04,324
  - **Type:** SQL Injection
  - **IP Address:** 99.88.77.66
  - **Log Message:** Potential SQL injection: 99.88.77.66 -> /site?id=union

- **Timestamp:** 2025-11-20 12:01:04,425
  - **Type:** Forbidden Access
  - **IP Address:** 111.111.111.111
  - **Log Message:** Forbidden access attempt: 111.111.111.111 -> /secure/config

- **Timestamp:** 2025-11-20 12:01:04,526
  - **Type:** Brute Force
  - **IP Address:** 172.30.50.25
  - **Log Message:** Brute force attempt from 172.30.50.25 - 3 failed attempts

- **Timestamp:** 2025-11-20 12:01:04,627
  - **Type:** SQL Injection
  - **IP Address:** 233.12.55.9
  - **Log Message:** Potential SQL injection: 233.12.55.9 -> /login?password=';DROP

- **Timestamp:** 2025-11-20 12:01:04,728
  - **Type:** Forbidden Access
  - **IP Address:** 98.76.54.32
  - **Log Message:** Forbidden access attempt: 98.76.54.32 -> /private/system

- **Timestamp:** 2025-11-20 12:01:04,829
  - **Type:** Brute Force
  - **IP Address:** 172.30.50.25
  - **Log Message:** Brute force attempt from 172.30.50.25 - 4 failed attempts

- **Timestamp:** 2025-11-20 12:01:04,930
  - **Type:** SQL Injection
  - **IP Address:** 46.29.10.1
  - **Log Message:** Potential SQL injection: 46.29.10.1 -> /items?filter=union--

- **Timestamp:** 2025-11-20 12:01:05,031
  - **Type:** Forbidden Access
  - **IP Address:** 123.45.67.89
  - **Log Message:** Forbidden access attempt: 123.45.67.89 -> /root/admin

- **Timestamp:** 2025-11-20 12:01:05,132
  - **Type:** Brute Force
  - **IP Address:** 172.30.99.100
  - **Log Message:** Brute force attempt from 172.30.99.100 - 3 failed attempts

- **Timestamp:** 2025-11-20 12:01:05,233
  - **Type:** SQL Injection
  - **IP Address:** 44.10.21.76
  - **Log Message:** Potential SQL injection: 44.10.21.76 -> /query?text=drop table

- **Timestamp:** 2025-11-20 12:01:05,334
  - **Type:** Forbidden Access
  - **IP Address:** 200.10.10.20
  - **Log Message:** Forbidden access attempt: 200.10.10.20 -> /admin/settings

- **Timestamp:** 2025-11-20 12:01:05,435
  - **Type:** Brute Force
  - **IP Address:** 172.30.99.100
  - **Log Message:** Brute force attempt from 172.30.99.100 - 4 failed attempts

- **Timestamp:** 2025-11-20 12:01:05,536
  - **Type:** SQL Injection
  - **IP Address:** 177.88.99.100
  - **Log Message:** Potential SQL injection: 177.88.99.100 -> /api?cmd=insert into

- **Timestamp:** 2025-11-20 12:01:05,637
  - **Type:** Forbidden Access
  - **IP Address:** 150.130.120.110
  - **Log Message:** Forbidden access attempt: 150.130.120.110 -> /root/files

- **Timestamp:** 2025-11-20 12:01:05,738
  - **Type:** Brute Force
  - **IP Address:** 192.168.100.50
  - **Log Message:** Brute force attempt from 192.168.100.50 - 3 failed attempts

- **Timestamp:** 2025-11-20 12:01:05,839
  - **Type:** SQL Injection
  - **IP Address:** 144.33.55.10
  - **Log Message:** Potential SQL injection: 144.33.55.10 -> /q?id=select

- **Timestamp:** 2025-11-20 12:01:05,940
  - **Type:** Forbidden Access
  - **IP Address:** 10.10.10.10
  - **Log Message:** Forbidden access attempt: 10.10.10.10 -> /etc/shadow

- **Timestamp:** 2025-11-20 12:01:06,041
  - **Type:** Brute Force
  - **IP Address:** 192.168.100.50
  - **Log Message:** Brute force attempt from 192.168.100.50 - 4 failed attempts

- **Timestamp:** 2025-11-20 12:01:06,142
  - **Type:** SQL Injection
  - **IP Address:** 199.22.11.33
  - **Log Message:** Potential SQL injection: 199.22.11.33 -> /test?cmd=union select

- **Timestamp:** 2025-11-20 12:01:06,243
  - **Type:** Forbidden Access
  - **IP Address:** 155.155.155.155
  - **Log Message:** Forbidden access attempt: 155.155.155.155 -> /hidden/key

- **Timestamp:** 2025-11-20 12:01:06,849
  - **Type:** Forbidden Access
  - **IP Address:** 172.16.0.22
  - **Log Message:** Forbidden access attempt: 172.16.0.22 -> /root/private

- **Timestamp:** 2025-11-20 12:01:06,950
  - **Type:** SQL Injection
  - **IP Address:** 88.22.11.33
  - **Log Message:** Potential SQL injection: 88.22.11.33 -> /data?x=select 1

- **Timestamp:** 2025-11-20 12:01:07,051
  - **Type:** Brute Force
  - **IP Address:** 192.168.50.11
  - **Log Message:** Brute force attempt from 192.168.50.11 - 3 failed attempts

- **Timestamp:** 2025-11-20 12:01:07,152
  - **Type:** Forbidden Access
  - **IP Address:** 90.12.33.44
  - **Log Message:** Forbidden access attempt: 90.12.33.44 -> /secure/settings

- **Timestamp:** 2025-11-20 12:01:07,253
  - **Type:** SQL Injection
  - **IP Address:** 101.55.77.99
  - **Log Message:** Potential SQL injection: 101.55.77.99 -> /filter?q=union select

- **Timestamp:** 2025-11-20 12:01:07,354
  - **Type:** Brute Force
  - **IP Address:** 192.168.50.11
  - **Log Message:** Brute force attempt from 192.168.50.11 - 4 failed attempts

- **Timestamp:** 2025-11-20 12:01:07,455
  - **Type:** Forbidden Access
  - **IP Address:** 200.200.200.200
  - **Log Message:** Forbidden access attempt: 200.200.200.200 -> /admin/root

- **Timestamp:** 2025-11-20 12:01:07,556
  - **Type:** SQL Injection
  - **IP Address:** 170.88.12.13
  - **Log Message:** Potential SQL injection: 170.88.12.13 -> /api?search=drop database

- **Timestamp:** 2025-11-20 12:01:07,657
  - **Type:** Forbidden Access
  - **IP Address:** 45.12.23.34
  - **Log Message:** Forbidden access attempt: 45.12.23.34 -> /root/bin


## Errors
- Line 121: Error processing - invalid literal for int() with base 10: '-'
- Line 122: Error processing - not enough values to unpack
- Line 123: Error processing - unexpected end of string
- Line 124: Error processing - list index out of range
- Line 125: Error processing - could not convert string to float: 'abc'
