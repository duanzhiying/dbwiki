---
doc_type: enterprise_case
title: 电商平台数据库查询优化实战
concepts: [查询优化, 索引, 分页查询, 性能优化]
difficulty: 0.8
prerequisites: [SQL基础, 索引原理, 查询优化]
author: teacher
date: 2024-12-19
tags: [企业案例, 查询优化, 电商, 性能]
status: approved
---

# 电商平台数据库查询优化实战
> 作者：teacher


## 📊 业务场景
某电商平台商品列表页在高峰期响应缓慢，用户体验差。需要优化分页查询性能。

## 🔍 问题分析
### 原始查询
```sql
-- 问题查询：使用OFFSET进行分页
SELECT * FROM products 
WHERE category_id = 5 
ORDER BY created_at DESC 
LIMIT 20 OFFSET 1000;
```

### 性能问题
1. **OFFSET性能差**: 需要跳过1000条记录，性能随偏移量线性下降
2. **索引利用不充分**: 没有合适的复合索引
3. **内存消耗大**: 需要加载大量不需要的数据

## 🔧 优化方案

### 1. 使用游标分页
```sql
-- 优化后：使用ID游标分页
SELECT * FROM products 
WHERE category_id = 5 AND id > 1000 
ORDER BY id DESC 
LIMIT 20;
```

### 2. 创建复合索引
```sql
-- 为查询创建复合索引
CREATE INDEX idx_products_category_id_created_at 
ON products(category_id, created_at DESC, id);
```

### 3. 查询重写
```sql
-- 进一步优化：只查询必要字段
SELECT id, title, price, image_url 
FROM products 
WHERE category_id = 5 AND id > 1000 
ORDER BY id DESC 
LIMIT 20;
```

## 📈 优化效果
- **响应时间**: 从2.5秒降低到50毫秒
- **并发能力**: 支持1000+并发用户
- **资源消耗**: CPU使用率降低60%

## 💡 关键经验
1. **避免大偏移量**: 使用游标分页替代OFFSET
2. **合理设计索引**: 根据查询模式创建复合索引
3. **查询字段优化**: 只查询必要的字段
4. **监控和测试**: 建立性能监控体系

## 扩展思考
- 如何处理深度分页问题？
- 如何设计高效的搜索功能？
- 如何平衡查询性能和存储成本？
