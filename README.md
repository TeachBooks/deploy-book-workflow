````{margin}
```{attributiongrey} Attribution
:class: attribution
This page reuses BSD 3-Clause License content from {cite:t}`deploy_book`. {fa}`quote-left`{ref}`Find out more here.<external_resources>`
```

```{admonition} User types
:class: tip
This page is useful for user type 3, 4 and 5.
```

{bdg-light}`GitHub Reusable Action`
````

(deploy-book-workflow)=
# Deploy Book workflow

The Deploy Book Workflow is a GitHub Reuseable Action which takes all versions of your TeachBooks and shared it online.

The Deploy Book Workflow is by default incorporated into any book that has been created using the [TeachBooks Template](https://github.com/TeachBooks/template). We also strongly encourage anyone to consider this tool as an alternative to the "standard" workflow provided by Jupyter Book because of it's additional features.

The workflow `call-deploy-book.yml` calls the `deploy-book.yml` workflow, which builds a Jupyter Book at the calling repository for all branches, and deploys them via GitHub Pages. It is currently configured to create a Jupyter Book using the TeachBooks Python package (i.e., `teachbooks build book`), although this may be adapted in the future to make it easier to use in other applications (e.g., to build books with other software or any static website in general).

The workflow allows you to:
- [Release all versions your TeachBook-repository to GitHub Pages](https://teachbooks.io/manual/features/release_book_online.html)
- [Write book fully in GitHub interface](https://teachbooks.io/manual/features/write_online.html)

The linked pages described those activities in more detail.

It works for any book created with the Jupyter Books and/or TeachBooks.

## Related features

A list of tools and features that are dependent on, or related to, the Deploy Book Workflow (DBW) is provided here:

- [TeachBooks template](https://github.com/TeachBooks/template): books created from the Template include DBW by default
- [Draft-release workflow](https://teachbooks.io/manual/features/draft-release.html): can be configured directly using the DBW
- [Auto-updating packages](https://teachbooks.io/manual/features/update_env.html): behaviors of this tool may influence the DBW
- [TeachBooks package](https://github.com/Teachbooks/teachbooks): included by default in the DBW
- [TeachBook recombiner](https://teachbooks.io/recombiner/): works best with books published with the DBW
- [Sharing content between books in table of contents](https://teachbooks.readthedocs.io/latest/external.html): is included by defualt in the DBW because of the use of the TeachBooks package
- [Sharing content between books using submodules](https://teachbooks.io/manual/external/Nested-Books/README.html): is supported by DBW.
- [Build pull requests from forks](https://teachbooks.io/manual/features/pull_request_build.html): created to provide DBW-like behavior for PR's from forked repositories
- [APA references](https://teachbooks.io/manual/features/apa.html): a temporary fix is included in `teachbooks` to enable use in the DBW

## Contribute
This tool's repository is stored on [GitHub](https://github.com/TeachBooks/deploy-book-workflow). The `README.md` of the branch `manual_docs` is also part of this [TeachBooks manual](https://teachbooks.io/manual/external/deploy-book-workflow/README.html) as a submodule. If you'd like to contribute, you can create a fork and open a pull request on the [GitHub repository](https://github.com/TeachBooks/deploy-book-workflow). To update the `README.md` shown in the TeachBooks manual, create a fork and open a merge request for the [GitHub repository of the manual](https://github.com/TeachBooks/manual). If you intent to clone the manual including its submodules, clone using: `git clone --recurse-submodulesgit@github.com:TeachBooks/manual.git`.

To test changes to the deploy book workflow do the following:
1. Create a fork of the repository and make a commit to `deploy-book.yml`
2. Using a book repository (e.g., a book created from the TeachBooks Template), edit the `call-deploy-book..yml` file such that `TeachBooks/deploy-book-workflow/.github/workflows/deploy-book.yml@main` is replaced with the repository and branch path to your modified file `deploy-book.yml`
3. Make a commit in the book repository that triggers the workflow and confirm that the job runs successfully.

Future improvements to the DBW may address the ability for a user to specify additional aspects of the build process, for example, the Python version or the specific book build commands (e.g., `teachbooks build` or `jupyter-book build`). If this is something that interests you, please create an Issue in the repository (perhaps with "feature request" in the title).
