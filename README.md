# MCP Screenshot Server

A Model Context Protocol (MCP) server that enables LLM-based AI agents to capture screenshots of the current screen. Designed for seamless integration with LLMs and AI agents using the MCP protocol.

---

## Features

- Exposes a `take_screenshot` tool for LLM agents via MCP.
- Captures the screen using [`pyautogui`](https://pypi.org/project/PyAutoGUI/).
- Returns screenshots as JPEG images (compressed for efficiency).
- Simple integration with Claude, MCP clients, or other LLM-based agents.

---

## Quickstart

### 1. Install & Run

You can run the MCP Screenshot Server using [`uvx`](https://github.com/uvx-dev/uvx):

```bash
uvx --from git+https://github.com/deerajd/Screenshot-MCP.git mcp-server
```

---

### 2. Integrate with Your LLM Agent

Add the following to your tool configuration (for Claude, MCP clients, etc.):

```json
"screenshot": {
  "command": "uvx",
  "args": [
    "--from",
    "git+https://github.com/deerajd/Screenshot-MCP.git",
    "mcp-server"
  ]
}
```

From your LLM agent, call:

```
take_screenshot()
```

The server will respond with a JPEG image of the current screen.

---

## Development

- Python 3.8+
- [`pyautogui`](https://pypi.org/project/PyAutoGUI/)
- [`FastMCP`](https://github.com/modelcontext/fastmcp)

---

## License

MIT License

---