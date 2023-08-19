#!/bin/bash

echo "...Installing packages..."

set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate

echo "...Build Script Completed!"

STORAGE_DIR=/opt/render/project/.render

if [[ ! -d $STORAGE_DIR/chrome ]]; then
  echo "...Downloading Chrome"
  mkdir -p $STORAGE_DIR/chrome
  cd $STORAGE_DIR/chrome
  wget -P ./ https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
  dpkg -x ./google-chrome-stable_current_amd64.deb $STORAGE_DIR/chrome
  rm ./google-chrome-stable_current_amd64.deb
  cd $HOME/project/src # Make sure we return to where we were
else
  echo "...Using Chrome from cache"
fi

# Get Chrome version
CHROME_VERSION=$(google-chrome --version 2>/dev/null | awk '{print $3}')
echo "Installed Chrome version: $CHROME_VERSION"

# Reinstall Chrome
echo "Reinstalling Chrome..."
cd $STORAGE_DIR/chrome
rm -r opt # Remove existing installation
dpkg -x ./google-chrome-stable_current_amd64.deb $STORAGE_DIR/chrome
echo "Chrome has been reinstalled."

# Get path to Chrome executable
CHROME_EXECUTABLE_PATH="/opt/render/project/.render/chrome/opt/google/chrome/google-chrome"
echo "Chrome executable path: $CHROME_EXECUTABLE_PATH"

# Update PATH to include Chrome's location
export PATH="${PATH}:/opt/render/project/.render/chrome/opt/google/chrome"

# add your own build commands...
