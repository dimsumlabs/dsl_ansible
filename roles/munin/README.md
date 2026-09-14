
# Configure munin-node

- Always enabled
- Ensures that munin-client is installed and listening for connections
- Configures the allowed hosts

## Example config

```
munin:
  allow:
    - '^192\.168\.1\..*$'
```
