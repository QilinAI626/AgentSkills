# 火山联网问答Agent API 参考
 
 ## 认证方式
 - APIKey 接入：Header 中使用 Authorization: Bearer <API_KEY>
 - TOP 网关接入：使用火山引擎标准 AK/SK 签名，ServiceName=volc_torchlight_api
 
 ## 接口地址
 - APIKey 接入：https://open.feedcoopapi.com/agent_api/agent/chat/completion
 - TOP 网关接入：https://mercury.volcengineapi.com?Action=ChatCompletion&Version=2024-01-01
 
 ## 请求方式
 - Method: POST
 - Content-Type: application/json
 
 ## 请求参数
 - bot_id：必填，智能体 ID
 - messages：必填，对话消息数组，最多保留最后 10 条
   - 如第一条为 system，始终保留
   - role: user / assistant / system
   - content: 文本或多模态对象
 - stream：是否流式，默认 false，建议流式
 - user_id、device_id：可选
 - knowledge：可选背景知识注入
 - model：可选，thinking 或 auto_thinking
 
 ## 限制
 - APIKey 接入超时 30s
 - TOP 网关请求体不超过 8MB，超时 30s
