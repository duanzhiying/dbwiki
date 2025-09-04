---
doc_type: course_design
title: 课程设计：图书管理系统
concepts: [数据库设计, E-R建模, 表结构设计, 业务逻辑]
difficulty: 0.6
prerequisites: [数据库基础, SQL语法, 系统分析]
author: student
date: 2024-12-19
tags: [课程设计, 图书管理, 数据库应用]
status: approved
---

# 课程设计：图书管理系统（学生版）

## 项目概述
设计并实现一个完整的图书管理系统，包括图书信息管理、借阅管理、用户管理等功能。

## 需求分析

### 功能需求
1. **图书管理**
   - 图书信息的增删改查
   - 图书分类管理
   - 图书状态管理（在库/借出/维修）

2. **借阅管理**
   - 图书借阅功能
   - 图书归还功能
   - 借阅记录查询
   - 逾期提醒

3. **用户管理**
   - 用户注册和登录
   - 用户信息管理
   - 借阅权限控制

### 非功能需求
- 支持并发访问
- 数据完整性保证
- 系统响应时间 < 2秒
- 支持1000+用户同时使用

## 数据库设计

### E-R图设计
```
用户 (User)
├── 用户ID (主键)
├── 用户名
├── 密码
├── 邮箱
└── 借阅权限

图书 (Book)
├── 图书ID (主键)
├── 书名
├── 作者
├── 出版社
├── ISBN
├── 分类ID (外键)
└── 状态

借阅记录 (BorrowRecord)
├── 记录ID (主键)
├── 用户ID (外键)
├── 图书ID (外键)
├── 借阅时间
├── 应还时间
└── 实际归还时间
```

### 表结构设计
```sql
-- 用户表
CREATE TABLE users (
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(100) NOT NULL,
    email VARCHAR(100),
    borrow_limit INT DEFAULT 5,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 图书分类表
CREATE TABLE categories (
    category_id INT PRIMARY KEY AUTO_INCREMENT,
    category_name VARCHAR(50) NOT NULL,
    description TEXT
);

-- 图书表
CREATE TABLE books (
    book_id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(200) NOT NULL,
    author VARCHAR(100),
    publisher VARCHAR(100),
    isbn VARCHAR(20),
    category_id INT,
    status ENUM('available', 'borrowed', 'maintenance') DEFAULT 'available',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES categories(category_id)
);

-- 借阅记录表
CREATE TABLE borrow_records (
    record_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT NOT NULL,
    book_id INT NOT NULL,
    borrow_date DATE NOT NULL,
    due_date DATE NOT NULL,
    return_date DATE NULL,
    status ENUM('active', 'returned', 'overdue') DEFAULT 'active',
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (book_id) REFERENCES books(book_id)
);
```

## 核心功能实现

### 1. 图书借阅
```sql
-- 借阅图书
INSERT INTO borrow_records (user_id, book_id, borrow_date, due_date)
VALUES (1, 101, CURDATE(), DATE_ADD(CURDATE(), INTERVAL 30 DAY));

-- 更新图书状态
UPDATE books SET status = 'borrowed' WHERE book_id = 101;
```

### 2. 图书归还
```sql
-- 归还图书
UPDATE borrow_records 
SET return_date = CURDATE(), status = 'returned'
WHERE record_id = 1;

-- 更新图书状态
UPDATE books SET status = 'available' WHERE book_id = 101;
```

### 3. 逾期检查
```sql
-- 查询逾期记录
SELECT br.*, u.username, b.title
FROM borrow_records br
JOIN users u ON br.user_id = u.user_id
JOIN books b ON br.book_id = b.book_id
WHERE br.due_date < CURDATE() AND br.status = 'active';
```

## 系统优化

### 索引设计
```sql
-- 为常用查询字段创建索引
CREATE INDEX idx_books_title ON books(title);
CREATE INDEX idx_books_author ON books(author);
CREATE INDEX idx_borrow_records_user ON borrow_records(user_id);
CREATE INDEX idx_borrow_records_due_date ON borrow_records(due_date);
```

### 性能优化
1. 使用合适的索引
2. 优化查询语句
3. 实现分页查询
4. 使用连接池

## 测试用例

### 功能测试
1. 用户注册和登录
2. 图书信息的增删改查
3. 图书借阅和归还
4. 借阅记录查询

### 性能测试
1. 并发借阅测试
2. 大数据量查询测试
3. 系统响应时间测试

## 项目总结

### 技术收获
- 掌握了完整的数据库设计流程
- 学会了E-R建模和表结构设计
- 理解了数据库约束和索引的作用
- 掌握了复杂SQL查询的编写

### 项目亮点
- 完整的需求分析和系统设计
- 规范的数据库设计
- 完善的错误处理机制
- 良好的用户体验设计

## 扩展功能
- 图书推荐系统
- 用户借阅统计
- 图书评价系统
- 移动端支持
