Certainly! Here's the edited version of your Markdown text, tailored for the **Indonesian Customs Tariff** domain and **Hascode API** usage, while keeping everything in **English**:

---

# MCP Server Example for Indonesian Customs Tariff & Hascode API

This repository provides an example implementation of a **Model Context Protocol (MCP)** server, customized for educational use in the context of **Indonesian customs tariff data** and **Hascode API integration**. The project demonstrates how to build a functional MCP server that connects to APIs such as Hascode to fetch tariff and HS code information for AI models.

## What is MCP?

MCP (Model Context Protocol) is an open standard designed to provide structured context to Large Language Models (LLMs). You can think of MCP like a USB-C port for AI—offering a standardized way to plug models into various external data sources, such as **customs tariff APIs**, **HS code lookups**, or **logistics databases**.

### Key Benefits

- Pre-built integrations for services like the **Hascode API**, which provides real-time HS code and duty rate information
- Flexibility to work across different LLM providers (OpenAI, Anthropic, etc.)
- A clean abstraction layer for securely accessing regulated data like import/export tariff structures

## Architecture Overview

MCP uses a client-server architecture that supports multiple data access points:

- **MCP Hosts**: AI tools like Claude Desktop or enterprise assistants that request structured customs data
- **MCP Clients**: Protocol intermediaries that handle 1:1 communication with servers
- **MCP Servers**: Lightweight components that expose data and capabilities, such as fetching Indonesian customs tariffs via API
- **Data Sources**: Includes local files (e.g., PDF duty schedules) and remote APIs like Hascode or customs office databases

## Core MCP Concepts

An MCP server typically exposes three types of capabilities:

- **Resources**: HS code datasets, tariff schedules, or API responses (e.g., duty rate for a specific product)
- **Tools**: API functions that an LLM can call to get updated customs information
- **Prompts**: Pre-configured templates (e.g., "What is the import duty for HS Code 8703.23.91.00 in Indonesia?")

## System Requirements

- Python 3.10 or higher
- MCP SDK 1.2.0 or higher
- `uv` package manager

## Getting Started

### Installing `uv` Package Manager

On MacOS/Linux:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Then restart your terminal to enable the `uv` command.

### Project Setup

1. Initialize your MCP project:
```bash
uv init mcp-server
cd mcp-server

uv venv
source .venv/bin/activate  # Use .venv\Scripts\activate on Windows

uv add "mcp[cli]" httpx
```

2. Create the main server file:
```bash
touch main.py
```

### Example: Integrate with Hascode API

In `main.py`, you can define a resource to fetch tariff data using Hascode:
```python
import httpx
from mcp import Resource

class HsCodeTariffResource(Resource):
    def read(self, hs_code: str):
        response = httpx.get(f"https://api.hascode.id/tariff?code={hs_code}")
        return response.json()
```

### Running the Server

Start the server:
```bash
uv run main.py
```

## Connecting to Claude Desktop

1. Install Claude Desktop
2. Edit the config file at:
   `~/Library/Application Support/Claude/claude_desktop_config.json`

```json
{
    "mcpServers": {
        "mcp-server": {
            "command": "uv",
            "args": [
                "--directory",
                "/ABSOLUTE/PATH/TO/YOUR/mcp-server",
                "run",
                "main.py"
            ]
        }
    }
}
```

3. Restart Claude Desktop

## Troubleshooting

If Claude Desktop fails to detect your server:

1. Check the config file path and syntax
2. Use the absolute path for all directories
3. Ensure `uv` is installed and working
4. Review Claude logs for connection issues

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

Would you like help writing the actual `main.py` that fetches Indonesian tariff data using Hascode API?