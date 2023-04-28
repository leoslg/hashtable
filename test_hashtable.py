from hash import hashtable

def test_create_ht():
    assert hashtable(size=100) is not None

def test_size_ht():
    assert len(hashtable(size=100)) == 100

def test_create_empty_values():
    assert hashtable(size=3).values == [None, None, None]

def test_insert_key_value_pairs():
    table = hashtable(size=100)

    table['hola'] = 'Hello'
    table[98] = 30  
    table[False] = True

    assert 'Hello' in hashtable.values
    assert 30 in hashtable.values
    assert True in hashtable.values