This role provides a base set of configuration that is expected on all
systems.

Nothing in here is configurable - if it needed configuration, it would be in
its own role

NOTE: this role is named with an `aa` so as to ensure it sorts before other
roles.

## hostname

- Ensures that the system hostname matches the inventory hostname
- Adds an entry to /etc/hosts for the hostname

## fix vim

The default config packaged with vim for some years now has configured a mouse
mode that is widely regarded as a bad idea.
 
For systems that inherit this Debian config, we turn off the mouse mode by
default - any individual user can turn it back on again if they want.
 

