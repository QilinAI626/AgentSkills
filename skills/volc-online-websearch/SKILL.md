---
name: volc-online-websearch
description: 火山联网问答Agent与联网检索增强工作流技能。支持文搜与图搜能力，Lite/Pro 版本能力不同。需要联网检索、引用来源、或对接火山联网问答Agent API时使用。
license: Complete terms in LICENSE.txt
---

# 火山联网问答 WebSearch Skill

## 目标
- 使用 WebSearch 检索并融合多来源信息
- 输出清晰答案并提供引用
- 如用户要对接火山引擎联网问答Agent，给出接口参数与请求示例

## 产品能力概览
- 文搜与图搜：均支持文本与图片问答
- Lite 与 Pro：Pro 版本在数据源、工具与富媒体能力上更丰富
- 详见 references/product-overview.md

## 适用场景
- 需要联网查证或补充最新信息，可以查询时事、新闻、股票、天气等  
- 需要带来源引用的回答
- 需要封装或调用火山引擎联网问答Agent API

## 工作流
1. 明确问题范围与输出格式
2. 生成 2-5 个检索关键词组合，优先用中文关键词，必要时补充英文
3. 调用 WebSearch 获取结果，必要时用 WebFetch 打开权威来源补细节
4. 对比不同来源，提取可核验事实
5. 输出答案与引用，并标注信息来源

## scripts
- scripts/volc_agent_chat.py
  - 用途：以 APIKey 方式调用火山引擎联网问答Agent
  - 依赖：Python 标准库，无需额外依赖
  - 用法：
    - export VOLC_AGENT_API_KEY=你的APIKey
    - python scripts/volc_agent_chat.py <bot_id> <user_message> [system_message] [stream] [model]

## references
- references/volc-agent-api.md：接口地址、参数与限制速查
- references/product-overview.md：产品能力概览（含文搜/图搜、Lite/Pro 差异）
- 官方文档：
  - https://www.volcengine.com/docs/85508/1510774?lang=zh
  - https://www.volcengine.com/docs/85508/1510834?lang=zh
  - https://www.volcengine.com/docs/85508/1512748?lang=zh

## 输出结构
始终使用以下结构：
- 答案
- 关键信息与引用
- 如涉及 API 集成：请求说明与示例

## 火山引擎 联网问答Agent API 关键说明
- 详见 references/volc-agent-api.md

## 示例
### WebSearch 答复示例
- 答案
  - 用 2-4 句话先给结论，再补充关键细节
- 关键信息与引用
  - 列出来源域名与标题，标注对应事实

### API 调用示例
如用户需要调用示例，输出如下模板并提醒使用环境变量保存密钥：

```bash
curl -X POST "https://open.feedcoopapi.com/agent_api/agent/chat/completion" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer ${VOLC_AGENT_API_KEY}" \
  -d '{
    "bot_id": "YOUR_BOT_ID",
    "messages": [
      {"role": "system", "content": "你是一个联网问答助手"},
      {"role": "user", "content": "你好"}
    ],
    "stream": true
  }'
```

### scripts 调用示例
```bash
export VOLC_AGENT_API_KEY="你的APIKey"
python scripts/volc_agent_chat.py "YOUR_BOT_ID" "你好" "你是一个联网问答助手" true
```

## 安全与合规
- 不直接要求或记录用户密钥
- 优先提示使用环境变量或密钥管理服务
