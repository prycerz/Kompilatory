# Mapper

## Przygotowanie środowiska
### Aby wygenerować parser w języku Python z pliku gramatyki Mapper.g4, użyj jednej z poniższych metod:
- Jeśli masz alias 'antlr4':
```bash
$ antlr4 -Dlanguage=Python3 -visitor Mapper.g4
```

### Jeśli nie masz aliasu, użyj pełnej ścieżki:
```bash
$ java -jar C:\antlr\antlr-4.13.1-complete.jar -Dlanguage=Python3 -visitor Mapper.g4
```

### Uruchamianie skryptu Python - wybór jednej z opcji:
1. Instalacja wymaganych pakietów
```bash
$ pip install requirements.txt
```
2. Aby uruchomić interpreter dla pliku example.map, wykonaj:
```bash
$ py MapperInterpreter.py example.map
```
lub
```bash
$ python MapperInterpreter.py example.map
```

## Przykład użycia

### Rysowanie obiektów
**Tile** - płytka do wyświetlenia, można ustawić:
- obiekt na pierwszym planie np. drzewo, krzaki, chatka
- obiekt w tle np. trawa, piasek, woda

**Pointer** - zmienia aktualne położenia, na które możemy położyć płytkę
```
tile mojaplytka = sand + cabin 
tile drugaplytka = rocks

draw mojaplytka

pointer down 10
draw drugaplytka
```
![Rezultat](./assets/readme/tile.png)


### Rysowanie zbioru płytek
**Blend** - tworzy zbiór płytek w podanym kształcie, w podanych proporcjach
```
blend mojblend = circle 10 sand 50% grass 50%
draw blend
```
![Rezultat](./assets/readme/blend.png)


### Łączenie tile i blend
```
pointer up 1
blend wyspa = circle 7 sand 100%
draw wyspa

blend zielenie = circle 6 tree 20% rocks 10% bush 30% grass 60%
draw zielenie

pointer up 2
pointer left 2 

blend village = rectangle 5 5 cabin 80%
draw village

pointer down 2
pointer right 2
draw church

pointer right 5
tile rockmountain = rocks + mountains
blend gory = circle 1 rockmountain 80%
draw gory

pointer left 7 
pointer up 3
blend lake = circle 2 water 100%
draw lake
```
![Rezultat](./assets/readme/blend_tile.png)
