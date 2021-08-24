from hypno import inject_py
import sys
import shutil
from pathlib import Path
class Injector:
    def __init__(self,pid,code_path):
        self.pid=pid
        self.code=code_path
    def __pre_run(self):
        pass
    def __check_env(self):
        pass
    def do_inject(self):
        inject_code="""import sys;sys.path.insert(0,"%s");code=open('%s').read();exec(code);"""
        inject_dir="/tmp/pyinpy"
        inject_dir=Path(inject_dir)
        inject_dir.mkdir(parents=True, exist_ok=True)
        shutil.copy(self.code,inject_dir)
        inject_code=inject_code%(inject_dir,inject_dir/self.code)
        print(inject_code)
        inject_py(int(self.pid),inject_code)