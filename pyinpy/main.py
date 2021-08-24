import os
import subprocess
from pyinpy.inject import Injector
from argparse import Namespace, ArgumentParser
from typing import Optional, List

def ptrace_check():
    ptrace_scope = '/proc/sys/kernel/yama/ptrace_scope'
    if os.path.exists(ptrace_scope):
        f = open(ptrace_scope)
        value = int(f.read().strip())
        f.close()
        if value == 1:
            print("WARNING: ptrace is disabled. Injection will not work.")
            print("You can enable it by running the following:")
            print("echo 0 | sudo tee /proc/sys/kernel/yama/ptrace_scope")
            print("")
    else:
        getsebool = '/usr/sbin/getsebool'
        if os.path.exists(getsebool):
            p = subprocess.Popen([getsebool, 'deny_ptrace'],
                    stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out, err = p.communicate()
            if str(out) == 'deny_ptrace --> on\n':
                print("WARNING: ptrace is disabled. Injection will not work.")
                print("You can enable it by running the following:")
                print("sudo setsebool -P deny_ptrace=off")
                print("")

def parse_args(args: Optional[List[str]]) -> Namespace:
    parser = ArgumentParser(description='Inject python code into a running python process.')
    parser.add_argument('pid', type=int, help='pid of the process to inject code into')
    parser.add_argument('python_code', type=str.encode, help='python code path to inject e.g.:/tmp/dump_memeory')
    return parser.parse_args(args)


def main(args: Optional[List[str]] = None) -> None:
    ptrace_check()
    parsed_args = parse_args(args)
    injector=Injector(parsed_args.pid,parsed_args.python_code)
    injector.do_inject()
if __name__ == "__main__":
    main()