# Design Documentation

## Python 3.7 or higher is required

## Create Python virtual environment and install packages
**1. Create virtual environment**
```bash
cd \<project\>
python -m venv ENV
```

**2. Start virtual environment**

For Windows:
```
ENV\Scripts\activate.bat
```
For MacOS and Linux:
```
source ENV/bin/activate
```

**3. Install packages**
```bash
# Update pip
python -m pip install -U pip
python -m pip install -r requirements.txt
```

## Create Sphinx Documentation

Follow [Sphinx README](sphinx/README.md).
