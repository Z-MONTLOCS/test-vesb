#!/bin/bash

echo "...Installing packages..."

#pip install -r requirements.txt

set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate

echo "...Build Script Completed!"


#CHROME_PATH="/opt/render/project/bin/chrome/opt/google/chrome"
#CHROMEDRIVER_PATH="/opt/render/project/bin"


CHROME_PATH="/opt/render/project/bin/chrome/opt/google/chrome"
CHROMEDRIVER_PATH="/opt/render/project/bin/chromedriver-linux64"  # Cambia esta ruta según la ubicación real de chromedriver

# Desinstalar Chromedriver si existe
if [[ -d $CHROMEDRIVER_PATH ]]; then
    echo "...Uninstalling Existing Chromedriver..."
    rm -rf $CHROMEDRIVER_PATH
fi

if [[ ! -d $CHROME_PATH ]]; then
    echo "...Downloading Chrome Binary..."
    wget -O /tmp/google-chrome.zip https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/116.0.5845.96/linux64/chrome-linux64.zip

    echo "...Installing Chrome Binary..."
    mkdir -p /opt/render/project/bin/chrome
    unzip /tmp/google-chrome.zip -d /opt/render/project/bin/chrome

    echo "...Cleaning Up..."
    rm /tmp/google-chrome.zip

    # Agregar la ubicación de Chrome al PATH
    export PATH="${PATH}:${CHROME_PATH}"

    echo "Installed Chrome Version:"
    /opt/render/project/bin/chrome/opt/google/chrome/chrome --version
else
    echo "...Detected Existing Chrome Binary"
fi

echo "...Downloading Chromedriver..."
wget -O /tmp/chromedriver.zip https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/116.0.5845.96/linux64/chromedriver-linux64.zip

echo "...Installing Chromedriver..."
unzip /tmp/chromedriver.zip -d /opt/render/project/bin

echo "...Cleaning Up..."
rm /tmp/chromedriver.zip

# Agregar la ruta al directorio chromedriver a la variable de entorno PATH
export PATH="${PATH}:${CHROMEDRIVER_PATH}"

echo "Installed Chromedriver Version:"
chromedriver --version

echo "...Installing packages..."
#pip install -r requirements.txt

echo "...Build Script Completed!"
