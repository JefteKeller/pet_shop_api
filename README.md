# ***Keller Pet***

## *Keller Pet* é uma plataforma para ajudar donos de PetShop a guardar dados de animais

>***
> Esta API web foi implementada com Django e Django Rest Framework.
>***

## Rotas disponíveis na API

`POST /animals/` - Dados de envio para cadastro de um animal:

``` Text
# REQUEST
{
    "name": 
    "Bidu",
    "age": 1,
    "weight": 30,
    "sex": "macho",
"group": {
    "name": "cao",
    "scientific_name": "canis familiaris"
},
"characteristic_set": [
    {
    "characteristic": "peludo"
    },
    {
    "characteristic": "medio porte"
    }
  ]
}
```

Resposta desse request incluindo informações sobre o `Grupo` e as `Características` do animal.

``` Text
// RESPONSE STATUS -> HTTP 201
{
  "id": 1,
  "name": "Bidu",
  "age": 1.0,
  "weight": 30.0,
  "sex": "macho",
  "group": {
    "id": 1,
    "name": "cao",
    "scientific_name": "canis familiaris"
  },
  "characteristic_set": [
    {
      "id": 1,
      "characteristic": "peludo"
    },
    {
      "id": 2,
      "characteristic": "medio porte"
    }
  ]
}
```


`GET /animals/` - Não é necessário enviar nenhuma informação para essa requisição.

```Text
# RESPONSE STATUS -> HTTP 200
[
  {
    "id": 1,
    "name": "Bidu",
    "age": 1.0,
    "weight": 30.0,
    "sex": "macho",
    "group": {
      "id": 1,
      "name": "cao",
      "scientific_name": "canis familiaris"
    },
    "characteristic_set": [
      {
        "id": 1,
        "characteristic": "peludo"
      },
      {
        "id": 2,
        "characteristic": "medio porte"
      }
    ]
  },
  {
    "id": 2,
    "name": "Hanna",
    "age": 1.0,
    "weight": 20.0, 
    "sex": "femea",
    "group": {
      "id": 2,
      "name": "gato",
      "scientific_name": "felis catus"
    },
    "characteristic_set": [
      {
        "id": 1,
        "characteristic": "peludo"
      },
      {
        "id": 3,
        "characteristic": "felino"
      }
    ]
  }
]
```

`GET /animals/<int:animal_id>/` - Filtrando animais pelo `animal_id` enviado pela URL.

``` Text
// RESPONSE STATUS -> HTTP 200
  {
  "id": 1,
  "name": "Bidu",
  "age": 1.0,
  "weight": 30.0,
  "sex": "macho",
  "group": {
    "id": 1,
    "name": "cao",
    "scientific_name": "canis familiaris"
  },
  "characteristic_set": [
    {
      "id": 1,
      "characteristic": "peludo"
    },
    {
      "id": 2,
      "characteristic": "medio porte"
    }
  ]
}
```

`DELETE /animals/<int:animal_id>/` - Passamos o `animal_id` do animal que queremos deletar do nosso Banco de Dados.

``` Text
# RESPONSE STATUS -> HTTP 204 (no content)
```

>***
> Não há corpo de resposta para a solicitação de `DELETE`.
>***
