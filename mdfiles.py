import requests
import argparse

def parse_arguments():
    """
    Business logic: CL arguments
    """
    parser = argparse.ArgumentParser(description='Find markdown files in a GitHub repository.')
    parser.add_argument('repo_owner', help='GitHub repository owner (username or organization)')
    parser.add_argument('repo_name', help='GitHub repository name')
    parser.add_argument('folder_path', help='Specific folder to search within the repository')
    parser.add_argument('--token', help='GitHub personal access token (optional, increases rate limit)')
    return parser.parse_args()

def get_folder_contents(owner, repo, path, token=None):
    """
    Business logic: Get the contents of a folder in a GitHub repository.
    """
    url = f"https://api.github.com/repos/{owner}/{repo}/contents/{path}"
    headers = {"Accept": "application/vnd.github.v3+json"}
    
    if token:
        headers["Authorization"] = f"token {token}"
    
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        print(f"Error: Could not access {path} (Status code: {response.status_code})")
        print(f"Response: {response.json().get('message', '')}")
        return []
    
    return response.json()

def find_markdown_files(owner, repo, folder_path, token=None, found_files=None):
    """
    business logic: Recursively find markdown files in a GitHub repository."""
    if found_files is None:
        found_files = []
    
    contents = get_folder_contents(owner, repo, folder_path, token)
    
    for item in contents:
        if item["type"] == "file" and item["name"].endswith(".md"):
            found_files.append(item["path"])
        elif item["type"] == "dir":
            find_markdown_files(owner, repo, item["path"], token, found_files)
    
    return found_files

def main():
    args = parse_arguments()
    
    print(f"Searching for markdown files in {args.folder_path} of {args.repo_owner}/{args.repo_name}")
    
    markdown_files = find_markdown_files(args.repo_owner, args.repo_name, args.folder_path, args.token)
    
    for file_path in markdown_files:
        print(f"  - {file_path}")
    
    print(f"\nFound {len(markdown_files)} markdown files:")

if __name__ == "__main__":
    main()