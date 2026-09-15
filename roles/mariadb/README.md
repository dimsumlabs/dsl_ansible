
- enabled by the existence of a host var

## Example

```
mariadb:
  databases:
    test1db:
  users:
    test1user:
      password: fixmefixme
      grants:
        test1db.*: ALL
```

# TODO

- deploy daily dump script
