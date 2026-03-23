Dokumentace k projektu: Kámen, nůžky, papír
Uživatelská příručka (User Guide)
Tento program je interaktivní hra, která běží v příkazovém řádku a umožňuje ti hrát proti náhodným tahům počítače.

Jak program používat:

Zadání vstupu: Po spuštění programu napiš svou volbu: kamen, nuzky nebo papir.

Tolerance písmen: Program automaticky převádí tvůj text na malá písmena, takže můžeš psát i s velkými (např. "Kamen").

Souboj: Počítač okamžitě náhodně vybere svou zbraň a zobrazí ji na obrazovce.

Vyhodnocení: Program porovná tvůj tah s počítačem a oznámí ti, zda jsi vyhrál, prohrál, nebo zda je to remíza.

Ukončení: Hra běží v nekonečné smyčce. Pokud chceš skončit, stačí napsat slovo konec.

Technický popis
Program je vytvořen v jazyce Python a využívá základní principy programování pro zpracování herní logiky.

Struktura a fungování:

Knihovna random: Program využívá modul random a funkci choice(), aby zajistil nepředvídatelné chování počítače.

Vstupy a ošetření: Pomocí funkce input() a metody .lower() program načítá data od uživatele a sjednocuje je pro snadné porovnávání.

Hlavní smyčka (while True): Tato část kódu zajišťuje, že se hra po každém kole nerestartuje, ale běží dál, dokud není splněna podmínka pro break (příkaz "konec").

Podmínky (if-elif-else): * Nejdříve se kontroluje shoda pro Remízu.

Následně jsou definovány tři konkrétní scénáře, kdy Hráč vyhrává (kámen vs nůžky, nůžky vs papír, papír vs kámen).

Všechny ostatní případy jsou vyhodnoceny jako Prohra.

Výpočty: Program pracuje s textovými řetězci uloženými v seznamu choices, které slouží jako základní stavební kameny pro herní logiku.