total_coast = input("Значение общей стоимости часов:")
total_coast = float(total_coast)
silv_count = 96
gold_count = silv_count/16
silv_coast = 48

gold_coast = (total_coast - (silv_coast * silv_count))/ gold_count
print(gold_coast)