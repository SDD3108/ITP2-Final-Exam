# ITP2-Final-Exam
S.Damir, Sara.Y, Danial.N, Ariana.Z

<!-- в utils будут всякие утилиты которые будут переиспользоваться, по типу сохранения файла, проверку пользователей и предметов на их наличие (valid)-->
<!-- в test я просто тестил так что забейте -->
<!-- в services будет по сути вся основная логика, чтение/изменение файлов,функции (от сюда мб будем импортировать) -->
<!-- в models  будут классы/модели проекта, то есть основные сущности/структуры с которыми будем работать чтоб понимать чего ждать итд. тут описывается структура объектов, их поля, методы, наследование, инкапсуляция и полиморфизм. По сути models отвечает за то, как выглядят пользователи, предметы и рекомендации внутри программы итд -->

case 7 simple recommendation system

## how to run

Python3 main.py
or
Python main.py


run for specific user:

Python3 main.py 1

run tests:

Python3 tests/test.py
or
cd tests
Python3 test.py

## input files (mock datas)

- `data/users.json`
- `data/items.json`

## output file 

- `outputs/recommendations.json`

## main logic

similarity is calculated using set intersection.

example:

user 1 liked: movie1 movie2

user 2 liked: movie2 movie3

same item: movie2

so movie3 can be recommended to user 1

## data structures

list is used to store users and items
dictionary is used for fast item lookup by id
set is used to find common liked items
tuple is used to return same items safely from similarity function

## oop

project uses classes:

<!-- потом / empty -->

inheritance:

<!--  -->

polymorphism:

<!--  -->

encapsulation:

class fields use protected style with `_field_name`
access is done through properties

## advanced python features

generator in `` (название функции которая генератор user)
decorator `` (название функции которая сохраняет файл)
lambda in sorting recommendations
regex in item id validation

## team contribution

### student 1
Initialized project
Hierarchy
Instructions for everyone
optimization and better logic
main program
colsole outputs
tests

### student 2
project description
README file
presentation
models
item and recommendation classes
user,regularUser,adminUser

### student 3
???

### student 4
???

## efficiency

instead of searching items in a list every time, the project uses dictionary:

<!-- потом найду в вашем коде, но пока что оно будет примерно так выглядить -->
<!-- self.items_map={item.item_id:item for item in items} -->

this gives fast lookup close to O(1).

similarity uses sets:

<!-- тут тоже -->
<!-- same_items=set1.intersection(set2) -->

this is faster and cleaner than comparing every item with nested loops.