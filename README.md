# Reusable workflow for `TeachBooks/template` and other books

The workflow `call-deploy-book.yml` calls the `deploy-book.yml` workflow in this repository, which builds the Jupyter books at the calling repository for all branches, and deploys them via GitHub Pages.
This workflow is used in `TeachBooks/template` and its forks. Feel free to juse it for your TeachBook aswell: copy the [`call-deploy-book.yml` workflow](https://github.com/TeachBooks/deploy-book-workflow/blob/main/.github/workflows/call-deploy-book.yml) to the `/.github/workflows` folder in your repository.

You can adapt the behaviour by setting repository variables as explained [here](https://docs.github.com/en/actions/learn-github-actions/variables#creating-configuration-variables-for-a-repository). Define the following repository variables:
- `PRIMARY_BRANCH` which is set to `main` whenever it's not defined in the repository variables.
  - This sets the branch which is hosted on root.
  - It is advised to make it `published` to start using draft-publish-workflow
- `BRANCH_ALIASES` which is set to `draft:main` whenever it's not defined in the repository variables.
  - This defines aliases for branches
  - It should be a space-separated list of alias-rules, e.g. 'draft:main alias:really-long-branch-name`
  - It is advised to link `book` to `publish`.
  - If no aliases are wanted, BRANCH_ALIASES may be set to ' ' (space).
- `BRANCHES_TO_DEPLOY`  which is set to `*` (all branches) whenever it's not defined in the repository variables.
  - This defines the branches to deploy.
  - It should be a space-separated list of branch names, e.g. 'main second third'.- 

In `call-deploy-book.yml` itself you can specify the trigger for this workflow. By default, a push to any branch trigger the workflow. You can limit the branches or subdirectories.

Whenever the workflow is triggered, progress can be seen under the `Actions` tab. From this tab, you can also initiate it without any trigger commits.

If you find the default template workflow could be improved, please open an issue at [Issues](https://github.com/TeachBooks/deploy-book-workflow/issues).


