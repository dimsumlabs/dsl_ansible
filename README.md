This repository contains the infrastructure configuration automation used
to setup and manage some of the DSL servers.

It is intended to both deploy configuration and serve as documentation for how
things are setup.

## User access setup

In order to access the infrastructure, you will need to be setup first.
You will need to ask someone who has existing access to create your access.

They will create and deploy a user for you, using the ssh key and the crypted
password that you provide them.

To generate this crypted password:
```
sudo apt-get -y install openssl
openssl passwd -6
```

## Running Ansible

You will need to have ansible installed and on your path before running
this repository.

On a Debian system, the Makefile can assist you with this:

```
make build_dep
```

## Coding Style

### Jinja in YAML

Ansible allows you to embed Jinja inside any YAML file that you load.  This
can quickly make it very hard to read and understand the logic of what is
happening.

Thus, we are keeping a clear separation between code and data - any files in
the host_vars, group_vars and vars directories should avoid using jinja.

### YAML style

To avoid making messy and hard to read yaml files, some features of yaml are
deliberately avoided.

- Do not use flow style, except for creating empty lists or dicts
- Do not use anchors and aliases - complex inheritance can make it almost
  impossible to see the actual data and so explicit is better than implicit
- Keys should be always kept consistently ordered - in ansible code, the
  ansible lint tool will advise about some ordering, but in the YAML data
  files, this usually means that things should be kept asciibetically sorted.
  This ensures that even if multiple people are adding things to a file, there
  will sill be a clear and consistent place and order.
