# Building with the Claude API

A hands-on learning repository that walks through the Claude (Anthropic) API from first `messages.create` call all the way to multi-index RAG, prompt caching, code execution, and a full MCP (Model Context Protocol) chat client. Each topic lives in its own numbered Jupyter notebook so you can work through them in order, or jump straight to the one you need.

## Prerequisites

- Python 3.9+
- An Anthropic API key exported as `ANTHROPIC_API_KEY` (a `.env` file works)
- `pip install anthropic python-dotenv` (plus `voyageai` for the embeddings / RAG notebooks and `mcp[cli]` for the MCP project)

## Repository index

### Notebooks — core API fundamentals

| # | Notebook | Topic | Description |
|---|----------|-------|-------------|
| 001 | [001_requests.ipynb](001_requests.ipynb) | Basic requests | First `messages.create` call: install the SDK, load the API key, send a prompt and inspect the response object. |
| 002 | [002_system-prompt.ipynb](002_system-prompt.ipynb) | System prompts | Shaping model behavior with the `system` parameter. |
| 003 | [003_temperature.ipynb](003_temperature.ipynb) | Temperature & sampling | How `temperature` and related knobs affect determinism and creativity. |
| 004 | [004_streaming.ipynb](004_streaming.ipynb) | Streaming responses | Consuming `stream=True` responses and handling event deltas. |
| 005 | [005_structured-data.ipynb](005_structured-data.ipynb) | Structured output | Coaxing Claude into producing clean, parseable JSON / structured data. |

### Notebooks — evaluation & prompt engineering

| # | Notebook | Topic | Description |
|---|----------|-------|-------------|
| 006 | [006_generating-test-datasets.ipynb](006_generating-test-datasets.ipynb) | Test dataset generation | Using Claude to generate an eval dataset (saved to [dataset.json](dataset.json)). |
| 007 | [007_model-based-grading.ipynb](007_model-based-grading.ipynb) | Model-based grading | Using an LLM as a judge to score model outputs. |
| 008 | [008_code-based-grading.ipynb](008_code-based-grading.ipynb) | Code-based grading | Deterministic, code-driven grading for structured tasks. |
| 009 | [009_prompting.ipynb](009_prompting.ipynb) | Prompt engineering loop | End-to-end eval harness: generate prompts, run them in parallel, grade, and build a report. |

### Notebooks — tool use

| # | Notebook | Topic | Description |
|---|----------|-------|-------------|
| 010 | [010_tools.ipynb](010_tools.ipynb) | Tool use basics | Defining a single tool (`add_duration_to_datetime`), handling `tool_use` / `tool_result` turns. |
| 011 | [011_multi-tools.ipynb](011_multi-tools.ipynb) | Multiple tools | Orchestrating a tool loop with several tools and chained tool calls. |
| 012 | [012_tool_streaming.ipynb](012_tool_streaming.ipynb) | Streaming tool calls | Streaming `input_json_delta` events while a tool call is being generated. |
| 013 | [013_text_editor_tool.ipynb](013_text_editor_tool.ipynb) | Text editor tool | Implementing Anthropic's text-editor tool (`view` / `create` / `str_replace` / `insert` / `undo`). |

### Notebooks — retrieval-augmented generation (RAG)

| # | Notebook | Topic | Description |
|---|----------|-------|-------------|
| 014 | [014_chunking.ipynb](014_chunking.ipynb) | Chunking strategies | Chunking by characters, sentences, and markdown sections over [report.md](report.md). |
| 015 | [015_embeddings.ipynb](015_embeddings.ipynb) | Embeddings | Generating embeddings with VoyageAI and running vector similarity search. |
| 016 | [016_bm25.ipynb](016_bm25.ipynb) | BM25 lexical search | A from-scratch `BM25Index` implementation for keyword retrieval. |
| 017 | [017_multi-index-RAG.ipynb](017_multi-index-RAG.ipynb) | Hybrid multi-index RAG | Combining embedding search and BM25 into a hybrid retrieval pipeline. |

