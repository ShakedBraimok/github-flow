from src.utils.branch import create_branch, checkout
from src.utils.pull_request import create_pull_request, merge_pull_request
from src.settings import feature_prefix as prefix
from src.settings import merge_mode, next_release_branch

def main(action, head_branch):
    head_branch_without_prefix = head_branch
    head_branch = prefix + head_branch
    base_branch = next_release_branch
    if action == "create":
        branch_output = create_branch(head_branch, base_branch)
        if branch_output[0] != "stderr" or "Switched to a new branch" in str(branch_output[1]):
            note = head_branch + " branch has been created, you can start your " \
                                 "feature development, at the end please run: " \
                                 "'git flow feature -a ready %s'." % head_branch
            status = "succeed"
        else:
            note = "Failed to create %s." % head_branch
            status = "failed"
        output = [branch_output[1],note,status]

    if action == "ready":
        pr_output = create_pull_request(head_branch, base_branch)
        print(pr_output)
        if pr_output[0] != "stderr":
            note = "A Pull-Request from %s to %s has been created, if all the checks" \
                   " are done successfully - finish your work by this" \
                   " command: 'git flow feature -a done %s'." % (head_branch,base_branch,head_branch_without_prefix)
            status = "succeed"
        else:
            note = "Pull-Request creating has been failed."
            status = "failed"
        output = [pr_output[1],note,status]

    if action == "done":
        merge_output = merge_pull_request(merge_mode, head_branch, base_branch)
        if merge_output[0] != "stderr":
            note = "Great work, your feature has been merged into %s branch." % base_branch
            status = "succeed"
            checkout(base_branch)
        else:
            note = "Your feature has NOT been merged."
            status = "failed"
        output = [merge_output[1],note,status]
    return output


if __name__ == "__main__":
   main(action="",branch_name="",src_branch_name="main")