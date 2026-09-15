from mcp.server.mcpserver import MCPServer

from tools.github_tools import list_repositories, create_repository, commit_and_push

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

@mcp.tool()
def commit_and_push_changes(repo_path: str, commit_message: str):
    """Stage all changes, commit, and push to the remote repository."""
    return commit_and_push(repo_path, commit_message)

if __name__ == "__main__":
    mcp.run()