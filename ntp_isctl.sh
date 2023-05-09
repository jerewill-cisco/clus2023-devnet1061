#!/usr/bin/bash
isctl create ntp policy \
    --Name isctl \
    --Description "This is an NTP policy created with isctl" \
    --Organization CLUS \
    --Enabled true \
    --NtpServers 1.1.1.1,2.2.2.2 \
    --Tags '[{"Key":"CLUS2023","Value":"Devnet-1061"},{"Key":"Language","Value":"isctl"}]' \
    --Timezone America/Phoenix
