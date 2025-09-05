# 更新日志

所有重要的项目变更都将记录在此文件中。

### 新增

## v0.0.2 - 2025-08-29

添加 Google 搜索代理功能

### 新增

- **Google 搜索代理**：实现 `google_search_agent` 模块
  - 添加 `google_search_agent/agent.py` 核心代理实现
  - 添加 `google_search_agent/__init__.py` 模块初始化文件
- 添加 Jupyter Notebook 文件 `agno.ipynb`，用于 AI 代理相关的研究和实验

### 变更

- **依赖管理**：更新 `pyproject.toml` 配置，添加新的依赖项
- **多工具代理**：优化 `multi_tool_agent/agent.py` 实现
- **依赖锁定**：更新 `uv.lock` 文件以包含新的依赖版本

## v0.0.1 - 2025-08-29

初始项目架构和多工具代理框架

### 新增

- **项目初始化**：建立基础的 ADK Agents 项目结构

  - 添加 `README.md` 项目说明文档
  - 添加 `main.py` 项目入口文件
  - 添加 `.gitignore` Git 忽略配置
  - 添加 `.python-version` Python 版本管理

- **多工具代理框架**：实现基础代理系统

  - 添加 `multi_tool_agent/` 模块目录
  - 添加 `multi_tool_agent/agent.py` 核心代理逻辑
  - 添加 `multi_tool_agent/__init__.py` 模块初始化

- **依赖管理系统**：建立现代 Python 项目管理

  - 添加 `pyproject.toml` 项目配置和依赖声明
  - 添加 `uv.lock` 依赖锁定文件

- **许可证**：添加 MIT 开源许可证 `LICENSE`

---

## 变更类型

- **新增** - 新功能、工具或文档
- **变更** - 现有功能或文档的修改
- **整理** - 文件移动、重组或清理
- **修复** - 错误修复或问题解决
- **移除** - 删除的功能或文件
- **安全** - 安全相关的改进
