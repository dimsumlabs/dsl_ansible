
Templated firewall

- enabled by the existance of a host var

## example config

```
nftables:
  template_type: simple_server
  ports:
    tcp:
      - 22
```
