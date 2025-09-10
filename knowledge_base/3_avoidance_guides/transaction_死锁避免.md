---
doc_type: avoidance_guide
title: 事务处理：死锁避免
concepts: [死锁, 事务, 锁机制, 并发控制]
difficulty: 0.8
prerequisites: [事务基础, 锁机制]
author: teacher
date: 2024-12-19
tags: [事务处理, 死锁, 并发控制]
status: approved
---

# 事务处理：死锁避免（教师版）
> 作者：teacher


## 问题描述
在高并发数据库系统中，死锁是常见的问题。当多个事务相互等待对方释放锁时，就会发生死锁，导致系统性能下降甚至服务中断。

## 死锁产生的原因
1. **资源竞争**: 多个事务同时访问相同的数据资源
2. **锁顺序不一致**: 不同事务以不同顺序获取锁
3. **长时间持有锁**: 事务执行时间过长，锁持有时间过久

## 预防策略

### 1. 资源有序分配
```sql
-- 错误示例：可能导致死锁
-- 事务A: 先锁用户表，再锁订单表
-- 事务B: 先锁订单表，再锁用户表

-- 正确做法：统一锁顺序
-- 所有事务都按相同顺序获取锁
BEGIN;
SELECT * FROM users WHERE id = 1 FOR UPDATE;
SELECT * FROM orders WHERE user_id = 1 FOR UPDATE;
COMMIT;
```

### 2. 设置锁超时
```sql
-- MySQL
SET innodb_lock_wait_timeout = 10;

-- PostgreSQL
SET lock_timeout = '10s';
```

### 3. 使用合适的隔离级别
```sql
-- 根据业务需求选择合适的隔离级别
-- READ COMMITTED: 减少锁持有时间
SET TRANSACTION ISOLATION LEVEL READ COMMITTED;
```

## 检测和解决

### 死锁检测
```sql
-- MySQL 查看死锁信息
SHOW ENGINE INNODB STATUS;

-- PostgreSQL 查看锁等待
SELECT * FROM pg_locks WHERE NOT granted;
```

### 死锁处理
1. **自动回滚**: 数据库自动选择一个事务进行回滚
2. **重试机制**: 应用层实现重试逻辑
3. **监控告警**: 建立死锁监控和告警机制

## 最佳实践
1. 保持事务简短
2. 按固定顺序访问资源
3. 使用合适的索引减少锁范围
4. 考虑使用乐观锁替代悲观锁
5. 建立完善的监控体系

## 扩展思考
- 如何设计重试机制？
- 乐观锁和悲观锁的适用场景？
- 如何监控数据库死锁情况？
