from wlts import wlts

service = wlts("http://localhost")

datasets = service.list_datasets()

