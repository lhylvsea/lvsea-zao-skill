# 造 Skill 方法

`lvsea-zao-skill` 采用一条可复核的生命周期：

```text
Intent → Research → Synthesis → Package → Eval → Review → Release → Operate
```

## 1. Intent

先证明这是重复工作和可复用输出，而不是把一次性答案包装成 Skill。锁定名称、owner、版本、目标路径、平台和发布意图。

## 2. Research

用 2–4 个意图查询覆盖结果、领域动作、质量机制和相邻说法。优先查 skills.sh、SkillsMP，再回到 GitHub 读真实 `SKILL.md`、许可证、维护、权限和安全信号。目录安装量、仓库 stars、维护时间和人工评价分开记录，不能合并为分数。

## 3. Synthesis

为每个被认真审阅的候选写四格台账：

- `keep`：机制与本任务一致，可以保留；
- `adapt`：机制有价值，但需要换工具、语言、平台或风险级别；
- `reject`：会增加噪声、权限、平台锁定或无实际收益；
- `invent`：针对当前用户和验收目标新建的连接、脚本或评测。

样本失败不能直接变成全局规则：先改写为领域中立行为，再判断是核心机制、可选适配还是仅限 eval 的 fixture；只有安全、事实、权限硬边界或跨无关领域复现的行为才升级为核心规则。

## 4. Package

根 `SKILL.md` 只负责路由、核心流程和输出契约。长方法进 `references/`，确定性行为进 `scripts/`，回归样例进 `evals/`，运行结果进 `reports/`。每个新增文件都必须有明确用途。

## 5. Eval / Review / Release

先检查触发边界，再检查包入口、上下文预算、权限和秘密；然后生成 IR、运行本地门禁。公开发布额外经过功能分支、PR、Release、公开发现和隔离安装。静态报告可以证明流程执行了检查，但不能冒充 provider 或人工输出质量证据。

## 6. Operate

维护 owner、review cadence、review due、回滚边界、失败回归和下一轮行动。版本化报告只记录可公开复核的信息，原始用户材料和凭据留在包外。
