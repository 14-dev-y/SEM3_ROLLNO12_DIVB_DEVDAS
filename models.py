models = [
    {'make': 'Nokia', 'model': 21, 'color': 'Black'},
    {'make': 'Mi Max', 'model': 20, 'color': 'Gold'},
    {'make': 'Samsung', 'model': 17, 'color': 'Blue'}
]

models.sort(key=lambda phone: phone['model'])
print(models)