### Notebooks — advanced capabilities

| # | Notebook | Topic | Description |
|---|----------|-------|-------------|
| 018 | [018_thinking.ipynb](018_thinking.ipynb) | Extended thinking | Enabling extended thinking and triggering redacted thinking blocks. |
| 019 | [019_images.ipynb](019_images.ipynb) | Vision / images | Sending images (base64) and running a property fire-risk assessment from a satellite photo. |
| 020 | [020_pdf-support.ipynb](020_pdf-support.ipynb) | PDF input | Passing PDFs (see [earth.pdf](earth.pdf)) as documents and using citations. |
| 021 | [021_caching.ipynb](021_caching.ipynb) | Prompt caching | Using `cache_control` on large prompts to reduce latency and cost. |
| 022 | [022_code_execution.ipynb](022_code_execution.ipynb) | Code execution & Files API | Uploading files via the Files API and using the code-execution beta tool. |

### `cli_project/` — MCP chat application

A standalone CLI chat app that connects to an MCP server, loads documents, and exposes slash-commands and `@document` mentions. See [cli_project/README.md](cli_project/README.md) for setup.

| File | Description |
|------|-------------|
| [cli_project/main.py](cli_project/main.py) | Entry point: wires up Claude, the MCP client(s), and the CLI chat loop. |
| [cli_project/mcp_server.py](cli_project/mcp_server.py) | FastMCP server exposing document read/edit tools and prompts. |
| [cli_project/mcp_client.py](cli_project/mcp_client.py) | Async stdio MCP client wrapper around `ClientSession`. |
| [cli_project/core/claude.py](cli_project/core/claude.py) | Thin Anthropic client wrapper used by the chat loop. |
| [cli_project/core/chat.py](cli_project/core/chat.py) | Core multi-turn chat + tool-use loop. |
| [cli_project/core/cli_chat.py](cli_project/core/cli_chat.py) | CLI-specific chat subclass: `@document` mentions and slash-commands. |
| [cli_project/core/cli.py](cli_project/core/cli.py) | `prompt_toolkit`-based REPL (autocomplete, history). |
| [cli_project/core/tools.py](cli_project/core/tools.py) | Tool-schema plumbing between MCP tools and the Anthropic SDK. |
| [cli_project/pyproject.toml](cli_project/pyproject.toml) | Project metadata and dependencies (installable via `uv pip install -e .`). |

### Supporting assets

| File | Description |
|------|-------------|
| [main.py](main.py) | Standalone `calculate_pi(n)` helper used as a sample target for tool-use / code-execution demos. |
| [test.py](test.py) | Tests for `calculate_pi` across various digit counts and edge cases. |
| [report.md](report.md) | ~18 KB interdisciplinary research report used as the corpus for chunking / embeddings / RAG notebooks. |
| [dataset.json](dataset.json) | Generated eval dataset (prompt inputs + solution criteria) used by the grading notebooks. |
| [earth.pdf](earth.pdf) | Sample PDF for the PDF-support notebook. |
| [streaming.csv](streaming.csv) | Sample CSV uploaded in the code-execution notebook. |
| [output.html](output.html) / [output.json](output.json) | Example outputs produced by notebook runs. |
| [top_churn_drivers_detailed.png](top_churn_drivers_detailed.png) | Chart generated by the code-execution notebook. |
| [images/](images/) | Property satellite images (`prop1.png` … `prop7.png`) used by the vision notebook. |

## Suggested path

If you're new to the Claude API, work the notebooks in numeric order — each one builds on helpers introduced earlier (e.g. `add_user_message`, `add_assistant_message`, `chat`). The RAG track (014 → 017) stands on its own, and `cli_project/` is a good capstone once you've worked through tool use (010–013) and MCP concepts.
