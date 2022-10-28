#/bin/sh

rm -rf _srcdoc
sphinx-apidoc -o ./_srcdoc ../..
python post.py