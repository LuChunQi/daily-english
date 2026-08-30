# 🗣 每日对话 Day 99 — 接手离职同事的核心系统：把"隐性知识"挖出来

周一 | 第15周主题：交接与知识传承（Handover & Knowledge Transfer）

> 场景：Tom（后端工程师）下周离职，他负责的支付回调系统要交接给你（Leo）。今天是最后一次交接会——文档已经看完，但真正要紧的东西，还没写下来。

─────────────────────────
📖【完整对话】
─────────────────────────

**A (Tom, leaving engineer):** Alright, this is our last handover session before I leave. Today I want to walk you through the payment callback system — it's the piece I'm most worried about leaving behind.
（好，这是我离开前最后一次交接会。今天带你过一遍支付回调系统——这是我最放心不下的一块。）

**B (Leo, taking over):** Appreciate it. I've skimmed the docs, but honestly it felt like drinking from a firehose. There's a lot going on under the hood.
（谢谢。文档我大致翻过了，但说实话像对着消防水管喝水，信息量太猛。表层底下还藏着太多东西。）

**A:** Yeah, the docs cover the happy path, but a lot of the tricky stuff is tribal knowledge — it lives in my head, not in Confluence.
（是的，文档只覆盖正常流程，那些坑人的东西都是"部落知识"——在我脑子里，不在 Confluence 里。）

**B:** That's exactly what I was afraid of. Right now, you're basically the single point of failure for this system.
（这正是我担心的。现在你就是这个系统的单点故障。）

**A:** Fair. So here's what I'd suggest: for my last week, let's do a pairing session every morning. You drive, I watch — and anything you stumble on, we document as we go.
（有道理。所以我建议：最后一周每天上午结对。你来操作，我在旁边看——你卡住的地方，咱们边做边记下来。）

**B:** That works for me. Can I also pick your brain on the incident from March? The one where callbacks backed up for six hours?
（可以。另外我能请教一下三月那次事故吗？回调积压六小时那次。）

**A:** Good question — that one never made it into the postmortem. Short version: the queue consumer deadlocked, and the retry logic actually made it worse. I'll leave a paper trail in the runbook so it never gets lost again.
（问得好——那次的事后报告里压根没写全。简短版：队列消费者死锁了，重试逻辑反而火上浇油。我会在 runbook 里留下完整记录，这事儿再也不能丢了。）

**B:** Please do. And once you're gone, who runs point on this? Should I own it end to end?
（务必。那你走之后谁来牵头？我是不是要端到端负责？）

**A:** I'd say yes, but loop in Rachel — she knows the banking side. And one more thing: don't try to fix everything at once. Get the runbook solid first, refactor later.
（我觉得是，但把 Rachel 拉进来——她懂银行那一侧。还有一句：别想一次修完所有问题。先把 runbook 做扎实，重构以后再说。）

**B:** Got it — small steps, good docs. Thanks, Tom. This actually makes me feel a lot better about taking over.
（明白——小步走，文档齐。谢了 Tom，这么一交接，我心里踏实多了。）

─────────────────────────
🎯【语块精讲】（8+1 个）
─────────────────────────

• **drink from a firehose** — 信息量大到根本来不及消化
  工作场景：Onboarding week felt like drinking from a firehose — five systems, three repos, zero docs.
  （入职第一周像对着消防水管喝水——五个系统、三个代码库、零文档。）
  日常场景：Visiting Tokyo for the first time? It's a lot — don't try to drink from the firehose, pick two neighborhoods.
  （第一次去东京？东西太多了，别贪多，挑两个街区逛就好。）

• **under the hood** — 表面之下；内部机制（技术圈高频）
  工作场景：The API looks simple, but under the hood there are seventeen microservices.
  （这个 API 看着简单，底下其实有十七个微服务。）
  日常场景：This car is quiet, but under the hood it's a 400-horsepower engine.
  （这车开起来安静，引擎盖底下可是 400 匹马力。）

