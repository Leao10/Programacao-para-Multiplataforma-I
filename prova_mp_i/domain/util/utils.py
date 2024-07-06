import re


class Validate:

    @staticmethod
    def cpf(cpf):
        cpf_pattern = re.compile(r'^(\d{3}\.\d{3}\.\d{3}-\d{2}|\d{11})$')
        if not cpf_pattern.match(cpf):
            raise ValueError('CPF must be in the format XXX.XXX.XXX-XX or XXXXXXXXXXX')
        return cpf

    @staticmethod
    def phone(phone):
        phone_pattern = re.compile(r'^(\d{10,11}|\(\d{2}\)\d{8,9}|\(\d{2}\)\d{4,5}-\d{4})$')
        if not phone_pattern.match(phone):
            raise ValueError('Phone number must have 10 or 11 digits')
        return phone