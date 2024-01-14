from src.core.exceptions.sycococopyexception import SycococopyException

'''
The RoleMismatchException is raised when the defined roles do not match with the roles used in the
protocol. Provides a message to indicate if defined roles were not used and/or if roles in the
protocol were not declared.
'''
class RoleMismatchException(SycococopyException):

    def __init__(self, used_roles: set[str], defined_roles: set[str]):
        self.surplus_defined_roles: set[str] = defined_roles.difference(used_roles)
        self.surplus_used_roles: set[str] = used_roles.difference(defined_roles)
        
    def __str__(self) -> str:
        message: str = "\nROLE MISMATCH DETECTED!\n" 
        if len(self.surplus_defined_roles) > 0:
            message += "You defined the following roles that were not used:\n"
            for surplus_role in self.surplus_defined_roles:
                message += f"\t{surplus_role}\n"
        if len(self.surplus_used_roles) > 0:
            message += "You used the following roles that were not defined:\n"
            for surplus_role in self.surplus_used_roles:
                message += f"\t{surplus_role}\n"
        return message        
