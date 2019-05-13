#!/usr/bin/env bash
#
# Add credentials on the server to access without password
# Create a public key on LOCAL computer and copy in server
#   ssh-keygen -b 4096 -t rsa
#   scp .ssh/id_rsa.pub user@server:.ssh/new_key
#
# On SERVER side, do this.
#   cd .ssh
#   cat new_key >> authorized_keys
#   chmod 0700 ~/.ssh/
#   chmod 0600 ~/.ssh/authorized_keys
#
#
# Configure parameters
#
SERVER="192.168.10.10"
SERVER_USER="odoo"
LOCAL_ADDONS_DIRECTORY="addons"
SERVER_ADDONS_DIRECTORY="~/odoo-11.0/addons"

# 0 use python file, 1 use odoo service, if otherwise do nothing
SERVICE=0;
BIN_PATH="/home/odoo/odoo-11.0/odoo-bin"

scp -r $LOCAL_ADDONS_DIRECTORY/* odoo@$SERVER:$SERVER_ADDONS_DIRECTORY/
echo "copied"

if [[ $SERVICE -eq 0 ]]; then
    ssh $SERVER_USER@$SERVER killall python3
    ssh $SERVER_USER@$SERVER $BIN_PATH &
else
    if [[ $SERVICE -eq 1 ]]; then
        ssh $SERVER_USER@$SERVER service odoo restart
    fi
fi
echo "service restarted"