#! /usr/bin/env python

from larning.ci import ci_manager, rmdirs, mkdirs
from os import getcwd
from os.path import join
from larning import __name__ as PROJ_NAME

with ci_manager() as (iF, tF, pF, sF):
    WD = getcwd()
    BUILD, EGG, DIST, DOCS, PYTEST = (
        join(WD, "build"),
        join(WD, PROJ_NAME + ".egg-info"),
        join(WD, "dist"),
        join(WD, "docs"),
        join(WD, ".pytest_cache"),
    )
    _BUILD = join(DOCS, "_build")
    tF.delete_temp_dirs = [rmdirs, [BUILD, EGG, DIST, _BUILD, PYTEST]]
    tF.create_docs_dir = [mkdirs, [DOCS]]
    pF.install_make = [DOCS, "sudo", "apt", "install", "make"]
    pF.init_docs = [DOCS, "sphinx-quickstart"]
    pF.apidoc = [WD, "sphinx-apidoc", "-f", "-e", "-M", "-o", "./docs", f"./{PROJ_NAME}"]
    pF.latexpdf = [WD, "sphinx-build", "-M", "latexpdf", "./docs", f"./docs/_build"]
    pF.html = [WD, "sphinx-build", "-M", "html", "./docs", f"./docs/_build"]

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

    sF.init_docs = [tF.create_docs_dir, pF.init_docs, pF.install_make]
    sF.setup = [pF.setup]

    sF.a = [
        pF.pytest,
        pF.black,
        tF.delete_temp_dirs,
        pF.apidoc,
        # pF.latexpdf,
        pF.html,
        pF.git_status,
        pF.git_add_all,
        pF.git_commit,
        pF.git_push,
        pF.sdist,
        pF.twine_check,
        pF.twine_upload,
    ]
