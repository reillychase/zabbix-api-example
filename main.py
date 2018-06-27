from pyzabbix import ZabbixAPI
import os

zapi = ZabbixAPI("https://zabbix.site.com/zabbix")
zapi.login("zabbix-user", "password")
print("Connected to Zabbix API Version %s" % zapi.api_version())


num_digits = 32
myhex = os.urandom(num_digits / 2).encode('hex')
psk_hex = myhex

zapi.template

zapi.hostgroups.get()

# Create a host, apply templates
host_id = zapi.host.create({"host":"test.com","tls_connect":"2","tls_accept":"2","tls_psk_identity":"test-psk01",
                            "tls_psk":psk_hex,"interfaces":[{"type":"1", "main":"1","useip":"0","ip":"127.0.0.1",
                            "dns":"test.com","port":"10050"}],"groups":[{"groupid":"15"}],
                            "templates":[{"templateid": "10001","templateid":"10255"}]})["hostids"][0]

# Delete a host
zapi.host.delete(host_id)
