# 数据库课程实验资源平台 (dbwiki)

## 项目概述

**项目名称**: 数据库课程实验资源平台 (dbwiki)
**项目性质**: 师生共建的数据库实验课程教改项目成果展示平台
**技术架构**: MkDocs + Material主题 + RAG知识问答（规划中）
**部署方式**: Vercel静态部署
**代码管理**: GitCode主仓库 + Gitee/GitHub镜像

### 核心目标
1. **教学资源共建共享**: 建立标准化的数据库实验教学资源库
2. **质量管控体系**: 建立三级审核机制，确保内容质量
3. **知识问答系统**: 基于RAG技术实现智能问答（后续规划）
4. **教学融合**: 支持翻转课堂和微课教学

## 目录结构

```
dbwiki/
├── .github/            # GitHub Actions 工作流配置
├── docs/              # MkDocs 构建源目录（自动同步）
├── knowledge_base/    # 知识库源文件目录
│   ├── 1_sql_pitfalls/         # 错误SQL点评
│   ├── 2_enterprise_cases/     # 企业真实案例
│   ├── 3_avoidance_guides/     # 避坑指南
│   ├── 4_excellent_labs/       # 优秀实验示范
│   ├── 5_course_designs/       # 课设案例库
│   ├── assets/                 # 静态资源（图片等）
│   └── raw_docs/               # 原始文档（临时存储）
├── scripts/           # 工具脚本
│   ├── sync_docs.py            # 文档同步工具
│   ├── add_updated_date.py     # 添加更新时间字段
│   └── add_frontmatter_to_body.py # 添加正文前端信息
├── site/              # 构建输出目录
├── .gitignore         # Git忽略文件
├── mkdocs.yml         # MkDocs配置文件
├── requirements.txt   # 项目依赖
└── README.md          # 项目说明文档
```

## 技术栈

- **静态站点生成**: MkDocs
- **主题**: Material for MkDocs
- **Markdown扩展**: pymdown-extensions
- **构建工具**: Python 3.x
- **版本控制**: Git
- **部署平台**: Vercel

## 项目构造顺序

### 1. 环境准备

1. **安装Python 3.x**
   - 确保安装了Python 3.7或以上版本
   - 验证安装：`python --version`

2. **克隆项目**
   ```bash
   git clone https://gitcode.com/kidzying/dbwiki.git
   cd dbwiki
   ```

3. **安装依赖**
   ```bash
   pip install -r requirements.txt
   ```

### 2. 项目配置

1. **配置MkDocs**
   - 编辑 `mkdocs.yml` 文件，设置站点信息和导航结构
   - 导航结构会自动同步到网站菜单

2. **配置同步脚本**
   - 脚本 `scripts/sync_docs.py` 负责将 `knowledge_base` 中的内容同步到 `docs` 目录
   - 会自动进行文件命名规范检查和元数据验证

### 3. 内容管理

1. **创建文档**
   - 在 `knowledge_base` 对应目录中创建Markdown文档
   - 遵循命名规范：`类型_内容_作者.md`（如 `lab1_basic_query_student.md`）

2. **文档元数据**
   每个文档必须包含以下元数据：
   ```yaml
   ---
   doc_type: [pitfall|enterprise_case|avoidance_guide|lab_demo|course_design]
   title: 文档标题
   concepts: [相关概念1, 相关概念2]
   difficulty: [0.3|0.6|0.9]  # 0.3=基础, 0.6=中级, 0.9=高级
   author: 作者姓名
   date: YYYY-MM-DD
   tags: [标签1, 标签2]
   status: [draft|review|approved]
   updated: YYYY-MM-DD
   ---
   ```

3. **图片管理**
   - 图片存储在 `knowledge_base/assets/images/` 对应目录中
   - 使用相对路径引用：`../assets/images/目录/图片名.png`

### 4. 开发流程

1. **同步内容**
   ```bash
   python scripts/sync_docs.py
   ```

2. **本地预览**
   ```bash
   mkdocs serve
   ```
   - 访问：http://127.0.0.1:8000/dbwiki/

3. **构建网站**
   ```bash
   mkdocs build --clean
   ```

4. **提交更改**
   ```bash
   # 提交内容改动
   git add knowledge_base/ docs/ mkdocs.yml
   git commit -m "docs(knowledge_base): 描述你的更改"

   # 提交构建产物（若需）
   git add -f site
   git commit -m "build(site): 更新静态站点"

   # 推送更改
   git push origin main
   ```

