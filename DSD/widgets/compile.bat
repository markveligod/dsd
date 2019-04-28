set UIFILE=%1
set UIDIR=%~dp1
set FILENAME=%~n1
set PSDNAME=%UIDIR%%FILENAME%_uis.py
CALL C:\Users\markveligod\AppData\Local\Programs\Python\Python37\Scripts\pyside2-uic.exe %UIFILE% -o %PSDNAME%
