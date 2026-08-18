# 运行模式

先选最轻模式，再按风险升级；不要为一次性任务制造完整工程。

## Scaffold

适合个人试验或首次验证。需要合法 frontmatter、清晰的使用入口、自然触发例子和明确排除项。

## Production

适合团队复用。增加 `agents/interface.yaml`、输入输出契约、触发评测、README 验证命令、安装说明和失败排查。

## Library

适合共享基础设施或跨客户端分发。增加 Skill IR、上下文预算、目标平台与降级说明、trust/permissions、owner、review cadence 和可移植性检查。

## Governed

适合公开发布、账号/网络/文件写入、付费服务或关键团队流程。必须增加秘密扫描、回滚边界、证据边界、公开声明守卫、功能分支/PR/Release/隔离安装证据。

## 升级条件

- 触发误伤或漏触发：至少升级到 `Production`。
- 需要跨客户端、长期维护或团队共享：升级到 `Library`。
- 要公开发布、改变外部状态或处理敏感权限：升级到 `Governed`。

缺少 provider 实跑、人工评审、真实客户端遥测、外部审批或用户结果时，保留 `missing evidence`，不能用计划替代证据。
