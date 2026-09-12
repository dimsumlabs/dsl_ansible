# doc

## Configure user accounts and groups

This role is designed to create user accounts on managed systems.  It is not
expected to be used when there is a large number of users or a large number
of changes.  It should be suitable for a DevOps team and a small number of
dev teams.

This role will also default to removing access for the initial deploy user
authorized keys (the "ubuntu" user or "admin" user).  This can be disabled
with a host var setting `users_manage_deploy_access: false`

Finally, this role will remove "junk" groups that might be created by a
generic cloud-init that is built to work for both Debian and R-hell.
Currently, this is just removing "wheel" on Debian-like systems.

## Example config:

This role is enabled on all systems as part of the basic ansible managed
steps.

Users are added to the user database file, usually located at vars/userdb.yml

```
johnqc:
  access:
    host_groups:
      bastion:
        a_hostgroup_name:
  authentication:
    htpasswd: $apr1$H7kIELxF$6hyrv6BRDw27lzI0piehp/
    ssh_key: ssh-ed25519 AZAAVejFgesEYabPEBxRdyCQRLbTZ8WUsfDhOenfyGbFQPZz5f+NYapEr/iP6QAJKog
    password: $6$ScIUiXlbeHTaASpp$KlpG.PgYCbnNk9X0.J1F554.H7lNG2RkIJF8pvtNHAONb/9EInWB8q2acPdTpUL9/BvSDKD834xVYx0OKJChF1
  comment: John Citizen
  host_groups:
    linux:
  uid: 1019
  unix_groups:
    sudo:
```

NOTE: The UID must be kept be unique!  The linter script "lint_userdb.py" can
be used to check this constraint.

The example above is suitably chosen to not collide with any system or default
user accounts.  The user ids normally start at 1000, so using uids that are
1020 and above will also not collide with most systems that have had some
manual users created.

### Access

All the settings related to which systems/groups/services the user will be
able to access are grouped together under this one section.

#### account

The user account will only exist on hosts that are members of one (or more) of
these host groups.  This may result in accounts being removed.

Note that the ansible "all" group is a virtual group and will not match
anything, so you will always need to use more granular groups.

#### removable

This is a boolean value (default: True)  It controls if the users role will be
allowed to remove this user.

This is used for users that are intended for internal or system functions, but
due to various limitations might have been added to the userdb.

#### ssh_key

A list of host groups that the user's ssh keys are eligible for installing on.
Note that the user must also have an account (see above) on the host before
the presence of a ssh_key access will have any effect.

This setting is also used when the userdb is used to create system accounts,
as those users would have an account but no ssh keys based access.

### Authentication

All the settings related to authentication are grouped together under in one
section.

#### ssh_key

Choose one:

- Statically define ssh_key(s) in the userdb file by setting the ssh_key
  variable as seen in the example above (for multiple keys, use a multi-line
  string)

- Have the automation find the user's keys on github, allowing the user to
  self-service.  Set the ssh_key to the string "github" and also set the
  variable "authentication.github_user".  When choosing this option DO NOT
  specify the user's public key.

```
johnqc:
  authentication:
    github_user: johnqcitizen
    ssh_key: github
  comment: John Citizen
  uid: 1020
```

Note that downloading from github can cause slowness if github is slow and may
show lots of churn in the deltas deployed if people regularly change their
github key(s).

There is also a security concern that it is delegating a core part of the
permission control to a third party service - one that has no agreement with
us to provide reliability.

Thus, it is recommended that core team members use static ssh_key definitions.

#### password

No user will login to the box with a password - only ssh keys are used to
start a new remote session.

However, if the user is prompted for a password for sudo actions, their userdb
entry can define their own personal password for this.  Only the one-way-hash
of the password is stored in this file.

To generate the crypted password:
```
sudo apt-get -y install openssl
openssl passwd -6
```

Note that since these crypted passwords have a random salt, invoking the
mkpasswd command twice with the same password will result in two different
crypted strings.

#### passwords

Instead of using the single password above, a passwords dictionary containing
a hostname and the crypted password as the value will be used if there is a
matching hostname.

### linger

This setting defaults to `false`, but can be changed by adding it to the
user definition.

If `true`, the systemd loginctl linger status will be enabled for this user.

### unix_groups

If given, the unix_groups variable is a list of the unix groups on the remote
machines that this user account will be a member of.

This group needs to be one that exists.  This is either because it is a
standard group name, or because the unix_groupdb has created it (See below)

One important group is "sudo", without this group, the user will not be able
to even attempt to run root commands with sudo.

Note: the user will be a member of the same groups on /every/ system.

## Groups

To allow groups to be used for permissions controls, this role will also load
the group database file, usually located at `vars/unix_groupdb.yml`

This file is a simple list of the group names to be created.  The gid will be
allocated and managed by the remote system from the "system" range of group
IDs.  This is the same method used by packages when they need to create groups
for their functioning.  It is not anticipated that we will need to keep the
group IDs consistent between multiple hosts - if so, this role will be
revisited.

The only option is "state", which may be "present" (the default) or "absent"
to remove a group.

example:
```
team_example:
  state: absent
team_clowns:
```
