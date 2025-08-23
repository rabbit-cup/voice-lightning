def max_data_len(data):
    """Ищет максимальную данную и считывает её длину
    data: масив данных"""
    data_one = 0
    for i in data:
        data_twu = len(i)
        if data_one < data_twu:
            data_one = data_twu
    return data_one