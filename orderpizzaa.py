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

print("Personal")
print("Medium")
print("Jumbo")

UkuranPizza = input("Silahkan pilih ukuran pizza :")
Harga_Ukuranpizza = 0
if UkuranPizza == "Personal":
    Harga_Ukuranpizza = 5000
    print("Anda memesan ukuran Personal", Harga_Ukuranpizza)
elif UkuranPizza == "Medium":
    Harga_Ukuranpizza = 10000
    print("Anda memesan ukuran Medium", Harga_Ukuranpizza)
elif UkuranPizza == "Jumbo":
    Harga_Ukuranpizza = 15000
    print("Anda memesan ukuran Jumbo", Harga_Ukuranpizza)
else:
    print("PESANAN ANDA TIDAK VALID")

print("Terimakaasih anda telah memesan pizza dengan ukuran", UkuranPizza, "dengan harga", Harga_Ukuranpizza)

# Biaya tambahan cheese
if Ekstra_Cheese == "Yes" :
    Extra_Fee = 13000
elif Ekstra_Cheese == "No" :
    Extra_Fee = 0
else:
    print ("Pesanan tidak valid")
    exit()

#Total biaya
total_biaya = hargatoping + harga_crustpizza + Harga_Ukuranpizza + Extra_Fee
# Menampilkan pesanan dan total biaya
print("Thank you for choosing pizza D4MI!")
print("You final bill will be : Rp", int(total_biaya))


   

