from rolepermissions.roles import AbstractUserRole # type: ignore

class People(AbstractUserRole):
    available_permissions ={
    'make_transfer': True,
    'receive_transfer': True,
    } 