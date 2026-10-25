# Telegram-бот «Дата и время» — учебный проект

Учебный Telegram-бот на [pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI):
умеет показывать дату, время и день недели, отвечает на «привет/пока» —
у него есть собственная клавиатура (`ReplyKeyboardMarkup`) с кнопками.

## Возможности
- команда `/start` выводит приветствие и клавиатуру с кнопками;
- кнопки/фразы: `Привет`, `Пока`, `Дата`, `Время`, `День недели`;
- дата и день недели определяются через `datetime` (день недели — по `weekday()`);
- ответ на кнопки и на обычный текст (переводится в нижний регистр).

## Как запустить
1. Создай бота у [@BotFather](https://t.me/BotFather) и получи токен.
2. Установи зависимость:
   ```
   pip install -r requirements.txt
   ```
3. Передай токен через переменную окружения (не вшивай её в код!):
   - Windows (CMD):
     ```
     set BOT_TOKEN=123456:ABC-DEF...
     python bot.py
     ```
   - Windows (PowerShell):
     ```
     $env:BOT_TOKEN = "123456:ABC-DEF..."
     python bot.py
     ```
   - Linux / macOS /Termux:
     ```
     BOT_TOKEN=123456:ABC-DEF... python bot.py
     ```
4. Напиши своему боту `/start`.

## Что сделано учебным приёмом
- `bot.polling()` — бесконечный цикл приёма сообщений;
- обработчик `content_types=['text']` + словарь `if/elif` для фраз;
- `ReplyKeyboardMarkup.row(...)` — раскладка кнопок.