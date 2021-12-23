params = {
    'city': 'zp',
    'street': 'rekbmk',
    'floor_num': '12',
    'room_amt': '1',
    'min_square_amt': '23',
    'max_square_amt': '35',
    'min_cost': '123414',
    'max_cost': '234445',
}


def remove_quotes(word: str):
    res = word.replace('"', '')
    res = res.replace("'", '')
    return res


def parse(params: dict):
    sql = 'select * from apartment '
    if params:
        sql += 'where '

    for k, v in params.items():
        if 'min' in k:
            name = k.lstrip('min_')
            sql += f"{name}>{v} and "
            continue
        if 'max' in k:
            name = k.lstrip('max_')
            sql += f"{name}<{v} and "
            continue

        sql += f"{k}='{v}' and "

    sql = sql.rstrip('and ')

    return sql


res = parse(params)
print(res)
