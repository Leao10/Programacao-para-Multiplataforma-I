from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import Session, relationship

from prova_mp_i.config.database import Base, engine


class Usuario(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(50))
    email = Column(String(50))
    password = Column(String(50))
    cpf = Column(String(11))
    phone = Column(String(11))

    endereco_id = Column(Integer, ForeignKey('enderecos.id', ondelete='CASCADE'))
    endereco = relationship('Endereco', back_populates='usuario', uselist=False)

    

    def __repr__(self):
        return f'<User(id={self.id}, name={self.name}, email={self.email}, password={self.password}, cpf={self.cpf}, phone={self.phone}, endereco={self.endereco})>'


class Endereco(Base):
    __tablename__ = 'enderecos'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    cep = Column(String(8))
    logradouro = Column(String(100))
    numero = Column(String(10))
    complemento = Column(String(50))
    bairro = Column(String(50))
    cidade = Column((String(50)))
    estado = Column(String(2))
    usuario = relationship('Usuario', back_populates='endereco', uselist=False)

    @staticmethod
    def create(session: Session, **kwargs):
        endereco = Endereco(**kwargs)
        session.add(endereco)
        session.commit()
        session.refresh(endereco)
        return endereco

    @staticmethod
    def update(session: Session, endereco_id: int, **kwargs):
        endereco = Endereco.read(session, endereco_id)
        if endereco:
            for key, value in kwargs.items():
                setattr(endereco, key, value)
            session.commit()
            session.refresh(endereco)
        return endereco

    @staticmethod
    def delete(session: Session, user_id: int):
        endereco = Endereco.read(session, user_id)
        if endereco:
            session.delete(endereco)
            session.commit()
        return user_id

    @staticmethod
    def read(session: Session, user_id: int):
        return session.query(Endereco).filter(Endereco.id == user_id).first()

    def __repr__(self):
        return f'<Endereco(id={self.id}, cep={self.cep}, logradouro={self.logradouro}, numero={self.numero}, complemento={self.complemento}, bairro={self.bairro}, cidade={self.cidade}, estado={self.estado})>'


Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)
