from typing import Optional

from prova_mp_i.domain.util.utils import Validate
from pydantic import BaseModel, EmailStr, ConfigDict, field_validator


class UsuarioDTO(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    email: EmailStr
    cpf: str
    phone: str

    @field_validator('cpf')
    def validate_cpf(cls, cpf):
        return Validate.cpf(cpf)

    @field_validator('phone')
    def validate_phone(cls, phone):
        return Validate.phone(phone)


class UsuarioCreateDTO(BaseModel):
    name: str
    email: EmailStr
    password: str
    cpf: str
    phone: str

    @field_validator('cpf')
    def validate_cpf(cls, cpf):
        return Validate.cpf(cpf)

    @field_validator('phone')
    def validate_phone(cls, phone):
        return Validate.phone(phone)


class UsuarioUpdateDTO(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None
    phone: Optional[str] = None

    @field_validator('phone')
    def validate_phone(cls, phone):
        return Validate.phone(phone)
