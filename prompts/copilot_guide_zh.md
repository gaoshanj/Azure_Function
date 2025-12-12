# GitHub Copilot 指南（中文，Azure_Function 仓库用）

本文件用于指导 GitHub Copilot 在本仓库中进行代码和文档生成的输出规范与工作流程，确保产出的一致性、可维护性以及便于 CI/CD 自动化集成。

## 目的
- 提供明确的输出格式、分组策略和变更表示，方便人工审阅与自动化合并。
- 统一代码风格、注释约定与文件组织结构，减少重复工作。
- 指导在 Azure Functions 项目中实现 API 功能、CI/CD 配置以及文档更新。

## 使用范围
- 仅适用于 Azure_Function 仓库中的代码、文档和 CI/CD 配置相关变更。

## 输出与变更格式规范

1) 步骤分解
- 给出一个逐步解决方案（step-by-step plan），用于描述将要执行的修改过程。

2) 按文件分组
- 将改动按目标文件分组输出，使用文件路径作为小节标题。

3) 文件级变更块
- 对每个需要修改的文件，给出简要变更摘要，随后附上一个代码块，包含实际改动。
- 代码块格式:
  - 语言标注为对应的语言（markdown、typescript、yaml、json、shell 等）。
  - 第一行以注释形式包含文件路径：
    // filepath: <实际文件路径>
  - 使用四个反引号开始代码块：
    ````markdown
    ```markdown
    // filepath: <实际文件路径>
    { 变更内容片段（包含原有代码的 ...existing code... 表示未改动部分） }
    ```
    ````

4) 变更片段编排
- 不重复现有代码，只在代码块中添加/修改需要的部分。
- 通过注释 ...existing code... 代表未改动的区域。

5) 新建文件
- 若需要创建新文件，给出新文件路径与初始内容的简短描述与代码块示例。

6) 代码块示例
- 以下为示例格式，便于直接应用到实际文件中：
````markdown
```markdown
// filepath: d:\OneDrive - gs82\Code\Azure_Function\README.md
# 示例标题

...existing code...
# 新增内容
```
````

## 变更输出示例

- 修改 README.md 的简要摘要
- 可能的新增提示模板文件

````markdown
```markdown
// filepath: d:\OneDrive - gs82\Code\Azure_Function\README.md
# Azure Function API with GitHub CI/CD

This repository hosts Azure Functions that implement API endpoints and are configured for continuous integration and deployment (CI/CD) via GitHub Actions. It is designed to enable direct CI/CD integration with Azure Functions from GitHub.

## 目标
- 在 Azure Functions 上实现 HTTP 触发的 API
- 使用 GitHub Actions 实现自动构建、测试和部署
- 提供本地开发与 Azure 部署指南

## 本地开发
...existing code...
```
````

- 新增提示模板文件（示例）
````markdown
```markdown
// filepath: d:\OneDrive - gs82\Code\Azure_Function\prompts\copilot_guide_zh.md
# 提示模板：为 Copilot 生成 Azure Function 相关代码的输出规范

...existing code...
```
````

请严格按照以上规范输出变更内容。