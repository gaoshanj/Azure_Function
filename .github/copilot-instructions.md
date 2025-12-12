```markdown
// filepath: d:\OneDrive - gs82\Code\Azure_Function\.github\copilot-instructions.md
# GitHub Copilot 指南（Azure_Function 仓库，CI/CD 指南）

本指南用于指导 AI 编码代理在本仓库中输出和变更表达，确保与 CI/CD 流程一致，便于人工审阅与自动化合并。

## 目标
- 快速实现最小可验证的 CI/CD 流程，训练qa Function 的部署可用性。
- 使用 GitHub Actions 自动构建、测试、部署 Azure Functions。
- 参考 prompts/copilot_guide_zh.md 的输出规范。

## 架构与边界
- Azure 上已创建 Function App trainingqa，CI/CD 的部署目标也会指向该 Function。
- 代码仓库结构要点：根目录包含 README.md、prompts/ 目录以及 copilot 指南模板。
- CI/CD 流程应覆盖构建、测试、打包与部署三个阶段，默认触发分支为 main。

## 关键工作流与实现要点
- 身份认证：通过 GitHub Secrets 提供的 AZURE_CREDENTIALS 进行 Azure 登陆。
- 部署工具：优先使用 Azure Functions 官方工作流组件（Azure/functions-action）进行打包与部署；必要时结合 az 登录后执行 Azure Functions 部署命令。
- 诊断信息：在输出中保留诊断信息，便于定位问题，例如 Azure SDK 的诊断字符串。

## 最小可用 CI/CD 示例（放在 .github/workflows/deploy_azure_function.yml）
````yaml
name: Deploy Azure Function
on:
  push:
    branches: [ main ]
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: azure/login@v1
        with:
          creds: ${{ secrets.AZURE_CREDENTIALS }}
      - uses: Azure/functions-action@v1
        with:
          app-name: trainingqa
          package: .
````
- 备注：如需指定订阅、资源组等，可通过 Secrets 传入额外参数。

## 具体约定与示例输出格式
- 变更输出应分组按文件组织，使用文件路径作为小节标题。
- 每个文件块包含简短变更摘要以及变更片段，片段中用 ...existing code... 表示未改动的部分。
- 参考 prompts/copilot_guide_zh.md 的输出模板，以确保风格一致。

## 现有内容的对齐
- 仓库根目录的 README.md 与 prompts/copilot_guide_zh.md 提供范例和输出格式，可作为对齐参考。
- 如果需要新增函数或端点，请在同一个 Function App 下扩展路由结构，保持部署的一致性。

## gpt-5-nano模型
- 模型每分钟Token限制：200K
- 每次回复为止：64K Token

```markdown