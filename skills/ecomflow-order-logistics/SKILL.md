---
name: ecomflow-order-logistics
description: Use for order status, shipment, carrier, tracking, ETA, missing delivery, and shipping exceptions; require authorized live records.
description_zh: 订单及国际物流咨询，核验订单身份与查询权限，绝不虚构轨迹。
description_en: Verify order and tracking data before drafting customer updates.
version: 1.0.0
author: EcomFlow AI
---

# 订单与物流 Skill

处理是否发货、订单状态、承运商、运单号、物流轨迹、预计送达、异常及“未收到货”。先识别订单号与平台；客户身份核验应在原店铺平台由人工客服完成。若尚未核验，不在英文回复披露订单明细。

检查 WorkBuddy 是否有可用且已授权的订单查询工具。只有订单实际匹配才可进一步查询该订单的物流记录；若需要最新承运商状态，须存在合法且已连接的追踪工具，并确认返回数据具有更新时间。普通历史物流记录不等同于实时追踪。不得虚构发货、签收、轨迹、预计送达日期或异常原因。

无工具、权限不足、订单不存在、物流记录缺失、轨迹不新鲜时，中文段明确限制，英文回复请买家通过平台私信提供订单号或说明客服正在核查。不要展示完整地址、电话、支付信息；运单号非必要不完整输出。不得自行修改订单或配送安排。

若买家仅问订单状态或是否发货，且授权订单工具本轮查到“已发货”，英文回复只确认这个状态，不主动展开缺少运单号、承运商、物流位置或预计送达信息。若买家明确询问这些详情，再按实际记录说明可核实的内容或局限。没有已核实的运单号时，不要说可以提供运单号；没有实际安排后续查询时，不要承诺稍后回复。

核验顺序见 @references/order-verification.md。
