# Package Manager Simulator 
## Overview

This is a simple package manager simulator written in Python. It allows you to install, uninstall, and list packages based on a given repository database and an installed packages database.

## Requirements

- Python 3.x
- `repo.db` and `pkgs.db` files must exist in the same directory as the script.

## Files

- `pkg.py`: The main Python script that contains the logic for the package manager simulator.
- `repo.db`: A file that contains the package dependencies. Each line should represent a package and its dependencies separated by a colon.
- `pkgs.db`: A file that contains the list of installed packages. This file will be modified by the `pkg.py` script as packages are installed or uninstalled.

## Usage

The package manager simulator provides the following commands:

### Install a package

This will install the package and all its dependencies.
```bash
python pkg.py install <PACKAGE_NAME>
```

### Uninstall a package
This will uninstall the package and any other packages that depend on it.
```bash
python pkg.py uninstall <PACKAGE_NAME>
```

### List installed packages
This will list all currently installed packages
```bash
python pkg.py list
```
