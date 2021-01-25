from src.utils.branch import create_branch, checkout
from src.utils.pull_request import create_pull_request, merge_pull_request
from src.utils.release import create_release, get_latest
from src.utils.bump_version import bump_version
from src.settings import hotfix_prefix as prefix
from src.settings import merge_mode, release_notes_file, released_branch, next_release_branch

def main(action, head_branch):
    head_branch_without_prefix = head_branch
    base_branch = released_branch
    head_branch = prefix + head_branch
    if action == "create":
        branch_output = create_branch(head_branch, base_branch)
        if branch_output != "stderr" or "Switched to a new branch" in str(branch_output[1]):
            note = head_branch + " branch has been created, you can start your " \
                                 "hotfix development, at the end please run: " \
                                 "'git flow feature -a ready %s'." % (head_branch)
            status = "succeed"
        else:
            note = "Failed to create %s." % head_branch
            status = "failed"
        output = [branch_output[1],note,status]

    if action == "ready":
        pr_rb_output = create_pull_request(head_branch, base_branch)
        if pr_rb_output[0] != "stderr":
            pr_nrb_output = create_pull_request(head_branch, next_release_branch)
            if pr_nrb_output[0] != "stderr":
                output_msgs = pr_rb_output[1] + pr_nrb_output[1]
                note = '2 Pull-Requests have been created (from "%s" to "%s" and from "%s" to "%s"), ' \
                       'if all the checks done successfully finish your work by this' \
                       ' command: "git flow hotfix -a done %s".' \
                       % (head_branch, base_branch, head_branch, next_release_branch, head_branch_without_prefix)
                status = "succeed"
                output = [output_msgs,note,status]
            else:
                note = "Failed to create a Pull-Request to %s." % next_release_branch
                status = "failed"
                output = [str(pr_nrb_output[1]), note, status]
        elif "already exists" in str(pr_rb_output[1]):
            print("Pull-Request to %s already exist." % base_branch)
            pr_nrb_output = create_pull_request(head_branch, next_release_branch)
            if pr_rb_output[0] != "stderr":
                note = 'A Pull-Request to %s has been created, ' \
                       'if all the checks done successfully finish your work by this' \
                       ' command: "git flow hotfix -a done %s".' \
                       % (next_release_branch, head_branch)
                status = "succeed"

            elif "already exists" in str(pr_nrb_output[1]):
                note = "Pull-Request to %s already exists." % next_release_branch
                status = "failed"

            else:
                note = "Failed to create a Pull-Reqquest to: %s." % next_release_branch
                status = "failed"
            output = [pr_nrb_output, note, status]

        else:
            note = "Your hotfix is not ready.\nPull-Requests for your hotfix branch have NOT been created."
            status = "failed"
            output = [str(pr_rb_output[1]), note, status]


    if action == "done":
        merge_rb_output = merge_pull_request(merge_mode, head_branch, base_branch)
        if merge_rb_output[0] != "stderr":
            merge_nrb_output = merge_pull_request(merge_mode, head_branch, next_release_branch)
            if merge_nrb_output[0] != "stderr":
                latest_version = get_latest()
                part_to_bump = "patch"
                version = bump_version(latest_version,part_to_bump)
                release_output = create_release(version,release_notes_file)
                note = "Congrats! a new release has been published."
                status = "succeed"
                merge_output = "Merged successfully."
                output = [merge_output + str(release_output[1]),note,status]
                checkout(base_branch)
            else:
                note = "Your Hotfix has NOT been merged to %s." % next_release_branch
                status = "failed"
                output = [str(merge_nrb_output[1]),note,status]
        else:
            note = "Your Hotfix has NOT been merged."
            status = "failed"
            output = [str(merge_rb_output[1]), note, status]

    return output



if __name__ == "__main__":
   main(action="",branch_name="",src_branch_name="main")