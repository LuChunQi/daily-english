🗣 每日对话 Day 104 — 写作日：周五下午的救火 → 正式 Capacity Review 提案邮件

周六 | 写作表达（Day 99-103 剧情线：接手系统 → 周会汇报 → 首个 page → 犒赏 → 复习，今天落笔成文）

─────────────────────────
✍️【背景回顾】
─────────────────────────

Day 103 场景 2 的口语现场：季度末周五下午 4 点，你（Leo）被 page——营销看板数据过期三小时，追溯发现是增长团队实验平台把事件量打到平时的 **6 倍**，而队列余量只够吃 **2 倍**。你当场协调：降到 30%、队列每分钟 5,000 条慢慢排空、晚 7 点追平、周一 QBR 保住。最后你提了个口头要求：

> "任何推送量超过两倍的发布，上线前先做容量评审——不用大会议，一份共享文档、一个现实的时间表、书面签核。"

Dev 答应了，还说 "you'll have my team's back on this. We owe you after today."

问题是：Dev 的 lead Elena 不在场，"欠你一次"是人情不是流程。口头承诺的保质期通常撑不过下一个季度末。所以今天你干一件写作日的正事：**把这句口头请求，写成一封会自动生效的提案邮件。**

对照着看你会发现：口语里救场的每一句话，在书面里各就各位——get paged 变成带时间戳的事实，that's on the docs as much as on you 变成 root cause，"我周五下午救火"变成 worst case 分析。

─────────────────────────
📝【正式邮件版】
─────────────────────────

**Subject:** Proposal: pre-launch capacity review for high-volume releases (async, ~10 min per launch)

**To:** Dev (Growth Eng), Elena (Growth Lead), Grace (Eng Manager, Data Platform)
**Cc:** Maya (Data Science), platform-team@company.com

Hi all,

Following Friday's queue saturation, I'm proposing a small process change: a lightweight capacity review before high-volume launches. Three sections below — what happened, the proposal, and the rollout. Reading time: about three minutes; if you only read one section, make it the second.

## What happened

- At **4:04 PM Friday (Sep 4)**, the on-call engineer (me) was paged: marketing dashboards were **three hours stale**. Nothing user-facing broke; Monday's QBR pulls from these dashboards.
- Root cause: the experiment platform, launched Friday morning, was pushing **~6x baseline event volume** into the shared ingestion queue.
- Documented headroom at the time: **2x baseline.** The queue drains at **~5,000 events/min**; after throttling the job to 30%, the backlog fully cleared at **7:10 PM**. Zero customer impact — the best-case version of a bad scenario.

One clarification before the proposal: **nothing below is a criticism of Friday's launch.** The launch followed the existing process. The root cause is a gap we all own — the queue's limits were never written down, so no amount of individual care could have caught this.

## The proposal

A pre-launch capacity review, triggered only by volume:

1. **Declare** (launch team, ~10 min): any launch projecting **>2x baseline event volume** fills a short checklist in the shared launch doc — projected peak, duration, throttle plan, on-call contact.
2. **Review** (data platform, within 2 business days): we return one of three outcomes in writing — **go / throttle / postpone**, with numbers attached.
3. **Record** (both, zero extra effort): the outcome is pasted into the runbook section of the launch doc. The queue's limits (2x headroom, 5K/min drain rate) are now in the runbook; this step keeps that page from going stale.

**What this is not:** not an approval gate, not a meeting, and not a delay for normal launches. Anything under 2x needs no review at all; urgent hotfixes proceed first and file the checklist afterward.

## Why this is worth ten minutes

- **For launch teams:** the alternative to a review is usually a Thursday-night throttle request and a delayed launch. Written numbers get you a same-week **go**, no firefighting.
- **For the platform:** a verbal "should be fine" leaves volume risk invisible until it surfaces as a Friday-afternoon page. Half of our queue incidents in the past two quarters started exactly this way.
- **Worst case:** the checklist adds ten minutes to a launch that would have been fine anyway. That is the full downside. The upside is not re-living Friday at quarter-end.

## Rollout

| # | Step | Owner | Due |
|---|------|-------|-----|
| 1 | Capacity checklist template added to the launch doc | Leo | Mon Sep 7 |
| 2 | Queue limits + drain rate merged into the runbook | Leo | Mon Sep 7 |
| 3 | Pilot with Growth's next two launches | Dev | Sep 7 – Sep 25 |
| 4 | Pilot review — keep, adjust, or drop | Elena + Grace | Fri Oct 2 |

