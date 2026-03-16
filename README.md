# Circle Intersection Project

## Popis projektu

Tento projekt implementuje jednoduché matematické funkce pro práci s kružnicemi.

Obsahuje funkce:

* `has_intersection(c1, c2)` – zjistí, zda se dvě kružnice protínají nebo dotýkají.
* `radius_sum(r1, r2)` – vrátí součet dvou poloměrů.

Kružnice jsou reprezentovány jako:

```
(x, y, r)
```

kde:

* `x`, `y` – souřadnice středu
* `r` – poloměr

---

## Spuštění projektu

1️⃣ Naklonuj repozitář

```
git clone https://github.com/username/circle-intersections.git
cd circle-intersections
```

2️⃣ Vytvoř virtuální prostředí

```
python -m venv venv
source venv/bin/activate
```

3️⃣ Nainstaluj závislosti

```
pip install -r requirements.txt
```

---

## Spuštění testů

Projekt používá **pytest**.

```
pytest
```

Pokud je některý test nastaven schválně špatně, uvidíš výpis chyby například:

```
FAILED tests/test_circle.py::test_intersection_wrong_expected
```

Tento test slouží k tréninku čtení chyb a hledání problémů v testech.

---

## Struktura projektu

```
src/
    circle.py

tests/
    test_circle.py
```

---

## Licence

Educational project.
