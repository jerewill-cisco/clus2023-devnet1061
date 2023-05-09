#!/usr/bin/bash
source vars.sh
terraform init
terraform apply -auto-approve
ansible-playbook ntp_ansible.yml
pwsh ntp_powershell.ps1
python3 ntp_pythonsdk.py
python3 ntp_pythonrequests.py
bash configure_isctl.sh
bash ntp_isctl.sh
