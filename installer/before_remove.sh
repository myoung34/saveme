#!/bin/bash
launchctl unload /Library/LaunchDaemons/local.aws_vault_proxy.plist
for user in $(find /Users -maxdepth 1 | grep -Ev '^\/Users\/(Shared|\.)' | tail -n +2); do
  rm -rf ${user}/Library/LaunchAgents/local.saveme.plist
done
rm -rf /Library/LaunchDaemons/local.aws_vault_proxy.plist
