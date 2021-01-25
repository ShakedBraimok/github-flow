import os
from src.utils.shell import shell_run
from jproperties import Properties

configs = Properties()

def git(*args):
    repo_abspath = get_repo_abspath()
    gd = "--git-dir=" + os.path.join(repo_abspath, ".git")
    wt = "--work-tree=" + repo_abspath
    commands = " ".join(["git", gd, wt] + list(args))
    result = shell_run(commands)
    return result

def get_repo_abspath():
    repo_abspath = shell_run("git rev-parse --show-toplevel")
    return repo_abspath


def get_dotgit_abs_path():
    repo_abspath = get_repo_abspath()
    return os.path.join(repo_abspath, ".git")

def get_url():
    repo_abspath = get_repo_abspath()
    git_config = os.path.join(repo_abspath, ".git/config")
    with open(git_config, 'rb') as config_file:
        configs.load(config_file)
    url = (configs.get("url")[0])
    return url

def git_pull():
    output = os.system("git pull --all")
    return output

