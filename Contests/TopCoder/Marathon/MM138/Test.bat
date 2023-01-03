@echo off
@REM setlocal enabledelayedexpansion
@REM date /t time /t > log.txt
@REM time /t >> log.txt
echo Current time: %date% %time% > log.txt
echo ----------------------------- >> log.txt

for /l %%n in (6,1,30) do (
    for /l %%v in (3,1,9) do (
@REM set sum=0
@REM for /l %%n in (6,1,10) do (
@REM     for /l %%v in (3,1,3) do (
        @REM echo N: %%n >> log.txt
        @REM echo V: %%v >> log.txt
        @REM java -jar tester.jar -exec "python DiceRollerV0.py" -seed 1 -novis -N %%n -V %%v >> log.txt
        echo N: %%n V: %%v >> log.txt
        java -jar tester.jar -exec "python DiceRollerV2.py" -seed 1 -novis -N %%n -V %%v >> log.txt
        @REM for /f %%s in ( 'java -jar tester.jar -exec "python DiceRollerV0.py" -seed 1 -novis -N %%n -V %%v' ) do set a = %%s
        @REM echo a %%a >> log.txt
        @REM java -jar tester.jar -exec "python DiceRollerV0.py" -seed 1 -novis -N %%n -V %%v > tmp.txt
        @REM set %res%=<tmp.txt
        @REM for /f "tokens=* delims= " %%i in ( 'java -jar tester.jar -exec "python DiceRollerV0.py" -seed 1 -novis -N %%n -V %%v' ) do (
        @REM     set a=%%i
        @REM     echo %a%>>log.txt
        @REM     set score=%a:~8,-2%
        @REM     @REM set /a sum=%sum%+%score%
        @REM     echo %score%>>log.txt
        @REM )
    )
)
@REM echo %sum%>>log.txt

