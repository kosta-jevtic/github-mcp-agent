from mcp.server.mcpserver import MCPServer

from tools.github_tools import list_repositories, create_repository, commit_and_push

from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request

class NgrokMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        request.headers.__dict__["_list"].append(
            (b"ngrok-skip-browser-warning", b"true")
        )
        return await call_next(request)
    

# Create an instance of MCPServer with the name "github-agent"
mcp = MCPServer(
    name="github-agent", 
    description="A custom MCP server that connects Claude AI to GitHub"
    )

@mcp.tool()
def get_repositories():
    """List all GitHub repositories for the authenticated user."""
    return list_repositories()

@mcp.tool()
def create_user_repository(name: str, description: str = "", private: bool = False):
    """Create a new GitHub repository for the authenticated user."""
    return create_repository(name, description, private)

@mcp.tool()
def commit_and_push_changes(repo_path: str, commit_message: str):
    """Stage all changes, commit, and push to the remote repository."""
    return commit_and_push(repo_path, commit_message)

if __name__ == "__main__":
    mcp.run(transport="streamable-http", host="0.0.0.0", port=8000)