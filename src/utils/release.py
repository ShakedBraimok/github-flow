import sys, getopt, os
from src.utils.git import git_pull
from src.utils.shell import execute

def main(argv):
    version = argv[0]
    output = create_release(version)
    return output

def create_release(version, release_notes_file):
    git_pull()
    if release_notes_file == "":
        command = 'gh release create ' + version + ' --notes "" -t ' + version
        output = execute(command.split(' '))
    else:
        command = ['gh', 'release', 'create', version, '-F', release_notes_file, '-t', version]
        output = execute(command)
        if "no such file or directory" in output[1]:
            command = 'gh release create %s --notes "" -t %s' % (version,version)
            output = execute(command.split(' '))
    return output

def get_latest():
    latest_line = os.popen("gh release list | grep Latest").read()
    if latest_line == "":
        return "0.0.0"
    splitted_line = latest_line.split("\t")
    latest_version = splitted_line[2]
    return latest_version

if __name__ == "__main__":
   main(sys.argv[1:])