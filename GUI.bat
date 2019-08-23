@echo off & mode 80,25 & color 07 & setlocal EnableDelayedExpansion

if exist "input.ini" (
	set line=1
	for /f "tokens=1*" %%i in (input.ini) do (
		if "!line!" equ "1" if not "%%i" equ "" set "url=%%i"
		if "!line!" equ "2" if not "%%i" equ "" set "threads=%%i"
		if "!line!" equ "3" if not "%%i" equ "" set "field1=%%i"
		if "!line!" equ "4" if not "%%i" equ "" set "field2=%%i"
		if "!line!" equ "5" if not "%%i" equ "" set "field3=%%i"
		if "!line!" equ "6" if not "%%i" equ "" set "field4=%%i"
		if "!line!" equ "7" if not "%%i" equ "" set "field5=%%i"
		set /a line+=1
	)
	del /f /q "input.ini" >nul
)

(
	postloris.py %url% %threads% %field1% %field2% %field3% %field4% %field5%
) || (
	python3 postloris.py %url% %threads% %field1% %field2% %field3% %field4% %field5%
) || (
	python postloris.py %url% %threads% %field1% %field2% %field3% %field4% %field5%
) || (
	py postloris.py %url% %threads% %field1% %field2% %field3% %field4% %field5%
)
