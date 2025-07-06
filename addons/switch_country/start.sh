#!/bin/bash

# Start the mitmproxy server without UI
mitmweb -s ./switch_country.py -m wireguard --listen-host 0.0.0.0 --listen-port 51820 --ignore-hosts "^ba.dn.nexoncdn.co.kr|^toy.log.nexon.io"
