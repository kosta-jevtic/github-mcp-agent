import os
from github import Github
from dotenv import load_dotenv


load_dotenv()

github_client = Github(os.getenv("GITHUB_TOKEN"))


def list_repositories():
    """
    List all repositories for the authenticated user.
    """
    try:
        user = github_client.get_user()
        repos = user.get_repos()
        result = []
        for repo in repos:
            result.append(f"- {repo.name} ({repo.html_url})")
    except Exception as ex:
        return f"Error: {str(ex)}"
    
    return "\n".join(result)


def create_repository(name: str, description: str = "", private: bool = False) -> str:
    """
    Create a new GitHub repository for the authenticated user.
    
    Args:
        name: Repository name
        description: Repository description (optional)
        private: Whether the repository should be private (default: False)
    """
    try:
        user = github_client.get_user()
        repo = user.create_repo(
            name=name,
            description=description,
            private=private,
            auto_init=True  # Creates repo with README
        )
        return f"Repository '{repo.name}' created successfully: {repo.html_url}"
    except Exception as ex:
        return f"Error: {str(ex)}"
    