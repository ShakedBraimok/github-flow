# GitHub-Flow (`git flow`)

`git flow` is a GitHub CLI extention. It provides commands for working easily and safely according the Git-Flow.

![create feature](https://github.com/ShakedBraimok/github-flow-assets/blob/master/create-feature-example.gif)
GitHub-Flow extention is available for anyone who wants to work according the Git flow easily and safely.
Through GitHub-Flow, you will be able to assimilate and enforce the Git-Flow in your team without the need for learning or mistakes along the workflow.

## Installation
`pip install github-flow`

## Configuration (github-flow.yaml)
The main advantage of this git-flow implementation (additional to the pull-reuests before the merge),
is the centralized configuration file, all the developers workflow will be the same according this conf file.

This conf file is required, please add it to the root directory of your repository before starting work with `git flow`. 

```
---
branch:
  feature_branch_prefix: feature/
  hotfix_branch_prefix: hotfix/
  release_branch_prefix: release/
  released_branch: main
  next_release_branch: develop

release:
  create_release: true
  release_notes_file: changelog.md #OPTIONAL

pull-request:
  merge_mode: squash
```

- **create_release** - if you want to bump version (according SemVer.org) and create a tag automatically - set `true`.
- **release_notes_file** - Remove this line from the conf file if you don't have a changelog/release-notes file.
- **merge_mode** - The merge mode that will be used in your workflow.
  - **merge** - Merge the commits with the base branch
  - **rebase** - Rebase the commits onto the base branch
  - **squash** - Squash the commits into one commit and merge it into the base branch

## Usage
### Getting Started
- **Add the configuration file to your project** <br />
All you need to do to make your repository supported by Github-Flow is to add github-flow.yaml file.
![show conf file](https://github.com/ShakedBraimok/github-flow-assets/blob/master/show-conf-file.gif)

### Feature
- **Create a Feature** <br />
  `git flow feature -a create [your_feature_name]` <br />
  Behind the scenes:
  - Create a new branch with the Feature prefix ([PREFIX]/[FEATURE_NAME]) from the Next-Release-Branch (the both vars - prefix and next-release-branch are configured in the configuration file).
![create feature](https://github.com/ShakedBraimok/github-flow-assets/blob/master/create-feature-example.gif)

- **Make Feature ready to deployment** <br />
  `git flow feature -a ready [your_feature_name]` <br /> 
  Behind the scenes:
  - Create a Pull-Request from this feature branch to the Next-Release branch.
![ready feature](https://github.com/ShakedBraimok/github-flow-assets/blob/master/ready-feature.gif)
  
- **Finish with the feature development** <br />
  `git flow feature -a done [your_feature_name]` <br />
  Behind the scenes:
  - Shows the Pull-Request's checks results.
  - After acception, merges the feature's Pull-Request.
![done feature](https://github.com/ShakedBraimok/github-flow-assets/blob/master/done-feature.gif)

### Hotfix
- **Create a Hotfix** <br />
  `git flow hotfix -a create [your_hotfix_name]` <br />
  Behind the scenes:
  - Create a new branch with the Hotfix prefix ([PREFIX]/[HOTFIX_NAME]) from the Released-Branch.
![create hotfix](https://github.com/ShakedBraimok/github-flow-assets/blob/master/create-hotfix.gif)
  
- **Make Hotfix ready to deployment** <br />
  `git flow hotfix -a ready [your_hotfix_name]` <br />
  Behind the scenes:
  - Create a Pull-Request from this hotfix branch to the Next-Release branch.
  - Create a Pull-Request from this hotfix branch to the Released branch.
![ready hotfix](https://github.com/ShakedBraimok/github-flow-assets/blob/master/ready-hotfix.gif)
  
- **Finish with the Hotfix development** <br />
  `git flow hotfix -a done [your_hotfix_name]` <br />
   Behind the scenes:
  - Shows the Pull-Requests' checks results.
  - After acception, merges the Pull-Requests.
  - Bump version (Patch).
  - Create a release tag with the new version.
![done hotfix](https://github.com/ShakedBraimok/github-flow-assets/blob/master/done-hotfix.gif)
  
### Release
- **Create a new Release** <br />
  `git flow release -a create [your_release_name]` <br />
   Behind the scenes:
  - Create a new branch with the Release prefix ([PREFIX]/[RELEASE_NAME]) from the Next-Release-Branch.
  - Create a Pull-Request to the Released-Branch.
![create release](https://github.com/ShakedBraimok/github-flow-assets/blob/master/create-release.gif)

- **Publish your Release** <br />
  `git flow release -a publish [your_release_name]` <br />
   Behind the scenes:
  - Shows the Pull-Request checks results.
  - After acception, merges the Pull-Requests.
  - Bump version (Minor).
  - Create a release tag with the new version.
![publish release](https://github.com/ShakedBraimok/github-flow-assets/blob/master/publish-release.gif)

## License
This project is under the GPLv3 license.
