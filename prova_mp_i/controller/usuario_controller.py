from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from prova_mp_i.config.database import get_db
from prova_mp_i.domain.dto.dtos import UsuarioDTO, UsuarioCreateDTO, UsuarioUpdateDTO
from prova_mp_i.repository.usuario_repository import UsuarioRepository
from prova_mp_i.service.usuario_service import UsuarioService

user_router = APIRouter(prefix='/users', tags=['Users'])

def get_user_repo(session: Session = Depends(get_db)):
    return UsuarioRepository(session=session)

@user_router.post('/', status_code=201, description='cria um novo usuario', response_model=UsuarioDTO)
async def create (request: UsuarioCreateDTO, user_repo: UsuarioRepository = Depends(get_user_repo)):
    usuario_service = UsuarioService(user_repo)
    return usuario_service.create(request)

@user_router.get('/{user_id}', status_code=200, description='Buscar o usuario por id', response_model=UsuarioDTO)
async def find_by_id (user_id: int, user_repo: UsuarioRepository = Depends(get_user_repo)):
    usuario_service = UsuarioService(user_repo)
    return usuario_service.read(user_id=user_id)

@user_router.get('/', status_code=200, description='Buscar todos os usuarios', response_model=list[UsuarioDTO])
async def find_all (user_repo: UsuarioRepository = Depends(get_user_repo)):
    usuario_service = UsuarioService(user_repo)
    return usuario_service.find_all()

@user_router.put('/{user_id}', status_code=200, description='Atualizar um usuario', response_model=UsuarioDTO)
async def update (user_id: int, user_data: UsuarioUpdateDTO, user_repo: UsuarioRepository = Depends(get_user_repo)):
    usuario_service = UsuarioService(user_repo)
    return usuario_service.find_all()

@user_router.delete('/{user_id}', status_code=204, description='Deletar o usuario por id')
async def delete (user_id: int, user_repo: UsuarioRepository = Depends(get_user_repo)):
    usuario_service = UsuarioService(user_repo)
    usuario_service.delete(user_id=user_id)