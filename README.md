# lvsea-zao-skill

> 把反复使用的工作流、提示词、SOP 或旧 Skill，造成为可发现、可评测、可移植、可治理、可发布的 Agent Skill 包。

[![License](https://img.shields.io/github/license/lhylvsea/lvsea-zao-skill?style=flat-square)](LICENSE)
[![Last commit](https://img.shields.io/github/last-commit/lhylvsea/lvsea-zao-skill?style=flat-square)](https://github.com/lhylvsea/lvsea-zao-skill/commits/main)

## 为什么值得用

很多“会做但难复用”的方法，散落在聊天记录、个人 Prompt、流程文件和脚本里。`lvsea-zao-skill` 先判断这是不是值得沉淀的重复任务，再把任务、输入、输出、边界、评测、权限和发布证据组织成一个正式 Skill 包。

它把两类优势接到一条链上：一方面先研究同类方案、测试触发边界并安全走 GitHub 发布；另一方面把 Skill IR、上下文预算、可移植性、信任边界和生命周期治理显式化。目标是少写无效说明，多交付能安装、能验证、能继续维护的包。

## 安装

```bash
npx skills add lhylvsea/lvsea-zao-skill
```

只安装这个 Skill：

```bash
npx skills add lhylvsea/lvsea-zao-skill --skill lvsea-zao-skill
```

安装后重启当前 Agent 客户端，再用自然语言触发。

## 你可以这样说

- “把这套制造现场安全检查 SOP 封装成团队可复用的 Skill，先补输入输出和触发边界。”
- “优化这个已有 Skill 的 description，补 should-trigger、should-not-trigger 和近邻误触发评测。”
- “把这套 Prompt 和脚本迁移成可跨 OpenAI、Claude 和通用 Agent Skills 使用的包，补 Skill IR 和权限边界。”
- “先研究 qiaomu-meta-skill 和 yao-meta-skill，再取长补短创建一个不抄袭的版本。”
- “发布这个 Skill 到 GitHub，走功能分支、PR、Release 和干净安装验证。”

## 它会做什么

1. 从 workflow、Prompt、转录、SOP、脚本或旧 Skill 中提炼可重复任务。
2. 记录目标用户、输入、输出契约、排除项、质量标准和权限边界。
3. 检索并核对同类方案，区分 `keep / adapt / reject / invent`，避免拼贴上游文字。
4. 创建精简的 `SKILL.md`，把长方法、确定性检查、评测和证据分层保存。
5. 运行触发回归、包结构检查、上下文预算、秘密扫描、信任和发布门禁。
6. 在用户明确授权后，通过功能分支、PR、版本化 Release、公开发现和隔离安装完成发布。

## 安装后得到的包

```text
lvsea-zao-skill/
├── SKILL.md                         # Agent 运行入口
├── README.md                        # 面向安装者的中文产品页
├── manifest.json                    # 版本、owner、成熟度与发布门禁
├── agents/interface.yaml            # 平台中立接口与权限声明
├── references/                      # 方法、治理、信任与可移植说明
├── scripts/                         # 可重复运行的校验、评测和发布工具
├── evals/trigger_cases.json         # 正触发、负触发、近邻和对抗案例
├── schemas/                         # Skill IR 结构约束
└── reports/                         # 先例、IR、评测、预算和发布证据
```

典型验证输出：

```text
Package validation: PASS
Trigger evaluation: PASS (all cases passed)
Skill IR: reports/skill-ir.json
Context budget: PASS or WARN with measured bytes
Public output evidence: missing evidence when no provider/human run exists
```

## 本地验证

在仓库根目录执行：

```bash
python scripts/validate_skill.py .
python scripts/trigger_eval.py . --cases evals/trigger_cases.json --output reports/trigger-eval.json
python scripts/export_skill_ir.py . --output reports/skill-ir.json
python scripts/context_sizer.py . --output reports/context-budget.json
python scripts/release_check.py . --phase local --run-tests
```

Windows PowerShell 也可使用 `py`：

```powershell
py scripts/validate_skill.py .
py scripts/trigger_eval.py . --cases evals/trigger_cases.json --output reports/trigger-eval.json
py scripts/export_skill_ir.py . --output reports/skill-ir.json
py scripts/context_sizer.py . --output reports/context-budget.json
py scripts/release_check.py . --phase local --run-tests
```

## 发布到 GitHub

发布前先做只读检查：

```bash
python scripts/publish_skill.py . --dry-run --github-user lhylvsea --repo-name lvsea-zao-skill
```

确认检查结果后，完整发布：

```bash
python scripts/publish_skill.py . --github-user lhylvsea --repo-name lvsea-zao-skill
```

发布器会拒绝直接推送 `main/master`、复用已有版本、秘密扫描失败、PR 检查失败或安装验证失败。它会创建或复用 `lhylvsea/lvsea-zao-skill`，使用 `codex/` 功能分支，创建 PR，合并后生成 `vX.Y.Z` Release，并通过 `npx skills add` 做隔离安装检查。

## 前置条件

- [ ] Node.js 18+ 与 npx：`node --version && npx --version`
- [ ] Python 3.9+：`python --version` 或 `python3 --version`
- [ ] Git：`git --version`
- [ ] 发布到 GitHub 时已登录 GitHub CLI：`gh auth status`
- [ ] 搜索先例时允许访问 skills.sh、SkillsMP 和公开 GitHub 源码
- [ ] 需要 provider 实跑、人工盲评、真实客户端遥测或私有 API 时，已经单独准备凭据和审批；本 Skill 不会代用户生成凭据

## 配置

本 Skill 默认不要求环境变量，也不会把凭据写入包。发布、搜索和安装由本机的 GitHub CLI、Node.js/npx 与网络环境提供能力。

| 配置项 | 必需 | 说明 |
|---|---:|---|
| `GITHUB_TOKEN` | 否 | 仅当 GitHub CLI 不使用系统登录态时，由用户自行配置 |
| `SKILLSMP_API_KEY` | 否 | SkillsMP 匿名额度不足时可选；不要写入 README、报告或提交记录 |
| `LVSEA_REVIEW_DUE` | 否 | 覆盖治理报告中的下次复核日期；不替代人工复核 |

## 重要边界

- 静态校验、触发 fixture 和本地报告证明包结构与规则检查，不等于 provider 实跑、人工盲评、用户满意度或业务结果。
- 找到的安装量、stars 和维护时间是采用/关注信号，不是评分，也不会合并成“最佳 Skill 分数”。
- 远程候选只做元数据和源码审阅；未经审查的第三方安装器、hook、脚本和生成命令不会被执行来“学习”。
- 发布、PR、Release、`npx skills add` 和本地安装同步都会改变外部状态，只在用户明确要求时执行。
- 公开仓库不应包含 Token、Cookie、私有附件、原始私人对话、公司内部源材料或本机绝对路径。

## Troubleshooting

| 问题 | 常见原因 | 处理 |
|---|---|---|
| `No valid skills found` | frontmatter 不完整，或仓库里存在嵌套的 `SKILL.md` | 运行 `python scripts/validate_skill.py .`，补齐 `name`/`description` 并将示例改名为 `SKILL.example.md` |
| Skill 永远不触发或到处误触发 | description 与自然说法不匹配，或负例太少 | 修改 `SKILL.md` 的 description 和 `evals/trigger_cases.json`，重新运行 `trigger_eval.py` |
| 发布器提示 `npx` 找不到 | Windows 将 npx 注册为 `npx.cmd`，或 Node.js 未进 PATH | 运行 `node --version`、`npx --version`；PowerShell 下确认 `Get-Command npx`，必要时重启终端 |
| PR 或 Release 门禁阻断 | 工作树不干净、版本已发布、检查未完成或请求修改 | 读取发布器的具体 gate，修复后提升 `manifest.json` 版本并重跑，不直接推默认分支 |
| 本地通过但别人装不上 | 只验证了源目录，没有公开发现或隔离安装证据 | 发布后运行 `npx skills add lhylvsea/lvsea-zao-skill --list`，再做全新临时目录安装 |

## 致谢与来源

本项目是独立整合实现，采用上游的公开方法与结构，不整库镜像：

- [joeseesun/qiaomu-meta-skill](https://github.com/joeseesun/qiaomu-meta-skill)：先例研究、`keep/adapt/reject/invent`、触发评测、证据边界和分支/PR/Release/安装发布链。
- [yaojingang/yao-meta-skill](https://github.com/yaojingang/yao-meta-skill)：意图建模、Skill IR、分层回归、上下文纪律、可移植性、信任边界和生命周期治理。
- [skills.sh](https://skills.sh/) 与 [SkillsMP](https://skillsmp.com/)：先例检索目录；其安装量和 stars 仅按原始语义记录。

## License

MIT。详见 [LICENSE](LICENSE)。
