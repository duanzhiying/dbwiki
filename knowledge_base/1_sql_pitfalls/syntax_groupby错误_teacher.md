<!--
doc_type: pitfall
title: GROUP BY子句使用错误
concepts: [group by, 聚合函数, sql错误]
difficulty: 0.6
category: 语法错误
author: 段老师
date: 2025-09-01
-->

# GROUP BY子句使用错误

## ❌ 错误代码
```sql
SELECT department, COUNT(*) FROM students;
```

## ✅ 正确写法
```sql
SELECT department, COUNT(*) AS count 
FROM students 
GROUP BY department;
```

## 💡 原因分析
在包含聚合函数的查询中，所有非聚合列都必须出现在GROUP BY子句中。
