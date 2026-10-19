🗣 每日对话 Day 125 — Sweep 复盘会：三个问题、一份 Wiki 页、一次交棒
周二 | 会议发言（本周主题：把热度变成结构之后——让结构自己跑起来）

> 剧情线：Day 124 周一，Maya 锁掉了 DevCon 巨帖、拿到了 wrap-up 主导权，还向 Leo 立了 flag：趁细节没淡，约一次 sweep 实验 retro。今天就是这场 retro——Maya 主持，频道里三位轮值同事（Ben、Chloe、Dev）到场，Leo 列席旁听。三十分钟，Maya 只准备了三个问题。会开到第 25 分钟，Ben 主动请缨下一班——Maya 的交棒时刻提前来了。

─────────────────────────
📖【完整对话】
─────────────────────────

**A (Maya, channel owner / retro host):** Thanks for making time, everyone. Thirty minutes, three questions on the board: what worked, what didn't, and what we keep. I'll take notes on the wiki page in real time, so what we say is what gets written — no memory games afterward.
（谢谢大家抽时间。三十分钟，白板上就三个问题：什么有效、什么没用、什么保留。我实时记在 wiki 页上——会上说什么，纸上就写什么，会后不玩记忆游戏。）

**B (Ben, Backend Dev):** Efficient. Last retro I went to had forty-one slides and no decisions. So — what worked, I'll start: the two-a-day sweep rhythm. Ten minutes, morning and late afternoon. It caught duplicates before they multiplied.
（够高效。我上次参加的复盘会有四十一页幻灯片、零个决定。那"什么有效"我先来：一天两班的清扫节奏。十分钟，早上一次、傍晚一次。重复报告还没繁殖就被拦住了。）

**A:** Captured — "two-a-day cadence caught dupes early." Chloe, anything from your week?
（记下了——"一天两班节奏，早拦重复"。Chloe，你那周有什么？）

**C (Chloe, Support Lead):** The digest line, honestly. Thirty seconds after every sweep, and users stopped piling on with "any update?" because the update cadence was visible. It's the cheapest trust-building tool I've ever used.
（说实话，是那条摘要。每班扫完三十秒发一条，用户就不再追问"有进展吗"了——因为更新节奏是看得见的。这是我用过最便宜的信任建设工具。）

**D (Dev, Frontend Dev):** Counterpoint, and it's mine to own. The wiki entry fee was too high. To submit a bug properly you needed a repo, a log, a screenshot — the form was a mile long. I watched two users give up halfway through.
（反方观点，而且这锅是我的。wiki 的进门门槛太高了。要正经提一个 bug，你得有复现步骤、日志、截图——表单长得没边。我亲眼看着两个用户填到一半放弃了。）

**A:** Good — that's exactly the kind of thing this meeting is for. Logged as "entry friction: form too long, drop-off observed." Is the fix to shorten the form, or to stage it?
（很好——这正是这场会存在的意义。记为"进门摩擦：表单太长，观察到中途放弃"。修法是砍短表单，还是分步？）

**D:** Stage it. Title and severity first — that's all triage needs. The rest of the fields can appear after the ticket exists, optional, fill-if-you-can. The pipe shouldn't interrogate people at the door.
（分步。先只要标题和严重度——分诊只需要这两样。其余字段等工单建好之后再展开，选填，能填则填。管道不应该在门口审问人。）

**B:** Seconded. Also — do we still need @here reserved for outages only? Two weeks in, the norm has held. Maybe write it into the channel description so it survives us.
（附议。另外——"@here 只留给服务中断"这条还需要吗？两周下来规矩立住了。也许该写进频道简介，让它活得比我们久。）

**A:** Good call — that's a "keep and codify." I'll draft the description tonight. Now, the awkward one: the rotation. Next week's slot is open, and I'm stepping back to let it rotate properly.
（好建议——这条记"保留并成文"。我今晚起草频道简介。现在说个有点尴尬的事：轮值表。下一周的班还空着，而我打算退出来，让轮值真正转起来。）

**B:** …I'll take it. I was going to wait and see who volunteered, but that's how the whole thing dies, isn't it — everyone waiting, nobody sweeping. Put me down.
（……我来吧。我本来想等等看谁举手，但整件事不就是这么死的吗——人人都在等，没人在扫。把我写上。）

**A:** Done — Ben owns next week. And one more thing before we wrap: Leo's been sitting quietly in the corner, which either means he approves or he's asleep. Leo?
（定了——下周 Ben 当班。收尾前还有一件事：Leo 一直安静地坐在角落，这要么说明他赞成，要么说明他睡着了。Leo？）

**D (Leo, Tech Lead):** Awake, and impressed. You ran a retro with no slides, captured decisions live, and handed off the baton before anyone asked. That's the whole lifecycle — build, run, document, hand over. The channel doesn't need me anymore. That's not a loss, that's the goal.
（醒着，而且很欣慰。你开了一场没有幻灯片的复盘、实时记下了决定、没等任何人开口就把接力棒交了出去。这就是完整的生命周期——搭建、运转、成文、交棒。这个频道不再需要我了。这不是损失，这本来就是目标。）

