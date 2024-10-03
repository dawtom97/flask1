# import asyncio
# import time

# async def async_task(name, delay):
#     print(f"Rozpoczynam zadanie: {name}")
#     await asyncio.sleep(delay)  # Asynchroniczne "czekanie"
#     print(f"Zadanie zakończone: {name}")

# async def main():
#     # Tworzymy listę zadań
#     tasks = [
#         async_task("Zadanie 1", 2),
#         async_task("Zadanie 2", 1),
#         async_task("Zadanie 3", 3)
#     ]
    
#     # Uruchamiamy zadania asynchronicznie
#     await asyncio.gather(*tasks)

# # Uruchamiamy pętlę zdarzeń
# start_time = time.time()
# asyncio.run(main())
# end_time = time.time()
# print(f"Czas wykonania: {end_time - start_time:.2f} sekundy")


# generator
def simple_generator():
    print("Pierwsza wartość")
    yield 1
    print("Druga wartość")
    yield 2
    print("Trzecia wartość")
    yield 3

# Użycie generatora
gen = simple_generator()

# Uzyskujemy wartości z generatora
print(next(gen))  # Pierwsza wartość, 1
print(next(gen))  # Druga wartość, 2
print(next(gen))  # Trzecia wartość, 3

