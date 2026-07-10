🗣 每日对话 Day 49 — 写作日：Sprint 排期讨论 → 正式 Sprint 计划邮件
周六 | 第8周 · 写作表达——从"说"变"写"

─────────────────────────
📝【场景说明】
─────────────────────────

Day 44 的口语场景是 Sprint Planning 会议：Sarah (EM)、Jake (PM)、Wei (Tech Lead) 三人讨论排期，最终达成共识。

今天的任务：把这场 **30 分钟会议的口头讨论** 变成一封 **Sprint 计划确认邮件**，发给整个团队 + 利益相关方。

你会看到：
1. 原始口语版（会议精华摘要）
2. 书面邮件版（完整正式邮件）
3. 逐项对比：口语习语 → 书面表达

─────────────────────────
🗣【口语版回顾】（会议精华）
─────────────────────────

Sarah: "We need to make some hard calls. The post-escalation fixes are non-negotiable — I'm putting my foot down."

Jake: "Can we scope the checkout redesign down to an MVP? Drop personalization, save 30 points?"

Wei: "Closer to 35 if we also drop the A/B test framework. We can bolt that on next sprint."

Sarah: "Let's cross that bridge when we come to it. I don't want to over-commit on day one."

─────────────────────────
✉️【书面邮件版】
─────────────────────────

**To:** engineering-team@company.com, product-team@company.com
**Cc:** stakeholders@company.com
**Subject:** Sprint 47 Plan — Confirmed Priorities & Deferred Items

---

Hi team,

Following today's sprint planning session, below is the confirmed plan for Sprint 47 (July 6 – July 19). This summary documents the decisions made, the rationale behind them, and the items deferred to future sprints.

**Sprint Capacity**
- Estimated capacity: 120 story points
- Committed scope: 115 story points (85 points committed, 30 points stretch)

**Confirmed Priorities (in order)**

1. **Post-Escalation Bug Fixes (P1)** — 25 pts
   Owner: Wei + Raj
   These are critical fixes stemming from the Sprint 46 production incident. They affect paying customers and have been prioritized as non-negotiable for this sprint.

2. **Payment Gateway Migration (Backend)** — 40 pts
   Owner: Wei + Raj
   This is a backend-only workstream with a hard deadline of July 31. Wei and Raj will proceed independently of the frontend team.

3. **Checkout Flow Redesign — MVP (Frontend)** — 35 pts
   Owner: Frontend pod
   Scoped down from the original 70-point estimate. The personalization engine and A/B test framework have been removed from this sprint. The MVP will deliver the streamlined checkout flow only.

4. **Stretch: Analytics Dashboard Upgrade** — 15 pts (stretch)
   Owner: Frontend pod (if checkout MVP completes early)
   To be reassessed at the mid-sprint check-in on July 13.

**Deferred Items**

| Item | Original Estimate | Reason for Deferral |
|------|------------------|---------------------|
| Checkout personalization engine | 20 pts | Descoped to accelerate core flow; planned for Sprint 48 |
| A/B test framework | 15 pts | Dependency on core flow completion; planned for Sprint 48 |
| Analytics dashboard (full) | 30 pts | Capacity constraint; stretch goal only this sprint |

**Key Decisions & Rationale**

- **Bug fixes take absolute priority.** The P1 issues from last sprint's escalation are affecting production users and cannot be deferred further.
- **Checkout redesign was scoped down to an MVP** to accommodate both the bug fixes and the payment migration within the sprint window. The full scope will be revisited in Sprint 48.
- **Payment migration runs in parallel** as it requires only backend resources and does not compete with the frontend-heavy checkout work.

**Looking Ahead**
A mid-sprint check-in is scheduled for Thursday, July 13 at 10:00 AM. If the checkout MVP is tracking ahead of schedule, we will reassess and potentially pull items from the top of the backlog.

Please reach out if you have any questions or concerns.

Best regards,
Sarah Chen
Engineering Manager

---

─────────────────────────
🔍【口语 → 书面：6 大转换技巧】
─────────────────────────

**技巧 1：习语 → 正式动词**

| 口语版 | 书面版 | 说明 |
|--------|--------|------|
| make some hard calls | confirm priorities and trade-offs | "hard calls"太口语，用正式名词短语 |
| put my foot down | prioritized as non-negotiable | 情绪化表达→客观陈述 |
| scope down to an MVP | scoped down from the original estimate | 动词保留，但加具体数字 |
| bolt that on next sprint | planned for Sprint 48 | "bolt on"太随意→明确计划 |
| cross that bridge when we come to it | to be reassessed at the mid-sprint check-in | 模糊口语→具体时间点 |
| ship neither on time | cannot be completed within the sprint window | 口语否定→正式描述 |
| half-baking both | accommodate both within the sprint window | 略 |

