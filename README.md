# Laboratory 2
В этой лабораторной работе мы работалы с списками, кортежами, множествами и словарями.
Так же мы работалы с 2D списками (матрицами)

## Задание 1
- Реализовал функции:
1. min_max(nums: list[float | int]) -> tuple[float | int, float | int]
2. unique_sorted(nums: list[float | int]) -> list[float | int]
3. flatten(mat: list[list | tuple]) -> list
   
<img width="605" height="278" alt="Dusan lab02 -1" src="https://github.com/user-attachments/assets/f913aac6-94f0-4b4d-ad59-11682867219d" />
<img width="601" height="180" alt="Dusan lab02 - 2" src="https://github.com/user-attachments/assets/386f3f56-29dd-443a-8d4a-dbd0caaff2b2" />


## Задание 2
- Реализовал функции:
1. transpose(mat: list[list[float | int]]) -> list[list]
2. row_sums(mat: list[list[float | int]]) -> list[float]
3. col_sums(mat: list[list[float | int]]) -> list[float]
   
<img width="382" height="338" alt="Dusan lab02 - 3" src="https://github.com/user-attachments/assets/5c3e82f1-82a0-42cc-8590-a1824dd9e1eb" />

## Задание 3 
- Реализовал:
1. format_record(rec: tuple[str, str, float]) -> str
    тип щаписи студента как кортеж ( fio: str, group: str, gpa: float)
   
<img width="581" height="112" alt="Dusan lab02 - 4" src="https://github.com/user-attachments/assets/87355ce3-66fd-4fee-aa22-86346be1439c" />

# Laboratory 3
Цель: нормализовать текст, аккуратно токенизировать, посчитать частоты слов и вывести топ-N.


## Задание 1
- Реализовал:
1. normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str
2. tokenize(text: str) -> list[str]
3. count_freq(tokens: list[str]) -> dict[str, int]
4. top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]

<img width="907" height="147" alt="Screenshot 2025-11-25 183128" src="https://github.com/user-attachments/assets/5fa83971-4ebf-4766-a2b8-70739fb48fda" />

## Задание 2
- Реализовал скрипт который читает одну строку текста из stdin и вызивает функции из `lib/text.py` и печтает:
  1. `Всего слов: <N>`
  2. `Уникальных слов: <N>`
  3. `Топ 5:` - по строке на запись в формате `слово:кол-во`
  4. 
  <img width="436" height="131" alt="Dusan lab03 - 2" src="https://github.com/user-attachments/assets/00f26590-97c7-4ea5-b1f8-926838200ad5" />
