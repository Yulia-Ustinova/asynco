import asyncio

import aiofiles

file_1 = input("Введите путь первого файла: ")
file_2 = input("Введите путь второго файла: ")


async def count_txt(file):
    async with aiofiles.open(file, "r", encoding="utf-8") as f:
        f_txt = await f.readlines()
        rows = len(f_txt)
        word_count = 0
        symbol_count = 0
        for line in f_txt:
            word_count += len(line.split())
            symbol_count += len(line)

    print(f"Файл {f.name}"
          f"\nКоличество строк: {rows}"
          f"\nКоличество слов: {word_count}"
          f"\nКоличество символов: {symbol_count}")


async def main():
    task1 = asyncio.create_task(count_txt(file_1))
    task2 = asyncio.create_task(count_txt(file_2))

    await task1
    await task2


if __name__ == "__main__":
    asyncio.run(main())
