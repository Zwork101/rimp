import sys

from rimp.installer import install_repl, update_cache, already_installed
from rimp.fetcher import collect_files


def load_repl(name: str, project: str, force_reinstall: bool = False, verbose: bool = True):
    if sys.platform == "win32":
        if ".rimp/Lib/site-packages" not in sys.path:
            sys.path.append(".rimp/Lib/site-packages")
    else:
        py = "python" + sys.version[:3]
        comp_dir = ".rimp/lib/" + py + "/site-packages"
        if comp_dir not in sys.path:
            sys.path.append(comp_dir)

    if not force_reinstall and already_installed(name, project):
        return

    repl_total = {}
    for file_path, contents in collect_files(name, project):
        repl_total[file_path] = contents

    install_repl(repl_total, verbose)
    update_cache(name, project)
