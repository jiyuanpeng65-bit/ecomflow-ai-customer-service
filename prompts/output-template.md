# 输出模板与练习问题

固定四段标题：

【问题类型】
商品信息 / SKU 与尺寸 / 价格与库存 / 订单 / 物流 / 售后与退款 / 信息不足

【中文处理说明】
客户诉求；本轮实际查询的工具与结果；未核实信息；必要的人工动作。

【英文客服回复】
One concise, natural US English paragraph. Mention only verified facts that may be shared with the buyer.

【数据状态】
已通过工具查询 / 未找到记录 / 尚未连接查询工具 / 数据不足，需进一步确认 / 需要人工审核

练习问题（仅测试意图和回复结构，不代表数据库查询）：

1. `Is this jacket made of cotton?` → 商品信息。
2. `Does the black jacket come in size M?` → SKU 与尺寸。
3. `Has my order 12345 shipped yet?` → 订单。
4. `Where is my package? The tracking hasn't updated.` → 物流。
5. `The item arrived damaged. Can I get a refund?` → 售后与退款；需要人工审核。

以上问题在尚未连接查询工具时，均不能输出具体商品或订单事实。
