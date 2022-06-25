# Unifi Updater
This tool is designed to auto-update your Unifi-Controller to the latest available version automatically, depending on the release-channel selected in your Unifi-Controller.

This tool is primarily designed for using release-candidates (RC) and early-access (EA) versions of the Unifi-Controller. If you want to run the regular stable releases, I recommend using the [Unifi PPA](https://help.ui.com/hc/en-us/articles/220066768-UniFi-Network-Updating-Third-Party-non-Console-UniFi-Network-Applications-Linux-Advanced-#STEPS).

WARNING: This tool could brick your Unifi-Controller installation. Make sure you have daily backups enabled, so that you can restore your installation in case an update fails.

## Compatibility
This tool has been tested on Ubuntu Server 20.04 LTS. It will most likely work on other Debian based systems aswell, as long as the dependencies are met.

## Dependencies
- git
- wget
- python3

## Installation
### Cloning the repository
Clone the git repository to your Unifi-Controller Server with `git clone https://github.com/spyfly/unifi-updater.git`

### Configuration
Rename `example_config.json` to `config.json` and enter your Unifi-Controller credentials. Verify that your credentials were correct, by running the script via `sudo python3 unifi_updater.py`.

### Setting up a cronjob
This script has to run as root. To setup a cronjob as root type `sudo crontab -e`.

Now you can create a cronjob, such as 
```
0 4 * * * cd /home/unifi/unifi-updater/ && python3 unifi_updater.py
```
This will run the update script every morning at 4 am. Make sure you adjust the `cd` command accordingly.

Now you are fully-setup and the script will update your Unifi-Controller to the latest version of the selected release channel in the controller itself.