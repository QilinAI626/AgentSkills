import json
import os
import sys
from urllib import request, error


def build_payload(bot_id, user_message, system_message, stream, model):
    messages = []
    if system_message:
        messages.append({"role": "system", "content": system_message})
    messages.append({"role": "user", "content": user_message})
    payload = {
        "bot_id": bot_id,
        "messages": messages,
        "stream": stream,
    }
    if model:
        payload["model"] = model
    return payload


def main():
    if len(sys.argv) < 3:
        print("Usage: python volc_agent_chat.py <bot_id> <user_message> [system_message] [stream] [model]")
        sys.exit(1)

    bot_id = sys.argv[1]
    user_message = sys.argv[2]
    system_message = sys.argv[3] if len(sys.argv) > 3 else ""
    stream_arg = sys.argv[4] if len(sys.argv) > 4 else "true"
    model = sys.argv[5] if len(sys.argv) > 5 else ""

    stream = str(stream_arg).lower() in {"1", "true", "yes"}
    api_key = os.environ.get("VOLC_AGENT_API_KEY", "").strip()
    if not api_key:
        print("Missing VOLC_AGENT_API_KEY")
        sys.exit(1)

    url = "https://open.feedcoopapi.com/agent_api/agent/chat/completion"
    payload = build_payload(bot_id, user_message, system_message, stream, model)
    data = json.dumps(payload).encode("utf-8")

    req = request.Request(url, data=data, method="POST")
    req.add_header("Content-Type", "application/json")
    req.add_header("Authorization", f"Bearer {api_key}")

    try:
        with request.urlopen(req, timeout=30) as resp:
            content_type = resp.headers.get("Content-Type", "")
            body = resp.read()
            if "application/json" in content_type:
                print(body.decode("utf-8"))
            else:
                sys.stdout.buffer.write(body)
    except error.HTTPError as e:
        err_body = e.read().decode("utf-8", errors="ignore")
        print(f"HTTPError {e.code}: {err_body}")
        sys.exit(1)
    except Exception as e:
        print(f"Request failed: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
