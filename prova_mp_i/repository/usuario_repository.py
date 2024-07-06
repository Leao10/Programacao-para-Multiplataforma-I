from sqlalchemy.orm import Session

from prova_mp_i.domain.model.models import Usuario

class IUserRepository():
    def create(self, user: object):
        raise NotImplementedError
    
    def read(self, user_id: int):
        raise NotImplementedError
    
    def update(self, user: object, user_data: dict):
        raise NotImplementedError
    
    def delete(self, user: object):
        raise NotImplementedError
    
    def find_all(self):
        raise NotImplementedError

class UsuarioRepository(IUserRepository):

    def __init__(self, session:Session):
        self.session = session


    def create(self, user = Usuario):
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        return user

    def update(self, user_id: int, **kwargs):
        user = self.read(user_id=user_id)
        if user:
            for key, value in kwargs.items():
                setattr(user, key, value)
            self.session.commit()
            self.session.refresh(user)
        return user

    def delete(self, user_id: int):
        user = self.read(user_id=user_id)
        if user:
            self.session.delete(user)
            self.session.commit()
        return user_id

    def read(self, user_id: int):
        return self.session.query(Usuario).filter(Usuario.id == user_id).first()
