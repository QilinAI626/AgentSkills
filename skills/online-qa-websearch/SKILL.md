---
name: online-qa-websearch
description: 面向联网问答与搜索增强场景的工作流技能。用户需要联网检索、引用来源、生成带证据的回答，或需要对接火山引擎联网问答Agent API时，都应使用此技能。
license: Complete terms in LICENSE.txt
---

# 联网问答 WebSearch Skill

## 目标
- 使用 WebSearch 检索并融合多来源信息
- 输出清晰答案并提供引用
- 如用户要对接火山引擎联网问答Agent，给出接口参数与请求示例

## 适用场景
- 需要联网查证或补充最新信息
- 需要带来源引用的回答
- 需要封装或调用火山引擎联网问答Agent API

## 工作流
1. 明确问题范围与输出格式
2. 生成 2-5 个检索关键词组合，优先用中文关键词，必要时补充英文
3. 调用 WebSearch 获取结果，必要时用 WebFetch 打开权威来源补细节
4. 对比不同来源，提取可核验事实
5. 输出答案与引用，并标注信息来源

## 输出结构
始终使用以下结构：
- 答案
- 关键信息与引用
- 如涉及 API 集成：请求说明与示例

## 火山引擎 联网问答Agent API 关键说明
以下信息用于用户集成或封装服务时输出：

- 认证方式
  - APIKey 接入：Header 中使用 Authorization: Bearer <API_KEY>
  - TOP 网关接入：使用火山引擎标准 AK/SK 签名，ServiceName=volc_torchlight_api
- 接口地址
  - APIKey 接入：https://open.feedcoopapi.com/agent_api/agent/chat/completion
  - TOP 网关接入：https://mercury.volcengineapi.com?Action=ChatCompletion&Version=2024-01-01
- 请求方法与格式
  - Method: POST
  - Content-Type: application/json
- 关键请求参数
  - bot_id：必填，智能体 ID
  - messages：必填，对话消息数组，最多保留最后 10 条
    - 如第一条为 system，始终保留
    - role: user / assistant / system
    - content: 文本或多模态对象
  - stream：是否流式，默认 false，建议流式
  - user_id、device_id：可选
  - knowledge：可选背景知识注入
  - model：可选，thinking 或 auto_thinking
- 限制
  - APIKey 接入超时 30s
  - TOP 网关请求体不超过 8MB，超时 30s

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

## 安全与合规
- 不直接要求或记录用户密钥
- 优先提示使用环境变量或密钥管理服务
