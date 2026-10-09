# EcomFlow AI：WorkBuddy 跨境电商客服助手

本项目是供 WorkBuddy 运行的客服专家定义与三个业务 Skill。Codex 负责维护文件；人工客服在 WorkBuddy 输入买家英文问题，核对英文草稿后自行发回 TikTok Shop、Amazon 等平台。项目不包含聊天网站、Agent 运行程序、数据库或数据连接器。

## 当前状态

| 状态                 | 当前结果 | 验证方式                                                  |
| ------------------ | ---- | ----------------------------------------------------- |
| 项目文件已创建            | 是    | 运行 `python tests/validate_project.py`，检查专家配置和三个 Skill |
| WorkBuddy 已实际加载并执行 | 尚未验证 | 按下文在 WorkBuddy 安装、召唤，并查看技能是否启用及真实对话输出                 |
| 飞书数据查询已连接          | 否    | 以后由你创建多维表格，并单独核对连接器权限及真实记录查询                          |

## 文件结构

- `.codebuddy-plugin/plugin.json`：官方专家包清单，声明一个 Agent 和三个 Skill。
- `agents/ecomflow-customer-service.md`：客服总 Agent 的角色、路由、安全规则和四段输出。
- `skills/ecomflow-product-support/`：商品和 SKU 咨询。
- `skills/ecomflow-order-logistics/`：订单和物流。
- `skills/ecomflow-after-sales/`：售后和退款。
- `prompts/output-template.md`：输出模板及练习问题。
- `PROJECT_RULES.md`：边界和状态说明。
- `dist/`：供 WorkBuddy “上传技能”使用的三个 ZIP 包（各自根目录都有 `SKILL.md`），以及供后续按开放平台官方渠道提交的专家包 ZIP。
- `tests/workbuddy-manual-cases.md`：七条 WorkBuddy 手工验收用例。

## 在 WorkBuddy 打开和启用

1. 在 WorkBuddy 的新建任务栏选择“本地工作空间”，选择克隆或下载后的项目文件夹。这让 WorkBuddy 能读取项目文件，但**仅打开文件夹不等于安装专家或 Skill**。
2. 左侧进入“专家·技能·连接器” → “技能” → “添加技能” → “上传技能”，分别选择 `dist/ecomflow-product-support.zip`、`dist/ecomflow-order-logistics.zip`、`dist/ecomflow-after-sales.zip`。上传后在“已安装”中确认三个名称都出现且已启用。若更新了 Skill 文件，重新打包并重新导入更新版本。
3. 进入“专家·技能·连接器” → “专家” → “我的专家” → “创建专家”。将 [专家定义](agents/ecomflow-customer-service.md) 的正文和 frontmatter 所列名称提供给 WorkBuddy 内置专家管理工具，明确名称为 `EcomFlow AI 客服`，内部标识为 `ecomflow-customer-service`，预加载三个已安装 Skill。可直接用 `prompts/workbuddy-registration.md` 中的注册指令。创建完成后，在“我的专家”找到并召唤。**不要直接改写用户级 `~/.workbuddy/experts` 的内部索引文件。**
4. `dist/ecomflow-ai-expert.zip` 按开放平台专家包结构打包，可用于后续按官方渠道提交。当前客户端的“我的专家”创建流程由内置专家管理工具完成；项目文件本身不会自动变成已注册专家。

官方参考：[WorkBuddy 专家说明](https://www.workbuddy.cn/docs/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Expert-Center)、[专家包配置](https://open.workbuddy.cn/docs/expert)、[Skill 格式](https://open.workbuddy.cn/docs/skill)、[上传与启用技能](https://www.workbuddy.cn/docs/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Skills-Market)。

## 如何验证加载与提问

先确认“已安装”列表中有三个 Skill，并在新对话中召唤 `EcomFlow AI 客服`。按 `tests/workbuddy-manual-cases.md` 逐条验收。可先粘贴买家的英文原话，例如：

> Does the black jacket come in size M, and is it in stock?

再测试：`Has my order 12345 shipped yet?`、`Where is my package?`、`The item arrived damaged. Can I get a refund?`。对照 `prompts/output-template.md`：输出应含四段固定标题；没有查询工具时，不能给出商品属性、库存、订单或物流事实；退款应提示人工审核。查看 WorkBuddy 对话中的 Skill 调用或上下文记录，确认被调用的 Skill 名称。若版本不显示调用日志，需以 Skill 安装状态及输出行为做有限验证，不能声称已看到工具调用。

**工具验证**：在 WorkBuddy 的“连接器”或工具列表里查看是否有可查询商品、SKU、订单、物流、政策的工具；用一条已知记录作实际查询，检查工具名、权限、返回记录和来源。没有实际工具调用，就不能把【数据状态】写为“已通过工具查询”。本项目没有注册任何业务数据工具。

## 后续接入飞书时要验证

你创建多维表格后，再检查 WorkBuddy 是否存在已授权、能读取**多维表格记录**的连接器。聊天机器人能收发消息，不代表能读多维表格。需逐项核对：连接器实际工具列表、所需表格的读取权限、应用或用户对表格的访问权、表格和字段标识、一次真实记录查询、错误与权限不足时的返回，以及订单数据的客服访问范围。测试成功后才能让 Agent 把记录标为“已通过工具查询”。本次没有配置飞书 App ID、App Secret 或任何飞书 API 程序。

## 本地校验

在项目目录运行：

```powershell
python tests/validate_project.py
```

这个脚本只检查项目结构、名称、Skill 安装包和关键约束。意图识别与英文回复的最终效果需在 WorkBuddy 内用 `prompts/output-template.md` 的练习问题人工验证；当前无真实查询工具，不能测试业务数据查询。


