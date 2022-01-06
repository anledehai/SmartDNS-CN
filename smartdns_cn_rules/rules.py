# 将dnsmasq-china-list解析成SmartDNS可用的格式

content = open("./accelerated-domains.china.conf")
with open("./accelerated-domains.china.smartdns.conf", "w+") as a:
    a.truncate(0)
    for line in content:
        a.write(line.replace(
            "server=/", "nameserver /").replace("/114.114.114.114", "/CN"))

content = open("./apple.china.conf")
with open("./apple.china.smartdns.conf", "w+") as b:
    b.truncate(0)
    for line in content:
        b.write(line.replace(
            "server=/", "nameserver /").replace("/114.114.114.114", "/CN"))

content = open("./google.china.conf")
with open("./google.china.smartdns.conf", "w+") as c:
    c.truncate(0)
    for line in content:
        c.write(line.replace(
            "server=/", "nameserver /").replace("/114.114.114.114", "/CN"))

exit()
