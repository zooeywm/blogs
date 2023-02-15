---
title: "Proxy Config"
weight: 1
# bookFlatSection: false
bookToc: true
# bookHidden: false
# bookCollapseSection: false
# bookComments: false
# bookSearchExclude: false
---

## Config proxy in wsl

Append these codes to `~/.bashrc`, then the wsl will use PC's proxy.

```bash
function proxy_set(){
host_ip=$(cat /etc/resolv.conf |grep "nameserver" |cut -f 2 -d " ")
# or you can set ip derict to your pc name
# host_ip="your-pc-name"
proxy_port="7890"
proxy="http://$host_ip:$proxy_port"
export HTTP_PROXY=$proxy
export HTTPS_PROXY=$proxy
export ALL_PROXY=$proxy
echo 'proxy was set'
}

function proxy_unset(){
unset HTTP_PROXY
unset HTTPS_PROXY
unset ALL_PROXY
echo 'proxy was unset'
}

proxy_set
```
