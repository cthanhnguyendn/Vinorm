# Build script for Vinorm on Windows
Write-Host "Building Vinorm for Windows..." -ForegroundColor Green

# Check if g++ is available
try {
    $null = Get-Command g++ -ErrorAction Stop
    Write-Host "✓ g++ compiler found" -ForegroundColor Green
} catch {
    Write-Host "✗ g++ compiler not found" -ForegroundColor Red
    Write-Host "Please install MinGW-w64 or MSYS2 from: https://www.mingw-w64.org/downloads/" -ForegroundColor Yellow
    Read-Host "Press Enter to exit"
    exit 1
}

# Set up paths
$CPP_SRC = "cpp_src\src"
$INCLUDE_DIR = "cpp_src\include"
$LIB_DIR = "cpp_src\lib"

# Check if ICU libraries exist for Windows
if (-not (Test-Path "$LIB_DIR\icudt64.dll")) {
    Write-Host "Warning: Windows ICU libraries not found." -ForegroundColor Yellow
    Write-Host "You need to download ICU for Windows from: https://icu.unicode.org/download" -ForegroundColor Yellow
    Write-Host "For now, we'll try to build without ICU (may not work properly)." -ForegroundColor Yellow
    Write-Host ""
}

# Build the main executable
Write-Host "Compiling main.cpp..." -ForegroundColor Cyan

$compileArgs = @(
    "-std=c++11",
    "-o", "vinorm\main.exe",
    "$CPP_SRC\main.cpp",
    "$CPP_SRC\ICUReadFile.cpp",
    "$CPP_SRC\ICUMapping.cpp", 
    "$CPP_SRC\ICUNumberConverting.cpp",
    "$CPP_SRC\ICUDictionary.cpp",
    "$CPP_SRC\SpecialCase.cpp",
    "$CPP_SRC\Address.cpp",
    "$CPP_SRC\Math.cpp",
    "$CPP_SRC\DateTime.cpp",
    "-I$INCLUDE_DIR",
    "-L$LIB_DIR",
    "-licudata", "-licui18n", "-licuio", "-licuuc",
    "-static-libgcc", "-static-libstdc++"
)

try {
    & g++ @compileArgs
    if ($LASTEXITCODE -eq 0) {
        Write-Host "✓ Build successful! Created vinorm\main.exe" -ForegroundColor Green
    } else {
        throw "Build failed"
    }
} catch {
    Write-Host "Build failed. Trying without ICU libraries..." -ForegroundColor Yellow
    
    # Try building without ICU
    $compileArgsNoICU = @(
        "-std=c++11",
        "-o", "vinorm\main.exe",
        "$CPP_SRC\main.cpp",
        "$CPP_SRC\ICUReadFile.cpp",
        "$CPP_SRC\ICUMapping.cpp",
        "$CPP_SRC\ICUNumberConverting.cpp",
        "$CPP_SRC\ICUDictionary.cpp",
        "$CPP_SRC\SpecialCase.cpp",
        "$CPP_SRC\Address.cpp",
        "$CPP_SRC\Math.cpp",
        "$CPP_SRC\DateTime.cpp",
        "-I$INCLUDE_DIR",
        "-DNO_ICU",
        "-static-libgcc", "-static-libstdc++"
    )
    
    try {
        & g++ @compileArgsNoICU
        if ($LASTEXITCODE -eq 0) {
            Write-Host "✓ Build successful (without ICU)! Created vinorm\main.exe" -ForegroundColor Green
        } else {
            throw "Build failed completely"
        }
    } catch {
        Write-Host "✗ Build failed completely." -ForegroundColor Red
        Read-Host "Press Enter to exit"
        exit 1
    }
}

Write-Host ""
Write-Host "Build completed! You can now run the Python tests." -ForegroundColor Green
Read-Host "Press Enter to continue" 