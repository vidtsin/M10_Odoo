#!/usr/bin/env bashç

scp -r addons/* odoo@192.168.10.10:~/odoo-11.0/
ssh god@192.168.10.10 sudo service odoo start