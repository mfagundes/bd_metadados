""" Imports que serão necessários no futuro
from ninja.security import APIKeyQuery
from ninja import Router
from typing import List
from django.contrib.auth import get_user_model

Importar modelos
from django.shortcuts import get_object_or_404

O código abaixo é uma evolução do autor do vídeo, que ainda não foi utilizado no projeto
    router_api = Router()

Está presente apenas para referência futura
class ApiKey(APIKeyQuery):
    param_name = "api_key"

    def authenticate(self, request, key):
        try:
            return Client.objects.get(key=key)
        except Client.DoesNotExist:
            pass


"""
from ninja import NinjaAPI, Schema

api = NinjaAPI(
    version="0.1.0",
    csrf=True,
    title="API",
    description="API do projeto",
    urls_namespace="public_api",
)


class HelloSchema(Schema):
    name: str = "World"


class UserSchema(Schema):
    id: int
    username: str
    email: str
    first_name: str
    last_name: str


class Error(Schema):
    message: str


@api.post("/hello")
def hello(request, data: HelloSchema):
    return {"message": f"Hello {data.name}"}


@api.get("/me", response={200: UserSchema, 403: Error})
def me(request):
    if not request.user.is_authenticated:
        return 403, {"message": "Please sign in first"}
    return request.user
