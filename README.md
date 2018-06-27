# zabbix-api-example
Zabbix API Example

An example of creating a host on Zabbix. I wrote some code to automatically provision and unprovision Zabbix monitoring on VPSes.

This creates a host, generates a 32 char hex PSK and sets up TLS PSK settings. Also adds the host to a custom group ID 15, and assigns 2 templates - 1001 is the Linux default template, and the other is a custom template.
