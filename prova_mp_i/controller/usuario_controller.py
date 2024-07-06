from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from prova_mp_i.config.database import get_db
from prova_mp_i.domain.dto.dtos import UsuarioDTO, UsuarioCreateDTO
from prova_mp_i.repository.usuario_repository import UsuarioRepository
from prova_mp_i.service.usuario_service import UsuarioService

user_router = APIRouter(prefix='/users', tags=['Users'])

def get_user_repo(session: Session = Depends(get_db)):
    return UsuarioRepository(session=session)

@user_router.post('/', status_code=201, description='cria um novo usuario', response_model=UsuarioDTO)
async def create (request: UsuarioCreateDTO, user_repo: UsuarioRepository = Depends(get_user_repo)):
    usuario_service = UsuarioService(user_repo)
    return usuario_service.create(request)

