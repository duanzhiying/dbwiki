---
doc_type: lab_demo
title: 实验示范：基础查询
concepts: [SELECT查询, WHERE条件, ORDER BY排序, 聚合函数]
difficulty: 0.3
prerequisites: [SQL基础语法]
author: student
date: 2024-12-19
tags: [基础查询, 实验示范]
status: approved
---

# 实验示范：基础查询（学生版）

## 实验目标
掌握基本的SQL查询操作，包括数据筛选、排序和聚合统计。

## 实验环境
- 数据库：MySQL 8.0
- 测试数据：学生信息管理系统

## 实验内容

### 1. 基本查询
```sql
-- 查询所有学生信息
SELECT * FROM students;

-- 查询指定字段
SELECT student_id, name, major FROM students;
```

### 2. 条件查询
```sql
-- 查询计算机专业的学生
SELECT * FROM students WHERE major = '计算机科学与技术';

-- 查询年龄大于20的学生
SELECT * FROM students WHERE age > 20;

-- 复合条件查询
SELECT * FROM students 
WHERE major = '计算机科学与技术' AND age > 20;
```

### 3. 排序查询
```sql
-- 按年龄升序排列
SELECT * FROM students ORDER BY age ASC;

-- 按专业和年龄排序
SELECT * FROM students 
ORDER BY major, age DESC;
```

### 4. 聚合统计
```sql
-- 统计学生总数
SELECT COUNT(*) as total_students FROM students;

-- 按专业统计学生人数
SELECT major, COUNT(*) as count 
FROM students 
GROUP BY major;

-- 查询平均年龄
SELECT AVG(age) as avg_age FROM students;
```

## 实验要求
1. 完成所有查询语句的编写
2. 验证查询结果的正确性
3. 尝试修改查询条件，观察结果变化
4. 记录实验过程中遇到的问题

## 思考题
1. 如何查询年龄在18-25之间的学生？
2. 如何统计每个专业的平均年龄？
3. 如何查询成绩最高的前5名学生？

## 实验总结
通过本次实验，我掌握了：
- 基本的SELECT查询语法
- WHERE条件的使用方法
- ORDER BY排序的应用
- 聚合函数的基本用法

## 扩展练习
- 尝试使用LIMIT限制查询结果数量
- 学习使用DISTINCT去除重复数据
- 练习使用LIKE进行模糊查询
