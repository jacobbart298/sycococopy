class RoleMismatchException(Exception):

    def __init__(self, used_roles, defined_roles):
        used_roles = used_roles
        defined_roles = defined_roles

        self.surplus_defined_roles = defined_roles.difference(used_roles)
        self.surplus_used_roles = used_roles.difference(defined_roles)
        
    def __str__(self):
        message = "" 
        if len(self.surplus_defined_roles ) > 0:
            message += "You defined the following roles that were not used:\n"
            for surplus_role in self.surplus_defined_roles:
                message += f"\t{surplus_role}\n"
        if len(self.surplus_used_roles) > 0:
            message += "You used the following roles that were not defined:\n"
            for surplus_role in self.surplus_used_roles:
                message += f"\t{surplus_role}\n"

        return message        
        