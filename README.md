<picture>
  <source media="(prefers-color-scheme: dark)" srcset="resources/bmconnect_banner_dark.png">
  <img alt="bm+connect" src="resources/bmconnect_banner.png">
</picture>

[![GitHub license](https://img.shields.io/github/license/beep-projects/bmconnect)](https://github.com/beep-projects/bmconnect/blob/main/LICENSE) [![Pylint](https://github.com/beep-projects/bmconnect/actions/workflows/pylint.yml/badge.svg)](https://github.com/beep-projects/bmconnect/actions/workflows/pylint.yml) [![GitHub issues](https://img.shields.io/github/issues/beep-projects/bmconnect)](https://github.com/beep-projects/bmconnect/issues) [![GitHub forks](https://img.shields.io/github/forks/beep-projects/bmconnect)](https://github.com/beep-projects/bmconnect/network) [![GitHub stars](https://img.shields.io/github/stars/beep-projects/bmconnect)](https://github.com/beep-projects/bmconnect/stargazers) ![GitHub repo size](https://img.shields.io/github/repo-size/beep-projects/bmconnect) ![visitors](https://visitor-badge.glitch.me/badge?page_id=beep-projects.bmconnect)

# bmconnect
Script to upload your measurements from a Beurer 58 blood pressure meter to your Garmin Connect account. I would love to add support for other devices, see [contributing](#Contribute)  
Currently I only own a Beurer BM58, wich connects as HID device `ID 0c45:7406 Microdia USB Device`.
There are other versions of this device around that incorporate the USB-Serial Controller `pl2303` and connect as new ttyUSB device. Support for this version is not tested, but please give it a try if you own such a device. Your feedback is higly appreciated.

## Installation
At the moment, I have tested this only on an Ububtu Linux, but the script should also run on other distributions or Windows if python is installed.

### install the script and its dependencies
```
git clone https://github.com/beep-projects/bmconnect/
cd bmconnect
```
Create virtual python environment and get the required modules
```
python3 -m venv venv
venv/bin/pip3 install -r requirements.txt
```
### Configure bmconnect
Note, the config will be saved for the user running bmconnect.py, so if you intend to install bmconnect to be automatically run as soon as a device is plugged in, you have to run the following command as `sudo`.
You need to configure `--login`, but you can also configure `--user` and `--language`.
```
venv/bin/python3 bmconnect.py --login
```
### Grant access to everyone
By default, only the root user can access the device. By adding this rule to udev, you allow it for all users
```
sudo cp 98-beurerBM58.rules /etc/udev/rules.d/
```
### Test if everything works
Now you can test if everything works fine for you. Plug in your device and execute. Remember, if you ran the configuration with `sudo` you also have to make this call as `sudo`
```
venv/bin/python3 bmconnect.py
```
### Patch bmconnect.service 
If the test was successful, you can continue to install the rules, to run `bmconnect.py` everytime you plug in your Beurer device. First, you have to patch the service file, to use your current installation
```
# edit this line: 
# ExecStart=[path to python venv]/python3 [path to script]/bmconnect.py
# by hand, or via
sed -i "s|^ExecStart=.*|ExecStart="$(pwd)"\/venv\/bin/python3 "$(pwd)"\/bmconnect.py|" bmconnect.service
```
### install bmconnect.service to systemd
Now you need to install the bmconnect.service for systemd. You only need to copy it, but not enable it via `systemctl`, because this service should not run on startup.
```
sudo cp bmconnect.service /etc/systemd/system
sudo systemctl daemon-reload
```
### Install udev rule to call the service
Finally, you need to tell udev to start the service, everytime a Beurer device is plugged in
```
sudo cp 99-beurerBM58.rules /etc/udev/rules.d/
```
### Done
udev should load the rules automatically, so just plugin your Beurer device and check

### Debugging
debugging udev and services is tricky, so I advice to first run the script in your python environment as described above. If everything looks good on that level, you can watch the syslog, while you plugin your device.
```
tail -f /var/log/syslog
```

## Contribute
If you want to contribute to the project, I have created a small [Contributing Guide](CONTRIBUTING.md). To keep it short, it is best if you simply open a new [Discussion](https://github.com/beep-projects/bmconnect/discussions) and talk about what you are up to, or where you need help.

If you want to add support for another Beurer device, you can register at https://connect.beurer.com/developer/ and get access to the documentation of communication protocols. The needed code changes can be talked about in the [Discussions](https://github.com/beep-projects/bmconnect/discussions).

Projects which I used as a starting point
- https://github.com/muling-tt/beurer_bm58
- https://gitlab.com/dieheins/bpmeter
- https://github.com/curzon01/bm58
- https://github.com/cyberjunky/python-garminconnect
