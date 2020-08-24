from collections.abc import Callable
from pydantic import validate_arguments
from typing import Iterable
from os import system
from larning.strings_i import concatenate_with_separation
from subprocess import check_output,STDOUT,run,CompletedProcess
from os import environ
from larning.property import with_property

@with_property("exit_code","stdout","stderr")
class Bash(Callable):
    @validate_arguments
    def __init__(self, *args: str,shell=False,env=None):
        self._env,self._shell=env,shell
        self._args= concatenate_with_separation(args, " ") if shell else [environ[arg[1:]] if arg[0] == "$" else arg for arg in args]

    def __str__(self):
        return self._args if self._shell else concatenate_with_separation(self._args, " ")

    def __call__(self):
        p :CompletedProcess= run(self._args,capture_output=True,env=self._env,shell=self._shell)
        self.stdout,self.stderr,self.exit_code=p.stdout.decode("ascii"),p.stderr.decode("ascii"),p.returncode
        p.check_returncode()
        return self




