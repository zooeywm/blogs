---
title: "Hugo In Wsl"
weight: 1
# bookFlatSection: false
bookToc: true
# bookHidden: false
# bookCollapseSection: true
# bookComments: false
# bookSearchExclude: false
---

## Open systemd in wsl

If you are trying to install hugo with snap, you should open systemd first, nor the snapd will not work.

> refer to link: [ubuntu-wsl-enable-systemd](https://ubuntu.com/blog/ubuntu-wsl-enable-systemd)

In your wsl, add

```toml
[boot]
systemd = true
```

to `/etc/wsl.conf`

## Install Hugo with snap

Then, you can smoothly install hugo according to [hugo doc](https://gohugo.io/installation/linux/#snap).

{{< hint info >}}
**Possibility to use a proxy**  
If you meet some problem such as connection error, you might use proxy
{{< /hint >}}