• **tribal knowledge** — 部落知识：只存在于少数人脑子里、没写成文档的隐性知识
  工作场景：Half our deploy process is tribal knowledge — if Dave quits, we're stuck.
  （我们一半的部署流程都是"部落知识"——Dave 一离职我们就抓瞎。）
  日常场景：Ask Grandma for the recipe — it's tribal knowledge, it's not written anywhere.
  （问奶奶要菜谱吧——全在她脑子里，哪儿都没记。）

• **single point of failure** — 单点故障（人 or 系统都适用）
  工作场景：Tom was the single point of failure — one person leaving shouldn't take down a whole system.
  （Tom 就是单点故障——一个人离职不该拖垮一整个系统。）
  日常场景：We only kept one copy of the house key. That's a single point of failure.
  （家里钥匙只留了一把，这就是单点隐患。）

• **document as you go** — 边做边记录，别攒到最后
  工作场景：Don't wait until the project ends — document as you go, even messy notes help.
  （别等项目结束才写文档——边做边记，哪怕是乱糟糟的笔记也有用。）
  日常场景：Moving apartments? Document as you go — label every box the moment you tape it.
  （搬家也是同理——边搬边记，封箱的瞬间就贴上标签。）

• **pick someone's brain (about/on)** — 请教某人；"借用一下你的脑子"
  工作场景：Do you have 15 minutes? I'd love to pick your brain about the billing migration.
  （有 15 分钟吗？想请教一下计费迁移的事。）
  日常场景：You've been to Kyoto twice — can I pick your brain on where to stay?
  （你去过两次京都——能取取经住哪儿合适吗？）

• **leave a paper trail** — 留下书面痕迹，可追溯
  工作场景：For anything money-related, always leave a paper trail — email beats verbal.
  （凡是涉及钱的事，一定留下书面记录——邮件胜过口头。）
  日常场景：Keep every receipt during the trip so you can expense it later. Leave a paper trail.
  （出差期间留好所有发票，回头才能报销，留个凭证。）

• **run point (on)** — 牵头负责某事（源自篮球"控球组织进攻"）
  工作场景：I'll run point on the migration — you all just unblock me when I yell.
  （迁移这事我来牵头——我一喊卡住你们就来搭把手就行。）
  日常场景：For the family reunion, Aunt May is running point on logistics.
  （家庭聚会这次是梅姨总管后勤。）

• 🎁 **make it into + 地方** — 成功进入/被收录进（本课彩蛋）
  工作场景：That incident never made it into the postmortem — let's fix that.
  （那次事故没写进事后报告——补上。）
  日常场景：His joke didn't make it into the final cut of the video.
  （他的段子在视频成片里被剪掉了。）

─────────────────────────
🔄【变造挑战】（3 题）
─────────────────────────
用今天学到的表达，换场景重新说：

1. 你刚转到新团队，接手的系统几乎没有任何文档，前任也联系不上了。向你的经理描述这个处境（用 firehose 和 tribal knowledge）。
   💡 提示：It feels like drinking from a firehose — most of the setup is tribal knowledge, and the guy who knew it is gone.

2. 老板在会上问谁愿意牵头一个跨团队的迁移项目，你答应了，但需要数据组的人配合（用 run point 和 loop in）。
   💡 提示：Happy to run point on it — as long as we can loop in someone from the data team.

3. 资深同事下周开始休假三周，你想在他走之前请教他一个关于性能优化的问题（用 pick your brain）。
   💡 提示：Before you head off — could I pick your brain on the caching issue? Thirty minutes max.

💡 今日一句：**Can I pick your brain on the incident from March?**
（pick someone's brain 是职场最自然的请教开场白——今天找个机会，跟同事"借脑子"用一次。）

─────────────────────────
📚 复习锚点
─────────────────────────
本课回收复用：walk through (Day 22/47) · happy path (Day 68) · loop in (Day 02) · stumble on → good catch 家族
下周五复习日将把 Day 99-102 语块汇总重练。
