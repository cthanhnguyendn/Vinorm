@echo off
cd /d %~dp0cpp_src\src
call build_main.bat
if exist main.exe (
    copy /Y main.exe ..\..\vinorm\main.exe
    echo main.exe copied to vinorm\main.exe
) else (
    echo main.exe not found. Build may have failed.
) 