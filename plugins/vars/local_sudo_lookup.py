import os
import subprocess

from ansible.errors import AnsibleParserError
from ansible.plugins.vars import BaseVarsPlugin
from ansible.inventory.host import Host


class VarsModule(BaseVarsPlugin):
    """
    Ansible provides no sane way to build an environment that allows you to
    lookup a per-host become password from an external password manager.
    """

    def get_vars(self, loader, path, entities):
        script_name = os.environ.get("LOCAL_SUDO_LOOKUP")
        if not script_name:
            # If we dont have the required config variable, do nothing
            return {}

        # TODO:
        # - in the reference ansibple source, it converts entities to a list
        #   before calling super.  Is this needed?

        super(VarsModule, self).get_vars(loader, path, entities)

        # TODO:
        # - When is the entity a list and when is it not a list?
        #       - seen so far: a list of the groups about to be managed
        # - handle this better

        if isinstance(entities, list):
            hosts = []
            for entity in entities:
                if isinstance(entity, Host):
                    hosts.append(entity)

            if len(hosts) == 0:
                return {}

            if len(hosts) > 1:
                print("hosts:", hosts)
                raise AnsibleParserError("lookup handed too many host entries")

            host = hosts[0]
        else:
            host = entities

        # TODO
        # - skip if this entity already has a ansible_become_pass set

        data = {}
        try:
            out = subprocess.check_output(
                [script_name, '--sudo', '^' + host.name + '$'])
            data['ansible_become_pass'] = out.decode('utf8').strip('\n')
        except subprocess.CalledProcessError:
            pass

        return data
