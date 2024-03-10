概述：
月会费固定440，若用户订阅了追加服务，那月额还要加上各个追加服务的料金。
另外一定期间中会有活动(campaign)，campaign期间固定费以及追加服务料金可能打折。

糯米团会员每月固定440：live会員先行抽選，可以看成员blog
追加服务1 (¥100)：live前排
追加服务2 (¥70)：特典映像
追加服务3 (¥350)：当月可以收到一张成员的签名生写

当月料金按当月1号時点で登録している追加サービスによって計算する。
つまり、解約したい場合は先月(3/31まで)解約手続きを完了し今月(4/1)に算入しません。
一方、追加サービスを契約する場合は、たとえ3/31としても、３月の分を払わないといけない。

架构：
用户表（id, 名字, 密码(hash), ~~追加服务list,~~ 当月料金, 历史24个月的月费记录list）

~~一个用户订阅的追加服务应该存在list里作为一个数据库属性好，还是以是否订阅了某服务有几个服务就有几个bool的属性。但哪天有了追加服务4的话要改变表的schema。绝大部分用户只订阅了固定基础的话，还会有很多的false数据浪费存储空间。~~ 在订阅表里管理

两年以上的数据由系统管理员清除吧。用户可以追溯检查近两年内各月的消费额。

追加服务表（id, 名称, 月费, 描述）

Campaign表（id, 开始日期, 结束日期, 固定额折扣, 追加服务1折扣, 追加服务2折扣, 追加服务3折扣）
那天有追加服务4的话，还要再增加一个属性
两年以上的campaign对象就可以删了

（这里的Campaign先按照所有用户统一的情况，即Campaign是一视同仁的，不会给特定的用户群特定的折扣。之后可能再考虑新規ユーザ、vip, svip分类别给不同程度的割引）

一个campaign至少持续一个月.

追加服务折扣存一个float，如果小于0就是减一定数额



其实按学院派的作法，用户和服务之间的订阅关系应该单独建表。

订阅表（id, 用户id, 服务id, 订阅开始日）

一旦新增了一条订阅记录，就立刻更新该用户的当月料金

一旦有了一个新的campaign就更新服务表的月费（打折对所有用户一视同仁）   检查订阅表