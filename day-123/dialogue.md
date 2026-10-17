🗣 每日对话 Day 123 — 写作日：第一周 sweep digest → 一封会被抄进 Handover Doc 的周报邮件

周日 | 写作表达（本周主题：用户大会落幕之后——把热度变成结构，把结构变成习惯；Day 118-122 的口语现场今天落笔成文）

─────────────────────────
✍️【背景回顾】
─────────────────────────

Day 121 的口语现场：#offline-bugs 开张第一天，频道 owner Maya 拉着 Leo 对口径，十分钟里处理了四件事——**P1 开工单（ticket #412，数据丢失）**、**全大写 @here 温和引导**、**三张同步工单 duplicate in 不 lump in**、**Infra 邻居 redirect the pipe**。收尾时 Leo 只提了一个要求：每班 sweep 之后发一行摘要——"Trust is built in the receipts."

一周过去了。频道活了：14 条 → 每天 6-8 条稳定输入，Maya 和新轮值人 Ben 各值三班，14 张工单里 P1 #412 周四复现成功、根因已修，三张同步工单两张确认同根合并，@here 越界从首周 4 次降到上周 0 次，两例跨频道"顺便看一眼"都改道成功。规矩不再是 Leo 的话，是频道自己长出来的样子。

然后 Leo 说了那句写作日专用台词：**"A digest is for a day. A report is for a quarter. And this week, they should be the same document."**（摘要管一天，报告管一季。而这一周，它们该是同一份文档。）

为什么？因为一行 digest 的读者是频道里的人，而周报的读者是**没空泡频道的人**——Elena 要的是"大会热度现在落到哪一步"；三个月后接手轮值的人要的是"这些规矩当初为什么定、什么情况下可以放宽"。口头结构（三桶、频道规矩、回执文化）在 Slack 里会沉底；写成一封邮件，它就成了可以抄进 Handover Doc 的正式记录。

写作日的正事：把一周的 sweep digest 汇总成**一封周报邮件**——数字带日期、规矩带理由、入口指向频道、异议窗口收口。对照着看你会发现：口语里那句 "trust is built in the receipts" 在书面里变成了整封邮件的骨架——**每个数字后面都站着一个日期，每条规矩后面都跟着一个可引用的出处。**

─────────────────────────
📝【正式邮件版】
─────────────────────────

**Subject:** #offline-bugs weekly report — Week 1: 14 tickets, 1 P1 resolved, norms holding

**To:** Leo (Senior Dev), Elena (VP Product), Ben (next rotation owner)
**Cc:** #offline-bugs channel (pinned)

Hi all,

One week in, here's the record for **#offline-bugs — Week 1 (Oct 12–16)**: 14 tickets opened from channel traffic, 1 P1 resolved, and every channel norm held without a single enforcement fight. The long version is below; the short version is the table at the end.

This email is the **first entry in what will become the handover doc** for channel owners — so the second half is about *how the norms worked*, not just what happened. Future owners: read this before your first sweep.

## 1. The week in numbers

