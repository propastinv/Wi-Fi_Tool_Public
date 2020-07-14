# Point Checker

![N|Solid](https://upload.wikimedia.org/wikipedia/commons/f/f8/Python_logo_and_wordmark.svg)

### Installation

Point Checker requires [Python](https://www.python.org/) v3.6+ to run.

Install the dependencies:

```sh
$ cd $(project dir)
$ mv .env.example .env
$ pip install -r requirements.txt
```
Run project:
```sh
$ cd $(project dir)
$ python3 main.py
```
Build project:
```sh
$ cd $(project dir)
$ pyinstaller -w -F --icon=supericon.ico maim.py
$ mv /src/supericon.ico /dist/supericon.ico
$ ./main.(exe/bin)
```



