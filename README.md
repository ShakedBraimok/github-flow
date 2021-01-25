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

## License
This project is under the GPLv3 license.
