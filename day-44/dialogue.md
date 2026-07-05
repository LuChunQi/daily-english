🗣 每日对话 Day 44 — Sprint 排期博弈：当需求多过产能
周一 | 第7周 · 专项突破——工作讨论深度场景

─────────────────────────
📖【完整对话】
─────────────────────────

**场景：** Sprint Planning 会议。团队本迭代产能有限，但产品和业务方都插需求。工程经理 Sarah 和产品经理 Jake 需要协商排期，技术负责人 Wei 也要表态。

**A — Sarah (Engineering Manager)**
**B — Jake (Product Manager)**
**C — Wei (Tech Lead)**

---

**A (Sarah):** Alright, let's get into sprint planning. We've got capacity for about 120 story points this sprint, but the backlog has roughly 200. We need to make some hard calls today.
> 好的，我们开始排期会吧。这迭代我们大概有 120 故事点的产能，但待办池里差不多有 200 点。今天得做一些艰难的决定。

**B (Jake):** I hear you, but everything in the backlog is marked "urgent" by someone. The checkout flow redesign is the CEO's pet project, and the payment gateway migration has a hard deadline end of this month.
> 我理解，但待办池里每件事都被某个人标成"紧急"。结账流程改版是 CEO 的心头好，支付网关迁移这个月底有硬截止。

**A (Sarah):** I get that both are important, but we literally can't do both full justice in two weeks. If we split the team, we'll end up half-baking both and shipping neither on time. I'd rather we sequence them properly.
> 我知道两个都重要，但两周内我们真的没法把两个都做好。如果团队拆开做，两个都会半吊子，最后都按时交不了。我宁可我们合理安排先后顺序。

**C (Wei):** If I can chime in — the payment migration is mostly backend work that Raj and I can handle independently. The checkout redesign needs heavy frontend and design collaboration. So they're not actually competing for the same people.
> 我插一句——支付迁移主要是后端活，Raj 和我可以独立搞定。结账改版需要大量前端和设计协作。所以它们其实不抢同一拨人。

**B (Jake):** That's a fair point, Wei. So we could run them in parallel if we staff them right. But that still leaves the analytics dashboard upgrade and the bug fixes from last sprint's escalation completely out.
> 有道理，Wei。那如果我们人员配得对，可以并行跑。但这样分析看板升级和上迭代线上故障的 bug 修复就完全排不进来了。

**A (Sarah):** The post-escalation fixes are non-negotiable. Those are P1 bugs affecting paying customers — we can't let them linger. I'm putting my foot down on that one.
> 线上故障的修复没得商量。那些是影响付费用户的 P1 bug——不能拖。这件事我坚持。

**B (Jake):** OK, I won't fight you on the bug fixes. But can we at least scope the checkout redesign down to an MVP? If we cut the personalization piece and just ship the streamlined flow, that saves what, 30 points?
> 行，bug 修复我不跟你争。但结账改版能不能至少缩到 MVP？如果砍掉个性化推荐那块，只做精简流程，那能省掉……30 点？

**C (Wei):** Closer to 35 if we also drop the A/B test framework setup. We can always bolt that on next sprint once the core flow is live. Ship the foundation, iterate on top.
> 如果连 A/B 测试框架也先不做，能省 35 点左右。核心流程上线后，下迭代再叠上去就行。先发地基，再迭代。

**B (Jake):** I can live with that. So the plan is: bugs first, payment migration in parallel on the backend, and a scoped-down checkout MVP on the frontend. The analytics dashboard gets pushed to next sprint?
> 可以接受。那计划就是：先修 bug，支付迁移后端并行，结账 MVP 前端做。分析看板推到下迭代？

**A (Sarah):** Exactly. And let's document what we're deferring and why, so nobody's caught off guard when they ask why their feature didn't make the cut. I'll send out a summary after this meeting.
> 没错。我们把推迟了什么、为什么推迟都记下来，这样别人问起来为什么他的需求没排上，也不至于被打个措手不及。会后我发个总结。

