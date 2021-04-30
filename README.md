# MRpub

To test it locally, you will need to:
1. Clone/fork this GitHub repo: `git clone https://github.com/neurolibre/neurolibre.com`
1. Make sure you're inside the **neurolibre.com/** directory (`cd neurolibre.com`), then **clone the submodule for themes:** `git submodule update --init --recursive --remote`
1. If [Hugo](https://gohugo.io/) is not installed, follow the steps in their documentation to install it on your machine: https://gohugo.io/getting-started/installing/
1. To run the website locally, make sure you are still in `neurolibre.com/` dir and type `hugo serve -D`.
   - The -D option is to serve the website including the draft .md files.
