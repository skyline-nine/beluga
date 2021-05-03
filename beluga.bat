@echo off

set /A clock=0
set /A date=0
set /A logout=0

 
title beluga v0.1

echo hello user welcome to beluga os



pause

echo opening beluga...

echo welcome to beluga os v0.1

pause
:MainMenu
echo 1:clock
echo 2:date
echo 3:logout
echo please enter the number behind the program that you wish to use
set /p choice= "Please Select one of the above options :" 

if %choice%==1 set /A clock+=1
if %choice%==2 set /A date+=1
if %choice%==3 set /A logout+=1

if %clock%==1 goto :clock
if %date%==1 goto :date
if %logout% = 0 goto :logout

:clock
echo loading clock
echo %TIME%
pause
set /A clock = 0
echo exiting clock
goto :MainMenu
:date
echo loading date
date /t
pause
set /A date = 0 
echo exiting date
goto :MainMenu

:logout
set /p choice= "are you sure"


if %choice%=="yes" goto :end
if %choice%=="no" goto :MainMenu

:end
pause
exit