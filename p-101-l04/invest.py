def invest(amount, rate, years):
    n = 1
    while n <= years:
        amount = amount + amount * rate / 100
        n += 1
        print(f"{amount:.2f}")
    return amount

amount = float(input("Podaj kwote jaka chcesz oszczedzac: "))
rate = float(input("Podaj procent: "))
years = int(input("Ile lat chesz oszczadzac: "))
total_amount = invest(amount, rate, years)
print(f"Lacznie zebierzesz kwote: {total_amount:.2f}")

