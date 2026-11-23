#!/bin/bash
# macOS: starts Google Chrome in debug mode for Instagram automation.
# Run with: bash launch_chrome.sh

if [ ! -d "/Applications/Google Chrome.app" ]; then
  echo "Google Chrome was not found in /Applications. Install Chrome and try again."
  exit 1
fi

echo "Starting Chrome in debug mode for Instagram automation..."

open -na "Google Chrome" --args \
  --remote-debugging-port=9222 \
  --user-data-dir="$HOME/chrome_debug/instagram" \
  --remote-allow-origins=http://localhost:9222 \
  --no-first-run \
  --no-default-browser-check \
  https://www.instagram.com/

echo
echo "Chrome started! Login to Instagram in the opened window."
echo "Keep that window open while running the script."
