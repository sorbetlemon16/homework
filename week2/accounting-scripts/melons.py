melon_names = {
    1: 'Honeydew',
    2: 'Crenshaw',
    3: 'Crane',
    4: 'Casaba',
    5: 'Cantaloupe',
}

melon_prices = {
    1: 0.99,
    2: 2.00,
    3: 2.50,
    4: 2.50,
    5: 0.99,
}

melon_seedlessness = {
    1: True,
    2: False,
    3: False,
    4: False,
    5: False,
}

melons = {}
for key, name in melon_names.items():
    melons[name] = {
        'seedless': melon_seedlessness[key],
        'price': melon_prices,
        'flesh_color': None,
        'weight': None,
        'rind_color': None
    }
