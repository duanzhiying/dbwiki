<!--
doc_type: enterprise_case
title: 电商平台千万级数据查询优化
concepts: [分页优化, 索引, 查询缓存]
difficulty: 0.8
category: 性能优化
author: 李工程师
date: 2025-09-01
-->

# 电商平台查询优化实战

## 业务场景
商品列表页在千万级数据量下的分页查询性能优化...

## 优化方案
```sql
-- 优化前 (性能低下)
SELECT * FROM products LIMIT 10 OFFSET 10000;

-- 优化后 (性能提升50倍)
SELECT * FROM products WHERE id > 10000 LIMIT 10;
```