**技巧 2：结论先行（BLUF — Bottom Line Up Front）**

口语版是"讨论→争论→达成共识"的线性过程。邮件版第一段就给出结论：
> "Below is the confirmed plan for Sprint 47..."

然后才是支撑细节。读邮件的人 10 秒内就能抓到重点。

**技巧 3：用表格替代段落叙述**

口语版里 Jake 说 "drop personalization, save 30 points" 是散落在对话中的。邮件版用 **Deferred Items 表格** 一目了然：
- 什么被砍了
- 原来多大
- 为什么砍
- 什么时候做

表格 > 段落，永远是职场邮件的铁律。

**技巧 4：时态选择——过去时 vs 现在时**

- 过去时：描述会议中发生了什么（"decisions made", "was scoped down"）
- 现在时：描述当前状态和计划（"is non-negotiable", "will proceed independently"）

口语版混在一起说，邮件版严格区分。写邮件时问自己：这是"已经决定的事"还是"接下来要做的事"？

**技巧 5：名词化（Nominalization）**

口语喜欢用动词和代词，书面喜欢用名词短语：

| 口语（动词为主） | 书面（名词为主） |
|-----------------|-----------------|
| "We need to fix the bugs first" | "Post-escalation bug fixes take absolute priority" |
| "They affect paying customers" | "affecting production users" |
| "We decided to cut the A/B framework" | "The A/B test framework has been removed from this sprint" |

名词化让句子更紧凑、信息密度更高，适合邮件和文档。

**技巧 6：语气调节——从"我坚持"到"客观陈述"**

口语版 Sarah 说："I'm putting my foot down on that one" — 这是一个人表态。
邮件版变成："These are critical fixes... prioritized as non-negotiable for this sprint" — 用被动语态和客观理由，让决定看起来不是个人意志，而是团队共识。

职场邮件黄金法则：**用理由说服人，不用权威压人。**

─────────────────────────
📋【口语 → 书面 速查对照表】
─────────────────────────

| # | 口语表达 | 书面替代 | 语境 |
|---|---------|---------|------|
| 1 | make some hard calls | confirm priorities and trade-offs | 排期/资源 |
| 2 | put my foot down | prioritized as non-negotiable | 强调优先级 |
| 3 | half-bake | cannot be completed within... | 质量风险 |
| 4 | bolt on | to be added in a subsequent sprint | 迭代计划 |
| 5 | cross that bridge when we come to it | to be reassessed at [time] | 不确定事项 |
| 6 | over-commit | exceed sprint capacity | 产能管理 |
| 7 | ship first and iterate later | deliver the core scope first, then iterate | 交付策略 |
| 8 | caught off guard | without prior visibility / notification | 信息同步 |
| 9 | make the cut | included in the sprint scope | 排期结果 |
| 10 | non-negotiable | non-negotiable / mandatory / critical | ✅ 直接可用 |
| 11 | scope down to an MVP | scoped down to a minimum viable release | 范围管理 |
| 12 | in the loop | kept informed / notified | 信息共享 |
| 13 | do full justice | adequately resourced / fully addressed | 资源分配 |
| 14 | sounds like a plan | confirmed / agreed upon | 确认共识 |
| 15 | let's document this | please find the summary below | 邮件开场 |

─────────────────────────
✏️【动手练习】
─────────────────────────

**练习 1：** 把下面这句口语改成邮件中的正式表达：

> "We can't do both at the same time — if we try, we'll mess up both. Let's do one first and then the other."

💡 提示：用 "cannot be completed within the sprint window" + "sequenced appropriately"

**练习 2：** 把下面这句口语改成邮件中的表格行：

> "The analytics dashboard thing — we're not doing it this sprint because we just don't have enough people. Maybe next sprint if things go well."

💡 提示：用 Deferred Items 表格格式（Item / Estimate / Reason / Planned for）

**练习 3：** Day 45 的口语场景是"会上被质疑数据"。如果会后要发一封邮件确认数据口径，邮件标题应该怎么写？

💡 提示：Subject 要包含 [Decision] 或 [Confirmed] + 具体主题

─────────────────────────

💡 **今日一句：**
> **"Below is the confirmed plan for Sprint 47, including priorities, rationale, and deferred items."**
>
> 这是一封完美的邮件开场白——一句话说清了：这是什么（确认的排期计划）、包含什么（优先级 + 理由 + 砍了什么）、给谁看（全团队）。以后写 Sprint 邮件，直接套这个句式。
