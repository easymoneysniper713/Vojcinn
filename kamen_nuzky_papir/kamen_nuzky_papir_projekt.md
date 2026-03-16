# Kámen, nůžky, papír – Python projekt

## Popis projektu

Tento projekt je jednoduchá terminálová hra **Kámen, nůžky, papír** napsaná v Pythonu. Hráč hraje proti počítači, který si svůj tah vybírá náhodně. Program běží stále dokola, takže můžeš hrát více kol za sebou. Hra se ukončí až ve chvíli, kdy hráč napíše **„konec“**.

## Jak program funguje

Program nejdříve požádá hráče, aby zadal jednu z možností: **kamen**, **nuzky** nebo **papir**. Potom počítač náhodně vybere jednu z těchto možností pomocí knihovny `random`. Program následně porovná výběr hráče s výběrem počítače a vypíše výsledek – jestli jde o **remízu**, **výhru hráče** nebo **prohru hráče**. Poté se hra znovu zeptá na další tah a celý proces se opakuje.

## Jak projekt spustit

Nejprve je potřeba mít nainstalovaný Python. Kód si ulož do souboru například s názvem `hra.py`. Poté otevři terminál ve složce s projektem a spusť program příkazem:

```bash
python hra.py
```

## Jak hru používat

Do terminálu napiš jednu z těchto možností:

* `kamen`
* `nuzky`
* `papir`

Po každém kole program vypíše tah počítače a výsledek hry. Pokud chceš hru ukončit, napiš **konec** a program se vypne.

## Použité principy

Projekt využívá několik základních prvků Pythonu. Používá se cyklus `while True`, který umožňuje, aby hra běžela stále dokola. Funkce `input()` slouží pro načtení vstupu od hráče. Funkce `random.choice()` náhodně vybírá tah počítače. Podmínky `if`, `elif` a `else` pak určují výsledek hry podle pravidel kámen–nůžky–papír.

Tento projekt je vhodný pro začátečníky, protože ukazuje základní práci s cykly, podmínkami, vstupem od uživatele a jednoduchou herní logikou v Pythonu.
