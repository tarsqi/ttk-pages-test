"""publish.py

Create a new version of the documentation in the versions directory, using the
version number in the VERSION file in the top-level of the repository.

Also creates or updates the docs/index.html file to reflect the new current
version as well as the list of all existing versions that run on Python 3.

Usage: just run the script from this directory.

"""

import os
import re
import time
import shutil
from string import Template


MAIN_INDEX_TEMPLATE_FILE = 'templates/main_index.html'
VERSION_INDEX_TEMPLATE_FILE = 'templates/version_index.html'
MANUAL_INDEX_TEMPLATE_FILE = 'manual/index.html'
VERSION_FILE = '../VERSION'


def read_version():
    with open(VERSION_FILE) as fh:
        return fh.read().strip()


def get_date():
    return time.strftime("%B %Y")


def get_d():
    return time.strftime("%B %Y")


def read_template(template_file):
    with open(template_file) as fh:
        return Template(fh.read())


def copy_current_version(version, date1, date2, timestamp):
    # copy everything in themanual directory
    os.makedirs("versions/%s" % version, exist_ok=True)
    shutil.copytree("manual", "versions/%s/manual" % version, dirs_exist_ok=True)
    # now overwrite the index file using the template
    index_file = f"versions/{version}/manual/index.html"
    index_template = "manual/index.html"
    manual_index_template = read_template(MANUAL_INDEX_TEMPLATE_FILE)    
    with open(index_file, 'w') as fh:
        fh.write(manual_index_template.substitute(
            VERSION=version, DATE=date1, DATE_STR=date2, TIMESTAMP=timestamp))

    
def create_version_index_file(version):
    version_index_template = read_template(VERSION_INDEX_TEMPLATE_FILE)    
    with open('versions/%s/index.html' % version, 'w') as fh:
        fh.write(version_index_template.substitute(VERSION=version))


def create_main_index_file(version):
    main_index_template = read_template(MAIN_INDEX_TEMPLATE_FILE)
    versions = generate_versions_list()
    with open('index.html', 'w') as fh:
        fh.write(main_index_template.substitute(VERSION=version, VERSIONS=versions))


def generate_versions_list():
    versions = sorted(os.listdir('versions'), reverse=True)
    versions = [v for v in versions if is_valid(v)]
    strbuffer = ''
    for version in versions:
        strbuffer += f'      <li><a href="versions/{version}/index.html">version {version}</a></li>\n'
    return strbuffer


def is_valid(version):
    return re.match("^\d+\.\d+\.\d+$", version) is not None


if __name__ == '__main__':

    version = read_version()
    date1 = time.strftime("%Y%m%d")
    date2 = time.strftime("%B %Y")
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    copy_current_version(version, date1, date2, timestamp)
    create_version_index_file(version)
    create_main_index_file(version)
