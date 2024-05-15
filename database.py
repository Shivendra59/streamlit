from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey,
    Integer,
    LargeBinary,
    String,
    create_engine,
    func,
    Float,
)
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

engine = create_engine("postgresql://postgres:test@localhost:5432/demostreamtest")
Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    email = Column(String(255), unique=True, index=True)
    password = Column(String(255), index=True)
    role = Column(String(50))
    leaves = relationship("MyLeave", back_populates="user")
    balance_leave = relationship("BalanceLeave", uselist=False, back_populates="user")


class MyLeave(Base):
    __tablename__ = "leave"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    appiled_to = Column(String(255))
    cc = Column(String(255))
    reason = Column(String(255), index=True)
    leaveType = Column(String(50))
    leaveDuration = Column(String(50))
    applied_date = Column(DateTime, default=func.now())
    from_date = Column(DateTime, default=func.now(), onupdate=func.now())
    to_date = Column(DateTime, default=func.now(), onupdate=func.now())
    document = Column(LargeBinary, nullable=True)
    status = Column(String(50))
    action = Column(String(255))
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="leaves")


class BalanceLeave(Base):
    __tablename__ = 'balance_leave'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    leave_type = Column(String(50), unique=True)
    balance = Column(Float)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="balance_leave")

Session = sessionmaker(bind=engine)
session = Session()
