@echo off

title beluga v0.2

echo hello user welcome to beluga os

pause

echo opening beluga...

echo welcome to beluga os v0.2

pause
:MainMenu
echo clock
echo ldate
echo open FH
echo logout
echo clear
echo upcoming
set /p choice= "Please Select one of the above options:" 

if %choice%== clock goto :clock
if %choice%== date  goto :date
if %choice%== FH  goto :FH
if %choice%== logout  exit
if %choice%== clear goto :clear
if %choice%== upcoming goto :upcoming

:clock
echo loading clock
echo %TIME%
pause
echo exiting clock
goto :MainMenu

:date
echo loading date
date /t
pause
echo exiting date
goto :MainMenu

:upcoming
echo hello we are proud to announce that beluga will soon be moving to an new language
echo we expect it to be aviaible within a month from 5/3/2021 now we shall return you to your main area
pause
goto :MainMenu

:clear
cls
goto :MainMenu

:FH
echo welcome to file hunter

title file hunter 0.1

:menu
echo 1:locate
echo 2:exit
set /p choice= "please pick an option stated above:"
if %choice%== locate goto :exp
if %choice%== exit goto :MainMenu

:exp
set /p dir= "please enter the file name that you wish to go to:"
start %dir%
goto :menu
