from mcp.server.mcpserver import MCPServer

from tools.github_tools import list_repositories, create_repository

# Create an instance of MCPServer with the name "github-agent"
mcp = MCPServer("github-agent")

@mcp.tool()
def get_repositories():
    """List all GitHub repositories for the authenticated user."""
    return list_repositories()

@mcp.tool()
def create_user_repository(name: str, description: str = "", private: bool = False):
    """Create a new GitHub repository for the authenticated user."""
    return create_repository(name, description, private)

if __name__ == "__main__":
    mcp.run()