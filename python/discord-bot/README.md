# Discord-бот «Дружище» — учебный проект

Учебный Discord-бот на [discord.py](https://discordpy.readthedocs.io/):
здоровается случайной фразой, поддерживает диалог «как дела?» и
админ-команды `!забанить` / `!кикнуть` в его текущей версии.

## Возможности
- `!привет / !салам / !сау` — случайная реплика из списка приветствий;
- `!поиграем?`, `!ты классный`, `!пока` — готовые ответы из словаря `ANSWERS`;
- `!как дела?` — бот спрашивает в ответ и следующий ответ сверяет
  со словарём `HOWAREYOU` через `client.wait_for('message', check=...)`;
- `!забанить <ник>` и `!кикнуть <ник>` — ищет участника по нику
  и выдаёт бан/кик (`Perm.ban_members`, `Perm.kick_members`).

## Как запустить
1. Создай приложение на [Discord Developer Portal](https://discord.com/developers/applications)
   и получи токен (вкладка Bot → Reset Token).
2. Установи зависимость:
   ```
   pip install -r requirements.txt
   ```
3. Токен передавай через переменную окружения, а не вшивай в код:
   - Windows (CMD):      `set DISCORD_TOKEN=твой.токен.сюда`   → `python bot.py`
   - PowerShell:         `$env:DISCORD_TOKEN = "твой.токен.сюда"` → `python bot.py`
   - Linux / macOS:      `DISCORD_TOKEN=... python bot.py`
4. Включи у бота на портале Server Members Intent и Message Content Intent
   (секция Privileged Gateway Intents) — код их требует `intents.members`,
   `intents.message_content`.

## Изменения в этой версии (по сравнению с исходником курсовой работы)
- токен вынесен в переменную окружения (`os.environ`) вместо вшитой строки
  в коде — так его можно выложить на GitHub и не слить случайно;
- убран несуществующий аргумент `permissionns` у `discord.Client`
  (на discord.py 2.x он вызывает ошибку TypeError);
- `delete_message_days` → `delete_message_seconds` (новый API discord.py).

> Важно: если раньше токен улетал куда-то в код, который ты где-то отправлял,
> сбрось его на портале (Reset Token) — старый считается скомпрометированным.