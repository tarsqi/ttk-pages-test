# 	ttk-pages-test

Testing the GitHub Pages site for TTK. At the initial commit the content of `docs` in this repo is the same as `docs` in https://github.com/tarsqi/ttk at tag *v3.0.0*.

To create a new version first update the version number in `../VERSION`. and then run the `docs/publish.py` script:

```bash
$> cat 3.0.1 > VERSION
$> cd docs
$> python3 publish.py
```

With the version number as above the following will happen:

1. A new directory `docs/versions/3.0.1` is created.
1. The contents of directory `docs/manual` are copied to `docs/versions/3.0.1`.
1. A new index file `docs/versions/3.0.1/index.html` is created using the template in `docs/manual/index.html`. That template takes four variables: the version number, a date in "YYYYMMDD" format, a date in "Month Year" format and a timestamp.
1. The file `docs/index.html` is created (or overwritten) using the template in `docs/templates/main_index.html` which requires one variable: the version number.

TODO:

- When this is done, create version 3.0.1. Do not create a version 3.0.0 of the documentation!  (**DONE**)

- Update CHANGELOG.  (**DONE**)

- Include running `make_documentation.py` in `publish.py`.  (**<span style="color:red;">OPEN ISSUE, NO HURRY</span>**)

- Rethink the whole documentation string issue.  (**<span style="color:red;">OPEN ISSUE, NO HURRY</span>**)

  - do we really want each version to link back to the latest docstrings? → NO
  - do we really want them on the docs site? → YES
  - may want to move some documentation out of `docs/`
    - keep publications for sure
    - maybe also some of the design documents
    - but only link to them from the main page, not from the manuals

- For version 3.0.2, think about using a publish directory that contains templates and such.  (**<span style="color:red;">OPEN ISSUE, v3.0.2</span>**)

  - should also have `make_documentation.py`
  - and instructions on where all documentation is

- The link to the random notes on github.com has to be changed from `ttk-test-pages` to `ttk.` Actually, make it the right one right now, but be sure never to add an index file to the directory unless you are willing to maintain it.  For the github.io link, it will not do anything unless there is an index link, so maybe I should generate that file automatically.  (**DONE**)

- Move some of these notes to the ttk repository.  (**<span style="color:red;">OPEN ISSUE, v3.0.2</span>**)

- Rewrite the text on the docstrings, should make clear that for any version you can run the script (allow for the possible differences between <=3.0.1 and >=3.0.2).  (**<span style="color:red;">OPEN ISSUE, v3.0.2</span>**)

  