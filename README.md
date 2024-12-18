<p align="center">
  <img src="https://github.com/fearux/hangman_game/raw/main/docs/logo.png" alt="Логотип игры" />
</p>

## Виселица
### Description
Консольное приложение на Python, имитирующее популярную игру "Виселица". Цель игрока заключается в том, чтобы как можно раньше угадать секретное слово, вводя каждый новый ход букву. Ответы игрока ограничены попытками. После 6 попытки игрок проигрывает.
 
### Project functionality 
- Пользовательский ввод и его обработка
- Рендеринг каждого шага, демонстрация состояния игры
- Набор слов читается и обрабатывается из файла

### Interface
![Интерфейс игры](https://github.com/fearux/hangman_game/raw/main/docs/hangman.png)

### Installation
1. Склонировать репозиторий
```bash
git clone https://github.com/fearux/hangman.git
```
2.  Перейти в основню директорию проекта
```bash
cd hangman/src
```
3. Убедитесь, что в директории есть файл *ru_words.txt*
```bash
ls data
```
4. Запустите основной файл проета:
```bash
python3 -m hangman.main
```
или
```bash
python -m hangman.main
```

<a href="https://ru.freepik.com/icon/gallow_1428300">Источник иконки: Nikita Golubev</a>