**B (Jake):** Sounds like a plan. One last thing — if the checkout MVP wraps up early, can the frontend folks pick up a couple of dashboard tickets?
> 就这么定了。最后一件——如果结账 MVP 提前做完，前端的人能不能捡几个看板的 ticket？

**A (Sarah):** Let's cross that bridge when we come to it. I don't want to over-commit on day one. If we finish early, we'll reassess and pull from the top of the backlog.
> 到时候再说吧。我不想第一天就过度承诺。如果真提前完成了，我们重新评估，从待办池最上面拉。

---

─────────────────────────
🎯【语块精讲】（8 个）
─────────────────────────

**1. make some hard calls**
做出艰难的决定/取舍（call = decision）
- 工作场景：We've got to make some hard calls on the budget this quarter.（这季度预算上我们得做些艰难取舍。）
- 日常场景：Choosing between the two job offers was a hard call.（在两份 offer 之间选择真不容易。）

**2. do something full justice**
把某事做到位、充分发挥（反义：half-bake 敷衍了事）
- 工作场景：If we rush both projects, we won't do either full justice.（如果赶两个项目，哪个都做不好。）
- 日常场景：You should take your time with the presentation to do it full justice.（演示要做好，别赶。）

**3. split the team / staff them right**
拆分团队 / 合理配人手
- 工作场景：If we split the team across three projects, quality will suffer.（团队拆三个项目，质量肯定下降。）
- 日常场景：They staffed the event right — enough volunteers, no chaos.（活动人手配得好——志愿者够，没乱套。）

**4. chime in**
插话、补充意见（比 interrupt 更礼貌，表示建设性发言）
- 工作场景：If I can chime in — I think we're overcomplicating this.（我补充一句——我觉得这事搞复杂了。）
- 日常场景：Feel free to chime in if you have ideas.（有想法随时插嘴。）

**5. non-negotiable / put my foot down**
没得商量的 / 态度强硬起来
- 工作场景：The deadline is non-negotiable — the client is expecting delivery.（截止日期没商量——客户等着交付。）
- 日常场景：I put my foot down when they tried to change the rules mid-game.（他们比赛中途想改规则，我没答应。）

**6. scope down to an MVP**
把范围缩减到最小可行版本
- 工作场景：Let's scope this down to an MVP and iterate based on user feedback.（先缩到 MVP，根据用户反馈迭代。）
- 日常场景：We scoped down the wedding to just close family.（婚礼缩减到只有至亲参加。）

**7. bolt on / ship the foundation, iterate on top**
附加功能 / 先发基础再迭代
- 工作场景：We can bolt on analytics next quarter — ship the core first.（分析功能下季度再加——先把核心发了。）
- 日常场景：Start with a basic workout routine, then bolt on accessories later.（先从基础训练开始，再加辅助项目。）

**8. cross that bridge when we come to it**
到时候再说（不过早担心还没发生的事）
- 工作场景："What if the API breaks?" "Let's cross that bridge when we come to it."（"万一 API 挂了？" "到时候再说。"）
- 日常场景：Don't worry about the exam results yet — cross that bridge when you come to it.（别急着想考试成绩——到时候再说。）

**Bonus: caught off guard / make the cut**
- caught off guard：被打个措手不及（be surprised, unprepared）
- make the cut：达标、入选（from sports — reaching the qualifying standard）

─────────────────────────
🔄【变造挑战】（3 题）
─────────────────────────

用今天学到的表达，换场景重新说：

**1.** 你的朋友想同时学吉他、学法语、开始健身，你建议他一次专注一件事。
   💡 提示：用 "split / do full justice / sequence" 的思路

**2.** 开会时同事提出了一个方案，你想礼貌地补充一个不同的角度。
   💡 提示：用 "chime in / if I can / from my perspective"

**3.** 老板问"如果项目提前做完能不能加活"，你想委婉地说先别急。
   💡 提示：用 "cross that bridge / over-commit / reassess"

─────────────────────────

💡 **今日一句：**
> **"I'd rather we sequence them properly."**
> 宁可排好先后，也别一锅炖。这句话在排期、资源分配、优先级讨论中极其好用——简洁、专业、有主见。今天试着找个场景用一次！
