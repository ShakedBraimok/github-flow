import os
from src.settings import color
from src.utils.shell import execute

def create_pull_request(source_branch, dest_branch):
    branch_type = (source_branch.split("/")[0]).upper()
    pr_title = '"%s PR - %s --> %s"' % (branch_type,source_branch,dest_branch)
    pr_body = input("Pull Request (%s --> %s) Description: " % (source_branch, dest_branch))
    command = ['gh','pr','create','--head', source_branch,'--base',dest_branch,'--title', pr_title,'--body',pr_body]
    output = execute(command)
    if output[0] == "stderr":
        return output
    else:
        pr_url = output[-1]
        output = ["stdout",("A Pull-Request has been created %s." % pr_url)]
    return output

def merge_pull_request(merge_mode, source_branch, dest_branch):
    pr_number = get_pr_number(source_branch,dest_branch)
    if pr_number != None:
        print(color.BOLD + color.UNDERLINE + "PR Checks:" + color.END)
        print(get_pr_checks(pr_number))
        print(color.BOLD + ("The PR #%s will be merged, are you sure?" % pr_number) + color.END)
        answer = input("y/n: ")
        if answer.lower() == "y" or answer.lower == "yes":
            command = ['gh','pr','merge',pr_number,'--'+merge_mode]
            output = execute(command)
            if "stderr" == output[0]:
                return output
        else:
            output = ["stderr",None]
    else:
        output = ["stderr","Pull-Request does not exist."]
    return output


def get_pr_checks(pr_number):
    command = "gh pr checks " + pr_number
    pr_checks = os.popen(command).read()
    return pr_checks

def get_pr_number(source_branch, dest_branch):
    command = "gh pr list --base %s | grep %s" % (dest_branch,source_branch)
    output = os.popen(command).read()
    if (output!=""):
        pr_number = output.split('\t')[0]
    else:
        pr_number = None
    return pr_number



