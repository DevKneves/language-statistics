import requests
import json

# Substitua 'your_github_username' pelo seu nome de usuário
username = 'your_github_username'
# Substitua 'YOUR_GITHUB_TOKEN' pelo seu token pessoal
token = 'YOUR_GITHUB_TOKEN'
headers = {'Authorization': f'token {token}'}

def get_languages():
    url = f'https://api.github.com/users/{username}/repos'
    response = requests.get(url, headers=headers)
    repos = response.json()
    
    language_stats = {}
    
    for repo in repos:
        repo_name = repo['name']
        languages_url = f'https://api.github.com/repos/{username}/{repo_name}/languages'
        languages_response = requests.get(languages_url, headers=headers)
        languages = languages_response.json()
        
        for language, bytes in languages.items():
            if language in language_stats:
                language_stats[language] += bytes
            else:
                language_stats[language] = bytes
    
    return language_stats

def print_language_stats(stats):
    total_bytes = sum(stats.values())
    for language, bytes in stats.items():
        percentage = (bytes / total_bytes) * 100
        bar_length = int(percentage / 2)  # Ajuste o comprimento da barra conforme necessário
        bar = '#' * bar_length + '-' * (50 - bar_length)  # Barra gráfica com caracteres ASCII
        print(f"{language:10} {bytes:10} bytes {bar} {percentage:6.2f}%")

if __name__ == "__main__":
    stats = get_languages()
    print_language_stats(stats)

