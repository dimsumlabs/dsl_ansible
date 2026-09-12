This repository contains the infrastructure configuration automation used
to setup and manage some of the DSL servers.

It is intended to both deploy configuration and serve as documentation for how
things are setup.

## User access setup

In order to access the infrastructure, the vars/userdb.yml needs to be updated
with the correct details.  Then someone who has existing access needs to
deploy the change.

The details in the userdb that you will need to supply include:
- Crypted password (generate with `openssl passwd -6`)
- SSH public key

To ensure a minimum level of security:
- no users will ever be able to login with their password.
- to use sudo, you must type a password in
- There is no root password known

This means that the combination of the ssh key and the user password become
a very light-weight two factor process.

## Running Ansible

You will need to have ansible installed and on your path before running
this repository.

On a Debian system, the Makefile can assist you with this:

```
make build_dep
```

### Check your login

To quickly check if your environment is setup and your user account, ssh key
and sudo password are all working, you can use this command:

```
ansible --become -K -m ping linux
```

### Standard deploy

To run through the standard playbook and deploy everything needed, a command
similar to the following can be used:

```
ansible-playbook main.yml --check -K
```

### Avoiding needing to type in the become password

Due to our security expectations, the sudo - or "become" - password will need
to be given to ansible on each run (The `-K` option in the above examples is
turning on the ansible prompt for this password)

Since typing the password can quickly get tedious - and we want to avoid
people trying to avoid the security requirements - this repo also includes
an ansible plugin to allow integrating with your existing password manager.

If your environment contains "LOCAL_SUDO_LOOKUP", and that points to a
script, then the included plugin will call that script to fetch the required
password(s).

The script is called as "{SCRIPT} --sudo ^{HOSTNAME}$" and should return the
password on stdout.

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
