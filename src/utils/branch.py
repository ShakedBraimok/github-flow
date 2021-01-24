import sys, getopt, os
from src.utils.shell import execute

def main(argv):
    branch_name = argv[0]
    src_branch_name = argv[1]
    output = create_branch(branch_name,src_branch_name)
    return output

def create_branch(branch_name,src_branch_name):
    command = 'git checkout -b %s origin/%s' % (branch_name,src_branch_name)
    output = execute(command.split(' '))
    push_branch(branch_name)
    return output

def push_branch(branch_name):
    output = os.popen('git push -u origin %s' % branch_name).read()
    return output

def checkout(branch_name):
    command = 'git checkout %s && git pull' % branch_name
    output = execute(command.split(' '))

    return output

if __name__ == "__main__":
   main(sys.argv[1:])