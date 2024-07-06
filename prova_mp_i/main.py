from prova_mp_i.config.database import get_db
from prova_mp_i.repository.usuario_repository import UsuarioRepository
from prova_mp_i.domain.model.models import Usuario


def main():
    with get_db() as session:

        usuario_repository = UsuarioRepository(session=session)

        user_data = {
            'name': 'John Doe',
            'email': 'email@email.com',
            'phone': '1199999999',
            'password': '123123',
            'cpf': '12312312312',
        }

        # CREATE
        user_to_create = Usuario(**user_data)
        user = usuario_repository.create(user_to_create)

        user_id = user.id
        print(f'User created with id: {user_id}')

        # READ
        user_read = usuario_repository.read(user_id=user_id)
        print(f'user read: {user_read}')

        # UPDATE
        user_update_data = {"name": "Novo nome"}
        user_updated = usuario_repository.update(user_id=user_id, **user_update_data)
        print(f'user updated: {user_updated}')

        # DELETE
        # user_deleted_id = usuario_repository.delete(user_id)
        # print(f'user deleted with id: {user_deleted_id}')


if __name__ == '__main__':
    main()
