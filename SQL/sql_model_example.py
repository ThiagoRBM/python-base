#!/usr/bin/env python3

#  Exemplo do sql alchemy com sql model

from sqlmodel import SQLModel, Field, create_engine, Session, select, Relationship
# SQLModel é uma subclasse do declarative_base do sql alchemy
# ao mesmo tempo ela é uma BaseModel do pydantic
from typing import Optional

# We have to monkey patch this attributes
# https://github.com/tiangolo/sqlmodel/issues/189
from sqlmodel.sql.expression import Select, SelectOfScalar

SelectOfScalar.inherit_cache = True  # type: ignore
Select.inherit_cache = True  # type: ignore


class Person(SQLModel, table=True):
    #  table = True substitui o __tablename__ =  "person"
    id: Optional[int] = Field(default=None, primary_key=True)
    #  ao invés de Column como no sql alchemy puro, usa type annotations
    #  do typing. Deixando como optional.
    name: str
    #  aspas abaixo porque a classe Balance foi criada abaixo e aqui ela é
    #  usada. Com anotação de tipo é possível resolver isso com as aspas
    #  "atributo virtual"
    balance: "Balance" = Relationship(back_populates="person")


class Balance(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    value: int
    #  abaixo, criando o relacionamento
    person_id: int = Field(foreign_key="person.id")
    # "atributo virtual"
    person: Person = Relationship(back_populates="balance")


engine = create_engine("sqlite:///database_sql_model.db", echo=False)
# usando o do SQLModel que sabe interpretar type annotation

SQLModel.metadata.create_all(bind=engine)

with Session(engine) as session:
    ...
    # #  adicionando pessoas e comentando para nao adicionar multiplas vezes
    # # person = Person(name="thiago")
    # # session.add(person)
    # #
    # # person = Person(name="fulano")
    # # session.add(person)
    # #
    # # session.commit()
    # # SELECT FROM PERSON WHERE person.name = "thiago";
    # # sql = select(Person).where(Person.name == "thiago")
    # sql = select(Person)
    # #  print(sql)
    # results = session.exec(sql)  # exec sabe anotação de tipos
    # #  print(results)
    # for person in results:
    # balance = Balance(value=60, person=person)
    # print(balance)
    # session.add(balance)
    # session.commit()
    ### FAZENDO JOINS
    sql = select(Person)
    results = session.exec(sql)
    for person in results:
        print(person.name, person.balance)
        print(person.name, person.balance[0].value)
    print("*" * 20)

    sql = select(Balance).where(Balance.value > 3)
    results = session.exec(sql)
    for balance in results:
        print(balance.person.name, balance.value)
    print("*" * 20)

    sql = select(Person, Balance).where(Balance.person_id == Person.id)
    results = session.exec(sql)  # agora tuplas são retornadas
    for person, balance in results:
        print(person.name, balance.value)
    print("*" * 20)

    sql = select(Person, Balance).join(Balance, isouter=True)  #  left join
    print(f"comando sql:\n{sql}")  #  vendo o comando que roda por trás
    #  esse comando dá para copiar e colar no SQL
    print()
    results = session.exec(sql)
    for person, balance in results:
        print(person.name, balance.value)
    print("*" * 20)
