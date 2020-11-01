'''
Slovníky (dictionaries) podobně jako seznamy v sobě obsahují další hodnoty.
Na rozdíl od seznamů, ve kterých jsou všechny prvky uspořádané do jedné sekvence, ve slovnících máme dva druhy prvků:
klíč (angl. key) a hodnotu (angl. value).
Každému klíči je přiřazena jedna hodnota.
'''

# Sbírka, která je neuspořádaná proměnlivá a indexovaná.
# V Pythonu jsou slovníky psány se složenými závorkami, a mají klíče a hodnoty
car = {
  'brand': 'Ford',
  'model': 'Mustang',
  'year': 1964
}

point = {'x': 1, 'y': 10}

# Vytvoření slovníku pomocí konstruktoru dict()
point = dict(x=1, y=10)

# Změna hodnoty jednoho prvku slovníku
point['x'] = 2

# Vložení nového prvku do slovníku
point['z'] = 20

# Přístup k položkám slovníku
print(f'point["x"]: {point["x"]}')
print(f'point.get("x"): {point.get("x")}')

# Zjištění, zda existuje hodnota
if 'z' in point:
    print(f'point.get("z"): {point.get("z")}')

# Když hodnota neexistuje, vrací 0    
print(f'point.get("v", 0): {point.get("v", 0)}')

# Odstranění prvku ze slovníku  
del point['x']
print(f'point: {point}')

print(f'car.pop(): {car.pop("model")}')

# Odstraní poslední prvek ze slovníku
print(f'car.popitem(): {car.popitem()}')

# Procházení slovníkem - vypíše vždy pár klíč - hodnota
for key, value in point.items():
    print(f'{key} - {value}')

# Dictionary comprehension - zkráceně vytvoří slovník, jehož klíče tvoří čísla od 0 do 9 a hodnoty druhé mocniny 
values = {x: x ** 2 for x in range(10)}
print(f'values: {values}')

# Unpacking operator - pro slovníky se používají **
first = {'x': 1, 'y': 2}
second = {'x': 10, 'z': 5}
common = {**first, 'a': 15, **second}
print(f'common: {common}')

# Nested dictionary - vnořené slovníky
myfamily = {
  'child1' : {
    'name' : 'Emil',
    'year' : 2004
  },
  'child2' : {
    'name' : 'Tobias',
    'year' : 2007
  },
  'child3' : {
    'name' : 'Linus',
    'year' : 2011
  }
}
print(f'Nested dictionary myfamily: {myfamily}')

# ??? 4. cvičení ???
#H a) Navrhněte vlastní vnořený slovník tvořený 3 reálnými objekty s aspoň 6 klíči tak, abyste kromě jednoduchých
# datových typů (čísla, řetězce, boolean) ve slovníku vhodně využili i všechny v tomto bloku probrané strukturované
# typy - tedy set, tuple a list.
# Volte příklad vycházející z reality - např. slovník aut, slovník filmů, slovník historických postav atd.
# b) Pomocí vhodných metod přidejte do slovníku nový prvek a nějaký starý naopak odstraňte
# c) Proveďte výpis obsahu slovníku tak, aby i v konzoli vytvořil hezky naformátovanou tabulku i s mezerami
# viz níže uvedený vzor.
'''
Slovník myfamily
---------------------------------------------
child           name                year
---------------------------------------------
child1          Emil                2004
child2          Tobias              2007
child3          Linus               2011
---------------------------------------------
Počet záznamů: 3
'''

leagueChamps = {
  'champ1' : {
      'Position': 1,
      'name' : 'Aatrox',
      'role' : 'Fighter',
      'difficulty' : 'Easy'
    },
  'champ2' : {
        'Position': 2,
        'name' : 'Ahri',
        'role' : 'Mage',
        'difficulty' : 'Moderate'
      },
  'champ3' : {
        'Position': 3,
        'name' : 'Akali',
        'role' : 'Assasin',
        'difficulty' : 'Moderate'
      },
}
del leagueChamps['champ1']
leagueChamps['champ1'] = {'Position' : '4', 'name' : 'Alistar', 'role' : 'tank', 'difficulty' : 'hard'}
print('\n')
print('Šampioni ze hry League of Legends:')
print('----------------------------------')
print('Pozice  Jméno       Role          Obtížnost')
print('---------------------------------------------')
print(leagueChamps['champ1']['Position'], '.    ', leagueChamps['champ1']['name'], '    ', leagueChamps['champ1']['role'], '     ' , leagueChamps['champ1']['difficulty'])
print(leagueChamps['champ2']['Position'], '.    ', leagueChamps['champ2']['name'], '      ', leagueChamps['champ2']['role'], '        ' , leagueChamps['champ2']['difficulty'])
print(leagueChamps['champ3']['Position'], '.    ', leagueChamps['champ3']['name'], '     ', leagueChamps['champ3']['role'], '     ' , leagueChamps['champ3']['difficulty'])
print('----------------------------------------------')
print('Počet záznamů: %d ' % len(leagueChamps))


#print(f'point["x"]: {leagueChamps["champ3"]}}')
#print(f'Šampioni League of Legends: {leagueChamps}')