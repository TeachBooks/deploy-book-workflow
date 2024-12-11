(deploy-book-workflow)=
# Releasing book online

```{admonition} User types
:class: tip
This page is useful for user type 3, 4 and 5.
```
+++
{bdg-light}`GitHub Reusable Action`

We developed a workflow which builds your TeachBook in your repository for all branches and publishes them online via GitHub Pages. In simplified terms, it builds the website based on your repository.

The [TeachBooks Template](https://github.com/TeachBooks/template) uses this functionality for example. The workflow `call-deploy-book.yml` calls the `deploy-book.yml` workflow, which builds the Jupyter books at the calling repository for all branches, and deploys them via GitHub Pages.

The workflow has the following features:
- Releasing of your [TeachBook](https://teachbooks.io/)-repository (built with [Jupyter Book](https://github.com/executablebooks/jupyter-book)) to GitHub Pages
- Ability to release both private (GitHub Pro, GitHub Team, GitHub Enterprise Cloud, or GitHub Enterprise Server required) and public (GitHub Free is enough) repositories.  
GitHub Teams is free for teachers as described in the [GitHub documentation](https://docs.github.com/en/education/explore-the-benefits-of-teaching-and-learning-with-github-education/github-education-for-teachers/about-github-education-for-teachers#github-education-features-for-teachers).  
If you have an organization for your TeachBook on GitHub, link your GitHub team rights to your organization as described on the [GitHub website](https://github.com/team#organizations).
- Releasing all or a selection of branches, allowing to build a draft version of the TeachBook online which reduces the need for local builds of the book
- Provides a summary describing where the TeachBook is released, errors in the build process per branch and how the release step is configured
- Caching of already built books so that it can be partially reused when another branch is released or the next build contains critical errors
- Caching of python environment to speed up the workflow
- Allowing to use submodules within your book
- Customizable trigger for the workflow itself
- Optionally preprocess branches using the [`teachbooks` package](https://github.com/TeachBooks/TeachBooks).
- Converting branch-names to well-defined URLs
- Customizable settings on where the books should be deployed including alias for branch-names and selection of one branch to be deployed on root. The workflow will gives warnings if these settings are ill-defined or conflicting. Although aliases are not allowed by GitHub Pages, it seems you can use one alias, but not more.
- Redirects the root directory to one of the branches or copies one of the branches to root.
- Adds an 'archived'-banner to old branches / branches of previous years.

## How to start using this workflow
As previously mentioned, this workflow is used in `TeachBooks/template`. Feel free to use it for your TeachBook as well:
1. Add [`teachbooks`](https://github.com/TeachBooks/TeachBooks) to your `requirements.txt` file in your root folder
2. Move all the TeachBook files (including `_config.yml` and `_toc.yml`) to a subdirectory `book/`.
3. Copy the [`call-deploy-book.yml`](https://github.com/TeachBooks/deploy-book-workflow/blob/main/.github/workflows/call-deploy-book.yml) workflow to the `/.github/workflows` folder in your repository.
4. Set source for GitHub pages to GitHub Actions under <svg aria-label="Edit repository metadata" role="img" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-gear float-right">    <path d="M8 0a8.2 8.2 0 0 1 .701.031C9.444.095 9.99.645 10.16 1.29l.288 1.107c.018.066.079.158.212.224.231.114.454.243.668.386.123.082.233.09.299.071l1.103-.303c.644-.176 1.392.021 1.82.63.27.385.506.792.704 1.218.315.675.111 1.422-.364 1.891l-.814.806c-.049.048-.098.147-.088.294.016.257.016.515 0 .772-.01.147.038.246.088.294l.814.806c.475.469.679 1.216.364 1.891a7.977 7.977 0 0 1-.704 1.217c-.428.61-1.176.807-1.82.63l-1.102-.302c-.067-.019-.177-.011-.3.071a5.909 5.909 0 0 1-.668.386c-.133.066-.194.158-.211.224l-.29 1.106c-.168.646-.715 1.196-1.458 1.26a8.006 8.006 0 0 1-1.402 0c-.743-.064-1.289-.614-1.458-1.26l-.289-1.106c-.018-.066-.079-.158-.212-.224a5.738 5.738 0 0 1-.668-.386c-.123-.082-.233-.09-.299-.071l-1.103.303c-.644.176-1.392-.021-1.82-.63a8.12 8.12 0 0 1-.704-1.218c-.315-.675-.111-1.422.363-1.891l.815-.806c.05-.048.098-.147.088-.294a6.214 6.214 0 0 1 0-.772c.01-.147-.038-.246-.088-.294l-.815-.806C.635 6.045.431 5.298.746 4.623a7.92 7.92 0 0 1 .704-1.217c.428-.61 1.176-.807 1.82-.63l1.102.302c.067.019.177.011.3-.071.214-.143.437-.272.668-.386.133-.066.194-.158.211-.224l.29-1.106C6.009.645 6.556.095 7.299.03 7.53.01 7.764 0 8 0Zm-.571 1.525c-.036.003-.108.036-.137.146l-.289 1.105c-.147.561-.549.967-.998 1.189-.173.086-.34.183-.5.29-.417.278-.97.423-1.529.27l-1.103-.303c-.109-.03-.175.016-.195.045-.22.312-.412.644-.573.99-.014.031-.021.11.059.19l.815.806c.411.406.562.957.53 1.456a4.709 4.709 0 0 0 0 .582c.032.499-.119 1.05-.53 1.456l-.815.806c-.081.08-.073.159-.059.19.162.346.353.677.573.989.02.03.085.076.195.046l1.102-.303c.56-.153 1.113-.008 1.53.27.161.107.328.204.501.29.447.222.85.629.997 1.189l.289 1.105c.029.109.101.143.137.146a6.6 6.6 0 0 0 1.142 0c.036-.003.108-.036.137-.146l.289-1.105c.147-.561.549-.967.998-1.189.173-.086.34-.183.5-.29.417-.278.97-.423 1.529-.27l1.103.303c.109.029.175-.016.195-.045.22-.313.411-.644.573-.99.014-.031.021-.11-.059-.19l-.815-.806c-.411-.406-.562-.957-.53-1.456a4.709 4.709 0 0 0 0-.582c-.032-.499.119-1.05.53-1.456l.815-.806c.081-.08.073-.159.059-.19a6.464 6.464 0 0 0-.573-.989c-.02-.03-.085-.076-.195-.046l-1.102.303c-.56.153-1.113.008-1.53-.27a4.44 4.44 0 0 0-.501-.29c-.447-.222-.85-.629-.997-1.189l-.289-1.105c-.029-.11-.101-.143-.137-.146a6.6 6.6 0 0 0-1.142 0ZM11 8a3 3 0 1 1-6 0 3 3 0 0 1 6 0ZM9.5 8a1.5 1.5 0 1 0-3.001.001A1.5 1.5 0 0 0 9.5 8Z"></path> </svg>`Settings` - <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-browser">    <path d="M0 2.75C0 1.784.784 1 1.75 1h12.5c.966 0 1.75.784 1.75 1.75v10.5A1.75 1.75 0 0 1 14.25 15H1.75A1.75 1.75 0 0 1 0 13.25ZM14.5 6h-13v7.25c0 .138.112.25.25.25h12.5a.25.25 0 0 0 .25-.25Zm-6-3.5v2h6V2.75a.25.25 0 0 0-.25-.25ZM5 2.5v2h2v-2Zm-3.25 0a.25.25 0 0 0-.25.25V4.5h2v-2Z"></path> </svg> `Pages` - `Build and deployment` - `Source` - `GitHub Actions` (as long as you don't do this the workflow deploys all branches which build successfully).
5. (Only required for private repositories) Create a Personal Access Token (classic) with at least the scopes `repo`, `read:org` and `gist` as described in the [github documentation](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens), and add this token with the name `GH_PAT` as a `Repository secret` or `Organization secret` (<svg aria-label="Edit repository metadata" role="img" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-gear float-right">    <path d="M8 0a8.2 8.2 0 0 1 .701.031C9.444.095 9.99.645 10.16 1.29l.288 1.107c.018.066.079.158.212.224.231.114.454.243.668.386.123.082.233.09.299.071l1.103-.303c.644-.176 1.392.021 1.82.63.27.385.506.792.704 1.218.315.675.111 1.422-.364 1.891l-.814.806c-.049.048-.098.147-.088.294.016.257.016.515 0 .772-.01.147.038.246.088.294l.814.806c.475.469.679 1.216.364 1.891a7.977 7.977 0 0 1-.704 1.217c-.428.61-1.176.807-1.82.63l-1.102-.302c-.067-.019-.177-.011-.3.071a5.909 5.909 0 0 1-.668.386c-.133.066-.194.158-.211.224l-.29 1.106c-.168.646-.715 1.196-1.458 1.26a8.006 8.006 0 0 1-1.402 0c-.743-.064-1.289-.614-1.458-1.26l-.289-1.106c-.018-.066-.079-.158-.212-.224a5.738 5.738 0 0 1-.668-.386c-.123-.082-.233-.09-.299-.071l-1.103.303c-.644.176-1.392-.021-1.82-.63a8.12 8.12 0 0 1-.704-1.218c-.315-.675-.111-1.422.363-1.891l.815-.806c.05-.048.098-.147.088-.294a6.214 6.214 0 0 1 0-.772c.01-.147-.038-.246-.088-.294l-.815-.806C.635 6.045.431 5.298.746 4.623a7.92 7.92 0 0 1 .704-1.217c.428-.61 1.176-.807 1.82-.63l1.102.302c.067.019.177.011.3-.071.214-.143.437-.272.668-.386.133-.066.194-.158.211-.224l.29-1.106C6.009.645 6.556.095 7.299.03 7.53.01 7.764 0 8 0Zm-.571 1.525c-.036.003-.108.036-.137.146l-.289 1.105c-.147.561-.549.967-.998 1.189-.173.086-.34.183-.5.29-.417.278-.97.423-1.529.27l-1.103-.303c-.109-.03-.175.016-.195.045-.22.312-.412.644-.573.99-.014.031-.021.11.059.19l.815.806c.411.406.562.957.53 1.456a4.709 4.709 0 0 0 0 .582c.032.499-.119 1.05-.53 1.456l-.815.806c-.081.08-.073.159-.059.19.162.346.353.677.573.989.02.03.085.076.195.046l1.102-.303c.56-.153 1.113-.008 1.53.27.161.107.328.204.501.29.447.222.85.629.997 1.189l.289 1.105c.029.109.101.143.137.146a6.6 6.6 0 0 0 1.142 0c.036-.003.108-.036.137-.146l.289-1.105c.147-.561.549-.967.998-1.189.173-.086.34-.183.5-.29.417-.278.97-.423 1.529-.27l1.103.303c.109.029.175-.016.195-.045.22-.313.411-.644.573-.99.014-.031.021-.11-.059-.19l-.815-.806c-.411-.406-.562-.957-.53-1.456a4.709 4.709 0 0 0 0-.582c-.032-.499.119-1.05.53-1.456l.815-.806c.081-.08.073-.159.059-.19a6.464 6.464 0 0 0-.573-.989c-.02-.03-.085-.076-.195-.046l-1.102.303c-.56.153-1.113.008-1.53-.27a4.44 4.44 0 0 0-.501-.29c-.447-.222-.85-.629-.997-1.189l-.289-1.105c-.029-.11-.101-.143-.137-.146a6.6 6.6 0 0 0-1.142 0ZM11 8a3 3 0 1 1-6 0 3 3 0 0 1 6 0ZM9.5 8a1.5 1.5 0 1 0-3.001.001A1.5 1.5 0 0 0 9.5 8Z"></path> </svg>`Settings` > <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-key-asterisk">    <path d="M0 2.75A2.75 2.75 0 0 1 2.75 0h10.5A2.75 2.75 0 0 1 16 2.75v10.5A2.75 2.75 0 0 1 13.25 16H2.75A2.75 2.75 0 0 1 0 13.25ZM2.75 1.5c-.69 0-1.25.56-1.25 1.25v10.5c0 .69.56 1.25 1.25 1.25h10.5c.69 0 1.25-.56 1.25-1.25V2.75c0-.69-.56-1.25-1.25-1.25Z"></path><path d="M8 4a.75.75 0 0 1 .75.75V6.7l1.69-.975a.75.75 0 0 1 .75 1.3L9.5 8l1.69.976a.75.75 0 0 1-.75 1.298L8.75 9.3v1.951a.75.75 0 0 1-1.5 0V9.299l-1.69.976a.75.75 0 0 1-.75-1.3L6.5 8l-1.69-.975a.75.75 0 0 1 .75-1.3l1.69.976V4.75A.75.75 0 0 1 8 4Z"></path></svg>`Secrets and variables` > `Actions` > `Repository secrets` or `Organization secrets`.)
6. Trigger the workflow by making an edit to the TeachBook by editing and committing changes to one of the files in the `book/` subdirectory (available under <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-code UnderlineNav-octicon d-none d-sm-inline">    <path d="m11.28 3.22 4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.275-.326.749.749 0 0 1 .215-.734L13.94 8l-3.72-3.72a.749.749 0 0 1 .326-1.275.749.749 0 0 1 .734.215Zm-6.56 0a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042L2.06 8l3.72 3.72a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L.47 8.53a.75.75 0 0 1 0-1.06Z"></path></svg> `Code`) or manually activating the workflow under <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-play UnderlineNav-octicon d-none d-sm-inline">    <path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM1.5 8a6.5 6.5 0 1 0 13 0 6.5 6.5 0 0 0-13 0Zm4.879-2.773 4.264 2.559a.25.25 0 0 1 0 .428l-4.264 2.559A.25.25 0 0 1 6 10.559V5.442a.25.25 0 0 1 .379-.215Z"></path></svg>`Actions` - `All workflows` -  `call-deploy-book` - `Run workflow` - `Use workflow from branch: <the branch you did step 1, 2 and 3 in>` - `Run workflow` (this workflow).
7. Now checkout the progress and summary of the releasing workflow under <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-play UnderlineNav-octicon d-none d-sm-inline">    <path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM1.5 8a6.5 6.5 0 1 0 13 0 6.5 6.5 0 0 0-13 0Zm4.879-2.773 4.264 2.559a.25.25 0 0 1 0 .428l-4.264 2.559A.25.25 0 0 1 6 10.559V5.442a.25.25 0 0 1 .379-.215Z"></path></svg>`Actions` - `All workflows` -  `call-deploy-book` -`<the most recent workflow run>`.

(gh-workflow-settings)=
## Customize the workflow: TeachBook releasing settings
You can adapt the behaviour by setting repository variables as explained [here](https://docs.github.com/en/actions/learn-github-actions/variables#creating-configuration-variables-for-a-repository) or using the [VS Code Extension GitHub Actions](https://marketplace.visualstudio.com/items?itemName=GitHub.vscode-github-actions). Define the following repository variables:
- `PRIMARY_BRANCH` which is set to `main` whenever it's not defined in the repository variables.
  - This sets the branch or alias (when using 'redirect' for `BEHAVIOR_PRIMARY`) which is shown on root.
  - It is advised to show your most recent branch on root.
- `BEHAVIOR_PRIMARY` which is set to `redirect` whenever it's not defined in the repository variables.
  - This indicates whether to copy the PRIMARY_BRANCH to root ('copy') or redirect from root to the PRIMARY_BRANCH ('redirect')
  - Advised to use 'redirect' if you expect to archive a version in the future so that the URL doesn't change for the reader.
- `BRANCH_ALIASES` which is set to ` ` (just a space) whenever it's not defined in the repository variables.
  - This defines an alias (custom URL) for a branch
  - Variables should be a space-separated list of branch names, e.g. 'alias:really-long-branch-name`
  - If no alias is wanted, `BRANCH_ALIASES` may be set to ` ` (just a space)
- `BRANCHES_TO_DEPLOY`  which is set to `*` (all branches) whenever it's not defined in the repository variables.
  - This defines the branches to deploy.
  - It should be a space-separated list of branch names, e.g. 'main second third'.
- `BRANCHES_TO_PREPROCESS` which is to to ` ` (just a space = no branch) whenever it's not defined in the repository variables
  - This defines the branches to preprocess with the [`TeachBooks` package](https://teachbooks.io/TeachBooks/cli/cli.html#cmdoption-teachbooks-build), which removed book-pages and config lines defined with `# START REMOVE FROM RELEASE` and `# END REMOVE FROM RELEASE`
  - It should be a space-separated list of branch names, e.g. 'main second third'.
  - If no preprocessing is required, `BRANCH_TO_PREPROCESS` may be set to ' ' (space).
- `BRANCHES_ARCHIVED` which is set to ` ` (space, no branch) whenever it's not defined in the repository variables
  - This adds a banner to the released branch: You are viewing an archived version of the book. Click here for the latest version.
  - It should be a space-separate list of branch names, e.g. 'main second third'.

In `call-deploy-book.yml` itself you can specify the trigger for this workflow. By default, a push to any branch triggers the workflow. You can limit the branches or subdirectories.

## View the workflow progress and summary

Whenever the workflow is triggered, its progress and a summary can be seen under the <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-play UnderlineNav-octicon d-none d-sm-inline">    <path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM1.5 8a6.5 6.5 0 1 0 13 0 6.5 6.5 0 0 0-13 0Zm4.879-2.773 4.264 2.559a.25.25 0 0 1 0 .428l-4.264 2.559A.25.25 0 0 1 6 10.559V5.442a.25.25 0 0 1 .379-.215Z"></path></svg>`Actions`- `All workflows` -  `call-deploy-book` in GitHub! It shows you a descriptive summary:
- Ill-defined repository configuration variables (in `Annotations`)
- Which branches are released and where (`https://<username/organization_name>.github.io/<repository_name>` (case sensitive)) including which branch is released on the website root and the applied alias
- Errors in the build process 
- How the repository variables are defined during the build.

Here's an example for a summary for the template book:

> ### Branches deployed
> | Branch 🎋 | Link 🔗 | Build status ☑️ |
> | :--- | :--- | :--- |
> | main | [https://teachbooks.github.io/template/main](https://teachbooks.github.io/template/main) | ✅ `Released` |
> | version2 | [https://teachbooks.github.io/template/version2](https://teachbooks.github.io/template/version2) | 🔴 `Build failed [1]` |
> | version3 | [https://teachbooks.github.io/template/version3](https://teachbooks.github.io/template/version3) | ⭕ `Build failed [2]` |
> 
> #### Legend for build status
> ✅ `Released` - build success, new version released.
>
> 🔴 `Build failed [1]` - build failure, previous version of the book reused.
>
> ⭕ `Build failed [2]` - build failure, no previous version reused.
>
> #### Primary book at root
> The book at the website root <https://teachbooks.github.io/template/> redirects to the primary branch `main` (status: ✅ `Released`).
> 
> ### Aliases
> | Alias ➡️ | Target 🎯 | Link 🔗 |  Build status ☑️ |
> | :--- | :--- | :--- | :---- |
> | draft | main | [https://teachbooks.github.io/template/draft](https://teachbooks.github.io/template/draft) | ✅ `Released` |
> 
> ### Preview of build errors & warnings
> For more details please see the corresponding `build-books` jobs in the left pane.
>
> On branch `version2`:
> ```
> �[91m/home/runner/work/template/template/book/some_content/overview.md:5: WARNING: Non-consecutive header level increase; H1 to H3 [myst.header]�[39;49;00m
> ``` 
>
> On branch `version3`:
> ```
> /home/runner/work/_temp/ff8c8325-8d8b-4c0b-a2b2-32d2169c55bc.sh: line 8: teachbooks: command not found
> ```
>
> ### Repository configuration variables
> Variables can be set at <https://github.com/TeachBooks/template/settings/variables/actions>
>
> ```
> PRIMARY_BRANCH=main (default value used)
> BRANCH_ALIASES=draft:main
> BRANCHES_TO_DEPLOY=* (default value used)
> BRANCHES_TO_PREPROCESS=main
> BEHAVIOR_PRIMARY=redirect (default value used)
> BRANCHES_ARCHIVED= (default value used)
> ```

## Contribute
This tool's repository is stored on [GitHub](https://github.com/TeachBooks/deploy-book-workflow). The `README.md` of the branch `manual_docs` is also part of the [TeachBooks manual](https://teachbooks.io/manual/external/deploy-book-workflow/README.html) as a submodule. If you'd like to contribute, you can create a fork and open a pull request on the [GitHub repository](https://github.com/TeachBooks/deploy-book-workflow). To update the `README.md` shown in the TeachBooks manual, create a fork and open a merge request for the [GitHub repository of the manual](https://github.com/TeachBooks/manual). If you intent to clone the manual including its submodules, clone using: `git clone --recurse-submodulesgit@github.com:TeachBooks/manual.git`.
