from rimp import load_repl


load_repl("21natzil", "Permissions", verbose=True)
import perms
print(dir(perms))


load_repl("21natzil", "discordy", force_reinstall=True)
import discordy
print(dir(discordy))

### The below don't work ... 
#   the files are copied to the temp directory
#   but get lost during installation

# from discordy import objects
# print(dir(objects))

# from discordy.objects.snowflake import SnowflakeObj
# s = SnowflakeObj(508356525983793152)
# print(s.timestamp)