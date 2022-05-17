@echo off

cd C:\Users\Hewlett Packard\Desktop\batch filse

title beluga v0.3

echo hello user welcome to beluga os



pause



:start
echo welcome to beluga os v0.3

pause
:MainMenu
title beluga os v0.3
echo clock
echo ldate
echo open File hunter (FH)
echo open Web Scraper (WS)
echo logout
echo clear
echo upcoming
set /p choice= "Please Select one of the above options:" 

if %choice%== clock goto :clock
if %choice%== date  goto :date
if %choice%== FH  goto :FH
if %choice%== WS goto :S
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

title file hunter 0.3

:menu
echo 1:locate
echo 2:exit
set /p choice= "please pick an option stated above:"
if %choice%== locate goto :exp
if %choice%== exit goto :MainMenu

:exp
set /p dir= "please enter the file name that you wish to go to:"
if exist %dir% goto :open;
else goto :error;

:open
start %dir%
set dir= ""
goto :menu

:error
echo i am sorry but you have entered the file name or extension incorrectly please re enter the file name and extension
goto :exp

:S
title Web Scraper 0.1
echo 1:search
echo 2:exit
set /p choice= "please pick an option stated above:"
if %choice%== search goto:search
if %choice%== exit goto :MainMenu
:search
set /p page= "enter your prefered web browser"
set /p look= "please enter the website that you wish to find"
set /p aorb= "would you like to do a advanced search or basic search (a/b)"
if %aorb%== a goto:advanced
if %aorb%== b goto:basic

:advanced
set /p dom= "enter your domain extension here (example .com .net)"
start %page% %look%%dom%
goto :S

:basic
start %page% %look%.com
goto :S

:veri
start codegen.bat
exit
