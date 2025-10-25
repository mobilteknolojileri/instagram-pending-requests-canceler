@echo off
echo Starting Chrome in debug mode for Instagram automation...
echo.
echo IMPORTANT: Replace YOUR_USER_AGENT_HERE with your actual user agent
echo Get your user agent from: https://iplogger.org/useragents/
echo.

start chrome.exe ^
--remote-debugging-port=9222 ^
--user-data-dir="C:\chrome_debug\instagram" ^
--remote-allow-origins=http://localhost:9222 ^
--user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36" ^
--start-maximized ^
https://www.instagram.com/

echo.
echo Chrome started! Login to Instagram in the opened window.
echo Keep this window open while running the script.
pause