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
### Feature
**Create a Feature**
`git flow feature -a create [your_feature_name]`
**Make Feature ready to deployment**
`git flow feature -a ready [your_feature_name]`
**Finish with the feature development**
`git flow feature -a done [your_feature_name]`

### Hotfix
**Create a Hotfix**
`git flow hotfix -a create [your_hotfix_name]`
**Make Hotfix ready to deployment**
`git flow hotfix -a ready [your_hotfix_name]`
**Finish with the Hotfix development**
`git flow hotfix -a done [your_hotfix_name]`

### Release
**Create a new Release**
`git flow release -a create [your_release_name]`
**Publish your Release**
`git flow release -a publish [your_release_name]`

## License
This project is under the GPLv3 license.
