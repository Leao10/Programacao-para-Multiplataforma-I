import logging
from fastapi import HTTPException
from pydantic import TypeAdapter
from sqlalchemy.exc import IntegrityError

from prova_mp_i.domain.dto.dtos import UsuarioCreateDTO, UsuarioDTO, UsuarioUpdateDTO
from prova_mp_i.domain.model.models import Usuario
from prova_mp_i.repository.usuario_repository import UsuarioRepository

logger = logging.getLogger('fastapi')

class UsuarioService:

    def __init__(self, usuario_repository: UsuarioRepository):
        self.usuario_repository = usuario_repository

    def create(self, user_data: UsuarioCreateDTO) -> UsuarioDTO:
        self.logger.info('Criando um novo usuario')
        user = Usuario(**user_data.model_dump())
        try:
            created = self.usuario_repository.save(user)
            return TypeAdapter(UsuarioDTO).validate_python(created)
        except IntegrityError as e:
            self.logger.error(f'Erro ao criar o usuário: {user_data.model_dump()}', e)
            raise HTTPException(status_code=409, detail=f'Usuario ja existe na base: {e.args[0]}')

    def read(self, user_id: int) -> UsuarioDTO:
        self.logger.info('Buscando um usuario')
        return TypeAdapter(UsuarioDTO).validate_python(self._read(user_id))

    def _read(self, user_id: int) -> Usuario:
        user = self.usuario_repository.read(user_id)
        if user is None:
            raise HTTPException(status_code=404, detail=f'Usuário {user_id} não encontrado.')
        return user

    def find_all(self) -> list[UsuarioDTO]:
        self.logger.info('Buscando todos os usuarios')
        users = self.usuario_repository.find_all()
        return [TypeAdapter(UsuarioDTO).validate_python(user) for user in users]

    def update(self, user_id: int, user_data: UsuarioUpdateDTO):
        user = self._read(user_id)
        user_data = user_data.model_dump(exclude_unset=True)
        for key, value in user_data.items():
            setattr(user, key, value)
        user_updated = self.usuario_repository.save(user)
        return TypeAdapter(UsuarioDTO).validate_python(user_updated)

    def delete(self, user_id: int) -> int:
        user = self._read(user_id)
        self.usuario_repository.delete(user)
        return user_id
