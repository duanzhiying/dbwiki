---
doc_type: pitfall
title: GROUP BY子句使用错误
concepts: [group by, 聚合函数, sql错误, 语法错误]
difficulty: 0.6
prerequisites: [基础SQL, 聚合函数]
author: teacher
date: 2024-12-19
tags: [语法错误, 常见问题, group by]
status: approved
---

# GROUP BY子句使用错误

## ❌ 错误代码示例
```sql
SELECT department, COUNT(*) FROM students;
```

## ✅ 正确写法
```sql
SELECT department, COUNT(*) AS count 
FROM students 
GROUP BY department;
```

## 💡 解析说明
在包含聚合函数的查询中，所有非聚合列都必须出现在GROUP BY子句中。

## 错误原因分析
1. **语法规则**: SQL标准要求，当使用聚合函数时，SELECT子句中的非聚合列必须出现在GROUP BY子句中
2. **数据库实现**: 不同数据库对此规则的处理可能不同，但都应该遵循标准
3. **常见场景**: 在统计查询中经常出现此类错误

## 学习要点
- 理解聚合函数的工作原理
- 掌握GROUP BY子句的使用规则
- 学会识别和避免此类语法错误

## 扩展思考
- 如何设计复杂的统计查询？
- 聚合函数还有哪些常见用法？
- 如何优化包含GROUP BY的查询性能？
