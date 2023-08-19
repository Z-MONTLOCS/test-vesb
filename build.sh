#!/bin/bash

echo "...Installing packages..."

#pip install -r requirements.txt

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

# be sure to add Chrome's location to the PATH as part of your Start Command
export PATH="${PATH}:/opt/render/project/.render/chrome/opt/google/chrome"

# add your own build commands...

# Uninstall any existing Chrome
echo "...Uninstalling Chrome (if exists)"
sudo apt-get remove google-chrome-stable

# Install the downloaded Chrome package
echo "...Installing Chrome"
sudo dpkg -i $STORAGE_DIR/chrome/opt/google/chrome/google-chrome-stable_current_amd64.deb

echo "...Chrome Installation Completed"
