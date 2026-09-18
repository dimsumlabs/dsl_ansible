
- enabled by the existence of a host var

## Example

```
mariadb:
  databases:
    test1db:
  users:
    test1user:
      passpath: mariadb/test1user
      grants:
        test1db.*: ALL
```

The password field describes the pathname suffix to the pass database.  This
is prefixed with the hostname.
