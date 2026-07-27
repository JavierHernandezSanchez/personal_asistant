# Personal Assistant

## Vision
Personal Assistant is a modular AI assistant designed to help with everyday knowledge work.

The long-term goal is to build an assistant capable of reasoning, using tools, remembering previous interactions and executing multi-step tasks while remaining simple, understandable and extensible.

## Current status
Current version

✓ Tool abstraction

✓ ReadFileTool

✓ ToolRegistry

⬜ Agent

⬜ LLM integration

⬜ Memory

⬜ Planning

## Architecture
The assistant is composed of four main concepts:

- Agent
- Tools
- Memory
- LLM

## Roadmap
Phase 1
- Read files
- List directories
- Execute tools

Phase 2
- LLM integration
- Chat

Phase 3
- Memory

Phase 4
- Planning

Phase 5
- Voice

## Project structure
src/
    tool.py
    tool_registry.py
    tools/