## 部署方式

### Vercel部署（推荐）
1. 登录 Vercel 账号
2. 导入 GitCode 仓库
3. 配置构建命令：`mkdocs build --clean`
4. 配置输出目录：`site`
5. 部署完成后获取访问地址

### GitHub Pages部署
1. 启用 GitHub Actions
2. 配置 `.github/workflows/mkdocs-gh-pages.yml`
3. 推送更改后自动构建并部署

## 贡献指南

### 提交流程
1. Fork 仓库
2. 创建分支
3. 添加内容
4. 提交 PR
5. 助教审核
6. 教师审核
7. 合并发布

### 三级审核机制

#### 第一级：学生自检
- [ ] 文件命名符合规范
- [ ] 元数据完整填写
- [ ] 内容结构清晰
- [ ] SQL语法正确
- [ ] 无抄袭问题

#### 第二级：助教审核
- [ ] 技术内容准确性
- [ ] 文档格式规范
- [ ] 代码可执行性
- [ ] 学习价值评估

#### 第三级：教师审核
- [ ] 教学价值评估
- [ ] 学术正确性
- [ ] 内容创新性
- [ ] 最终质量确认

## 文档规范

### 命名规范

#### 1. 错误SQL点评 (1_sql_pitfalls/)
- **格式**: `类型_错误描述_作者.md`
- **示例**: `syntax_groupby错误_teacher.md`

#### 2. 企业案例 (2_enterprise_cases/)
- **格式**: `行业_案例描述_作者.md`
- **示例**: `ecommerce_查询优化_teacher.md`

#### 3. 避坑指南 (3_avoidance_guides/)
- **格式**: `主题_具体内容_作者.md`
- **示例**: `transaction_死锁避免_teacher.md`

#### 4. 实验示范 (4_excellent_labs/)
- **格式**: `lab编号_实验名称_作者.md`
- **示例**: `lab1_basic_query_student.md`

#### 5. 课设案例 (5_course_designs/)
- **格式**: `系统类型_系统名称_作者.md`
- **示例**: `library_管理系统_student.md`

### 内容标准

#### 1. 错误SQL点评标准
- **错误代码**: 提供真实的错误SQL示例
- **正确代码**: 提供修正后的正确SQL
- **错误分析**: 详细说明错误原因
- **学习要点**: 总结关键知识点
- **扩展思考**: 提供相关练习题

#### 2. 企业案例标准
- **业务背景**: 清晰描述业务场景
- **技术挑战**: 说明面临的技术问题
- **解决方案**: 详细的技术解决方案
- **效果评估**: 量化的改进效果
- **经验总结**: 可复用的经验教训

#### 3. 避坑指南标准
- **问题描述**: 清晰描述常见问题
- **原因分析**: 深入分析问题根因
- **预防措施**: 具体的预防方法
- **最佳实践**: 推荐的最佳实践
- **工具推荐**: 相关工具和方法

## 常见问题

### 1. 同步失败
- **原因**: 文件命名不符合规范或元数据不完整
- **解决**: 检查文件名和元数据，确保符合要求

### 2. 图片显示问题
- **原因**: 图片路径不正确或文件不存在
- **解决**: 使用正确的相对路径，确保图片已上传到assets目录

### 3. 导航不显示
- **原因**: 文档未添加到mkdocs.yml的nav配置中
- **解决**: 在mkdocs.yml中添加文档路径

### 4. 构建错误
- **原因**: Markdown语法错误或配置问题
- **解决**: 检查Markdown语法，确保配置文件正确

## 项目维护

### 日常维护
1. **内容更新**: 定期更新和补充教学内容
2. **质量监控**: 持续监控内容质量和用户反馈
3. **技术维护**: 保持技术栈的更新和安全性
4. **用户支持**: 及时响应用户问题和建议

### 版本管理
- **主版本**: 重大功能更新
- **次版本**: 新内容添加
- **修订版本**: 错误修复和小改进

## 联系方式

- **项目维护者**: kidzying
- **反馈渠道**: GitCode Issues
- **邮件**: [项目相关邮件地址]

---

*最后更新: 2026-02-05*
*版本: v1.1*
*维护者: kidzying*
