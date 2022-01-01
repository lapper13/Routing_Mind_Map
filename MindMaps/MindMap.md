
# Hostname: Always On Nexus
## Operating System: nxos
## VRF: TEST Address Family: ipv4
### Route: 12.12.12.1/32
#### Active: True
#### Metric: 0
#### Route Preference: 0
#### Source Protocol: local
#### Next Hop: 1
##### Outgoing Interface: 1
###### Outgoing Interface: Ethernet1/3
###### Outgoing Interface: 6d05h
### Route: 12.12.12.0/24
#### Active: True
#### Metric: 0
#### Route Preference: 0
#### Source Protocol: direct
#### Next Hop: 1
##### Outgoing Interface: 1
###### Outgoing Interface: Ethernet1/3
###### Outgoing Interface: 6d05h
### Route: 7.7.7.1/32
#### Active: True
#### Metric: 0
#### Route Preference: 0
#### Source Protocol: local
#### Next Hop: 1
##### Outgoing Interface: 1
###### Outgoing Interface: Ethernet1/4
###### Outgoing Interface: 6d05h
### Route: 7.7.7.0/24
#### Active: True
#### Metric: 0
#### Route Preference: 0
#### Source Protocol: direct
#### Next Hop: 1
##### Outgoing Interface: 1
###### Outgoing Interface: Ethernet1/4
###### Outgoing Interface: 6d05h
## VRF: management Address Family: ipv4
### Route: 10.10.20.95/32
#### Active: True
#### Metric: 0
#### Route Preference: 0
#### Source Protocol: local
#### Next Hop: 1
##### Outgoing Interface: 1
###### Outgoing Interface: mgmt0
###### Outgoing Interface: 6d05h
### Route: 10.10.20.0/24
#### Active: True
#### Metric: 0
#### Route Preference: 0
#### Source Protocol: direct
#### Next Hop: 1
##### Outgoing Interface: 1
###### Outgoing Interface: mgmt0
###### Outgoing Interface: 6d05h
### Route: 0.0.0.0/0
#### Active: True
#### Metric: 0
#### Route Preference: 1
#### Source Protocol: static
#### Next Hop: 1
##### Outgoing Interface: 1
###### Outgoing Interface: 
###### Outgoing Interface: 6d05h
## VRF: default Address Family: ipv4
### Route: 192.168.22.22/32
#### Active: True
#### Metric: 0
#### Route Preference: 0
#### Source Protocol: direct
#### Next Hop: 2
##### Outgoing Interface: 2
###### Outgoing Interface: Loopback222
###### Outgoing Interface: 4d23h
#### Next Hop: 1
##### Outgoing Interface: 1
###### Outgoing Interface: Loopback222
###### Outgoing Interface: 4d23h
### Route: 192.168.2.1/32
#### Active: True
#### Metric: 0
#### Route Preference: 0
#### Source Protocol: local
#### Next Hop: 1
##### Outgoing Interface: 1
###### Outgoing Interface: Loopback201
###### Outgoing Interface: 6d05h
### Route: 192.168.2.0/24
#### Active: True
#### Metric: 0
#### Route Preference: 0
#### Source Protocol: direct
#### Next Hop: 1
##### Outgoing Interface: 1
###### Outgoing Interface: Loopback201
###### Outgoing Interface: 6d05h
### Route: 172.21.4.1/32
#### Active: True
#### Metric: 0
#### Route Preference: 0
#### Source Protocol: local
#### Next Hop: 1
##### Outgoing Interface: 1
###### Outgoing Interface: Loopback14
###### Outgoing Interface: 05:31:23
### Route: 172.21.4.0/24
#### Active: True
#### Metric: 0
#### Route Preference: 0
#### Source Protocol: direct
#### Next Hop: 1
##### Outgoing Interface: 1
###### Outgoing Interface: Loopback14
###### Outgoing Interface: 05:31:23
### Route: 172.21.3.1/32
#### Active: True
#### Metric: 0
#### Route Preference: 0
#### Source Protocol: local
#### Next Hop: 1
##### Outgoing Interface: 1
###### Outgoing Interface: Loopback13
###### Outgoing Interface: 05:31:33
### Route: 172.21.3.0/24
#### Active: True
#### Metric: 0
#### Route Preference: 0
#### Source Protocol: direct
#### Next Hop: 1
##### Outgoing Interface: 1
###### Outgoing Interface: Loopback13
###### Outgoing Interface: 05:31:33
### Route: 172.21.2.1/32
#### Active: True
#### Metric: 0
#### Route Preference: 0
#### Source Protocol: local
#### Next Hop: 1
##### Outgoing Interface: 1
###### Outgoing Interface: Loopback12
###### Outgoing Interface: 05:31:41
### Route: 172.21.2.0/24
#### Active: True
#### Metric: 0
#### Route Preference: 0
#### Source Protocol: direct
#### Next Hop: 1
##### Outgoing Interface: 1
###### Outgoing Interface: Loopback12
###### Outgoing Interface: 05:31:41
### Route: 172.21.1.1/32
#### Active: True
#### Metric: 0
#### Route Preference: 0
#### Source Protocol: local
#### Next Hop: 1
##### Outgoing Interface: 1
###### Outgoing Interface: Loopback11
###### Outgoing Interface: 05:31:50
### Route: 172.21.1.0/24
#### Active: True
#### Metric: 0
#### Route Preference: 0
#### Source Protocol: direct
#### Next Hop: 1
##### Outgoing Interface: 1
###### Outgoing Interface: Loopback11
###### Outgoing Interface: 05:31:50
### Route: 10.10.1.1/32
#### Active: True
#### Metric: 0
#### Route Preference: 0
#### Source Protocol: direct
#### Next Hop: 2
##### Outgoing Interface: 2
###### Outgoing Interface: Loopback10
###### Outgoing Interface: 6d05h
#### Next Hop: 1
##### Outgoing Interface: 1
###### Outgoing Interface: Loopback10
###### Outgoing Interface: 6d05h
## VRF: default Address Family: ipv6
### Route: 2001:db8:acad:1::1/128
#### Active: True
#### Metric: 0
#### Route Preference: 0
#### Source Protocol: local
#### Next Hop: 1
##### Outgoing Interface: 1
###### Outgoing Interface: Loopback400
###### Outgoing Interface: 6d05h
### Route: 2001:db8:acad:1::/64
#### Active: True
#### Metric: 0
#### Route Preference: 0
#### Source Protocol: direct
#### Next Hop: 1
##### Outgoing Interface: 1
###### Outgoing Interface: Loopback400
###### Outgoing Interface: 6d05h