If anything above mischaracterizes Friday's discussion, or a constraint is missing, reply by **EOD Wednesday, September 9**. Barring objections, the checklist goes live **Monday, September 14**, starting with Growth's launches — who have already volunteered to pilot it. Thanks, Dev.

Best,
Leo

─────────────────────────
🎧【朗读版】（音频文字稿：你把邮件读给 Maya 听）
─────────────────────────

A (Leo): Following Friday's queue saturation, I'm proposing a small process change: a lightweight capacity review before high-volume launches. Three sections below — what happened, the proposal, and the rollout. If you only read one section, make it the second.
B (Maya): Smart opening. What did you put in the facts?
A: At 4:04 PM Friday, the on-call engineer — me — was paged: marketing dashboards were three hours stale. Nothing user-facing broke; Monday's QBR pulls from those dashboards. Root cause: the experiment platform, launched Friday morning, was pushing about six times baseline event volume into the shared ingestion queue. Documented headroom at the time: two x baseline. The queue drains at about five thousand events a minute; after throttling the job to thirty percent, the backlog fully cleared at 7:10 PM. Zero customer impact.
B: And the blame part? That's where these emails usually go wrong.
A: One clarification before the proposal: nothing below is a criticism of Friday's launch. The launch followed the existing process. The root cause is a gap we all own — the queue's limits were never written down, so no amount of individual care could have caught this.
B: Oh, that's good. You turned "whose fault" into "what's missing." What's the actual proposal?
A: Three steps. One: declare — any launch projecting more than two x baseline fills a short checklist: projected peak, duration, throttle plan, on-call contact. Two: review — data platform returns go, throttle, or postpone in writing, within two business days. Three: record — the outcome goes into the runbook, so the limits never go stale again.
B: And what it's not?
A: Not an approval gate, not a meeting, and not a delay for normal launches. Anything under two x needs no review at all; urgent hotfixes proceed first and file the checklist afterward.
B: The pushback you'll get is "process slows us down." How did you answer that one?
A: I did the math for them. Worst case, the checklist adds ten minutes to a launch that would have been fine anyway — that's the full downside. The upside is not re-living Friday at quarter-end. And for launch teams, the alternative is usually a Thursday-night throttle request and a delayed launch. Written numbers get you a same-week go.
B: When does it start?
A: Checklist template and runbook updates land Monday. Growth pilots it with their next two launches. Pilot review on October second — keep, adjust, or drop. And the ending: reply by end of day Wednesday if anything mischaracterizes the discussion. Barring objections, it goes live September fourteenth.
B: An objection window and a start date — the polite version of "it's happening." You know this is going straight into our team playbook, right?

─────────────────────────
🔬【口语 vs 书面对比解析】（6 组）
─────────────────────────

**1. "Dev, got a sec?... Name it." → 目的句开头（先告诉读者为什么在读）**

- 口语：*"Dev, got a sec? I just got paged — the marketing dashboards are three hours stale."*（有空吗？我被 page 了……）
- 书面：*"Following Friday's queue saturation, I'm proposing a small process change: a lightweight capacity review before high-volume launches. Three sections below — what happened, the proposal, and the rollout."*
- 📌 技巧：口语开场靠**打断确认**（got a sec = 借两分钟注意力），书面开场靠**定位句**（这封是什么 + 怎么读）。注意三个细节：① *Following Friday's...* 一句话锚定背景，让没在场的人也能进入；② *a small process change* / *lightweight* 提前给流程恐惧症打预防针；③ *"If you only read one section, make it the second"* ——给忙碌读者一条逃生通道，这是高级邮件礼仪，也变相强调了提案段的地位。

**2. "I just traced it back — six times the usual volume" → What happened（时间戳 + 数字的事实段）**

- 口语：*"I just traced it back — your events are six times the usual volume. The queue had headroom for maybe two x, not six."*
- 书面：*"At 4:04 PM Friday (Sep 4), the on-call engineer (me) was paged... the experiment platform... was pushing ~6x baseline event volume... Documented headroom at the time: 2x baseline. The queue drains at ~5,000 events/min; the backlog fully cleared at 7:10 PM."*
- 📌 技巧：口语的 trace it back to 是**当场说服**（我查过了，信我），书面版把这句话拆成一排**带时间戳的数字**：4:04 PM、6x、2x、5K/min、7:10 PM。提案邮件的信用全部建立在这一段上——读者不需要信你，只需要信数字。另注意 *(me)* 这个小括号：主动认领身份，比"the on-call engineer"被动语态更坦荡，又不像"I got paged"那么主观。

