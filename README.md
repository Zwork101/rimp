
# rimp
A hacky project that lets you import repls from https://repl.it into your project

## How to install
```
pip install rimp
```

Wow, that was easy wasn't it?

## How to use

There's only 1 command you'll need to know how to use, `load_repl`.

*load_repl*(name: `str`, project: `str`, force_reinstall: `bool`=False, verbose: `bool`=True):

**name**: The name of the repl.it user you're installing from (eg.
[https://repl.it/@**21natzil**/Permissions](https://repl.it/@21natzil/Permissions))

**project**: The name of the repl you're installing (eg. [https://repl.it/@21natzil/**Permissions**]((https://repl.it/@21natzil/Permissions)))

**force_reinstall**: If True, rimp will install the repl again, even if it's already downloaded

**verbose**: If False, it will *not* print anything to stdout with installation information

It's advised you checkout the `test.py` file for examples of this being used. ***PLEASE NOTE***, you can only import
repls with a proper `setup.py` file. If you want an example on the most minimal `setup.py` file you can make:

* See [this link](https://repl.it/@21natzil/Permissions) if you only wish to make *files* importable
* See [this link](https://repl.it/@21natzil/discordy) if you wish to make a whole directory importable

From here, it's just a matter of figuring out what you must import, which depends on the repl you're installing and should look at those docs.

## Things to note
1. The `name` option in the `setup.py` is required but can be anything
2. Downloading huge repls is slow, but only needs to be done once, so only set force_reinstall to True when necessary.
3. I have not tested on Mac, however it should work on Windows + Linux
4. This project installs repls to a .rimp file in the current working directory.

### Change Log
**0.0.0** - Project Creation
