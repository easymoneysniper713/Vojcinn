Dokumentace projektu: Dungeon Quest

Popis a cíl projektu:
Tato aplikace je textová RPG hra, ve které hráč prochází dungeonem, bojuje s nepřáteli, sbírá zlato a získává zkušenosti. Cílem projektu je vytvořit jednoduchou hru v konzoli, která simuluje základní herní mechaniky jako souboj, levelování a správu inventáře. Hlavním cílem hráče je přežít co nejdéle, porazit co nejvíce nepřátel a dosáhnout co nejvyšší úrovně.

Jak program používat:
Spuštění: Po spuštění programu se zobrazí úvodní obrazovka a výzva k zadání jména postavy.

Průběh hry: Hráč se postupně přesouvá mezi náhodnými místnostmi. V každé místnosti může nastat souboj s nepřítelem, setkání s obchodníkem, nalezení zlata nebo odpočinek.

Ovládání: V boji hráč volí akce pomocí čísel. 1 znamená útok, 2 použití lektvaru a 3 pokus o útěk.

Inventář: Hráč může používat lektvary pro doplnění zdraví.

Obchod: Hráč může nakupovat zbraně a lektvary za získané zlato.

Ukončení: Hra končí smrtí hráče nebo zadáním „q“ pro ukončení.

Funkcionalita programu:
Aplikace běží v herní smyčce, dokud hráč nezemře nebo hru neukončí. Každý průchod smyčkou představuje jednu místnost. Program využívá náhodné generování událostí a spravuje stav hráče (životy, zkušenosti, level, inventář, zlato).

Technická část:
Algoritmus souboje: Program používá cyklus, ve kterém se střídají tahy hráče a nepřítele. Poškození je generováno náhodně v určitém rozsahu. Kritický zásah může poškození zdvojnásobit.

Levelovací systém: Hráč získává zkušenosti (XP) za poražené nepřátele. Po dosažení určité hodnoty XP postoupí na vyšší úroveň, zvýší se jeho maximální počet životů a částečně se vyléčí.

Logické větvení: Program využívá podmínky if, elif a else pro řízení průběhu hry, například při výběru akce hráče, kontrole smrti, nákupu v obchodě nebo generování událostí.

Náhodnost: Program využívá knihovnu random pro výběr nepřátel, místností, výpočet poškození, šanci na kritický zásah a úspěšnost útěku.

Datové struktury: Program pracuje se slovníky (dict) pro ukládání zbraní a lektvarů, se seznamy (list) pro nepřátele a místnosti a s třídou Player pro uchování informací o hráči.

Vstupy a výstupy: Program používá funkci input() pro získání vstupu od uživatele a print() pro výpis informací. Pro přehlednější výpis jsou použity formátované řetězce (f-strings). Funkce slow_print() zajišťuje postupné zobrazování textu.

Ošetření chyb: Program kontroluje neplatné vstupy uživatele, nedostatek lektvarů a nedostatek zlata. Při neplatné volbě hráč ztrácí tah.

Požadavky:
- Python 3.x (doporučeno 3.8 nebo vyšší)
- Žádné externí knihovny nejsou potřeba (používají se pouze standardní knihovny: random, time, os, msvcrt)

Instalace:
1. Stáhněte nebo naklonujte repozitář.
2. Ujistěte se, že máte nainstalovaný Python.
3. Spusťte program příkazem: python dungeon_quest.py

Changelog (Patch Notes):
- **Verze 1.1** (23. března 2026): Přeloženy všechny řetězce do češtiny pro úplnou lokalizaci. Opraveny nekonzistence v názvech zbraní, nepřátel a místností.
- **Verze 1.2** (25. března 2026): Přidána nová funkce brňení
- **Verze 1.3** (26. března 2026): byly přidány questy.
- **Verze 1.4** (31. března 2026): Byly přidané hry