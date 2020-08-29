#! /usr/bin/env python

from larning.ci import ci_manager, rmdirs
from os import getcwd
from os.path import join
from larning import __name__ as larning_name

print(larning_name)
with ci_manager() as (iF, tF, pF, sF):
    original_wd = getcwd()
    build_d, egg_d, dist_d = (
        join(original_wd, "build"),
        join(original_wd, larning_name + ".egg-info"),
        join(original_wd, "dist"),
    )
    print(build_d, egg_d, dist_d)
    tF.delete_dirs = [rmdirs, [build_d, egg_d, dist_d]]
    pF.black = [original_wd, "black", "."]
    pF.git_status = [original_wd, "git", "status"]
    pF.git_add_all = [original_wd, "git", "add", "."]
    pF.git_commit = [original_wd, "git", "commit", "-m", iF.commit_message]
    pF.git_push = [original_wd, "git", "push"]
    pF.pytest = [original_wd, "pytest", "-s"]
    pF.install = [original_wd, "./setup.py", "install"]
    pF.sdist = [original_wd, "./setup.py", "sdist", "bdist_wheel"]
    pF.twine_check = [original_wd, "twine", "check", "dist/*"]
    pF.twine_test = [
        original_wd,
        "twine",
        "upload",
        "-u",
        "tasigabi97",
        "-p",
        iF.pipy_password,
        "--repository-url",
        "https://test.pypi.org/legacy/",
        "dist/*",
    ]
    pF.twine_upload = [
        original_wd,
        "twine",
        "upload",
        "-u",
        "tasigabi97",
        "-p",
        iF.pipy_password,
        "dist/*",
    ]

    sF.a = [
        pF.twine_test,
        tF.delete_dirs,
        pF.install,
        pF.black,
        pF.pytest,
        pF.git_status,
        pF.git_add_all,
        pF.git_commit,
        pF.git_push,
        pF.sdist,
        pF.twine_check,
        pF.twine_test,
        pF.twine_upload,
    ]
