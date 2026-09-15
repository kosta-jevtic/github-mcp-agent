# GitHub MCP Agent

A custom MCP server that connects Claude AI to GitHub, enabling agents to manage repositories and automate workflows through natural language.

## Tools

- **get_repositories** — List all GitHub repositories for the authenticated user
- **create_user_repository** — Create a new GitHub repository
- **commit_and_push_changes** — Stage all changes, commit, and push to remote

## Prerequisites

- Python 3.11+
- uv (package manager)
- GitHub Personal Access Token (classic) with `repo` scope
- ngrok account (for exposing local server)

## Setup

### 1. Clone the repository
```bash
git clone git@github-personal:kosta-jevtic/github-mcp-agent.git
cd github-mcp-agent
```

### 2. Install dependencies
```bash
uv sync
```

### 3. Configure environment
```bash
cp .env.example .env
# Add your GitHub token to .env
GITHUB_TOKEN=your_token_here
```

### 4. Run the server
```bash
uv run python main.py
```

### 5. Expose via ngrok
```bash
ngrok http 8000 --request-header-add "ngrok-skip-browser-warning:true"
```

### 6. Connect to Claude.ai