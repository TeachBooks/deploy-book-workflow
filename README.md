# Reusable workflow for `TeachBooks/template`

The workflow `call-deploy-book.yml` in `TeachBooks/template` (and in repositories cloned from `TeachBooks/template`) calls the `deploy-book.yml` workflow in this repository, which builds the Jupyter books at the calling repository,
and deploys them via GitHub Pages.

If you find the default template workflow could be improved, please open an issue at [Issues](https://github.com/TeachBooks/deploy-book-workflow/issues).


