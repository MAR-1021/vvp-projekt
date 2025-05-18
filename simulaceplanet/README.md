# Simulace pohybu planet ve 2D

Tento repozitář obsahuje projekt do předmětu **Vědecké výpočty v Pythonu**, jehož cílem je simulovat pohyb planet v dvourozměrném prostoru. Simulace je implementována v jazyce Python a využívá knihovny **NumPy** a **Matplotlib**.

## Funkcionalita

Knihovna umožňuje:
- reprezentovat planetu jako objekt s pozicí, rychlostí, zrychlením a hmotností,
- počítat gravitační síly mezi planetami,
- integrovat pohyb pomocí [Leapfrog metody](https://en.wikipedia.org/wiki/Leapfrog_integration),
- vizualizovat trajektorie planet pomocí Matplotlib,
- ukládat animace simulace do souborů.


## Spuštění simulace

Ukázkový příklad naleznete v Jupyter notebooku:

```bash
cd examples
jupyter notebook examples.ipynb
```

## Testování

Pro spuštění jednotkových testů:

```bash
pytest
```

## Dokumentace

Automaticky generovaná dokumentace pomocí Sphinx se nachází ve složce `docs/`. Pro její vytvoření spusťte:

```bash
cd docs
make html
```

Výstup najdete v `docs/build/html/index.html`.


## Závislosti
- numpy
- matplotlib
- pytest (pro testování)
- sphinx (pro dokumentaci)



Šimon Marek
16-5-2025
