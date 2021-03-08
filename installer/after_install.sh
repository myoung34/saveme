#!/bin/bash
/usr/bin/pip3 install saveme >/var/log/saveme.log 2>&1

cp $(/usr/bin/python3 -c 'import sysconfig; print(sysconfig.get_paths()["purelib"])')/saveme/ns-icon.icns /usr/local/bin
cp /opt/saveme/launchdaemon.plist /Library/LaunchDaemons/local.aws_vault_proxy.plist

launchctl load -w /Library/LaunchDaemons/local.aws_vault_proxy.plist

rm -rf /opt/saveme
