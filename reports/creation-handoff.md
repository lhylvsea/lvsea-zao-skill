# Creation Handoff

## Result

- Skill: `lvsea-zao-skill` `0.1.0`
- Owner: `海洋哥 / lhylvsea`
- Job: 将重复工作流、Prompt、SOP、脚本、笔记或旧 Skill 变成可发现、可评测、可移植、可治理、可发布的 Agent Skill 包。
- Local path: the package root containing this report
- Publication status: local package under validation; GitHub publication is requested and will be verified separately.

## Reference skills studied

- [qiaomu-meta-skill](https://github.com/joeseesun/qiaomu-meta-skill)：学习先例检索、取舍台账、触发评测、证据边界和功能分支/PR/Release/安装发布链；落到 `references/skill-engineering-method.md`、`scripts/trigger_eval.py`、`scripts/release_check.py` 和 `scripts/publish_skill.py`。
- [yao-meta-skill](https://github.com/yaojingang/yao-meta-skill)：学习 Intent/Skill IR/治理/可移植/上下文纪律/`missing evidence`；落到 `manifest.json`、`agents/interface.yaml`、`scripts/export_skill_ir.py`、`scripts/context_sizer.py` 和 `references/`。

## Absorbed and rejected

- `keep`：先研究后创建；保留上游机制而非复制长文；触发、结构、秘密、信任、发布和安装分层验证；公开声明服从证据边界。
- `adapt`：将 Qiaomu 发布器改为 `lhylvsea` owner；将 Yao 大型 Skill OS 压缩为首版实际需要的 IR、预算、治理、回归和发布契约；修复 Windows `.cmd` 工具解析。
- `reject`：Qiaomu 个人 Profile/二维码；Yao 的 telemetry、Review Studio、world-class evidence 和庞大报告资产；所有未经审查的远程脚本执行；直接推送默认分支。
- `invent`：轻量四类触发回归、跨平台命令解析、单一本地 gate 汇总、面向中文用户的发布 README 与可回滚同步边界。

## Advantages and evidence

- `[design advantage]` 将“可触发”与“可治理/可发布”放在同一个最小包契约中，而不是只生成一份 `SKILL.md`。
- `[design advantage]` 以平台中立 IR 连接 OpenAI、Claude、Generic Agent Skills 和 VS Code 目标，并显式写出降级和未验证边界。
- `[design advantage]` 首版不携带任一上游的个人品牌资产和大规模运营系统，减少公开包的隐私、维护和上下文负担。
- `[validated advantage]` 待本地 `validate_skill.py`、四类 trigger eval、context budget、unit tests 和 release gates 全部通过后，才能把对应结果写成已验证优势。
- `[hypothesis]` “轻入口 + 硬门禁”预计比整库搬运更适合海洋哥的 Windows/Codex 工作流，但尚无 provider-backed 或人工盲评对比，保留为 `missing evidence`。

## Verification and limits

- Package validation: generated after final reports are in place.
- Trigger regression: covers positive, negative, near-neighbor and adversarial cases.
- IR/context/release checks: deterministic local evidence; not a quality or business-outcome guarantee.
- Output evidence: static fixture only; provider-backed and human evidence remain `missing evidence`.
- Deliberately excluded: private material, credentials, unreviewed remote execution, direct default-branch writes, automatic merge bypass and unearned “best/production/world-class” claims.
