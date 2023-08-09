UserFiltrationWithoutSQL
===========

This API is intended for users who do not know sql or know it at an absolute minimum level, it allows you to interact with the database


**TODO**
~~~~
More features are coming soon.

- API transition from synchronous to asynchronous.
- JWT Authorization.
- Test coverage.
- Basic CRUD operations.
- Redis.
- Dockerfile.
~~~~

Basic Usage
-----------
1)Сreate an .env file (example in .env.example).

2)Create your DB(PostgreSQL).

3)Run migrations.

`>>> alembic init migrations`

3)Insert your path to DB into **alembic.ini**

`>>>alembic revision --autogenerate -m "first_migration"
`

Instead of _'first_migration'_ type your migration name, it can be anything.

4)Upgrade migrations to current.

`>>>alembic upgrade heads`