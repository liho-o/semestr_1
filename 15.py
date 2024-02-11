sm = float(input("Введите расстояние в сантиметра: "))
dm = sm / 2.54
ft = dm / 12
yard = ft / 3
mile = yard / 1760
print(f'{yard} ярдов',f'{mile} мили', f'{ft} футов', f'{dm} дюймов', sep='\n')