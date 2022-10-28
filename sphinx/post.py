import os

# We don't want to document undocumented members in python source code.
# There are three ways to achieve this:
#  1. Remove "undoc-members" from *.rst files
#  2. Use "no-undoc-members" instead of "undoc-members" in *.rst files
#  3. Set option in conf.py: autodoc_default_options = {'undoc-members': None|True|False}
#
# Method 3 doesn't work for me. I tried value None, True, False, none of them works.
# The created *.rst files always contain "undoc-members".
# This script replaces "undoc-members" with "no-undoc-members" in *.rst files.

# Loop through each file in _srcdoc, replace "undoc-members" with "no-undoc-members".
for root, dirs, files in os.walk(os.path.abspath("./_srcdoc")):
    for file in files:
        # argument of open should be absolute path of file
        with open(os.path.join(root, file), 'r') as fid:
            txt = fid.read()

        newtxt = txt.replace("undoc-members", "no-undoc-members")
        with open(os.path.join(root, file), 'w') as fid:
            fid.write(newtxt)


