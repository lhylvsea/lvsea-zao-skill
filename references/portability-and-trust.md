# 可移植性与信任边界

## 平台中立

Skill IR 记录任务语义、触发、输入、输出、流程、边界、资源、风险和证据；`agents/interface.yaml` 再声明客户端适配。没有实际测试的平台只能标为目标适配或降级说明，不能写成“已验证支持”。

当前约定：

| 平台 | 交付方式 | 证据边界 |
|---|---|---|
| OpenAI | metadata-adapter | 需要目标客户端实际安装或调用证据 |
| Claude | neutral source + adapter | 需要目标客户端实际安装或调用证据 |
| Generic Agent Skills | canonical source | 以根 `SKILL.md` 和结构校验为基础 |
| VS Code | neutral source + review notes | 需要目标客户端实际安装或调用证据 |

## Trust boundary

- 本地源代码是待审阅输入；远程候选默认只读元数据和公开源码；
- 未审查的第三方脚本、hook、安装器和生成命令不执行；
- 网络访问、GitHub 写入、PR/Release、npx 安装、文件覆盖和本地同步都必须由明确请求触发；
- 包内不保存 Token、Cookie、私钥、私有附件、原始私人对话或本机绝对路径。

## 回滚边界

- 本地写入只限明确的目标 Skill 目录；发布前保留 Git 分支和 commit；
- 已发布版本不可覆盖，修复必须提升 semver；
- 本地安装同步前保留旧副本或使用隔离目录；
- PR、Release、远程仓库和安装副本是外部状态，失败时停止并报告具体状态，不自动删除用户资源。

## 证据降级

网络目录失败、平台安装不可用、provider/人工评审缺失或权限未批准时，继续完成可安全的本地检查，并在报告中保留 `missing evidence`，降低对结果的公开声明。
