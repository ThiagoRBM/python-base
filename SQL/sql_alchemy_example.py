#!/usr/bin/env python3

# Ele se conecta a postgres, oracle, mysql e outros bancos relacionais.

# funcao que faz "metaprogramação". Retorna classes e objetos. É uma ORM.
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base(
)  # factory function, funcao que cria objetos. Ela cria a base internamente. declarative_base é a base model das classes


class Person(Base):
    __tablename__ = "person"  # nome da tabela no arquivo.db
    # sql alchemy é antigo e muito usado. Então ainda não tem anotações de tipo novo
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(255))  # str de tamanho 255 no banco de dados

    def __str__(self):
        return self.name.upper(
        )  # método para mostrar o nome na linha de query lá embaixo (l ~ 73)


class Balance(Base):
    __tablename__ = "balance"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    value = Column(Integer, nullable=False)  # NOT NULL no sql

    person_id = Column(
        Integer, ForeignKey(Person.id)
    )  # conectando com a foregn key (do Person), é criada uma coluna que equivale à tabela estrangeira
    person = relationship(
        'Person', foreign_keys='Balance.person_id'
    )  # cria o relacionamento da tabela balance com a tabela Person


# nome padrão do sql alchemy para conectar no banco de dados
engine = create_engine(
    "sqlite:///database_sql_alchemy.db"
)  # no sql alchemy é preciso especificar qual o tipo de db será conectado e a maneira de fazer isso é com esse prefixo sqlite:///, ex: mysql://localhost:3662@user:senha. Chama "connections string".

#  cria as tabelas com base nas subclasses de Base criadas. Para o SQLite, pode ser usada a ferramenta DB Browser for SQLite (só funciona no sqlite)
Base.metadata.create_all(bind=engine)

# objeto session se conecta com uma seção de banco de dados. Ela controla quem acessa e as transações (que depois são comitadas). Sessão de interação com o banco de dados

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# autocommit: commits automáticos, autoflush: limpa o histórico depois do commit, é bom conseguir ver o histórico, bind: engine

session = SessionLocal()  # classe cirada acima

## ADICIONANFO INFORMACOES (ESTA COMENTADO PARA NAO ADICIONA MAIS TODAS VEZ QUE O SCRIPT RODAR)

# person = Person(name="Fulano")  # adicionando uma pessoa, SEM SER COMMITADO
#
# session.add(
# person
# )  # adicionou a pessoa ao session que vai rodar internamente INSERT INTO PERSON (NAME) values ('Fulano') , que é o formato de query usado no sql
#
# person = Person(name="Ciclano")
# session.add(person)
#
# session.commit()  # agora o commit é feito

## FAZENDO CONSULTA

# esse results equivale ao cursor do sqlite3
results = session.query(Person).filter(
    Person.name == "Ciclano"
)  # o comando é transformado na query sql padrão: WHERE person.name = "Ciclano" dá para ser composta com & e etc

for result in results:
    print(result, result.id)
    print("*" * 20)
    print()
    print()

## ADICIONANDO VALORES NA TABELA BALANCE
# comentado para não ficar adicionando repatidas vezes
#results = session.query(Person)  # pegando todas as pessoas
# for result in results:
# #  adicionando pontos para cada pessoa
# balance = Balance(value=40, person_id=result.id)
# session.add(balance)
# print(f"valor adicionado para {result.id}")
#
# session.commit()

## FAZENDO CONSULTA COM LEFT JOIN

results = session.query(
    Balance)  # aqui funciona porque o relationship foi criado lá em cima
for result in results:
    print(result.value, result.person.name)
print("*" * 20)

#  caso não haja relationship, outra maneira de fazer a mesma query. A diferença é que o resultado vem como tupla
results2 = session.query(Person.name, Balance.value).join(Balance,
                                                          isouter=True)
for result in results2:
    print(result)
print("*" * 20)

# uma outra maneira de fazer a mesma coisa

results3 = session.query(Person, Balance).join(Balance, isouter=True)
for result in results3:
    print(result)
    print(result[0].name, result[1].value)
print("*" * 20)
