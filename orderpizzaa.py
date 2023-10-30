print("Selamat datang di Toko pizza D4MI\n")

print("Frankfurter")
print("Meat Monsta")
print("Super Supreme")
print("Super Supreme Chicken")

TopinggPizza = input("\ningin pizza varian apa ? :")
hargaPizza = 0
if TopinggPizza == "Frankfurter":
    hargatoping = 35000
elif TopinggPizza == "Meat Monsta":
    hargatoping = 30000
elif TopinggPizza == "Super Supreme":
    hargatoping = 40000
elif TopinggPizza == "Super Supreme Chicken":
    hargatoping = 50000
else:
    print("\nToping tidak ada")

print("=====================================\n")

print("Pan Crust")
print("Stuffed Crust")
print("Crown Crust")
print("Cheesy Bire")

crustpizza = input("\nSilakan pilih Crush Pizza :")
harga_crustpizza = 0
if crustpizza == "Pan Crust":
    harga_crustpizza = 5000
elif crustpizza == "Stuffed Crust":
    harga_crustpizza = 6000
elif crustpizza == "Crown Crust":
    harga_crustpizza = 40000
elif crustpizza == "Cheesy Bites":
    harga_crustpizza = 50000
else:
    print("PESANAN ANDA TIDAK VALID")
