from prova_mp_i.config.database import get_db
from prova_mp_i.domain.dto.dtos import UsuarioCreateDTO, UsuarioUpdateDTO
from prova_mp_i.repository.usuario_repository import UsuarioRepository
from prova_mp_i.domain.model.models import Usuario
from prova_mp_i.service.usuario_service import UsuarioService


def main():
    with get_db() as session:

        usuario_repository = UsuarioRepository(session=session)
        usuario_service = UsuarioService(usuario_repository)

        # CREATE
        usuario_create_dto = UsuarioCreateDTO(
            name="John Doe",
            email="emiil@email.com",
            password="123123",
            cpf="12312312312",
            phone="11999999999"
        )
        user_to_create = usuario_service.create(usuario_create_dto)

        user_id = user_to_create.id
        print(f'User created with id: {user_id}')

        # READ
        user_read = usuario_service .read(user_id=user_id)
        print(f'user read: {user_read}')

        # UPDATE
        user_update_data = UsuarioUpdateDTO(
            name="John Doe",
            email="emiil@email.com",
            password="123123",
            cpf="12312312312",
            phone="11999999999"        
        )
        user_updated = usuario_repository.update(user_id=user_id, user_data=user_update_data)
        print(f'user updated: {user_updated}')

        # DELETE
        #user_deleted_id = usuario_repository.delete(user_id)
        #print(f'user deleted with id: {user_deleted_id}')


if __name__ == '__main__':
    main()
