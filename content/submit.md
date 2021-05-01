# What can be shared on MR-Pub?

MR-Pub currently welcomes interactive [Jupyter Books](https://jupyterbook.org/intro.html) along two tracks:
 - **Education** notebooks related to a workshop in the MRI field.
 - **Research** notebooks for articles published in Magnetic Resonance in Medicine.

# How to submit?

1. Create a public repository on [GitHub](https://github.com/) which will host the files.
2. Create a `content` folder at the root of your repository:
> * Place your [Jupyter](https://jupyter.org/) notebook(s) (`.ipynb`) and markdown files (optional)
> * Create a [`_toc.yml`](https://jupyterbook.org/customize/toc.html) to structure your book with the table of contents.
> * Create a [`_config.yml`](https://jupyterbook.org/customize/config.html) to configure book settings.
5. Create a `binder` folder at the root of your repository:
> * Add your [configuration files](https://mybinder.readthedocs.io/en/latest/using/config_files.html) to capture all the software dependencies.
> * For a list of sample repositories for use with Binder, see the [Sample Binder Repositories](https://mybinder.readthedocs.io/en/latest/examples/sample_repos.html) page.
6. Go to https://mybinder.org
7. Fill the repository name and save the given URL. This will be used to share your binder notebooks with others.
8. Click on `launch` and wait for the build. Please be patient, as the first build may take a long time depending on your setup. When your notebook loads, you are ready to share your notebooks!
9. [Create an issue](https://github.com/neurolibre/submit/issues/new?assignees=pbellec&labels=&template=submission.md&title=%5BSUBMISSION%5D) in this repository, using the "Submission" template, and fill in all the information. 
10. Our team will fork your repository on https://github.com/neurolibre. We will test that everything is working, and contact you using your github handle for any issue we identify. The issues will be open on our fork of the repo, and you will be expected to submit pull request to this fork to address any issue.

–
