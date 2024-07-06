from pydantic import BaseModel, EmailStr, field_validator, ConfigDict, field_validatior

class UsuarioDTO(BaseModel):

    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    email: EmailStr
    password: str
    cpf: str
    phone: str


class UsuarioCreateDTO(BaseModel):

    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    email: EmailStr
    password: str
    cpf: str
    phone: str

    @field_validator('cpf')
    def validate_cpf(cls, cpf):
        

class UsuarioUpdateDTO(BaseModel):

    model_config = ConfigDict(from_attributes=True)

    id: Optional[int]
    name: Optional[str]
    email: Optional[EmailStr]
    password: Optional[str]
    cpf: Optional[str]
    phone: Optional[str]