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
