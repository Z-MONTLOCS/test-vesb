#!/bin/bash

echo "...Installing packages..."

#pip install -r requirements.txt

set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate

echo "...Build Script Completed!"

STORAGE_DIR=/opt/render/project/.render

echo "...Downloading Chrome"
mkdir -p $STORAGE_DIR/chrome
cd $STORAGE_DIR/chrome
wget -P ./ https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
dpkg -x ./google-chrome-stable_current_amd64.deb $STORAGE_DIR/chrome
rm ./google-chrome-stable_current_amd64.deb
cd $HOME/project/src # Make sure we return to where we were

# Get path to Chrome executable
CHROME_EXECUTABLE_PATH="/opt/render/project/.render/chrome/opt/google/chrome/google-chrome"
echo "Chrome executable path: $CHROME_EXECUTABLE_PATH"

# be sure to add Chrome's location to the PATH as part of your Start Command
export PATH="${PATH}:/opt/render/project/.render/chrome/opt/google/chrome"

# add your own build commands...
