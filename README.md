# Ханойские башни

Этот репозиторий содержит простую программу на Python, которая может решить головоломку "Ханойские башни". Программа была создана с использованием языка Python и может быть запущена из командной строки.

## Установка

1. Клонируйте репозиторий:

```
git clone https://github.com/<your-username>/hanoi-towers.git
cd hanoi-towers
```

2. Убедитесь, что у вас установлен Python версии 3.x.x.

3. Запустите программу, выполнив команду:

```
python hanoi.py
```

## Использование

При запуске программы вы должны будете ввести следующие параметры:

- Количество дисков (от 3 до 20)
- Количество башен (от 3 до 10)
- Номер начальной башни (от 1 до количества башен)
- Номер конечной башни (от 1 до количества башен)

Программа затем выведет последовательность перемещений, необходимых для решения головоломки Ханойские башни.

## Алгоритм

Алгоритм состоит из трех шагов:

1. Перемещение n-1 диска с первой башни на вторую, используя третью башню как промежуточную.
2. Перемещение оставшегося диска с первой башни на третью.
3. Перемещение n-1 диска со второй башни на третью, используя первую башню как промежуточную.

## Автор

Эта программа была создана Чагиным Денисом.
