---
published: true
title: "[MS-SQL] Database별 커넥션 개수 확인"
categories:
  - Database
  - MS-SQL
date: 2019-10-04 18:12:00.000Z
---

```sql
SELECT 
    DB_NAME(dbid) as DBName, 
    COUNT(dbid) as NumberOfConnections,
    loginame as LoginName
FROM
    sys.sysprocesses
WHERE 
    dbid > 0
GROUP BY 
    dbid, loginame;
```