@ECHO OFF

REM if _srcdoc exists, delete it
if exist _srcdoc rmdir _srcdoc /s /q

sphinx-apidoc -o ./_srcdoc ../..

python post.py