#!/bin/bash
/usr/bin/pip3 install saveme==0.0.3 >/var/log/saveme.log 2>&1

cp $(/usr/bin/python3 -c 'import sysconfig; print(sysconfig.get_paths()["purelib"])')/saveme/ns-icon.icns /usr/local/bin
cp /opt/saveme/launchdaemon.plist /Library/LaunchDaemons/local.aws_vault_proxy.plist

for user in $(find /Users -maxdepth 1 | grep -Ev '^\/Users\/(Shared|\.)' | tail -n +2); do
  username=$(echo ${user} | sed 's/^\/Users\///g')
  echo "Installing launchagent for user ${username}" >>/var/log/saveme.log 2>&1
  cp /opt/saveme/launchagent.plist ${user}/Library/LaunchAgents/local.saveme.plist
  chown $(id -u ${username}):$(id -g ${username}) ${user}/Library/LaunchAgents/local.saveme.plist >>/var/log/saveme.log 2>&1
  # To start, run:
  #   launchctl load -w ${user}/Library/LaunchAgents/local.saveme.plist
done
launchctl load -w /Library/LaunchDaemons/local.aws_vault_proxy.plist

rm -rf /opt/saveme
