# Content To Skill 融合说明

## 来源与审阅边界

- 来源：[gnipbao/content-to-skill](https://github.com/gnipbao/content-to-skill)。
- 审阅提交：`ce5776a5161065836ed4647f9b96629d062ffdee`（2026-08-31）。
- 许可证：MIT；本文件记录语义采用，不镜像上游目录或大段正文。
- 上游的 `scripts/check_skill_package.py` 没有复制进来。`lvsea-zao-skill` 继续以自己的 `validate_skill.py`、触发评测、IR、上下文、信任和发布门禁作为唯一校验链。

## keep / adapt / reject

| 决策 | 上游机制 | 在 `lvsea-zao-skill` 中的落点 |
|---|---|---|
| `keep` | 先声明来源边界，再把证据转成行为 | `Intent` 阶段的来源清单、`BLOCKED_SOURCE` 和证据分级 |
| `keep` | 机制卡而不是逐段摘要 | `Synthesis` 阶段的机制卡模板和输出契约 |
| `keep` | 默认一个边界清楚的 Skill | 根入口唯一；仅在独立路由、状态或领域确实存在时扩展家族 |
| `keep` | 不可访问来源停机、请求材料或做 dry-run | 安全边界、证据降级和发布声明守卫 |
| `keep` | 面向未来请求的重测提示 | `evals/` 触发回归与包内重测提示，验证不依赖原始来源 |
| `adapt` | `QUICK_CONVERT`、`SOURCE_AUDIT`、`PACKAGE_BUILD`、`REPAIR_FROM_FEEDBACK` | 映射到 `Scaffold`、`Production`、`Library`、`Governed` 及本文件的入口模式 |
| `adapt` | 上游轻量结构校验 | 复用现有 governed package validator，避免两套结构真相 |
| `reject` | 独立的 `content-to-skill` 根入口和重复 `agents/openai.yaml` | 保留 `lvsea-zao-skill` 作为唯一 Skill 创建、评测、治理和发布权威 |
| `reject` | 把一个来源机械拆成多个 Skill | 先记录合并/舍弃理由，只有独立任务边界成立才拆分 |

## 来源边界模板

处理非平凡来源时，在 `reports/` 或创建交接中保留以下最小记录：

```md
## Source Boundary
Source type:
Root or access path:
Read:
Not read:
High-signal sections:
Observed:
Inferred:
User-provided:
Unavailable:
User job:
Target runtime:
Assumptions:
```

使用 `Read from source`、`Inferred`、`User-provided`、`Unavailable` 和 `Dry-run` 区分事实、推断、用户输入、缺失材料和未执行验证。视频或音频只有链接/标题时，不把元数据当作方法证据。

## 机制卡模板

只保留会改变未来 Agent 行为的控制项：

```md
## Mechanism Card
Name:
Source evidence:
Trigger:
User job:
Decision rule:
Procedure:
Output:
Quality signal:
Failure mode:
Skill location:
Keep / merge / discard:
```

若一个候选只提供观点、口号、重复例子或无法支持的结论，放入 `discard` 或不确定性记录，不直接写入根 `SKILL.md`。

## 重测要求

每个非平凡新 Skill 至少保留一个像真实用户请求的前向重测。优先覆盖：

- 短材料能否生成紧凑的程序型 Skill，而不是长篇总结；
- 视频/音频有转写和无转写时是否走不同分支；
- 弱 Skill 是否能按原始来源修复决策、输出和验证；
- 多来源有冲突时是否记录合并、保留和舍弃，而不是盲目扩张成 Skill 家族。

重测结果只证明对应请求和当前包版本的行为；没有真实客户端、provider 或人工复核时，仍标为 `missing evidence`。
