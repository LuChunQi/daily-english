🗣 每日对话 Day 101 — On-call 首秀：Slack 上处理第一个 Page
周三 | 日常沟通（Slack 排障协调）

> 剧情连续：Day 99 你接手了离职同事的核心数据管道，Day 100 周会上正式接下 pager。今天是你 on-call 的第一个早晨——6 点，手机响了。

─────────────────────────
📖【完整对话】
─────────────────────────

**场景：早上 6:40，你（Leo）被告警叫醒，排查后发现问题出在数据科学团队昨晚新上的任务，于是在 Slack 上找到对方团队工程师 Maya。**

**A (Leo, Data Platform 新 Owner):** Morning Maya, got a sec? I'm on-call for the data platform this week — first week, actually — and I got paged at 6 AM. The ingestion queue is badly backed up.
（早啊 Maya，有空吗？这周我负责数据平台的 on-call——其实是第一周——今早 6 点就被 page 了。数据摄入队列严重堆积。）

**B (Maya, Data Science 工程师):** Oh no, sorry to hear that! Is it affecting anything downstream, or is it just slow?
（糟糕，抱歉听到这个！有影响到下游吗，还是只是慢？）

**A:** A few dashboards are stale, but nothing user-facing yet. I went through the runbook and traced the backlog back to the batch job that rolled out yesterday afternoon — it's pushing about ten times the usual volume.
（几个看板的数据已经过期了，但还没有影响到面向用户的功能。我翻了值班手册，把堆积追溯到你团队昨天下午上线的批处理任务——它的量大概是平时的十倍。）

**B:** Ah, that would be us. We're backfilling six months of training data for the new model. I didn't realize it would hammer the shared queue like that — my bad for not giving you a heads-up.
（啊，那就是我们了。我们在给新模型回填六个月的训练数据。没想到会把共享队列打成这样——没提前跟你打个招呼是我的疏忽。）

**A:** Totally understandable — the handover docs don't spell out how much headroom the queue has, so that's on the docs as much as on you. Could you throttle the job back until the backlog clears?
（完全理解——交接文档里根本没写队列还剩多少余量，所以这事儿一半怪文档、一半怪你。能把任务降速跑，等积压清完再提速吗？）

**B:** Sure, I can dial it down to 20% right now. Is that enough, or do you want me to pause it altogether?
（可以，我现在就降到 20%。够吗，还是干脆先全停？）

**A:** 20% should do it — the queue drains at about 5,000 events a minute, so give it two or three hours to catch up. If it's not clearing by lunch, pause it and resume tonight when traffic is lighter.
（20% 应该够了——队列每分钟能消化 5000 条事件，给它两三个小时就能追平。如果到中午还没清完，就先暂停，今晚流量低的时候再跑。）

**B:** Deal. And going forward, I'll ping you before any big backfills — is this DM the best channel, or should I use the ops channel?
（成交。以后大规模回填前我都会先说一声——用这个私信联系你方便，还是走 ops 频道？）

**A:** Ops channel is better — that way the whole team sees it, not just whoever's on the hook that week. I'll also add queue capacity numbers to the runbook, so the next person doesn't have to figure this out at 6 AM.
（ops 频道更好——这样整个团队都能看到，而不只是当周值班的人。我还会把队列容量数据补进值班手册，免得下一个人早上 6 点摸黑自己摸索。）

**B:** Sounds like a plan. Quite the baptism by fire for your first week on-call, huh?
（就这么定了。第一周值班就遇上"火线洗礼"，哈？）

**A:** Honestly? Better to get the scary stuff out of the way early. By the time this rotation ends, I'll know this system inside out.
（说实话？吓人的事早点来更好。等这轮值班结束，我就把这个系统摸得里外通透了。）

─────────────────────────
🎯【语块精讲】（8+1 个）
─────────────────────────

