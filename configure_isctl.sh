#!/usr/bin/bash
touch ~/.isctl.yaml
echo "insecure: false" >~/.isctl.yaml
echo "keyfile: key.pem" >>~/.isctl.yaml
echo -n "keyid: " >>~/.isctl.yaml && cat key.id >>~/.isctl.yaml && echo "" >>~/.isctl.yaml
echo "output: default" >>~/.isctl.yaml
echo "server: intersight.com" >>~/.isctl.yaml
