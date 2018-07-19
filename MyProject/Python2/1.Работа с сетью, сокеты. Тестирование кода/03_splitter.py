# splitter.py
import types

import val as val


def split(line, types=None, delimiter=None):
    """ Разбивает​ ​ текстовую​ ​ строку​ ​ и​ ​ при​ ​ необходимости
    выполняет​ ​ преобразование​ ​ типов.  ​
    ​Например: 
    ​>>>​ ​ split('GOOG​ ​ 100​ ​ 490.50') 
    ['GOOG',​ ​ '100',​ ​ '490.50']  ​
    ​>>>​ ​ split('GOOG​ ​ 100​ ​ 490.50',[str,​ ​ int,​ ​ float]) 
    ​['GOOG',​ ​ 100,​ ​ 490.5] 
    ​>>> 
    ​По​ ​ умолчанию​ ​ разбиение​ ​ производится​ ​ по​ ​ пробельным​ ​ символам, но имеется возможность 
    указать другой символ-разделитель, в виде именованного​ ​ аргумента: 
    ​>>>​ ​ split('GOOG,100,490.50',delimiter=',') 
    ​['GOOG',​ ​ '100',​ ​ '490.50'] 
    ​>>>
    """
    fields = line.split(delimiter)
    if types:
        fields = [types(val) for types.val in zip(types, fields) ]
    return fields

print(split('GOOG 100 490.50'))
print('GOOG 100 490.50')
