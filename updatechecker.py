import json
import requests
import base64
from phoibe import send_message

def getVersion():
    file = open("settings.json", "r")
    data = json.load(file)
    version = data['systemsettings']['version']
    ver, version, codename = version.split(" ")
    return version

def saveVersion():
    version, codename = getVersion()
    with open("version.txt", "r+") as f:
        f.write(version)

def checkVersion():
    installedVersion = getVersion()
    url = 'https://api.github.com/repos/teenchatbot/botversion/contents/version.txt'
    req = requests.get(url)
    if req.status_code == requests.codes.ok:
        req = req.json()
        content = base64.b64decode(req['content'])
        content = content.decode()
        ver, version, codename = content.split(" ")
        print(version)
        print(installedVersion)
        if version == installedVersion:
            send_message("your version is up to date")
        else:
            send_message("you need to update to " + version + ", " + "your version is " + installedVersion)
    else:
        print("content not found")
