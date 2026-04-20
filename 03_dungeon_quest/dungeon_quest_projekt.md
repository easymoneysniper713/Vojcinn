Dokumentace projektu: Dungeon Quest

Popis a cíl projektu:
Tato aplikace je textová RPG hra, ve které hráč prochází dungeonem, bojuje s nepřáteli, sbírá zlato a získává zkušenosti. Cílem projektu je vytvořit jednoduchou hru v konzoli, která simuluje základní herní mechaniky jako souboj, levelování, správu inventáře, questy a sbírání artefaktů. Hlavním cílem hráče je přežít co nejdéle, porazit co nejvíce nepřátel, splnit questy a dosáhnout co nejvyšší úrovně.

Jak program používat:
Spuštění: Po spuštění programu se zobrazí úvodní obrazovka s menu pro novou hru, zobrazení statistik nebo konec. Po výběru nové hry se zobrazí výzva k zadání jména postavy.

Průběh hry: Hráč se postupně přesouvá mezi náhodnými místnostmi. V každé místnosti může nastat souboj s nepřítelem, setkání s obchodníkem, nalezení zlata, artefaktu, odpočinek nebo nic. Hra zahrnuje quest systém, kde hráč plní úkoly pro odměny.

Ovládání: V boji hráč volí akce pomocí čísel: 1 útok, 2 použití lektvaru, 3 pokus o útěk, 4 obchod, 5 správa vybavení, 6 AFK režim. Mimo boj lze pokračovat nebo ukončit hru.

Inventář: Hráč může používat lektvary pro doplnění zdraví.

Obchod: Hráč může nakupovat zbraně, zbroje a lektvary za získané zlato.

Správa vybavení: Hráč může přepínat mezi dostupnými zbraněmi a zbrojemi.

Artejakty: Hráč může sbírat artefakty, které poskytují bonusy k útoku, obraně, kritickým zásahům nebo regeneraci HP.

Questy: Hráč dostává questy typu zabití určitých nepřátel, navštívení místností nebo získání zlata. Po splnění získává odměny.

Statistiky: Po skončení hry se uloží statistiky a lze zobrazit top skóre.

Ukončení: Hra končí smrtí hráče nebo zadáním „q“ pro ukončení.

Funkcionalita programu:
Aplikace běží v herní smyčce, dokud hráč nezemře nebo hru neukončí. Každý průchod smyčkou představuje jednu místnost. Program využívá náhodné generování událostí, spravuje stav hráče (životy, zkušenosti, level, inventář, zlato, artefakty, questy) a ukládá statistiky do JSON souboru.

Technická část:
Algoritmus souboje: Program používá cyklus, ve kterém se střídají tahy hráče a nepřítele. Poškození je generováno náhodně v určitém rozsahu. Kritický zásah může poškození zdvojnásobit. Obrana zbroje a artefaktů snižuje poškození.

Levelovací systém: Hráč získává zkušenosti (XP) za poražené nepřátele a splněné questy. Po dosažení určité hodnoty XP postoupí na vyšší úroveň, zvýší se jeho maximální počet životů a částečně se vyléčí.

Quest systém: Questy jsou náhodně přiřazovány a sledují pokrok hráče. Po splnění se přiřadí nový quest.

Artefakty: Artefakty poskytují trvalé bonusy k poškození, obraně, kritickým zásahům nebo regeneraci HP na začátku každé místnosti.

Logické větvení: Program využívá podmínky if, elif a else pro řízení průběhu hry, například při výběru akce hráče, kontrole smrti, nákupu v obchodě, správě vybavení nebo generování událostí.

Náhodnost: Program využívá knihovnu random pro výběr nepřátel, místností, výpočet poškození, šanci na kritický zásah, úspěšnost útěku, nalezení artefaktů a questů.

Datové struktury: Program pracuje se slovníky (dict) pro ukládání zbraní, zbrojí, lektvarů a artefaktů, se seznamy (list) pro nepřátele, místnosti a questy, a s třídou Player pro uchování informací o hráči. Statistiky se ukládají do JSON souboru.

Vstupy a výstupy: Program používá funkci input() pro získání vstupu od uživatele a print() pro výpis informací. Pro přehlednější výpis jsou použity formátované řetězce (f-strings). Funkce slow_print() zajišťuje postupné zobrazování textu. AFK režim zobrazuje náhodné citáty.

Ošetření chyb: Program kontroluje neplatné vstupy uživatele, nedostatek lektvarů, nedostatek zlata a neplatné volby. Při neplatné volbě hráč ztrácí tah.

Požadavky:
- Python 3.x (doporučeno 3.8 nebo vyšší)
- Žádné externí knihovny nejsou potřeba (používají se pouze standardní knihovny: random, time, os, msvcrt, json)

Instalace:
1. Stáhněte nebo naklonujte repozitář.
2. Ujistěte se, že máte nainstalovaný Python.
3. Spusťte program příkazem: python dungeon_quest.py

Changelog (Patch Notes):
- **Verze 1.1** (23. března 2026): Přeloženy všechny řetězce do češtiny pro úplnou lokalizaci. Opraveny nekonzistence v názvech zbraní, nepřátel a místností.
<<<<<<< HEAD
- **Verze 1.2** (25. března 2026): Přidána nová funkce brňení
- **Verze 1.3** (26. března 2026): byly přidány questy.
- **Verze 1.4** (31. března 2026): Byly přidané hry
=======
- **Verze 1.2** (25. března 2026): Přidána nová funkce brnění (zbroje).
- **Verze 1.3** (26. března 2026): Přidány questy pro dodatečnou motivaci hráče.
- **Verze 1.4** (10. dubna 2026): Přidány artefakty s bonusy k útoku, obraně a regeneraci.
- **Verze 1.5** (15. dubna 2026): Přidána správa vybavení pro přepínání zbraní a zbrojí.
- **Verze 1.6** (18. dubna 2026): Přidán AFK režim s inspirativními citáty a systém statistik s ukládáním a zobrazením top skóre.
>>>>>>> 91c476a88a13be1b76f01f6f69a56242ea37c33d
