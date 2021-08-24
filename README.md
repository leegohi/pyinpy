# pyinpy

A tool/library allowing to inject python code into a running python process.
Based on [kmaork/hypno](https://github.com/kmaork/hypno)

hypno encode the injected python code with base64, put it on the name of the so or dll, and implement the void init(void) __attribute__((constructor)) function in the so or dll. When dlopen loads the library file, it will default execute the init function, hypno obtains the loaded library file name and decode it to py_code in the init function and then executes PyRun_SimpleString(py_code);

However, the file name is limited, so the length of the injected python code is also limited. pyinpy eliminates this limitation by referring to the  pyrasite code
### Installation
```shell script
git clone https://github.com/leegohi/pyinpy
cd pyinpy && python setup.py install
```
Both source distributions and `manylinux1` wheels are upoloaded to pypi for every release.

### Usage
#### CLI
```shell script
pyinpy <pid>  <python_code_path>
```

#### API
```python
from pyinpy import Injector

Injector(pid, python_code).do_inject()
```
