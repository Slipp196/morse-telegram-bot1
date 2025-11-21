import asyncio
from aiogram import Bot, Dispatcher, types

import os
API_TOKEN = os.getenv("BOT_TOKEN")


# Русская азбука Морзе
MORSE_RU = {
    ".-": "А", "-...": "Б", ".--": "В", "--.": "Г",
    "-..": "Д", ".": "Е", "...-": "Ж", "--..": "З",
    "..": "И", ".---": "Й", "-.-": "К", ".-..": "Л",
    "--": "М", "-.": "Н", "---": "О", ".--.": "П",
    ".-.": "Р", "...": "С", "-": "Т", "..-": "У",
    "..-.": "Ф", "....": "Х", "-.-.": "Ц", "---.": "Ч",
    "----": "Ш", "--.-": "Щ", "--.--": "Ъ", "-.--": "Ы",
    "-..-": "Ь", "..-..": "Э", "..--": "Ю", ".-.-": "Я",
    "-----": "0", ".----": "1", "..---": "2", "...--": "3",
    "....-": "4", ".....": "5", "-....": "6", "--...": "7",
    "---..": "8", "----.": "9"
}


# Декодер морзе: буквы = пробел, слова = /
def decode_morse(text: str) -> str:
    words = text.split("/")     # разделение слов
    decoded_words = []

    for w in words:
        w = w.strip()
        letters = w.split(" ")  # разделение букв
        decoded = ""

        for l in letters:
            if not l.strip():   # пропуск пустых значений
                continue
            decoded += MORSE_RU.get(l, "?")

        decoded_words.append(decoded)

    return " ".join(decoded_words)


async def main():
    bot = Bot(token=API_TOKEN)
    dp = Dispatcher()

    @dp.message()
    async def handle_message(msg: types.Message):
        decoded = decode_morse(msg.text)
        await msg.answer(decoded)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

