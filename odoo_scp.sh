#!/usr/bin/env bash

echo "start"
scp -r addons/* odoo@192.168.10.10:~/odoo-11.0/addons/
echo "copied"
ssh odoo@192.168.10.10 killall python3
ssh odoo@192.168.10.10 /home/odoo/odoo-11.0/odoo-bin &
echo "end"