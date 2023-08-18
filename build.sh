#!/bin/bash

CHROME_PATH="/opt/render/project/bin/chrome/opt/google/chrome"
CHROMEDRIVER_PATH="/opt/render/project/bin"

# Desinstalar Chromedriver si existe
if [[ -d $CHROMEDRIVER_PATH ]]; then
    echo "...Uninstalling Existing Chromedriver..."
    rm -rf $CHROMEDRIVER_PATH
fi

if [[ ! -d $CHROME_PATH ]]; then
    echo "...Downloading Chrome Binary..."
    wget -O /tmp/google-chrome.deb https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb

    echo "...Installing Chrome Binary..."
    mkdir -p /opt/render/project/bin/chrome
    dpkg -x /tmp/google-chrome.deb /opt/render/project/bin/chrome

    echo "...Cleaning Up..."
    rm /tmp/google-chrome.deb

    echo "...Adding Chrome to Path..."
    export PATH="${PATH}:${CHROME_PATH}"
    echo "Installed Chrome Version:"
    google-chrome --version
else
    echo "...Detected Existing Chrome Binary"
fi

# Obtener la versión de Chrome
CHROME_VERSION=$(google-chrome --version | awk '{print $3}' | cut -d'.' -f1-3)

# Construir la URL de la versión de ChromeDriver
CHROMEDRIVER_URL="https://chromedriver.storage.googleapis.com/LATEST_RELEASE_$CHROME_VERSION"

# Obtener la versión de ChromeDriver a partir de la URL
CHROMEDRIVER_VERSION=$(curl -sS $CHROMEDRIVER_URL)

echo "...Fetching Chromedriver Version..."
echo "Latest Chromedriver Version: $CHROMEDRIVER_VERSION"

# Construir la URL de descarga de ChromeDriver
CHROMEDRIVER_DOWNLOAD_URL="https://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip"

echo "...Downloading Chromedriver..."
wget -O /tmp/chromedriver.zip $CHROMEDRIVER_DOWNLOAD_URL

echo "...Installing Chromedriver..."
unzip /tmp/chromedriver.zip -d /opt/render/project/bin

echo "...Cleaning Up..."
rm /tmp/chromedriver.zip

echo "...Adding Chromedriver to Path..."
export PATH="${PATH}:${CHROMEDRIVER_PATH}"
echo "Installed Chromedriver Version:"
chromedriver --version

echo "...Installing packages..."
#pip install -r requirements.txt

echo "...Build Script Completed!"


echo "...Installing packages..."

#pip install -r requirements.txt

set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate


echo "...Build Script Completed!"






