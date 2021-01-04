from typing import Callable
from fastapi import Depends
from pydantic import BaseModel

from . import CRUDGenerator, NOT_FOUND

# TODO:
# try:
#     from databases.core import Database
#     from sqlalchemy.sql.schema import Table
# except ImportError:
#     databases_installed = False
# else:
#     databases_installed = True


class MongoCRUDRouter(CRUDGenerator):

    # TODO: type hinting
    def __init__(self, schema: BaseModel, collection, *args, **kwargs):
        # assert databases_installed, "Databases and SQLAlchemy must be installed to use the DatabasesCRUDRouter."
        self.collection = collection

        # TODO:
        # if 'prefix' not in kwargs:
        #     kwargs['prefix'] = table.name
        #
        # if 'create_schema' not in kwargs:
        #     kwargs['create_schema'] = self.schema_factory(schema, self._pk)

        super().__init__(schema, *args, **kwargs)

    def _get_all(self) -> Callable:
        async def route():
            cursor = self.collection.find({})
            res = []
            print(cursor)
            async for o in cursor:
                res.append(o)

            print(res)
            return res

            # return [o async for o in cursor]

        return route

    def _get_one(self) -> Callable:
        async def route(item_id):
           pass

        return route

    def _create(self) -> Callable:
        async def route(schema: self.create_schema):
            pass

        return route

    def _update(self) -> Callable:
        async def route(item_id: int, schema: self.schema):
            pass

        return route

    def _delete_all(self) -> Callable:
        async def route():
            pass

        return route

    def _delete_one(self) -> Callable:
        async def route(item_id: int):
            pass

        return route
