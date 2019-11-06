from wlts import wlts

service = wlts("http://0.0.0.0:5000/wlts/")

# Retorna todas as coleções de dados disponíveis
collections_list = service.list_collections()

# Exemplo de Retorno

{
  "collections":[
    "prodes",
    "deter_amz",
    "deterb_amz",
    "terraclass",
    "mapbiomas"
  ]
}


for collection_name in collections_list["collections"]:
    print(collection_name)

# Outra possibilidade é retornar separado (feature_collection e image_collection) (neste caso é necessário dois -for- para percorrer as coleções )

# {
#   "feature_collection": [
#     "string"
#   ],
#   "image_collection": [
#     "string"
#   ]
# }
#

# Retorna todas as coleções de dados do tipo feature_collection disponível
collections = service.list_collections(collection_type="feature_collection")

# {
#   "feature_collection": [
#     "string"
#   ]
# }

{
  "collections":[
    "prodes",
    "deter_amz",
    "deterb_amz",
    "terraclass"
  ]
}

# Retorna o describe de uma coleção
collection_describe = service.describe_collection("prodes")

print(collection_describe['description'])

print(collection_describe['period']['start_date'])
print(collection_describe['period']['end_date'])

# Informações do sistema de classificação associado a uma coleção.
print(collection_describe['classification_system_class']['classification_system'])

# Retorna todas as classes da coleção
for class_name in collection_describe['classification_system_class']['class_name']:
    print(class_name)


# Exemplos da operação de trajetória. Parâmetros obrigatórios: latitude e longitude

# Retorna a trajetória de todas as coleções que possuem interseção com a coordenada informada.
# Por padrão o parâmetro  class_type = original.

# http://0.0.0.0:5000/wlts/trajectory?latitude=-60.658&longitude=-12.3975
trajectory_a = service.trajectory(latitude=-60.658, longitude=-12.3975)

# Retorno do serviço
{"query":{"class_type":null,"collections":null,"end_date":null,"latitude":-60.658,"longitude":-12.3975,"start_date":null},
"result":{"trajectory":[{"classification_class":"Floresta","collection_name":"terraclass","data":"2004"},
{"classification_class":"Floresta","collection_name":"terraclass","data":"2008"},{"classification_class":"Floresta","collection_name":"terraclass","data":"2010"},
{"classification_class":"Floresta","collection_name":"terraclass","data":"2012"},{"classification_class":"Floresta","collection_name":"terraclass","data":"2014"},
{"classification_class":"Cicatriz de Queimada","collection_name":"deterb_amz","data":"2017-09-13Z"}]}}

# Retorno do Cliente

   classification_class collection_name         data
0              Floresta      terraclass  2004-01-01
1              Floresta      terraclass  2008-01-01
2              Floresta      terraclass  2010-01-01
3              Floresta      terraclass  2012-01-01
4              Floresta      terraclass  2014-01-01
5  Cicatriz de Queimada      deterb_amz  2017-09-13


# http://0.0.0.0:5000/wlts/trajectory?latitude=-60.658&longitude=-12.3975&collections=terraclass
trajectory_b = service.trajectory(collections=["terraclass"], latitude=-60.658, longitude=-12.3975)

# http://0.0.0.0:5000/wlts/trajectory?latitude=-60.658&longitude=-12.3975&collections=deterb_amz,terraclass&start_date=2000-02-18&end_date="2014-12-31"
trajectory_c = service.trajectory(collections=["terraclass", "deterb_amz"], latitude=-60.658, longitude=-12.3975, start_date="2000-02-18", end_date="2014-12-31")


# http://0.0.0.0:5000/wlts/trajectory?latitude=-60.658&longitude=-12.3975&class_type=map
trajectory_a = service.trajectory(latitude=-12.0, longitude=-54.0)