• **get paged** — 收到值班告警（被 pager/告警系统叫醒）
  工作场景：I got paged three times last night — can we talk about the alert threshold?（我昨晚被 page 了三次——能聊聊告警阈值吗？）
  日常场景：I'm paged so often I sleep with my phone on the pillow like it's a baby monitor.（我被 page 得太频繁，睡觉都把手机放枕边，跟婴儿监视器似的。）

• **stale / user-facing** — （数据）过期的 / 面向用户的
  工作场景：The numbers are stale — refresh the cache before the demo.（数据过期了——Demo 前先刷新缓存。）/ Nothing user-facing is broken yet.（还没有任何面向用户的功能挂掉。）
  日常场景：This map app shows stale traffic info — it keeps routing me into jams.（这个地图软件的路况信息是旧的——老把我导进堵车路段。）

• **trace (it) back to** — 追溯到（根源）
  工作场景：We traced the latency spike back to a config change pushed on Friday.（我们把延迟飙升追溯到了周五推的一个配置变更。）
  日常场景：I traced the weird smell in the kitchen back to a forgotten sweet potato.（我把厨房怪味的源头追到了一个被遗忘的红薯。）

• **headroom** — 余量、容量空间
  工作场景：The cluster only has 10% headroom left — time to scale up.（集群只剩 10% 的余量了——该扩容了。）
  日常场景：My schedule has zero headroom this week — one surprise and everything collapses.（我这周日程毫无余量——出一个意外就全盘崩溃。）

• **throttle back / dial it down** — 降速、调低
  工作场景：Throttle back the sync job during business hours.（工作时间把同步任务降速跑。）
  日常场景：I've dialed down my coffee to one cup a day — progress.（我把咖啡降到每天一杯了——进步。）

• **drain / catch up** — （队列）排空消化 / 追平积压
  工作场景：The queue drains at 5K events per minute; give it an hour to catch up.（队列每分钟消化 5 千条事件，给它一小时追平。）
  日常场景：I'm using the holiday to catch up on sleep and laundry.（我要用这个假期把觉和衣服都补上。）

• **that's on X as much as on Y** — 责任分摊（"一半怪 X 一半怪 Y"）
  工作场景：The deploy failed — that's on the pipeline as much as on us.（部署失败了——一半怪流水线，一半怪我们。）
  日常场景：We missed the movie — that's on the traffic as much as on me.（我们错过电影了——一半怪堵车，一半怪我。）

• **baptism by fire** — 火线洗礼（一上手就直面硬仗）
  工作场景：Leading the launch week was a baptism by fire for the new PM.（让新 PM 主导发布周，真是火线洗礼。）
  日常场景：My first dinner party for ten people? Total baptism by fire.（我第一次给十个人办晚宴？彻底的火线洗礼。）

• **(bonus) know something inside out** — 把某物摸得里外通透
  工作场景：Ask Priya — she knows the billing system inside out.（问 Priya 吧——计费系统她摸得透透的。）
  日常场景：After five trips to Tokyo, my sister knows that city inside out.（去了五次东京之后，我妹对那座城市了如指掌。）

─────────────────────────
🔄【变造挑战】（3 题）
─────────────────────────
用今天学到的表达，换场景重新说：

1. 你的第一个 on-call 周异常平静，周五老板问感受。你说：这周一次都没被 page，太安静了反而不安心。
   💡 提示：get paged + baptism by fire（反着用）

2. 新同事没打招呼就在共享测试环境跑大规模压测，环境挂了。你要指出问题，但不想全怪他——文档也没写环境限制。
   💡 提示：trace it back to + that's on X as much as on Y

3. 朋友问你新工作一个月的感想。你说：一开始很难，但现在整个业务都摸熟了。
   💡 提示：baptism by fire + know something inside out

💡 **今日一句：** *"I traced it back to the batch job that rolled out yesterday."*
排查问题的万能句式——trace it back to 后面跟结论，一句话就把"根因"说清楚。今天遇到任何"为什么"的问题，试着用 I traced it back to... 回答一次。
