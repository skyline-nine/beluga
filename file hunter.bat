@echo off

echo welcome to file hunter

:menu
echo 1:locate file
echo 2:exit
set /p choice="please pick an option stated above:"
if choice==1 goto :exp
if choice==2 goto :exit

:exp
set /p dir= "please enter the file url that you wish to go to:"
start cmd "%dir%"
goto :load

:load

goto :menu

:exit
set /p ays= "are you sure you want to exit:"
if ays="yes" goto :hic
if ays="no" goto :menu

:hic
set /p ays= "would you like to go back to home or exit the entire program(home/quit):"
if ays="home" start "beluga.bat"
if ays="quit" exit