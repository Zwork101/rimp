import json
from pathlib import Path
from subprocess import Popen
import sys
import tempfile
import os

CACHE_FILE = ".rimp/cache.json"


def create_dirs(remaining: str):
    paths = ""
    for parent in Path(remaining).parts[:-1]:
        paths = os.path.join(paths, parent)
        if not os.path.exists(paths):
            os.mkdir(paths)


def update_cache(name: str, project: str):
    if not os.path.exists(CACHE_FILE):
        create_dirs(CACHE_FILE)
        with open(CACHE_FILE, "w") as f:
            json.dump({name: [project]}, f)
    else:
        with open(CACHE_FILE) as f:
            contents = json.load(f)
        if name in contents:
            if project not in contents[name]:
                contents[name].append(project)
        else:
            contents[name] = [project]
        with open(CACHE_FILE, "w") as f:
            json.dump(contents, f)


def already_installed(name: str, project: str):
    try:
        with open(CACHE_FILE) as f:
            contents = json.load(f)
            if project in contents.get(name, []):
                return True
    except (FileNotFoundError, json.JSONDecodeError):
        return False


def install_repl(file_details: dict, verbose: bool):
    with tempfile.TemporaryDirectory() as temp_dir:
        for file_path, contents in file_details.items():
            complete_dir = os.path.join(temp_dir, file_path)
            create_dirs(complete_dir)
            with open(complete_dir, 'wb') as file:
                file.write(contents)

        with tempfile.TemporaryFile() as temp_file:
            Popen([sys.executable, "setup.py", "install", "--single-version-externally-managed",
                   "--prefix", os.path.abspath(".rimp"),
                   "--record", os.path.abspath(os.path.join(".rimp", ".meta"))],
                  cwd=temp_dir,
                  stdout=None if verbose else temp_file
            ).wait()

