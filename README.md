# File Manager system linked to an account

# Definir MVP
- Register account
- Login account
- Upload files
- Download Upload files
- Delete Upload files
- Change File Name

# Blocks & Components Diagram 

## Core
- Dependency Injection
    - DependencyInjectionBridge

- Get Environment Variables
    - EnvironmentVariablesProvider

## Database
- Create Database
    - DatabaseFactory

- Execute Query
    - DatabaseExecutorProvider

## Account
- Register Account
    - UserRepository

- Login Account
    - UserRepository

- Auth Account
    - UserRepository

## Files
- Upload File
    - FilesRepository

- Download File
    - FilesRepository

- Delete File
    - FilesRepository

- Change FileName
    - FilesRepository


## Email
- Build verification email
    - EmailBuildProvider

- Send verification email
    - EmailSenderProvider

# Project Base

## [Software Architecture](https://github.com/PheFreire/Software-Architecture-Concepts)
- [Hexagonal Achitecture](https://github.com/PheFreire/Hexagonal-Architecture-Concepts)

## Local Modularization
- Business Rule - Hexagonal Architecture Nomeclature - Script
- Exemple: src/domain/services/**account/repositories/user_repository.py**

## Tests
- Unit Teste
    - [unittest](https://docs.python.org/3/library/unittest.html)
    - [PyTest](https://docs.pytest.org/en/8.0.x/)

## Programming Language
- [Python^3.11](https://www.python.org/doc/)
- High Level | Dynamic | Interpreted | Object Oriented | Programming Language

# EntryPoints
- [FastAPI](https://fastapi.tiangolo.com/)

## Project Manager System
- [Poetry](https://python-poetry.org/)

## Database and ORM
- [PostgreSQL](https://www.postgresql.org/docs/)
- [PsycoPG](https://www.psycopg.org/)
