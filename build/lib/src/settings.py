from src.utils.config_file import get_config_value

#--- github-flow.yml parsing ---#
feature_prefix = get_config_value("branch","feature_branch_prefix")
hotfix_prefix = get_config_value("branch","hotfix_branch_prefix")
release_prefix = get_config_value("branch","release_branch_prefix")
next_release_branch = get_config_value("branch","next_release_branch")
released_branch = get_config_value("branch","released_branch")
create_release = get_config_value("release","create_release")
release_notes_file = get_config_value("release","release_notes_file")
release_title = get_config_value("release","release_title")
merge_mode = get_config_value("pull-request","merge_mode")

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'