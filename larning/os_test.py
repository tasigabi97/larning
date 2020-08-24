from larning.os import Bash
from larning.testing import name
from os import environ
from pytest import raises
from subprocess import CalledProcessError

@name(Bash.__init__, 1, globals())
def _():
    assert Bash("echo", 1)._args == ["echo","1"]
    assert Bash("$PATH")._args[0][0] =="/"
    assert Bash("echo", 1,shell=True)._args == "echo 1"
    assert Bash("$PATH",shell=True)._args =="$PATH"





@name(Bash.__str__, 1, globals())
def _():
    assert str(Bash("echo",1)) == "echo 1"
    assert str(Bash("echo",1,shell=True)) == "echo 1"
    #todo


@name(Bash.__call__, 1, globals())
def _():

    assert Bash("echo",1)().stdout == "1\n"
    assert Bash("echo",1)().stderr == ""
    assert Bash("echo",1)().exit_code == 0
    assert Bash("echo",1,shell=True)().stdout == "1\n"
    assert Bash("echo",1,shell=True)().stderr == ""
    assert Bash("echo",1,shell=True)().exit_code == 0
    with raises(FileNotFoundError):
        Bash("ech")()
    with raises(FileNotFoundError):
        Bash("set")()
    with raises(CalledProcessError):
        Bash("ech",shell=True)()
    assert Bash("set",shell=True)().exit_code == 0

