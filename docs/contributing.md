---
title: 贡献指南
---

## 为什么参与共建

数据库课程实验资源平台（dbwiki）面向师生共建，目标是沉淀高质量、可复用、可教学落地的实验教学内容。无论你是学生、助教还是教师，都可以参与贡献：纠正文档、完善案例、补充实验示范、撰写避坑指南等。

本指南基于项目《项目规范与实施计划》，对贡献流程、命名规范、元数据、质量标准与审核机制做了可操作的说明。

---

## 快速开始

1. Fork 仓库并创建分支：`feat/your-topic` 或 `docs/your-topic`
2. 在 `docs/` 下合适的目录新建 Markdown 文档（见“目录与命名规范”）
3. 在文档顶部补充“元数据头”（可复制下方模板）
4. 按“内容质量标准”完善结构与示例
5. 更新 `mkdocs.yml` 的 `nav` 导航条目
6. 本地预览：`mkdocs serve`，无误后提交 PR
7. 等待助教与教师的三级审核并合并发布

---

## 目录与命名规范

平台文档位于 `docs/` 目录，按类别组织：

```
docs/
├── 1_sql_pitfalls/          # 错误SQL点评
├── 2_enterprise_cases/      # 企业真实案例
├── 3_avoidance_guides/      # 避坑指南
├── 4_excellent_labs/        # 优秀实验示范
└── 5_course_designs/        # 课设案例
```

图片等静态资源放置于 `docs/assets/images/` 对应子目录，引用时使用相对路径。

---

## 元数据模板与说明

每个文档必须在开头包含以下元数据，用于构建与质量检查：

```yaml
---
doc_type: [pitfall|enterprise_case|avoidance_guide|lab_demo|course_design]
title: 简明标题
concepts: [概念1, 概念2, 概念3]
difficulty: [0.3|0.6|0.9]  # 0.3=基础, 0.6=中级, 0.9=高级
prerequisites: [先修知识1, 先修知识2]
author: 作者姓名
date: YYYY-MM-DD
tags: [标签1, 标签2, 标签3]
status: [draft|review|approved]
---
```

- 必填字段：`doc_type`、`title`、`concepts`、`difficulty`、`author`、`date`
- 建议补充：`prerequisites`、`tags`，便于检索与教学编排
- `status` 用于标注进度：`draft`（草稿）、`review`（审核中）、`approved`（已批准）

---

## 内容质量标准（按类别）

- 错误SQL点评
    - 必含：错误代码、正确代码、错误分析、学习要点、扩展练习
- 企业案例
    - 必含：业务背景、技术挑战、解决方案、效果评估、经验总结
- 避坑指南
    - 必含：问题描述、原因分析、预防措施、最佳实践、工具方法
- 实验示范
    - 推荐：实验目标、环境准备、步骤演示、验证方式、常见问题
- 课设案例
    - 推荐：需求分析、数据建模、关键功能、技术选型、演示与评估

文档层级建议：`# 标题` → `## 一级小节` → `### 二级小节`。SQL 代码块请使用三引号并标注语言：

```sql
SELECT dept_no, COUNT(*) 
FROM employees 
GROUP BY dept_no;
```

---

## 协作与审核流程

1. Fork 仓库 → 创建分支（`feat/*` 或 `docs/*`）
2. 新增/修改文档并完善元数据
3. 本地预览并自检（见“提交前自检清单”）
4. 提交 PR，选择对应类别标签
5. 三级审核：
    - 学生自检：命名、元数据、结构、语法、原创性
    - 助教审核：技术准确性、格式规范、可执行性、学习价值
    - 教师审核：教学价值、学术正确性、创新性、最终确认

---

## 提交前自检清单

- [ ] 文件命名符合目录与命名规范
- [ ] 顶部元数据完整（至少含：`doc_type/title/concepts/difficulty/author/date`）
- [ ] 文档层级与格式规范统一
- [ ] SQL/代码块语言标注正确
- [ ] 图片与链接可访问
- [ ] 内容结构齐全、示例准确、结论可靠

---

## 导航与构建

新增页面必须加入 `mkdocs.yml` 的 `nav`，中文标题与文件路径一致。例如：

```yaml
nav:
  - 实验示范:
    - 基础查询: 4_excellent_labs/lab1_基础查询.md
    - 触发器与存储过程：教材案例的MySQL实现: 4_excellent_labs/触发器与存储过程教材案例MySQL实现.md
```

本地预览与构建：

```bash
# 预览
mkdocs serve

# 生成静态站点
mkdocs build --clean
```

---

## 贡献示例模板（建议复制使用）

````markdown
---
doc_type: pitfall
title: GROUP BY 子句使用错误
concepts: [group by, 聚合函数, sql错误]
difficulty: 0.3
prerequisites: [基础SQL, 聚合函数]
author: your_name
date: 2025-01-01
tags: [语法错误, 常见问题]
status: review
---

# GROUP BY 子句使用错误

## 错误代码
```sql
SELECT dept_no, emp_no, COUNT(*) FROM employees GROUP BY dept_no;
```

## 正确代码
```sql
SELECT dept_no, COUNT(*) FROM employees GROUP BY dept_no;
```

## 错误分析
说明原因……

## 学习要点
- 要点1
- 要点2

## 扩展练习
给出练习题或数据集链接……
````

---

## 行为准则与署名

- 尊重原创，严禁抄袭；引用内容请标注来源
- 教学友好，行文清晰，适度留白，便于课堂与自学
- 在元数据 `author` 字段保留署名；多人协作可写多人姓名

---

如需进一步了解项目规范与实施细节，请参考根目录的《项目规范与实施计划》文档。


