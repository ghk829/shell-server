import subprocess

def run_shell(command,timeout=None,stdin=None,stdout=subprocess.PIPE,stderr=subprocess.PIPE,env=None,shell=False):
    import shlex
    import os
    stdin_w = None


    from threading import Timer
    if shell:
        if type(command) == list:
            raise Exception("please put the command as string")
        if command.endswith(";"):
            command+="pwd"
        else:
            command+=";pwd"
    else:
        if type(command) == str:
            command = shlex.split(command)
    if stdin is not None:
        stdin_w = subprocess.PIPE

    with subprocess.Popen(command,stdin=stdin_w,stdout=stdout,stderr=stderr,env=env,shell=shell) as proc:
        timer = Timer(timeout, proc.kill)
        try:
            if stdin is not None:
                if type(stdin) == str:
                    import sys
                    stdin = stdin.encode(encoding=sys.getdefaultencoding())

                proc.stdin.write(stdin)
            timer.start()
            # print PROCESS ID
            print(proc.pid)
            stdout, stderr = proc.communicate()
            if shell:
                pwd = stdout.decode().split("\n")[-2]
                stdout = "\n".join(stdout.decode().split("\n")[:-2]).encode()
                print(pwd)
                os.chdir(pwd)
            # tuple result stdout:bytes stderr:bytes return
            return stdout,stderr
        finally:
            timer.cancel()
