Частота слов в тексте
=============================================

Задача:
-------

- создать функцию word_frequency, которая принимает в качестве параметра список строк, 
извлекает из всех строк слова и возвращает словарь с количеством для каждого слова.

Требования:
-----------
- Функция должна обрабатывать слова без учета регистра. 
- Функция должна удалять начальные и конечные пробелы из каждого слова.
- Функция должна исключать любые знаки препинания, прикрепленные к словам. 
- Функция должна исключать пустые строки как слова.
- Функция должна стремиться к оптимальной временной сложности.

Выполнение:
-----------
Задание выполнено в виде скрипта, который тестирует три функции, 
каждая из которых выполняет поставленную задачу.
Функции отличаются подсчётом извлечённых из строки слов.

Первая функция использует defaultdict, вторая - Counter, третья - обычный dict.

Для выбора оптимального времени выполнения функции тестируются с коротким тестовым списком строк 
и этим же списком, повторенным 1000 раз.
Как результат, выводятся словарь с частотой слов и время выполнения функции в микросекундах.

Результат тестов:
-----------------
- на коротком списке строк стабильно выигрывает функция word_frequency_3 с применением dict.
- на длинном списке строк выигрывает функция word_frequency_2 с применением Counter.

Вывод:
-----------------
- **рекомендуется применять функцию word_frequency_2, 
так как она показывает стабильно хорошее время выполнения, 
а стиль функции при этом *pythonic*.**