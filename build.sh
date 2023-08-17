#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate


CHROME_PATH=/opt/render/project/bin/chrome/opt/google/chrome/

if [[ ! -d $CHROME_PATH ]]; then

    echo "...Downloading Chrome Binary..."
    #wget <uri> -P /path/to/folder
    wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb -P /tmp

    echo "...Installing Chrome Binary..."
    mkdir -p /opt/render/project/bin/chrome
    dpkg -x /tmp/google-chrome-stable_current_amd64.deb /opt/render/project/bin/chrome
    # this is a directory with its own "etc", "opt", and "usr" subdir

    echo "...Cleaning Up..."
    rm /tmp/google-chrome-stable_current_amd64.deb

    echo "...Adding to Path..."
    #export PATH="${PATH}:${CHROME_PATH}/opt/google/chrome/"
    export PATH="${PATH}:/opt/render/project/bin/chrome/opt/google/chrome"

else
  echo "...Detected Existing Chrome Binary"
fi


#CHROMEDRIVER_PATH=/usr/local/bin/chromedriver
CHROMEDRIVER_PATH=/opt/render/project/bin/chromedriver

if [[ ! -d $CHROMEDRIVER_PATH ]]; then

    echo "...Downloading Chromedriver..."
    wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip

    echo "...Installing Chromedriver..."
    unzip /tmp/chromedriver.zip chromedriver -d /opt/render/project/bin

    echo "...Cleaning Up..."
    rm /tmp/chromedriver.zip

    echo "...Adding to Path..."
    export PATH="${PATH}:${CHROMEDRIVER_PATH}"
    echo $PATH
else
  echo "...Detected Existing Chromedriver Installation"
fi

echo "...Installing packages..."
#pip install -r requirements.txt

echo "...Build Script Completed!"