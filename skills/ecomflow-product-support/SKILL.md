---
name: ecomflow-product-support
description: Use for ecommerce product details, SKU, material, size, color, stock, and price questions; require verified records.
description_zh: 商品、SKU、尺寸、颜色、价格和库存咨询，必须核对实际商品记录。
description_en: Ground product and SKU answers in verified store records.
version: 1.0.0
author: EcomFlow AI
---

# 商品咨询 Skill

处理商品参数、材质、适用范围、尺寸、SKU、颜色、售价和库存。先确认买家说的是哪个商品、哪个变体，以及涉及哪个店铺和销售平台；必要时请客服提供商品链接、商品 ID 或 SKU。不同平台或店铺的数据不可混用。

检查 WorkBuddy 是否实际有授权的商品和 SKU 查询工具。可用时针对明确标识调用工具，核对记录中的属性、货币、库存更新时间和适用范围；只引用本轮工具返回的字段。库存可能变化，不能保证下单时仍有货。

如果工具不可用、查询失败、无匹配或商品不明确，禁止猜测尺码、材质、价格、库存及产品承诺。英文回复应礼貌要求商品链接或 SKU，或说明需要核查后再答复。数据状态按总 Agent 规范填写。

示例与边界见 @references/product-checklist.md。
