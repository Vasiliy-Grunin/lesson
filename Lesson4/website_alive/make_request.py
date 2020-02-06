def foo_answer(s):
    # проверка сайта
    if s.status_code == 200:
        return True
    else:
        return False
