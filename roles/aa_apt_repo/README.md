# doc

Deploy data and config needed for apt repositories.

This role supports adding apt repos a couple of different ways.  Any new way
to configure apt repos should be added here as well.

Activated by the presence of a key in the host vars.

NOTE: this role is named with an `aa` so as to ensure it sorts before other
roles.  This allows it to set the system up for other roles to install their
correct packages.

## Using extrepo

```yaml
apt_repo:
  extrepo:
    opentofu:
```

## Using custom repositories

```yaml
apt_repo:
  custom:
    ourname:
      enabled: no
      source:
        Types: deb
        URIs: https://example.com/apt
        Suites: stable
        Components: main
  key:
    ourname.asc: |
      -----BEGIN PGP PUBLIC KEY BLOCK-----
      FILL IN WITH YOUR PUB KEY
      -----END PGP PUBLIC KEY BLOCK-----
```

Note that there is no special handling for URIs that need auth.  It can either
be included in the URL directly, or this role could be extended with an
apt_repo.auth fetaure that adds entries to the /etc/apt/auth.conf.d/
