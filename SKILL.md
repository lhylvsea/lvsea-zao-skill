---
name: lvsea-zao-skill
description: |
  Create, improve, migrate, evaluate, package, govern, and publish reusable agent skills from repeated workflows, prompts, transcripts, SOPs, scripts, notes, or existing skill packages. Use when the user asks to 把流程做成 Skill、封装可复用能力、优化已有 Skill、补触发评测、建立 Skill IR、检查信任边界、准备团队复用、发布到 GitHub or verify a clean installation. Exclude one-off answers, summaries, translations, ordinary documentation, brainstorming, and copy-only README edits that do not create or maintain a reusable skill package.
metadata:
  author: "海洋哥 / lhylvsea"
  version: "0.1.0"
  upstream_inspiration: "https://github.com/joeseesun/qiaomu-meta-skill; https://github.com/yaojingang/yao-meta-skill"
---

# Lvsea 造 Skill

把反复发生的工作编译成可发现、可评测、可移植、可治理、可发布的 Skill 包，而不是把长 Prompt 换一个文件名。

## 路由规则

- 先根据本文件的 `description` 判断是否真的要创建或维护可复用 Skill；一次性回答、解释、翻译、普通文档和只改 README 不触发。
- 本 Skill 是 Skill 创建与发布的单一作者权威；不要再调用另一个 generic creator、discovery 或 publisher 来重复初始化。
- 一个包只保留一个可发现的根 `SKILL.md`；示例和测试夹具使用 `SKILL.example.md`、`SKILL.fixture.md`。
- 先锁定目标目录、Skill 名称、版本、owner 和发布范围，再写文件；涉及发布、安装、网络或账号时明确权限边界。

## 核心流程

1. `Intent`：确认重复任务、目标用户、输入、输出契约、排除项、质量标准和完成证据；小而安全的细节自行假设，影响包体或权限的冲突才提问。
2. `Research`：用意图关键词检索 skills.sh、SkillsMP 和 GitHub；核对源文件、许可证、维护状态、权限与安全信号，不执行未经审查的第三方代码。
3. `Synthesis`：建立 `keep / adapt / reject / invent` 台账，学习机制而不是拼贴上游正文；通过通用化门槛后才把样本失败升级为核心规则。
4. `Package`：保持入口精简，把长判断放在 `references/`，把确定性校验放在 `scripts/`，把触发样例放在 `evals/`，把证据放在 `reports/`。
5. `Eval`：先测触发面，再测近邻误触发、对抗案例、上下文预算、包结构、秘密信息、信任与权限边界；没有 provider 或人工证据时标记 `missing evidence`。
6. `Release`：公开发布必须经过本地门禁、功能分支、PR、版本化 Release、公开发现和隔离安装验证；禁止直接推送默认分支或复用已发布版本。
7. `Operate`：记录 owner、review cadence、review due、rollback boundary 和下一轮改进方向，不把临时报告、私有素材或凭据写进公开包。

## 模式与门禁

按 [模式说明](references/operating-modes.md) 选择最轻模式：个人试验用 `Scaffold`，团队复用用 `Production`，共享基础设施用 `Library`，公开发布或涉及账号/网络/文件写入用 `Governed`。

- 所有模式：frontmatter、清晰边界、可用 README、根入口唯一。
- `Production+`：interface、触发评测、输出契约、安装说明和先例研究。
- `Library+`：Skill IR、上下文预算、可移植性、信任边界和生命周期治理。
- `Governed`：秘密扫描、回滚边界、公开声明守卫、PR/Release/安装证据；外部或人工证据缺失必须如实标记。

## 输出契约

根据模式交付必要文件：根 `SKILL.md`、`README.md`、`agents/interface.yaml`、`manifest.json`、`evals/trigger_cases.json`、生成的 Skill IR、先例与创建交接报告，以及确有复用价值的 references/scripts。发布请求才创建远程仓库、PR、Release 或安装副本。

## 参考与验证

- 方法、意图和取舍：`references/skill-engineering-method.md`、`references/intent-dialogue.md`、`references/creation-handoff.md`。
- 评测、治理、权限和可移植：`references/evaluation-and-governance.md`、`references/portability-and-trust.md`。
- 本地最小验证：

  ```bash
  python scripts/validate_skill.py .
  python scripts/trigger_eval.py . --cases evals/trigger_cases.json --output reports/trigger-eval.json
  python scripts/export_skill_ir.py . --output reports/skill-ir.json
  python scripts/context_sizer.py . --output reports/context-budget.json
  python scripts/release_check.py . --phase local --run-tests
  ```

- 公开发布：先运行 `python scripts/publish_skill.py . --dry-run`，确认用户明确授权后再运行完整发布命令。

## 安全边界

- 只把明确授权的 Skill 文件写入目标包；不读取或发布 Token、Cookie、私有附件、原始私人对话和本机绝对路径。
- 远程候选默认只读元数据和源码；不为了学习而运行安装器、hook、脚本或生成命令。
- `npx skills add`、GitHub PR/Release、本地安装同步和任何外部写入都需要用户明确授权。
- 真实输出质量、用户满意度、provider 实跑、人工盲评和生态采用不能由静态文件名或本地 fixture 代替；证据不足时写 `missing evidence`。