**3. "That's on the docs as much as on you" → "a gap we all own"（把分锅句写成共同根因）**

- 口语：*"Honestly, that's on the docs as much as on you — the queue limits were never written down anywhere."*（一半怪文档一半怪你。）
- 书面：*"Nothing below is a criticism of Friday's launch. The launch followed the existing process. The root cause is a gap we all own — the queue's limits were never written down, so no amount of individual care could have caught this."*
- 📌 技巧：这是本篇最值得学的一步。口语里 "on the docs as much as on you" 是**当面给对方台阶**；书面里如果你照搬，就变成了白纸黑字的问责记录。改写后做了三件事：① 否定批评意图；② 肯定对方合规；③ 把责任人从"人和文档"抽象成 **a gap we all own** + *no amount of individual care could have caught this*（再多小心也防不住——系统性缺口，不是个人失误）。同时被说服的还有 Elena：她团队被描述成"流程的遵从者"，自然愿意支持修流程。

**4. "headroom for maybe two x" → ">2x baseline"（把口头余量变成写下来的阈值）**

- 口语：*"The queue had headroom for maybe two x, not six."*
- 书面：*"any launch projecting **>2x baseline event volume** fills a short checklist..."* + *"Documented headroom at the time: 2x baseline."*
- 📌 技巧：口语里 headroom 是估算（*maybe* two x），书面里它必须**升格为触发条件**：>2x 就触发评审。这是把一次事故的教训“制度化”的关键动作——数字不再只是叙述，而是规则。对比一下就知道差距：'please give us a heads-up before big launches' 是请求（多大算大？），'any launch projecting >2x baseline' 是流程。**每一条模糊的口头约定，都藏着一个没写下来的数字。**

**5. "Not a big meeting — a shared doc..." → "What this is not"（提案的自我瘦身）**

- 口语：*"Not a big meeting — a shared doc, a realistic timeline, sign-off in writing. If it's just a verbal 'should be fine,' I'm the one putting out fires at 4 PM on Fridays."*
- 书面：*"**What this is not:** not an approval gate, not a meeting, and not a delay for normal launches. Anything under 2x needs no review at all; urgent hotfixes proceed first and file the checklist afterward."*
- 📌 技巧：新流程提案最大的死因是"流程恐惧"——听者脑补出无休止的会议和审批链。所以提案要**主动自我瘦身**：用一个 *What this is not* 段落连说三个 not，并且写清**豁免条款**（<2x 免审、hotfix 先斩后奏）。口语里 "not a big meeting" 是安抚，书面里的 not-list 是承诺——白纸黑字写下"我不是在给你加官僚负担"，反对声量直接减半。

**6. "I'll take it to our lead" / "We owe you" → 异议窗口 + 生效日 + 试点表（把承诺钉进日历）**

- 口语：*"Fair. I'll take it to our lead — and you'll have my team's back on this. We owe you after today."*
- 书面：*"reply by **EOD Wednesday, September 9**. Barring objections, the checklist goes live **Monday, September 14**, starting with Growth's launches — who have already volunteered to pilot it."* + Rollout 表第 4 行 *"Pilot review — keep, adjust, or drop. Elena + Grace. Fri Oct 2"*
- 📌 技巧：口语承诺的三件套（我带回去/我们支持你/欠你一次）在书面里对应三样东西：① **异议窗口**（reply by EOD Wednesday——沉默即通过，Day 84/97 的 silent approval）；② **生效日期**（goes live Sep 14——提案从"建议"变成"倒计时"）；③ **保质期**（Oct 2 pilot review——连流程本身都有 revisit 日期，反对者知道最坏也只忍四周）。最后补一句 Growth 已自愿试点——把人情的 "we owe you" 变成了写下来的 social proof。

─────────────────────────
🎯【写作技巧讲解：提案邮件的黄金结构】
─────────────────────────

职场邮件三大件我们已经集齐：状态同步（Day 90）、决策记录（Day 97），今天补上**流程提案**。它和前两者的核心区别：**决策邮件记录已发生的事，提案邮件制造将发生的事。** 六个要素：

**① 第一段 = 定位句 + 逃生通道**

三个问题一句话答完：这封是什么、按什么顺序读、你需不需要做什么。*Three sections below...* 让读者可以直奔关心的段落。给忙碌读者的路线图不是客套，是提高被读完率的第一技术。

**② 事实段带时间戳和数字——提案的信用基础**

