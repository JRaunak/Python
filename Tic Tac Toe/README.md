# Additional Modules
- >  ***pygame***
    - A graphics module for python
    - To download using command line, type "pip install pygame" in cmd without braces
    - The PyPI page for the module is [pygame.PyPI](https://pypi.org/project/pygame/)

- >  ***PyInstaller*** (optional)
    - A module to compile python scripts into standalone binaries/executables(.exe)
    - To use it, type "pyinstaller \<flags> \<filename>" in cmd in your python script directory
    - Flags are optional to use
    - Here are some basic Flags:
        - -w : To turn off the terminal while running the script
        - --onefile : To compile the whole script and dependent scripts in a single binary file
        - --icon <icon.ico> : To add an icon to the compiled binary
    - To download it using command line, type "pip install PyInstaller"
    - The PyPI page for the module is [pyinstaller.PyPI](https://pypi.org/project/PyInstaller/)
    - More Documentation can be found on [pyinstaller.docs](https://pyinstaller.readthedocs.io/en/stable/index.html)

# Structure of Code
- The directory has 1 python script containing the entire code.
- There is also an exe file with same name as the python script.
- A Dependency named 'Winnings.dat' consists of some serialized data for the script

# About
- Running the .exe file doesn't require any download or even python installed.<br>It is a standalone program. The Winnings.dat file is essential
- The .exe file is for those who just want to play the game.
- Those who want to check the source code, or make changes in it shall use the python script.
- To run the python script, all the non-optional modules/libraries are required.
- The PyInstaller module is required only for those who want <br> to rebuild their own script into an executable.

# Misc
- This is a basic game made using python's pygame module & compiled using PyInstaller
- For information on pygame, refer to [Pygame Docs](https://www.pygame.org/docs/)
- For additional information on PyInstaller, refer to [PyInstaller Docs](https://pyinstaller.readthedocs.io/en/stable/)
