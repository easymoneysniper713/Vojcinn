Dokumentace projektu: Dungeon Quest
Popis a cíl projektu:

Tato aplikace je textová RPG hra, ve které hráč prochází dungeonem, bojuje s nepřáteli, sbírá zlato a získává zkušenosti. Cílem projektu je vytvořit jednoduchou hru v konzoli, která simuluje základní herní mechaniky jako souboj, levelování a správu inventáře.

Hlavním cílem hráče je přežít co nejdéle, porazit co nejvíce nepřátel a dosáhnout co nejvyšší úrovně.

Jak program používat:
Spuštění:

Po spuštění programu se zobrazí úvodní obrazovka a výzva k zadání jména postavy.

Průběh hry:

Hráč se postupně přesouvá mezi náhodnými místnostmi.

V každé místnosti může nastat:

souboj s nepřítelem

setkání s obchodníkem

nalezení zlata

odpočinek (doplnění životů)

Ovládání v boji:

1 – útok

2 – použití lektvaru

3 – pokus o útěk

Inventář:

Hráč může používat lektvary pro doplnění zdraví.

Obchod:

Hráč může nakupovat:

nové zbraně

lektvary

Ukončení hry:

hráč zemře

nebo zadá q pro ukončení hry

Funkcionalita programu:

Aplikace běží v cyklu (herní smyčce), dokud hráč:

nezemře

nebo hru neukončí

Program využívá:

náhodné generování událostí

správu stavu hráče (HP, XP, level, inventář)

interakci s uživatelem pomocí vstupů

Každý průchod smyčkou představuje jednu herní „místnost“.

Technická část:
Algoritmus souboje:

Souboj probíhá ve smyčce:

hráč provede akci

nepřítel následně zaútočí

opakuje se, dokud jedna strana nezemře

Poškození je generováno náhodně v daném rozsahu.

Levelovací systém:

hráč získává XP za poražené nepřátele

po dosažení určité hodnoty XP se zvýší level

při levelování:

se zvýší maximální HP

hráč se částečně vyléčí

Logické větvení:

Program využívá podmínky (if, elif, else) pro:

výběr akce hráče

náhodné události (boj, obchod, odpočinek…)

kontrolu smrti hráče

kontrolu dostatku zlata při nákupu

Náhodnost:

Program využívá knihovnu random:

výběr nepřátel

výběr místností

výpočet poškození

šance na kritický zásah

šance na útěk

Datové struktury:

Program využívá:

slovníky (dict)

zbraně (WEAPONS)

lektvary (POTIONS)

seznamy (list)

nepřátelé (ENEMIES)

místnosti (ROOMS)

třídu (class Player)

uchovává všechny informace o hráči

Vstupy a výstupy:

vstup: funkce input()

výstup: print() a formátované řetězce (f-strings)

funkce slow_print() zajišťuje postupné vypisování textu pro lepší herní zážitek

Ošetření chyb:

Program kontroluje:

neplatné vstupy (např. špatná volba akce)

nedostatek lektvarů

nedostatek zlata při nákupu

Při neplatném vstupu hráč ztrácí tah.

Závěr:

Projekt ukazuje základní principy tvorby her v Pythonu:

práce s cykly a podmínkami

objektově orientované programování

práce s náhodností

interakce s uživatelem
