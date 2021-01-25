from src.utils.branch import create_branch, checkout
from src.utils.pull_request import create_pull_request, merge_pull_request
from src.utils.release import create_release, get_latest
from src.utils.bump_version import bump_version
from src.settings import release_prefix as prefix
from src.settings import merge_mode, release_notes_file, next_release_branch, released_branch

def main(action,head_branch):
    head_branch_without_prefix = head_branch
    head_branch = prefix + head_branch
    if action == "create":
        base_branch = next_release_branch
        branch_output = create_branch(head_branch, base_branch)
        if branch_output[0] != "stderr" or "Switched to a new branch" in str(branch_output[1]):
            base_branch =  released_branch
            pr_output = create_pull_request(head_branch, base_branch)
            if pr_output[0] != "stderr":
                output_msgs = str(branch_output[1]) + str(pr_output[1])
                note = "Created: %s branch and a Pull-Request (%s --> %s).\n When you ready to deploy your new release, " \
                       "please run the command: 'git flow release -a publish %s'" % (
                       head_branch, head_branch, base_branch, head_branch_without_prefix)
                status = "succeed"
            else:
                output_msgs = pr_output[1]
                note = "Release branch %s has been created, but failed to create a Pull-Request to %s." % (head_branch, base_branch)
                status = "failed"
        else:
            output_msgs = branch_output[1]
            note = "Failed to create the branch: %s." % (head_branch)
            status = "failed"

        output = [output_msgs,note,status]


    if action == "publish":
        base_branch = released_branch
        #--- MERGE ---#
        merge_output = merge_pull_request(merge_mode, head_branch, base_branch)
        # --- RELEASE ---#
        if merge_output[0] != "stderr":
            latest_version = get_latest()
            part_to_bump = "minor"
            version = bump_version(latest_version,part_to_bump)
            release_output = create_release(version,release_notes_file)
            note = "Congrats! a new release has been published."
            status = "succeed"
            output = [str(merge_output[1]) + str(release_output[1]),note,status]
            checkout(base_branch)
        else:
            note = "Your release has NOT been merged."
            status = "failed"
            output = [str(merge_output[1]),note,status]
    return output


if __name__ == "__main__":
   main(action="create",head_branch="test-release-branch",prefix="release/",base_branch="develop")