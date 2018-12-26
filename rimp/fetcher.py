import json
from urllib.parse import quote_plus

from bs4 import BeautifulSoup
import requests

REPL_URL = "https://repl.it/@{name}/{project}"
LOCATION_URL = "https://repl.it/data/repls/signed_urls/{repl_id}/{file_name}"
ACCESS_HEADERS = {"origin": "https://repl.it", "Referer": None}


def get_details(name: str, project: str):
    main_page = requests.get(REPL_URL.format(
        name=name,
        project=project
    ))
    if main_page.status_code != 200:
        raise ValueError("Invalid name or project name provided")
    soup = BeautifulSoup(main_page.text, features="html.parser").body
    script = soup.find_next("script").string.split('\n')[1][26:]
    return json.loads(script)

def get_file_urls(data: dict):
    repl_id = data['props']['pageProps']['initialState']['replEnvironment']['activeWid'][:-16]
    file_details = data['props']['pageProps']['initialState']['repls']['data'][repl_id]['fileNames']
    if 'setup.py' not in file_details:
        raise FileNotFoundError("Repl doesn't contain setup.py file")

    for file_path in file_details:
        yield file_path, LOCATION_URL.format(
            repl_id=repl_id,
            file_name=quote_plus(file_path)
        )

def get_file_contents(file_url: str, name: str, project: str):
    repl_url = REPL_URL.format(
        name=name,
        project=project
    )
    file_meta = requests.get(file_url).json()
    header_copy = ACCESS_HEADERS.copy()
    header_copy['Referer'] = repl_url
    file_content = requests.get(file_meta["urls_by_action"]["read"], headers=header_copy)
    return file_content.content

def collect_files(name: str, project: str):
    repl_meta = get_details(name, project)
    for file_path, file_url in get_file_urls(repl_meta):
        yield file_path, get_file_contents(file_url, name, project)