- **14 tickets** opened from 62 channel messages (≈ 1 ticket per 4.4 messages; triage ratio will be a useful baseline going forward).
- **1 P1 (ticket #412, data loss):** opened Wed Oct 14 09:05, reproduced Thu Oct 15 16:40, root cause fixed and deployed Fri Oct 16 11:20. **E2E: 50 hours.**
- **3 sync-related tickets:** 2 confirmed same root cause and merged into #412 on Thu; 1 remains open, repro pending.
- **4 @here uses:** all four in the first 36 hours; zero since Thursday. The norm is landing — nobody had to be told twice.
- **2 cross-scope requests ("take a quick look at our caching bug"):** both redirected to #infra-help with a pointer, not a rejection. Both reporters thanked us — that's the "redirect the pipe, not the person" payoff.
- **0 messages lost to the void:** every message got either a ticket number, a redirect, or a "needs more info" note within one sweep.

## 2. What the numbers say

**"Trust is built in the receipts" — this week tested that twice.**

First: the P1. Wednesday morning it was an angry all-caps message we couldn't reproduce. Because we opened #412 *before* understanding it ("treat it like one"), when repro landed Thursday, the ticket already had 6 data points attached and diagnosis took hours, not days. **The lesson for future owners: the ticket is the unit of trust — open it early, even when — especially when — you can't reproduce yet.**

Second: the digest. The daily one-line digest ("Sweep 1: 1 P1 opened, 3 sync tickets, 1 redirected") did more for channel tone than any rule. Volume of @here and all-caps dropped to zero within four days — not because people were told to stop, but because they could *see* the pipeline working. **Receipts lower the temperature; rules don't.**

## 3. Norms that held (and one we bent)

For the handover doc, the Week 1 verdict on each norm:

| Norm | Week 1 verdict | Notes for future owners |
|------|---------------|-------------------------|
| @here = outage only | **Holding** | 4 uses → 0. Coach publicly, once, with the reason. |
| Duplicate in, don't lump in | **Holding** | 2 of 3 sync tickets merged *after* proof. Never merge on suspicion. |
| No drive-by "quick looks" | **Holding** | Redirect with a pointer ("#infra-help will give this the attention it deserves"). |
| Sweep digest after every shift | **Holding — barely** | Ben missed Tuesday PM's digest; backlog made Wednesday morning's sweep 25 min instead of 10. The digest is the norm that protects all the others. |

## 4. Week 2 changes

Two adjustments, both minor:

1. **Rotation confirmed:** Maya (Mon/Tue/Thu), Ben (Wed/Fri). Handover moment is Tuesday EOD and Friday EOD — five minutes, in-channel, so the next owner inherits context in public.
2. **Escalation path written down:** if a P1 can't be reproduced within 24h, it goes to Leo; if Leo's OOO, to Elena's staff meeting agenda. (This lived in Leo's head until Thursday; now it doesn't.)

## Next steps

| Item | Owner | When |
|------|-------|------|
| P1 #412 post-incident note (1 page) | Maya | Mon Oct 19 |
| Open sync ticket #437 — chase repro | Ben | by Wed Oct 21 |
| Weekly report #2 (same format, appended below this one) | Ben | Fri Oct 23 |
| Norms section added to pinned channel description | Maya | Mon Oct 19 |
| This email appended to Handover Doc v0 | Maya | ✅ Done (with this send) |

If I've miscounted anything or a norm verdict reads wrong, reply by **EOD Monday, Oct 19**. Barring that, this email is the Week 1 record — and the template Week 2 inherits.

Best,
Maya

─────────────────────────
🔄【口语 → 书面对照表】（15 个）
─────────────────────────

| # | Day 118-122 口语版 | Day 123 书面版 | 说明 |
|---|--------------------|----------------|------|
| 1 | Trust is built **in the receipts** | every message got either a ticket number, a redirect, or a "needs more info" note within one sweep | 隐喻 → 可验证的枚举（receipt 的三种形态） |
| 2 | **Treat it like one**（先按 P1 对待） | opened #412 *before* understanding it … repro landed Thursday, the ticket already had 6 data points attached | 押注指令 → 带时间戳的因果链（早开工单→诊断提速） |
| 3 | **Duplicate in, don't lump in** | 2 of 3 sync tickets merged *after* proof. Never merge on suspicion | 对仗口诀 → 规则条款（when to merge 的判据） |
| 4 | **Redirect the pipe, not the person** | redirected to #infra-help with a pointer, not a rejection. Both reporters thanked us | 隐喻 → 动作描述 + 结果（连"被改道的人道谢"都入账） |
| 5 | **Death by "quick look"** | No drive-by "quick looks" → **Holding** | 夸张警告 → 表格里的规范名 + 状态列 |
| 6 | @here is **reserved for** outages | @here = outage only … 4 uses → 0. Coach publicly, once, with the reason. | 规矩原话 → 规范表 + 执行注记（怎么教练的） |
| 7 | Sweep digest 是**保护其他规矩的规矩** | The digest is the norm that protects all the others | 口语判断 → 直接写进 verdict 备注 |
| 8 | Receipts **lower the temperature**, rules don't | not because people were told to stop, but because they could *see* the pipeline working | 口号 → 机制解释（归因写明） |
| 9 | **Lead with the help**, not the rule | 规范表里 coach 注记：Coach publicly, once, **with the reason** | 回应次序原则 → 执行细则的一部分 |
| 10 | The ticket **is the unit of trust** | The lesson for future owners: the ticket is the unit of trust — open it early | 口语金句 → handover 教训（写给未来读者的位置） |
| 11 | 口头说 **"下一班 4 点"** | Next sweep cadence: rotation confirmed, handover moment is Tuesday EOD / Friday EOD | 口头交接 → 写死的时刻表（Owner + 频率 + 场所） |
| 12 | "问 Leo"（口头升级路径） | if a P1 can't be reproduced within 24h, it goes to Leo; if Leo's OOO, to Elena's staff meeting | 脑子里的路径 → 写下来的 escalation 条款（带 fallback） |
| 13 | 频道"活了"（14 条 → 每天 6-8 条） | 14 tickets opened from 62 channel messages (≈ 1 per 4.4; baseline going forward) | 感受 → 基线数字（本周立标尺，下周好对比） |
| 14 | 一周 14 张工单（随口报数） | opened Wed 09:05, reproduced Thu 16:40, fixed Fri 11:20. **E2E: 50 hours** | 模糊回顾 → 三时间戳 + 换算好的端到端时长 |
| 15 | "This one wins"（版本收口） | reply by **EOD Monday, Oct 19**. Barring that, this email is the Week 1 record | 语气威慑 → 异议窗口（silent approval，过期即生效） |

**对照表使用法**：左列是你这周说过的话，右列是写进周报的句。周报书面的核心不是"更正式"，是**让不在场的人也能审计**——每个数字有时间戳，每条规矩有执行注记，每次"没出事"都写清楚"为什么没出事"。口语的读者在场景里，书面的读者在三个月后。

─────────────────────────
✍️【写作技巧讲解】（6 个）
─────────────────────────

**1. 周报的第一读者是"未来的陌生人"**
频道里的人看过每天的 digest，他们不需要这封邮件。真正需要它的是 Elena（要一眼看到大会热度落地进展）、和三个月后接手轮值的 Ben 们——对他们来说 Week 1 只是传说。所以开头就声明文档地位："the first entry in what will become the handover doc"。写周期性报告前先问：**这封信六个月后会被谁在什么情况下翻出来？** 为那个读者写。

**2. 数字要换算成基线，不能只报流水**
"14 tickets from 62 messages" 是流水账；"≈ 1 ticket per 4.4 messages — baseline going forward" 是基线。基线的价值是让下周可以对比：输入没变但比例变了，说明频道里聊的内容在变味；比例没变但情绪变差，说明 digest 断了。**书面的数字要给未来的自己留一个比较的锚点**，否则它只是本局的得分，不是历史的数据。

**3. 时间戳三件套：opened / reproduced / resolved**
P1 #412 的三个时间戳一字排开（Wed 09:05 → Thu 16:40 → Fri 11:20），最后主动换算 E2E: 50 hours。为什么不让人自己算？因为**读者永远不该做算术**——你给原始时间戳是可审计，你给换算结果是可引用。Elena 转发这封邮件时引的会是"50 小时端到端"，不会是三个日期。

**4. 规矩要用"verdict 表"复盘，不能只列清单**
Week 1 四条规矩，三条 **Holding**，一条 **Holding — barely**。这个 "barely" 是全表最值钱的词：Ben 周二漏发 digest，周三早上 sweep 从 10 分钟变 25 分钟——后果立刻写上。诚实的 verdict 表比全绿的表更可信，而且它顺手变成了下周的改进项。**报告里给"差点没守住"留一栏，规矩才会越守越牢。**

**5. 口头共识必须在第一周内落成文字**
"Escalation path lived in Leo's head until Thursday; now it doesn't." ——那句 "now it doesn't" 就是书面化的全部意义。任何"大家都知道"的安排（谁顶班、怎么升级、什么算 P1）都有一个保质期：**直到第一个当事人休假为止**。写作日的心法：本周任何口头达成的共识，挑最重要的写进文档——不是因为你记性差，是因为文档的读者名单里有"未来的你"。

**6. 异议窗口 + 模板自认（silent approval 的周报版）**
"Reply by EOD Monday, Oct 19. Barring that, this email is the Week 1 record — and the template Week 2 inherits." 前半句是标准异议窗口；后半句是模板自认——直接宣布本周报就是以后周报的格式。这比"请提格式意见"强得多：**默认值你已经设好了，反对的成本高于顺从的成本**，格式就会稳定下来。Day 97/104/119 的收尾都是这个骨架，今天是它的周报变体。

─────────────────────────
🎧【朗读版】（音频文字稿：周五傍晚，Maya 把周报初稿读给 Leo 听）

A (Maya): Final read before I send the weekly. Opening: "14 tickets opened from 62 channel messages — approximately 1 per 4.4 messages. Triage ratio will be a useful baseline going forward." Do we need the ratio?
B (Leo): Do we need *history*? Yes. The count is this week's score; the ratio is the number next week argues with.
A: The P1 section. I wrote the timestamps as one line — "opened Wednesday 09:05, reproduced Thursday 16:40, fixed Friday 11:20 — end to end, 50 hours."
B: Good. Readers should never do arithmetic. Keep the stamps for audit, give the math for quoting.
A: Hardest part was the norms table. Watch the last row — "Sweep digest: Holding — barely. Ben missed Tuesday PM's digest; Wednesday's sweep took 25 minutes instead of 10. The digest is the norm that protects all the others."
B: That "barely" is the most valuable word in the email. A table that's all green teaches nobody anything.
A: And the escalation path — "lived in Leo's head until Thursday; now it doesn't."
B: My favorite clause I never wrote. Anything you left out that should be in?
A: The thanks. Both redirected reporters thanked us in-channel — I logged it under the redirect norm, but it felt like bragging.
B: That's not bragging, that's evidence. The norm *worked*, twice, measurably. Leave it exactly where it is.
A: Last line: "Reply by EOD Monday. Barring that, this email is the Week 1 record — and the template Week 2 inherits."
B: Send it. And Maya — one week ago you asked me what to do with five messages and a shaky hand.
A: And now I'm writing the handover doc for whoever's shaky next. The thread ages better. I heard.

─────────────────────────
🔄【变造挑战】（3 题）
─────────────────────────

用今天学到的表达，换场景重新写（书面练习）：

1. 你是小区业委会的"业主群治理负责人"，试行了一周新规矩：广告必须发到二手群、电梯报修走小程序工单、群里只讨论公共事务。一周下来：37 条消息里 6 单报修、2 条广告被改道、1 次全群 @ 引导成功、电梯 #3 周四修复。写这封**周报**发到群里，含：数字基线、规矩 verdict 表（其中"深夜免打扰"那条只做到 barely holding）、下周改进、异议窗口。
   💡 提示：先给"数字换算成基线"（1 工单/6.2 条消息——立下周对比锚点）+ verdict 表四行、一行 barely + "下周改什么"跟 barely 对应 + "回我到周日晚，之后本帖为定稿"

2. 你组织的朋友圈"读书打卡群"满 200 人，第一周轮值统计：打卡 84 人次、精华帖 5 条、2 人问"能不能发带货链接"被劝到专门的团购群、1 条深夜吵架帖被引导去私聊。现在要写**第一周轮值报告**固定成模板，让下一任轮值直接抄。哪些数字要设基线？哪些规矩要写 verdict？
   💡 提示：模板自认收尾（"本帖即模板，下周照此格式"）+ 数字换算（84 人次/200 人 = 参与率 42%——这是参与度基线）+ "吵架帖引导私聊"写执行注记（怎么引导的：先共情后转场）+ 手滑一处也要写（漏发某天 digest？）

3. 公司"新人答疑频道"你建的头一个月，月报要发给 HR 和全部门。数据：46 个问题、38 个已答、8 个待定（卡在等产品确认）、3 次跨部门"顺便问一下"改道成功、答案沉淀进 FAQ 12 条。老板只有 30 秒。写**月报开头三句话**（BLUF）+ 一张 verdict 表。
   💡 提示：BLUF 三句 = 一句话状态（46/38/8）+ 一句话最亮结果（12 条沉淀进 FAQ = 频道从"消耗时间"变"节省时间"的证据）+ 一句话指向正文 + verdict 表把"答案沉淀进 FAQ"也当一条规范打分（这是最容易被忽略但最值钱的规矩）

─────────────────────────
💡【今日一句】
─────────────────────────

**"A digest is for a day. A report is for a quarter. And this week, they should be the same document."**
（摘要管一天，报告管一季。而这一周，它们该是同一份文档。）

口语的产出是"当下被理解"，书面的产出是"以后能查"。一行 digest 的保质期是一天，但它积累一周就成了周报的原料；周报的保质期是一周，但它写下的规矩和基线会活进 handover doc，活到接手的人手里。你每天发的那些"小回执"，其实都是未来某份大文档的草稿——**写得认真一点，未来的你就抄得轻松一点。**

─────────────────────────
🎧【往期回顾】
─────────────────────────
- Day 118 周三 — 大会后 12 条 DM 的三桶分诊（make the rounds / triage / low-hanging fruit）
- Day 119 周六（写作日）— 分诊 → 三方都会转发的跟进邮件（本篇格式原型）
- Day 120 周一 — 400 条回复的帖子怎么"毕业"（not lock — graduate / sweep / route, not fix）
- Day 121 周三 — Maya 第一班 sweep 实战（sanity check / duplicate in, don't lump in）
- Day 122 周五 — 第18周复习：33 个语块速查+3个新场景重练
- 剧情线：10/3 大会落幕 → 118 分诊 DM → 119 跟进邮件 → 120 频道结构化 → 121 第一班 sweep → 122 复习收束 → 今天写作日：一周 digest 汇总成周报，handover doc 开篇。下一步：Day 124 周一回归工作讨论（剧情预告：轮值交棒，Ben 的第一班）

（变造挑战参考答案将在 Day 124 推送中公布）
