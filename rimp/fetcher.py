import json
from urllib.parse import quote_plus

# from bs4 import BeautifulSoup
import requests

REPL_URL = "https://repl.it/@{name}/{project}"
LOCATION_URL = "https://repl.it/data/repls/signed_urls/{repl_id}/{file_name}"
FILE_LIST_URL = "https://repl.it/data/repls/@{user}/{slug}"
ACCESS_HEADERS = {"origin": "https://repl.it", "Referer": None}


def get_details(name: str, project: str):
    main_page = requests.get(REPL_URL.format(
        name=name,
        project=project
    ))
    if main_page.status_code != 200:
        raise ValueError("Invalid name or project name provided")
    # soup = BeautifulSoup(main_page.text, features="html.parser").body
    # script = soup.find_next("script").string.split('\n')[1][26:]
    # return json.loads(script)
    text = main_page.text.replace("'",'"')
    idx1 = text.find("activeReplId")
    idx2 = text.find(":",idx1)
    idx4 = text.find('"',idx2)
    idx5 = text.find('"',idx4+1)
    repl_id = text[idx4+1:idx5]

    file_list_json = requests.get(
        FILE_LIST_URL.format(
            user=name,
            slug=project   
        )).json()
    file_list = file_list_json['fileNames']

    return {'repl_id':repl_id, 'file_list':file_list}

def get_file_urls(data: dict):
    repl_id = data['repl_id']
    file_list = data['file_list']
    if 'setup.py' not in file_list:
        raise FileNotFoundError("Repl doesn't contain setup.py file")

    for file_path in file_list:
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
