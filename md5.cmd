title md5 - by miles
set local enable delayed expansion
%~d0
cd %~dp0
if exist tmp.txt del tmp.txt
for /R %%s in (.,*) do (
echo %%s
) >>tmp.txt

if exist md5.txt del md5.txt
for /f "skip=1" %%a in (tmp.txt) do (
certutil -hashfile %%a MD5
)>>md5.txt

if exist tmp.txt del tmp.txt
echo all md5 is ok 
pause