先讲 what happened 再讲 proposal，顺序不能反：读者认同问题，才会认同方案。时间戳（4:04 PM）和量化（6x / 2x / 5K/min）让事实段无可争辩。**没有数字的提案只是观点。**

**③ 提案写成可执行步骤，触发条件量化**

Declare → Review → Record，每步标注**谁做、多久、做什么**。最关键的是触发条件 *projecting >2x baseline event volume*——制度化的本质就是把教训变成阈值。附带 *What this is not* 自我瘦身 + 豁免条款，提前拆掉"流程官僚化"的引信。

**④ Worst case 写成保险单**

*"The checklist adds ten minutes to a launch that would have been fine anyway. That is the full downside."*——把成本封顶（10 分钟）、把收益具象（不用重演周五下午四点）。**能写出 worst case 的提案才显得想清楚了。**

**⑤ Rollout 表 + 试点 + 评审日期**

Action / Owner / Due 三列起步，最后一定有一行"评审这个流程本身"（keep, adjust, or drop）。给反对者的潜台词：最坏情况你只忍四周。**连流程都要有保质期，别让任何决定永久免检。**

**⑥ 异议窗口 + 自动生效 + 已有支持者**

*Reply by EOD Sep 9. Barring objections, goes live Sep 14.* 沉默被赋予效力，日期被钉死。再加一句 *who have already volunteered to pilot it*——把口头人情转成书面 social proof，其余观望者的从众成本降到最低。

─────────────────────────
📋【本周口语 → 书面速查表】（15 个）
─────────────────────────

| 口语 | 书面 |
|------|------|
| Dev, got a sec? | Following [incident], I'm proposing... |
| I just got paged — dashboards are stale. | At 4:04 PM Friday, the on-call engineer was paged:... |
| I traced it back to the experiment platform. | Root cause: the platform was pushing ~6x baseline volume. |
| The queue had headroom for maybe two x. | Documented headroom: 2x baseline. |
| That's on the docs as much as on you. | The root cause is a gap we all own. |
| My bad for not giving you a heads-up. | The launch followed the existing process. |
| Can you throttle back? | Requested remediation: throttle to 30% until cleared. |
| Dial it down until the backlog drains. | The job was throttled to 30%; the backlog cleared at 7:10 PM. |
| If it's not clearing by lunch, pause it. | Fallback: pause and resume during off-peak hours. |
| Any launch pushing two x needs a review. | Trigger: any launch projecting >2x baseline volume. |
| Not a big meeting — a shared doc, sign-off in writing. | Not an approval gate, not a meeting. |
| If it's just "should be fine," I'm the one putting out fires. | A verbal "should be fine" leaves volume risk invisible. |
| I'll take it to our lead. | To: Elena (Growth), Grace (Data Platform) — requesting sign-off. |
| You'll have my team's back on this. | Growth has volunteered to pilot the process. |
| Fair enough, let's do it. | Reply by EOD Sep 9; otherwise it goes live Sep 14. |

─────────────────────────
🔄【变造挑战】（3 题）
─────────────────────────

**1.** 你们客户支持团队和电商团队口头约定过"大促前先通知支持组排班"，但从没落实。参考今天的开头段，写这封提案邮件的**第一段**（定位句 + 目录 + 逃生通道），并用一句话锚定背景事件。

   💡 提示：Following [上次大促支持爆仓的事件]，I'm proposing... / Three sections below... / If you only read one section...

**2.** 把这句口语改写成事实段里的一句（要求：时间戳 + 数字 + 去责化）："Basically the API was crazy slow all morning, and turns out someone pushed a huge export job, honestly not his fault since nobody knew the limit."

   💡 提示：At [time]... / Root cause: ... was pushing ~Nx baseline... / The root cause is a gap we all own...

**3.** 你提案"每周五下午为部署冻结窗口"（Friday deploy freeze, 4 PM–6 PM）。写**收尾两句话**：包含异议窗口、生效日期，并预告一个试点评审日。

   💡 提示：Reply by [date] if... / Barring objections, the freeze takes effect [date]. / We will review the policy on [date] — keep, adjust, or drop.

─────────────────────────
💡 **今日一句（书面版）：**
─────────────────────────

> *"Nothing below is a criticism of Friday's launch — the root cause is a gap we all own."*

提案邮件里最值钱的一步：把口头版的"一半怪你一半怪文档"，写成书面版的"这是我们共同的缺口"。分锅的话说出口只有五秒效果，写成 root cause 却能管一年。今天写任何需要指出问题的邮件时，试着用这个句式替换指责。
