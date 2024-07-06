from sqlalchemy.orm import Session

from prova_mp_i.domain.model.models import Usuario

class UsuarioRepository:

    def __init__(self, session: Session):
        self.session = session

    def save(self, user: Usuario):
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        return user

    def delete(self, user: Usuario):
        self.session.delete(user)
        self.session.commit()

    def read(self, user_id: int):
        return self.session.query(Usuario).filter(Usuario.id == user_id).first()

    def find_all(self):
        return self.session.query(Usuario).all()
