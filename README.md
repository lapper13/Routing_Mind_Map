# Routing_Mind_Map
IAATJ Discord Session 

## Important - make sure the hostname of the device is specified in the testbed.yaml file

Right now it is "Farhad1354"

So the testbed looks like this

```yaml
devices:
    Farhad1354:
     alias: 'Always On Nexus'
     type: 'router'
     os: 'nxos'
     role: 'dist'
     platform: n9k
     credentials:
       default:
         username: admin
         password: Admin_1234!
     connections:        
       cli:
         protocol: "ssh"
         ip: "sandbox-nxos-1.cisco.com"
         arguments:
           connection_timeout: 360
```

If somebody changes the hostname you have to update the name of the device in this file accordingly so pyATS can connect