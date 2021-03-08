SAVEME
======

### Simplified AWS Vault Execution Menu Environment ###

[![PyPI version](https://img.shields.io/pypi/v/saveme.svg)](https://pypi.python.org/pypi/saveme/)

![](https://cdn.zappy.app/2105ab6027a70bc39a3184a6cac73d7a.gif)

### OSX Menu Bar for AWS-Vault Metadata Server (via launchctl) ###


### Limitations ###

* This will only work on web based SSO logins
  * This is because prompting etc does not work from launchctl (even osascript)
* This is OSX only (Because of launchctl)

### Installing ###

* Grab a `.pkg` release off of the [Releases Page](https://github.com/myoung34/saveme/releases/)
* Open it in finder by right clicking and click open (the package is not signed)
* Follow the prompts
* Run `launchctl load -w ~/Library/LaunchAgents/local.saveme.plist`

### Uninstalling ###

* Clone this repo
* Run: `launchctl unload -w ~/Library/LaunchAgents/local.*`
* Run: `sudo bash installer/before_remove.sh`
* Run: `sudo bash installer/after_remove.sh`

### Testing ###

```
$ poetry install
$ poetry run tox
```
