# See Wireless Adapter Information

*from [Ubuntu Help Pages](https://help.ubuntu.com/stable/ubuntu-help/net-wireless-troubleshooting-hardware-check.html)*

Use the `lshw` (List Hardware) utility and search for the Class `network`.

```bash
$ sudo lshw -C network
  *-network                 
       description: Wireless interface
       product: Wireless 7265
       vendor: Intel Corporation
       ...
```
