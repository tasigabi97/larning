#! /usr/bin/env python

from larning.ci import ci_manager, rmdirs, mkdirs
from os import getcwd
from os.path import join
from larning import __name__ as project_name

with ci_manager() as (iF, tF, pF, sF):
    WD = getcwd()
    BUILD, EGG, DIST, DOCS = (
        join(WD, "build"),
        join(WD, project_name + ".egg-info"),
        join(WD, "dist"),
        join(WD, "docs"),
    )
    tF.delete_temp_dirs = [rmdirs, [BUILD, EGG, DIST]]
    tF.create_docs_dir = [mkdirs, [DOCS]]
    pF.init_docs = [DOCS, "sphinx-quickstart"]
    pF.black = [WD, "black", ".", "-t", "py38", "-l", "160"]
    pF.git_status = [WD, "git", "status"]
    pF.git_add_all = [WD, "git", "add", "."]
    pF.git_commit = [WD, "git", "commit", "-m", iF.commit_message]
    pF.git_push = [WD, "git", "push"]
    pF.pytest = [WD, "pytest", "-s"]
    pF.setup = [WD, "./setup.py", "install"]
    pF.sdist = [WD, "./setup.py", "sdist", "bdist_wheel"]
    pF.twine_check = [WD, "twine", "check", "dist/*"]
    pF.twine_upload = [
        WD,
        "twine",
        "upload",
        "-u",
        "tasigabi97",
        "-p",
        iF.pipy_password,
        "dist/*",
    ]

    sF.init_docs = [tF.create_docs_dir, pF.init_docs]
    sF.setup = [pF.setup]

    sF.a = [
        pF.black,
        pF.pytest,
        tF.delete_temp_dirs,
        pF.git_status,
        pF.git_add_all,
        pF.git_commit,
        pF.git_push,
        pF.sdist,
        pF.twine_check,
        pF.twine_upload,
    ]
