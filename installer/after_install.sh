#!/bin/bash
cp /opt/saveme/launchdaemon.plist /Library/LaunchDaemons/local.aws_vault_proxy.plist
launchctl load -w /Library/LaunchDaemons/local.aws_vault_proxy.plist
