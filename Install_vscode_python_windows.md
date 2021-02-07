# Install Visual Studion Code and Python in Windows:
# 1. Install Visual studio code:
From the link, install visual studio code for windows <br>
[https://code.visualstudio.com/download](https://code.visualstudio.com/download)
# 2. Install python:
Open the command line by typing `cmd` in the search of start menu <br>
Type `python3` and hit Enter, download python on you device from windows store.
# 4. Install python extension for vscode:
Open visual studio code by typing `vscode` in the search of start menu <br>
Inside it open the command par by using `Ctrl+Shift+p` then type `install extension`<br>
Install python extension
# 5. Install Microsoft visual C++ built tools:
Download Microsoft C++ buil tools from the link <br> 
[https://visualstudio.microsoft.com/visual-cpp-build-tools/](https://visualstudio.microsoft.com/visual-cpp-build-tools/)<br>
Install C++ build tools (requires 7GB of space)
# 6. Install Biopython:
In visual studio code open a terminal <br>
`Ctrl+Shift+p` then type `Create terminal`<br>
Run the following commands:
```shell
pip install --upgrade setuptools
pip install pylint
pip install biopython
```
# 7. Test the installation:
Create a folder with a name `bio`<br>
Open vscode create a file <br>
`Ctrl+Shift+p` then type `new file`<br>
name the file with `.py` extension e.g. `test.py`
and type the following:
```python
from Bio.Seq import Seq

seq=Seq('TCGA')
print(seq)
```
Run the script either by using run command in vscode (in the-upper right corner)
or by typing 'python test.py' in the terminal
