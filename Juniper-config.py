import jinja2

routers = [
    {"hostname": "R1", "interfaces" : [
        {"interface": "lo0", "ip": "10.0.0.1", "netmask": "/32", "wc-mask": "0.0.0.0", "area": "0.0.0.0"},
        {"interface": "e0.0", "ip": "10.0.12.1", "netmask": "/30", "wc-mask": "0.0.0.3", "area": "0.0.0.0"},
        {"interface": "e2.0", "ip": "10.0.71.2", "netmask": "/24", "wc-mask": "0.0.0.255", "area": "0.0.0.0"},
        {"interface": "e3.0", "ip": "192.168.1.1", "netmask": "/24", "wc-mask": "0.0.0.255", "area": "0.0.0.0"}
    ]},
    {"hostname": "R2", "interfaces" : [
        {"interface": "lo0", "ip": "10.0.0.2", "netmask": "/32", "wc-mask": "0.0.0.0", "area": "0.0.0.0"},
        {"interface": "e2.0", "ip": "10.0.12.2", "netmask": "/30", "wc-mask": "0.0.0.3", "area": "0.0.0.0"},
        {"interface": "e2.0", "ip": "10.0.27.2", "netmask": "/30", "wc-mask": "0.0.0.3", "area": "0.0.0.0"},
        {"interface": "e2.0", "ip": "10.0.23.1", "netmask": "/30", "wc-mask": "0.0.0.3", "area": "0.0.0.0"}
    ]},
    {"hostname": "R3", "interfaces" : [
        {"interface": "lo0", "ip": "10.0.0.3", "netmask": "/32", "wc-mask": "0.0.0.0", "area": "0.0.0.0"},
        {"interface": "e1.0", "ip": "10.0.34.1", "netmask": "/30", "wc-mask": "0.0.0.3", "area": "0.0.0.0"},
        {"interface": "e2.0", "ip": "10.0.23.2", "netmask": "/30", "wc-mask": "0.0.0.3", "area": "0.0.0.0"}
    ]},
    {"hostname": "R4", "interfaces" : [
        {"interface": "lo0", "ip": "10.0.0.4", "netmask": "/32", "wc-mask": "0.0.0.0", "area": "0.0.0.0"},
        {"interface": "e1.0", "ip": "10.0.34.2", "netmask": "/30", "wc-mask": "0.0.0.3", "area": "0.0.0.0"},
        {"interface": "e2.0", "ip": "10.0.45.1", "netmask": "/30", "wc-mask": "0.0.0.3", "area": "0.0.0.0"},
    ]},
    {"hostname": "R5", "interfaces" : [
        {"interface": "lo0", "ip": "10.0.0.5", "netmask": "/32", "wc-mask": "0.0.0.0", "area": "0.0.0.0"},
        {"interface": "e0.0", "ip": "10.0.56.1", "netmask": "/30", "wc-mask": "0.0.0.3", "area": "0.0.0.0"},
        {"interface": "e1.0", "ip": "10.0.58.1", "netmask": "/30", "wc-mask": "0.0.0.3", "area": "0.0.0.0"},
        {"interface": "e2.0", "ip": "10.0.45.2", "netmask": "/30", "wc-mask": "0.0.0.3", "area": "0.0.0.0"}
    ]},
    {"hostname": "R6", "interfaces" : [
        {"interface": "lo0", "ip": "10.0.0.6", "netmask": "/32", "wc-mask": "0.0.0.0", "area": "0.0.0.0"},
        {"interface": "e0.0", "ip": "10.0.56.2", "netmask": "/30", "wc-mask": "0.0.0.3", "area": "0.0.0.0"},
        {"interface": "e3.0", "ip": "192.168.6.1", "netmask": "/24", "wc-mask": "0.0.0.3", "area": "0.0.0.0"}
    ]}, 
    {"hostname": "R7", "interfaces" : [
        {"interface": "lo0", "ip": "10.0.0.7", "netmask": "/32", "wc-mask": "0.0.0.0", "area": "0.0.0.0"},
        {"interface": "e1.0", "ip": "10.0.27.1", "netmask": "/30", "wc-mask": "0.0.0.3", "area": "0.0.0.0"},
        {"interface": "e3.0", "ip": "192.168.7.1", "netmask": "/24", "wc-mask": "0.0.0.3", "area": "0.0.0.0"}
    ]},
    {"hostname": "R8", "interfaces" : [
        {"interface": "lo0", "ip": "10.0.0.8", "netmask": "/32", "wc-mask": "0.0.0.0", "area": "0.0.0.0"},
        {"interface": "e1.0", "ip": "10.0.58.2", "netmask": "/30", "wc-mask": "0.0.0.3", "area": "0.0.0.0"},
        {"interface": "e3.0", "ip": "192.168.8.1", "netmask": "/24", "wc-mask": "0.0.0.3", "area": "0.0.0.0"}
    ]}
]

interfaceLabels = ["lo0", "em0", "em1", "em2", "em3", "em4"]

environment = jinja2.Environment(loader=jinja2.FileSystemLoader("templates/"))
template = environment.get_template("juniper-config.txt")

for router in routers:
    filename = f"config_{router['hostname']}.txt"
    content = template.render(
        router,
        hostname = router['hostname'],
        interfaceLabels = interfaceLabels
    )
    with open(filename, mode="w", encoding="utf-8") as blah:
        blah.write(content)
        print(f"... wrote {filename}")
