from rimp import load_repl


load_repl("21natzil", "Permissions", verbose=False)
load_repl("21natzil", "discordy", force_reinstall=True)

import perms
print(dir(perms))

import discordy