**A:** Then the last line of the wiki page writes itself: "Retro complete. Rotation alive. Page closed — reopening is one edit away."
（那 wiki 页的最后一行自己写好了："复盘完成。轮值运转中。本页关闭——重开只需一次编辑。"）

─────────────────────────
🎯【语块精讲】（8+1 个）
─────────────────────────

• **make time** — 抽出时间（不是"有时间"，是"挤时间"；比 find time 更主动、更职场）
  工作场景：Thanks for making time on such short notice.
  （谢谢你临时也抽得出时间。）
  日常场景：Let's make time for a proper dinner this week — no phones.
  （这周抽个时间好好吃顿饭——不带手机的那种。）

• **no memory games** — 不玩记忆游戏（= 白纸黑字，当场锁定；会后谁说了什么都不算数）
  工作场景：Decisions go in the doc as we speak them — no memory games.
  （决定边说边写进文档——会后不靠回忆。）
  日常场景：Let's write the plan down now — no memory games at midnight when we're tired.
  （现在就把计划写下来——免得半夜累了我俩各记一版。）

• **catch (something) before it multiplies** — 在它繁殖之前拦住（问题早发现早处理，成本指数级低）
  工作场景：The daily sweep catches dupes before they multiply.
  （每日清扫在重复报告繁殖之前就把它们拦住。）
  日常场景：Fix the drip now — catch it before it multiplies into a flood.
  （现在就修那个滴水——趁它还没变成洪水。）

• **(the) entry fee is too high** — 门槛太高（进门的代价太贵；说得形象，不伤人）
  工作场景：Ten required fields? The entry fee is too high — users will bounce.
  （十个必填项？门槛太高了——用户会直接走人。）
  日常场景：That gym charges a joining fee, a monthly fee, and a class fee — the entry fee is too high.
  （那家健身房收入会费、月费、课时费——进门成本太高了。）

• **the pipe shouldn't interrogate people at the door** — 管道不该在门口审问人（流程要放人进来，不是吓跑人）
  工作场景：Ask for email only at signup — the pipe shouldn't interrogate people at the door.
  （注册时只要邮箱——管道不该在门口审问人。）
  日常场景：The visa form wanted my grandmother's address. The pipe interrogates you at the door.
  （签证表连我奶奶的地址都要。真是在门口审问人。）

• **keep and codify** — 保留并成文（口头行之有效的东西写成明文规矩，让它"活得比人久"）
  工作场景：The norm held for a month — time to keep and codify it in the handbook.
  （规矩立了一个月——该写进手册"保留并成文"了。）
  日常场景：Our "no phones at dinner" rule works. Let's keep and codify it on the fridge.
  （"吃饭不看手机"这规矩很有效。写下来贴冰箱上吧。）

• **that's how the whole thing dies** — 整件事就是这么死的（指出机制性死因，语气重但针对事不针对人）
  工作场景：If everyone waits for someone else to volunteer, that's how the whole thing dies.
  （如果人人都等别人举手，整件事就是这么死的。）
  日常场景：Nobody refills the water, everybody assumes someone did — that's how the whole thing dies.
  （没人续水，人人都以为别人续了——事情就是这么完蛋的。）

• **hand off the baton** — 交出接力棒（正式移交；比 hand over 更有"接力继续跑"的画面感）
  工作场景：She handed off the baton at the peak of the project — smart timing.
  （她在项目最高点交出接力棒——时机很聪明。）
  日常场景：I'm handing off the baton on carpool duty to your dad next month.
  （下个月拼车接送的班交给你爸。）

• **reopening is one edit away** — 重开只需一次编辑（优雅关门的收尾句：门关了，但没焊死）
  工作场景：We're closing the channel — reopening is one edit away if usage returns.
  （我们关闭这个频道——如果使用量回来，重开只需一次编辑。）
  日常场景：The book club is on pause — reopening is one message away.
  （读书会暂停中——重开只需一条消息。）

─────────────────────────
🔄【变造挑战】（3 题）
─────────────────────────
用今天学到的表达，换场景重新说：

1. 你主持家庭群的新规矩复盘会：红包接龙不能刷屏、团购走小程序、深夜不发语音。三条规矩试了两周，其中"深夜免打扰"执行得磕磕绊绊。你怎么开场，又怎么记录？
   💡 提示：用 **make time** 开场 + **no memory games** 说明你边说边记。

2. 小区业委会的线上报修小程序，业主们抱怨"填的东西太多，修个灯泡要填十分钟"。你是业委会成员，在复盘会上怎么提这个问题？
   💡 提示：用 **the entry fee is too high** + **the pipe shouldn't interrogate people at the door**。

3. 你所在的读书会，会长说"下个月谁来组织？大家自愿报名"，然后群里一片安静。你想打破沉默。
   💡 提示：用 **that's how the whole thing dies** 说机制，用 **hand off the baton** 或自己 **put me down** 破局。

💡 今日一句：**What we say is what gets written — no memory games.** — 开会最大的浪费是"会上说清楚了，会后各记一版"。今天找一次会议，把这句话用上：当场记，当场锁。

─────────────────────────
🎧 音频：day-125/dialogue.mp3
