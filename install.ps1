# Install codex-chats on Windows
$ErrorActionPreference = "Stop"

$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$TargetDir = "$env:USERPROFILE\bin"

New-Item -ItemType Directory -Force -Path $TargetDir | Out-Null

Copy-Item -Force "$ScriptDir\codex-chats" "$TargetDir\codex-chats"
Copy-Item -Force "$ScriptDir\codex-chats.bat" "$TargetDir\codex-chats.bat"

$UserPath = [Environment]::GetEnvironmentVariable("Path", "User")
if (-not $UserPath) { $UserPath = "" }

if ($UserPath -notlike "*${TargetDir}*") {
    $NewPath = if ($UserPath) { "$UserPath;$TargetDir" } else { $TargetDir }
    [Environment]::SetEnvironmentVariable("Path", $NewPath, "User")
    Write-Host "Added $TargetDir to your user PATH. Restart your terminal." -ForegroundColor Yellow
}

Write-Host "Installed to: $TargetDir\codex-chats.bat" -ForegroundColor Green
