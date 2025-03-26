def ucgen_to_yildiz(Rab, Rbc, Rca):
    R_sum = Rab + Rbc + Rca
    Ra = (Rab * Rca) / R_sum
    Rb = (Rab * Rbc) / R_sum
    Rc = (Rbc * Rca) / R_sum
    return Ra, Rb, Rc

# Kullanıcıdan giriş al
Rab = float(input("Rab değerini girin: "))
Rbc = float(input("Rbc değerini girin: "))
Rca = float(input("Rca değerini girin: "))

# Hesaplama
Ra, Rb, Rc = ucgen_to_yildiz(Rab, Rbc, Rca)

print(f"Üçgen'den Yildiz'a: Ra = {Ra}, Rb = {Rb}, Rc = {Rc}")