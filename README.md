# 	ttk-pages-test

Testing the GitHub Pages site for TTK.

At the initial commit the content of `docs` in this repo is the same as `docs` in https://github.com/tarsqi/ttk at tag *v3.0.0*.

To create a new version first update the version number in `../VERSION`.

Then run this script:

```bash
$> cd docs
$> python3 publish.py
```

If the version number is 3.0.0, the following will happen:

1. A new directory `versions/3.0.0` will be created.
1. The directory `docs/manual` will be copied to `versions/3.0.0`.
1. A new index file `versions/3.0.0/index.html` will be created.
1. The file `index.html` will be created or updated.

TODO:

- The file `docs/manual/index.html` should not be copied as is. If you do, it needs to be manually updated every time you create a new version since the file includes the version number, a version date and a timestamp. Replace those with `$VERSION`, `$DATE` and `$TIMESTAMP` and use the same kind of templating as done for the index files. (**DONE**)

- Add code that updates  `docs/index.html` so it automatically has a full list of versions. Well, look at `docs/templates/main_index.html` and `docs/publish.py`, some or all of that is already done. (**DONE**)

- That file also has some links to build scripts that are now broken. (**FIXED**)
  - it looks for "../../build/install-treetagger-osx.sh", which translates to "docs/versions/build/install-treetagger-osx.sh" which is problematic since it takes the build script outside the versioned docs
  - same problem occurs for "install-mallet-osx.sh"
  - solve this by:
    - copy the build scripts to a place inside the manualinside the manual
    - update the link to "build/install-treetagger-osx.sh"
    - include the build scripts in the copying
    - wait patiently for the tagger and mallet to be removed and remove the build scripts
  
- Other broken links (**FIXED**)
  - Further documentation design links and notes link
    - Just made them go up a few levels.
  - Further documentation published papers link
    - remove this since it is linked to from `docs/index.html`.
    - actually, kept it and did the same as with the design and notes links.
  
- When this is done, create version 3.0.1. Do not create a version 3.0.0 of the documentation!  (**<span style="color:red;">OPEN ISSUE</span>**)

- Update VERSION and CHANGELOG.  (**<span style="color:red;">OPEN ISSUE</span>**)

- Update support, add VA.  (**<span style="color:red;">OPEN ISSUE</span>**)

- Get rid of the version index with link back to the code, just make that the manual.  (**<span style="color:red;">OPEN ISSUE</span>**)

- Include running `make_documentation.py` in `publish.py`.  (**<span style="color:red;">OPEN ISSUE</span>**)

- Rethink the whole documentation string issue.  (**<span style="color:red;">OPEN ISSUE</span>**)

  - do we really want each version to link back to the latest docstrings?
  - do we really want them on the docs site?
  - may want to move some documentation out of `docs/`
    - keep publications for sure
    - maybe also some of the design documents
    - but only link to them from the main page, not from the manuals

- For version 3.0.2, think about using a publish directory that contains templates and such.  (**<span style="color:red;">OPEN ISSUE</span>**)

  - should also have `make_documentation.py`
  - and instructions on where all documentation is

- Move some of these notes to the ttk repository.  (**<span style="color:red;">OPEN ISSUE</span>**)

- Rewrite the text on the docstrings, should make clear that for any version you can run the script (allow for the possible differences between <=3.0.1 and >=3.0.2).  (**<span style="color:red;">OPEN ISSUE</span>**)

  