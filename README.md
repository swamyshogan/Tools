# GitHub Markdown File Finder

A simple Python script to locate all Markdown files in a GitHub repository directory and to group them 

## Description

This tool uses GitHub's API to scan a specified repository folder and list all `.md` files it finds. It searches recursively through all subdirectories of the specified path.

## Requirements

- Python 3.6+
- `requests` library

## Usage

```bash
python find_md_files.py OWNER_USERNAME REPO_NAME FOLDER_PATH [--token YOUR_TOKEN]
```

### Arguments

- `OWNER_USERNAME`: The GitHub username or organization that owns the repository
- `REPO_NAME`: The name of the repository
- `FOLDER_PATH`: The directory within the repository to search
- `--token`: (Optional) GitHub personal access token for authentication

### Examples

Search a public repository:
```bash
python find_md_files.py microsoft vscode docs
```

Search with authentication (recommended):
```bash
python find_md_files.py microsoft vscode docs --token ghp_xxxxxxxxxxxx
```

NOTE: 
- Using a token is recommended even for public repositories to avoid rate limiting
- For private repositories, a token with appropriate permissions is required