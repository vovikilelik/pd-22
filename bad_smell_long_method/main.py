# В задании представлена одна большая функция... 
# Делает она всего ничего:
# - читает из строки (файла)         `_read`
# - сортирует прочитанные значения   `_sort`
# - фильтрует итоговый результат     `_filter`

# Конечно, вы можете попробовать разобраться как она 
# это делает, но мы бы советовали разнести функционал 
# по более узким функциям и написать их с нуля


csv = """Вася;39\nПетя;26\nВасилий Петрович;9"""


def parse_user(text):
    data = text.split(';')
    return {'name': data[0], 'age': int(data[1])}


def parse_user_list(text):
    return list(map(parse_user, text.split('\n')))


def filter_users(person_list, age=10):
    return [p for p in person_list if age <= p['age']]


def get_users_list():
    user_list = parse_user_list(csv)
    filtered_user_list = filter_users(user_list)
    return sorted(filtered_user_list, key=lambda u: u['age'])


if __name__ == '__main__':
    print(get_users_list())
