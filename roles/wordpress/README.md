
- enabled by existence of host var

## example config

```
wordpress:
  yourinstallname:
    version: 6.7.7
    db_user: wpuser
    db_passpath: mariadb/test1user
    salts:
      auth_key: fillin
      secure_auth_key: fillin
      logged_in_key: fillin
      nonce_key: fillin
      auth_salt: fillin
      secure_auth_salt: fillin
      logged_in_salt: fillin
      nonce_salt: fillin
```

In the above example the "yourinstallname" is the internal site name.  This is
used to calculate the database name and the installation directory.

The database user and password, will need to match the database.  The
db_passpath field describes the pathname suffix to the pass database.  This is
prefixed with the hostname

Note that the version number is only used for an initial server setup. Upgrades
are assumed to be handled by wordpress itself.  Also, each version download
needs to be defined with a matching checksum in the role defaults.

## webserver

The host also needs to also deploy a webserver config.  The nginx role has a
template for this purpose.

## TODO

- salts
- https://api.wordpress.org/secret-key/1.1/salt/
