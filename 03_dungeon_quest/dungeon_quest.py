import random
import time
import os
import msvcrt


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def slow_print(text: str, delay: float = 0.03):
    for ch in text:
        print(ch, end="", flush=True)
        time.sleep(delay)
    print()


# ---------------------------------------------------------------------------
# Datové struktury
# ---------------------------------------------------------------------------

ARMORS = {
    "kožená zbroj": 2,
    "železná zbroj": 4,
    "rytířská zbroj": 6,
}

WEAPONS = {
    "dřevěný meč":   {"damage": (3, 7),   "crit": 0.05},
    "železný meč":   {"damage": (6, 12),  "crit": 0.10},
    "bojová sekera": {"damage": (8, 15),  "crit": 0.15},
    "kouzelná hůlka":{"damage": (10, 20), "crit": 0.25},
    "Michalova dýka":{"damage": (25, 25), "crit": 0.30},
}

ENEMIES = [
    {"name": "Goblin",        "hp": 15,  "damage": (2, 6),   "xp": 10,  "gold": (2, 8)},
    {"name": "Kostlivec",     "hp": 20,  "damage": (3, 8),   "xp": 15,  "gold": (3, 10)},
    {"name": "Troll",         "hp": 35,  "damage": (5, 12),  "xp": 30,  "gold": (8, 18)},
    {"name": "Drak",          "hp": 60,  "damage": (10, 20), "xp": 80,  "gold": (20, 50)},
    {"name": "Temný rytíř",   "hp": 45,  "damage": (7, 15),  "xp": 50,  "gold": (12, 25)},
    {"name": "Michalův hněv", "hp": 100, "damage": (15, 30), "xp": 150, "gold": (50, 100)},
]

SECRET_BOSS = {
    "name": "Temný Arcimág", "hp": 150, "damage": (20, 40),
    "xp": 300, "gold": (100, 200), "is_secret": True,
}

ROOMS = [
    "tmavá chodba", "zaprášená hala", "klenutý sklep",
    "předkovský hrob", "dračí doupě", "kouzelná komnata",
    "pokladnice", "zapomenutá kaple",
]

POTIONS = {"malý lektvar": 20, "velký lektvar": 40, "eliksír života": 70}

SPELLS = {
    "ohnivá koule":    {"damage": (15, 25), "mana": 15, "desc": "Způsobí 15-25 požáru",                 "rarity": "⭐",      "status": "oheň"},
    "ledový šíp":      {"damage": (10, 20), "mana": 10, "desc": "Způsobí 10-20 mrazivého poškození",    "rarity": "⭐",      "status": None},
    "blesk":           {"damage": (20, 35), "mana": 25, "desc": "Silný bleskový útok 20-35 + omráčení", "rarity": "⭐⭐",    "status": "omráčení"},
    "temnota":         {"damage": (30, 50), "mana": 40, "desc": "Prázdnota 30-50 + jed",                "rarity": "⭐⭐⭐",  "status": "jed"},
    "sluneční paprsek":{"damage": (40, 60), "mana": 50, "desc": "Čistá světelná energie 40-60",         "rarity": "⭐⭐⭐⭐","status": None},
}

ARTIFACTS = {
    "Krví zalitá čepel":  {"damage_bonus": 10, "crit_bonus": 0.10, "rarity": "⭐⭐⭐"},
    "Kroužek nemrtavého": {"hp_bonus": 30, "defense_bonus": 2,     "rarity": "⭐⭐⭐⭐"},
    "Plášť stínů":        {"defense_bonus": 3, "evade_bonus": 0.15,"rarity": "⭐⭐⭐"},
    "Amulet Feniksa":     {"hp_regen": 5,                          "rarity": "⭐⭐⭐⭐⭐"},
    "Dračí oko":          {"crit_bonus": 0.20, "damage_bonus": 5,  "rarity": "⭐⭐⭐⭐"},
    "Štít věčnosti":      {"defense_bonus": 4, "hp_bonus": 20,     "rarity": "⭐⭐⭐⭐"},
}

QUOTES = [
    "  💭 'Čas je peníze.' - Benjamin Franklin",
    "  💭 'Život je to, co se vám stane, zatímco si děláte jiné plány.' - John Lennon",
    "  💭 'Buď změnou, kterou chceš vidět ve světě.' - Mahatma Gandhi",
    "  💭 'Štěstí není cíl, ale způsob života.' - Albert Camus",
    "  💭 'Nejlepší způsob, jak předpovědět budoucnost, je ji vytvořit.' - Peter Drucker",
]

PROPHECIES = [
    "  🔮 Vidíš vizi: 'V tmě na tebe čeká zlo...'",
    "  🔮 Slyšíš hlas: 'Připrav se, smrtelník, nebezpečí se blíží!'",
    "  🔮 Cítíš chlad: 'Mocný nepřítel se probouzí...'",
    "  🔮 Vidíš přízrak: 'Ten, který přichází, byl kdysi lidský...'",
    "  🔮 Slyšíš hluk: 'Něco mocného se pohybuje v temnotě...'",
]

ARTIFACT_SYNERGIES = {
    ("Krví zalitá čepel", "Dračí oko"):        {"damage_bonus": 15, "crit_bonus": 0.15,  "name": "⚡ DRAČÍ ÚTOK"},
    ("Plášť stínů", "Kroužek nemrtavého"):     {"defense_bonus": 5, "evade_bonus": 0.10, "name": "👻 STÍNNÁ OCHRANA"},
    ("Amulet Feniksa", "Štít věčnosti"):       {"hp_regen": 8, "hp_bonus": 40,           "name": "🔥 FENIXOVO VZKŘÍŠENÍ"},
}

STATUS_EFFECTS = {
    "jed": {
        "icon": "☠️",
        "damage_per_turn": (3, 7),
        "duration": 3,
        "desc": "Způsobuje 3-7 poškození jedem každé kolo",
    },
    "oheň": {
        "icon": "🔥",
        "damage_per_turn": (5, 10),
        "duration": 2,
        "desc": "Způsobuje 5-10 poškození ohněm každé kolo",
    },
    "omráčení": {
        "icon": "⭐",
        "damage_per_turn": (0, 0),
        "duration": 1,
        "desc": "Nepřítel přeskočí svůj útok",
    },
}

# ---------------------------------------------------------------------------
# Achievement systém
# ---------------------------------------------------------------------------

ACHIEVEMENTS = {
    # Zabíjení
    "prvni_krev":       {"name": "🗡️ První krev",             "desc": "Poraz prvního nepřítele",             "condition": lambda p: p.kills >= 1},
    "lovec":            {"name": "⚔️ Lovec",                  "desc": "Poraz 10 nepřátel",                   "condition": lambda p: p.kills >= 10},
    "valecnik":         {"name": "🔥 Válečník",               "desc": "Poraz 50 nepřátel",                   "condition": lambda p: p.kills >= 50},
    "zabijak":          {"name": "💀 Zabiják",                "desc": "Poraz 100 nepřátel",                  "condition": lambda p: p.kills >= 100},
    # Průzkum
    "pruzkumnik":       {"name": "🗺️ Průzkumník",            "desc": "Navštiv 10 místností",                "condition": lambda p: p.rooms_visited >= 10},
    "dobrodruh":        {"name": "🌍 Dobrodruh",              "desc": "Navštiv 25 místností",                "condition": lambda p: p.rooms_visited >= 25},
    "legenda_dungeonu": {"name": "🏰 Legenda dungeonů",       "desc": "Navštiv 50 místností",                "condition": lambda p: p.rooms_visited >= 50},
    # Levely
    "zkusen":           {"name": "📈 Zkušený",                "desc": "Dosáhni úrovně 5",                    "condition": lambda p: p.level >= 5},
    "mocny":            {"name": "⚡ Mocný",                  "desc": "Dosáhni úrovně 10",                   "condition": lambda p: p.level >= 10},
    "nesmrtelny":       {"name": "✨ Nesmrtelný",             "desc": "Dosáhni úrovně 20",                   "condition": lambda p: p.level >= 20},
    # Zlato
    "obchodnik":        {"name": "💰 Obchodník",              "desc": "Nashromáždi 500 zlatých",             "condition": lambda p: p.gold >= 500},
    "bohac":            {"name": "👑 Boháč",                  "desc": "Nashromáždi 1000 zlatých",            "condition": lambda p: p.gold >= 1000},
    # Speciální nepřátelé
    "drakobijce":       {"name": "🐉 Drakobijce",            "desc": "Poraz Draka",                         "condition": lambda p: "Drak" in p.defeated_enemies},
    "rytir_tmy":        {"name": "🌑 Rytíř tmy",             "desc": "Poraz Temného rytíře",                "condition": lambda p: "Temný rytíř" in p.defeated_enemies},
    "tajny_boss":       {"name": "🔮 Arcimágův přemožitel",  "desc": "Poraz tajného bosse",                 "condition": lambda p: "Temný Arcimág" in p.defeated_enemies},
    # Artefakty
    "sberatel":         {"name": "💎 Sběratel",               "desc": "Získej 3 artefakty",                  "condition": lambda p: len(p.artifacts) >= 3},
    "mistr_artefaktu":  {"name": "🌟 Mistr artefaktů",       "desc": "Získej všechny artefakty",            "condition": lambda p: len(p.artifacts) >= len(ARTIFACTS)},
    # Kouzla
    "kouzelnik":        {"name": "🔮 Kouzelník",              "desc": "Nauč se 3 kouzla",                    "condition": lambda p: len(p.learned_spells) >= 3},
    # Přežití
    "posledni_vzdech":  {"name": "💪 Poslední vzdech",        "desc": "Přežij díky Last Stand",              "condition": lambda p: p.last_stand_used},
    # Společník
    "pritel_zvirat":    {"name": "🦸 Přítel zvířat",         "desc": "Získej společníka",                   "condition": lambda p: p.companion is not None},
}

# ---------------------------------------------------------------------------
# Společníci
# ---------------------------------------------------------------------------

COMPANIONS = {
    "Luč":          {"damage": (3, 8),   "heal": 5,  "desc": "Malý skřítek, léčí tě po každém kole.", "rarity": "⭐⭐"},
    "Stín":         {"damage": (5, 10),  "heal": 0,  "desc": "Temný duch, způsobuje extra poškození.", "rarity": "⭐⭐⭐"},
    "Ohnivá koule": {"damage": (8, 15),  "heal": 0,  "desc": "Magický elementál, silný útok.",         "rarity": "⭐⭐⭐⭐"},
    "Zlatý dráček": {"damage": (4, 6),   "heal": 10, "desc": "Drahocenný dráček, léčí více HP.",       "rarity": "⭐⭐⭐⭐⭐"},
}

QUESTS = [
    {"type": "kill",  "target": "Goblin", "amount": 3,   "reward_xp": 30, "reward_gold": 20},
    {"type": "kill",  "target": "Troll",  "amount": 2,   "reward_xp": 50, "reward_gold": 40},
    {"type": "rooms",                      "amount": 5,   "reward_xp": 25, "reward_gold": 15},
    {"type": "gold",                       "amount": 100, "reward_xp": 40, "reward_gold": 0},
]

# ---------------------------------------------------------------------------
# Hráč
# ---------------------------------------------------------------------------

class Player:
    def __init__(self, name: str):
        self.name = name
        self.hp = 100
        self.max_hp = 100
        self.gold = 10
        self.xp = 0
        self.level = 1
        self.weapon = "dřevěný meč"
        self.inventory: dict[str, int] = {"malý lektvar": 2}
        self.kills = 0
        self.rooms_visited = 0
        self.armor = "kožená zbroj"
        self.quest = None
        self.quest_progress = 0
        self.artifacts: list[str] = []
        self.companion: str | None = None
        self.mana = 50
        self.max_mana = 50
        self.learned_spells: list[str] = ["ohnivá koule"]
        self.last_stand_used = False
        self.prophecies_count = 0
        self.active_statuses: dict[str, int] = {}
        # --- Achievement systém ---
        self.achievements: list[str] = []
        self.defeated_enemies: list[str] = []

    def xp_to_next(self) -> int:
        return self.level * 50

    def gain_xp(self, amount: int):
        self.xp += amount
        while self.xp >= self.xp_to_next():
            self.xp -= self.xp_to_next()
            self.level += 1
            bonus = random.randint(10, 20)
            self.max_hp += bonus
            self.mana += 5
            self.hp = min(self.hp + bonus, self.max_hp)
            self.mana = min(self.mana + 5, self.max_mana)
            slow_print(f"\n✨ Postoupil jsi na úroveň {self.level}! +{bonus} max HP +5 max mana")
            check_achievements(self)  # <-- achievement check po level upu

    def attack(self) -> tuple[int, bool]:
        w = WEAPONS[self.weapon]
        dmg = random.randint(*w["damage"]) + self.level
        for artifact in self.artifacts:
            if "damage_bonus" in ARTIFACTS[artifact]:
                dmg += ARTIFACTS[artifact]["damage_bonus"]
        synergy_bonus = self._get_synergy_bonus()
        if synergy_bonus and "damage_bonus" in synergy_bonus:
            dmg += synergy_bonus["damage_bonus"]
        crit_chance = w["crit"]
        for artifact in self.artifacts:
            if "crit_bonus" in ARTIFACTS[artifact]:
                crit_chance += ARTIFACTS[artifact]["crit_bonus"]
        if synergy_bonus and "crit_bonus" in synergy_bonus:
            crit_chance += synergy_bonus["crit_bonus"]
        crit = random.random() < crit_chance
        if crit:
            dmg = int(dmg * 2)
        return dmg, crit

    def _get_synergy_bonus(self) -> dict:
        for artifacts_combo, bonuses in ARTIFACT_SYNERGIES.items():
            if all(art in self.artifacts for art in artifacts_combo):
                return bonuses
        return None

    def get_active_synergies(self) -> list[str]:
        active = []
        for artifacts_combo, bonuses in ARTIFACT_SYNERGIES.items():
            if all(art in self.artifacts for art in artifacts_combo):
                active.append(bonuses["name"])
        return active

    def use_potion(self) -> bool:
        available = {k: v for k, v in self.inventory.items() if v > 0}
        if not available:
            print("  Nemáš žádné lektvary!")
            return False
        print("\n  Dostupné lektvary:")
        items = list(available.keys())
        for i, name in enumerate(items, 1):
            print(f"  {i}. {name} (x{self.inventory[name]}) – léčí {POTIONS[name]} HP")
        choice = input("  Vyber (číslo nebo Enter pro zrušení): ").strip()
        if not choice.isdigit() or not (1 <= int(choice) <= len(items)):
            return False
        potion = items[int(choice) - 1]
        heal = POTIONS[potion]
        self.hp = min(self.hp + heal, self.max_hp)
        self.inventory[potion] -= 1
        slow_print(f"  🧪 Vypil jsi {potion} a obnovil {heal} HP. HP: {self.hp}/{self.max_hp}")
        return True

    def status(self):
        bar_len = 20
        filled = int(bar_len * self.hp / self.max_hp)
        bar = "█" * filled + "░" * (bar_len - filled)
        print(f"\n  👤 {self.name}  |  Úroveň {self.level}  |  XP: {self.xp}/{self.xp_to_next()}")
        print(f"  ❤️  [{bar}] {self.hp}/{self.max_hp}")
        print(f"  ⚔️  {self.weapon}  |  💰 {self.gold} zlatých")
        print(f"  💧 Mana: {self.mana}/{self.max_mana}")
        inv = ", ".join(f"{k}×{v}" for k, v in self.inventory.items() if v > 0)
        print(f"  🎒 {inv or 'prázdné'}")
        if self.artifacts:
            artifacts_str = ", ".join(f"{a} {ARTIFACTS[a]['rarity']}" for a in self.artifacts)
            print(f"  💎 Artefakty: {artifacts_str}")
        synergies = self.get_active_synergies()
        if synergies:
            print(f"  ⚡ AKTIVNÍ SYNERGIÍ: {', '.join(synergies)}")
        if self.companion:
            comp = COMPANIONS[self.companion]
            print(f"  🦸 Společník: {self.companion} {comp['rarity']}")
        if self.achievements:
            print(f"  🏅 Achievementy: {len(self.achievements)}/{len(ACHIEVEMENTS)}")
        if self.quest:
            if self.quest["type"] == "kill":
                print(f"  📜 Zabij {self.quest_progress}/{self.quest['amount']} {self.quest['target']}")
            elif self.quest["type"] == "rooms":
                print(f"  📜 Navštiv {self.quest_progress}/{self.quest['amount']} místností")
            elif self.quest["type"] == "gold":
                print(f"  📜 Získej {self.quest_progress}/{self.quest['amount']} zlata")

    def take_damage(self, dmg: int):
        defense = ARMORS[self.armor]
        for artifact in self.artifacts:
            if "defense_bonus" in ARTIFACTS[artifact]:
                defense += ARTIFACTS[artifact]["defense_bonus"]
        synergy_bonus = self._get_synergy_bonus()
        if synergy_bonus and "defense_bonus" in synergy_bonus:
            defense += synergy_bonus["defense_bonus"]
        real_dmg = max(1, dmg - defense)
        self.hp -= real_dmg
        return real_dmg

    def apply_status(self, effect: str):
        duration = STATUS_EFFECTS[effect]["duration"]
        self.active_statuses[effect] = duration
        icon = STATUS_EFFECTS[effect]["icon"]
        slow_print(f"  {icon} Byl jsi zasažen efektem: {effect.upper()}! ({duration} kola)")

    def tick_statuses(self) -> int:
        total_dmg = 0
        expired = []
        for effect, turns_left in self.active_statuses.items():
            info = STATUS_EFFECTS[effect]
            dmg = random.randint(*info["damage_per_turn"])
            if dmg > 0:
                self.hp -= dmg
                total_dmg += dmg
                slow_print(f"  {info['icon']} {effect.upper()} způsobil {dmg} poškození! HP: {self.hp}/{self.max_hp}")
            self.active_statuses[effect] = turns_left - 1
            if turns_left - 1 <= 0:
                expired.append(effect)
        for e in expired:
            del self.active_statuses[e]
            slow_print(f"  ✓ Efekt {e} skončil.")
        return total_dmg


# ---------------------------------------------------------------------------
# Achievement systém – funkce
# ---------------------------------------------------------------------------

def check_achievements(player: Player):
    """Zkontroluje a odemkne nové achievementy. Volá se po každé klíčové akci."""
    for key, ach in ACHIEVEMENTS.items():
        if key not in player.achievements:
            try:
                if ach["condition"](player):
                    player.achievements.append(key)
                    slow_print(f"\n{'=' * 50}")
                    slow_print(f"  🏅 ACHIEVEMENT ODEMČEN: {ach['name']}")
                    slow_print(f"  {ach['desc']}")
                    slow_print(f"{'=' * 50}")
            except Exception:
                pass


# ---------------------------------------------------------------------------
# Stavové efekty pro nepřítele
# ---------------------------------------------------------------------------

def apply_enemy_status(enemy: dict, effect: str):
    if "statuses" not in enemy:
        enemy["statuses"] = {}
    duration = STATUS_EFFECTS[effect]["duration"]
    enemy["statuses"][effect] = duration
    icon = STATUS_EFFECTS[effect]["icon"]
    slow_print(f"  {icon} {enemy['name']} byl zasažen efektem: {effect.upper()}! ({duration} kola)")


def tick_enemy_statuses(enemy: dict) -> tuple[int, bool]:
    if "statuses" not in enemy:
        return 0, False
    total_dmg = 0
    stunned = False
    expired = []
    for effect, turns_left in enemy["statuses"].items():
        info = STATUS_EFFECTS[effect]
        dmg = random.randint(*info["damage_per_turn"])
        if dmg > 0:
            enemy["hp"] -= dmg
            total_dmg += dmg
            slow_print(f"  {info['icon']} {effect.upper()} způsobil {enemy['name']} {dmg} poškození! HP: {enemy['hp']}")
        if effect == "omráčení":
            stunned = True
            slow_print(f"  ⭐ {enemy['name']} je omráčen a přeskočí útok!")
        enemy["statuses"][effect] = turns_left - 1
        if turns_left - 1 <= 0:
            expired.append(effect)
    for e in expired:
        del enemy["statuses"][e]
        slow_print(f"  ✓ Efekt {e} na {enemy['name']} skončil.")
    return total_dmg, stunned


# ---------------------------------------------------------------------------
# Proroctví
# ---------------------------------------------------------------------------

def trigger_prophecy(player: Player):
    if random.random() < 0.3 and player.prophecies_count < 3:
        player.prophecies_count += 1
        slow_print(random.choice(PROPHECIES))
        time.sleep(1)


# ---------------------------------------------------------------------------
# Boj
# ---------------------------------------------------------------------------

def _run_battle_turn(player: Player, enemy: dict) -> str:
    """Zpracuje jeden tah hráče. Vrátí: 'continue', 'fled', 'invalid'."""
    # Stavové efekty hráče
    player.tick_statuses()
    if player.hp <= 0:
        return "continue"

    # Stavové efekty nepřítele
    _, enemy_stunned = tick_enemy_statuses(enemy)
    if enemy["hp"] <= 0:
        return "continue"

    print(f"\n  Ty: {player.hp} HP", end="")
    if player.active_statuses:
        icons = " ".join(STATUS_EFFECTS[s]["icon"] for s in player.active_statuses)
        print(f" {icons}", end="")
    print(f"  |  {enemy['name']}: {enemy['hp']} HP")
    print("  [1] Útok  [2] Lektvar  [3] Útěk  [4] Obchod  [5] Vybavení  [6] Kouzla  [7] Nečinnost")
    action = input("  > ").strip()

    if action == "1":
        dmg, crit = player.attack()
        enemy["hp"] -= dmg
        slow_print(f"  {'💥 KRITICKÝ ZÁSAH! ' if crit else ''}Zasáhl jsi za {dmg} poškození.")
        if player.companion:
            comp = COMPANIONS[player.companion]
            comp_dmg = random.randint(*comp["damage"])
            enemy["hp"] -= comp_dmg
            slow_print(f"  🦸 {player.companion} útočí za {comp_dmg} poškození!")
            if comp["heal"] > 0:
                old_hp = player.hp
                player.hp = min(player.hp + comp["heal"], player.max_hp)
                if player.hp > old_hp:
                    slow_print(f"  💚 {player.companion} tě vyléčil o {player.hp - old_hp} HP!")

    elif action == "2":
        player.use_potion()

    elif action == "3":
        evade_chance = 0.6
        for artifact in player.artifacts:
            if "evade_bonus" in ARTIFACTS[artifact]:
                evade_chance += ARTIFACTS[artifact]["evade_bonus"]
        if random.random() < evade_chance:
            slow_print("  🏃 Podařilo se ti utéct!")
            return "fled"
        slow_print("  Útěk se nezdařil!")

    elif action == "4":
        shop(player)

    elif action == "5":
        equipment_manager(player)

    elif action == "6":
        cast_spell(player, enemy)

    elif action == "7":
        slow_print("  Vstoupil jsi do AFK režimu...")
        while True:
            print(random.choice(QUOTES))
            print("  Stiskni 1 pro návrat do hry, nebo jinou klávesu pro další quote...", end="", flush=True)
            key = msvcrt.getwch()
            print()
            if key == "1":
                slow_print("  Vrátil ses do hry!")
                break
            time.sleep(0.5)
    else:
        slow_print("  Neplatná volba, přišel jsi o tah!")

    # Útok nepřítele
    if enemy["hp"] > 0 and not enemy_stunned:
        e_dmg = random.randint(*enemy["damage"])
        real = player.take_damage(e_dmg)
        slow_print(f"  {enemy['name']} tě zasáhl za {real} poškození!")

    return "continue"


def battle(player: Player, enemy_template: dict) -> bool:
    enemy = dict(enemy_template)
    is_secret_boss = enemy_template.get("is_secret", False)
    if is_secret_boss:
        slow_print("\n" + "=" * 50)
        slow_print("⚡ ⚡ ⚡ NEOČEKÁVANÝ STŘET! ⚡ ⚡ ⚡")
        time.sleep(1)

    slow_print(f"\n⚔️  Narazil jsi na {enemy['name']}! (HP: {enemy['hp']})")
    trigger_prophecy(player)

    while player.hp > 0 and enemy["hp"] > 0:
        result = _run_battle_turn(player, enemy)
        if result == "fled":
            return False

    # Poslední vdech
    if player.hp <= 0 and not player.last_stand_used:
        if random.random() < 0.4:
            player.last_stand_used = True
            player.hp = player.max_hp // 2
            slow_print("\n" + "=" * 50)
            slow_print("🔥 POSLEDNÍ VDECH! 🔥")
            slow_print(f"  Podařilo se ti vstát! Obnovil jsi {player.hp} HP!")
            slow_print("=" * 50)
            check_achievements(player)  # achievement za last stand
            while player.hp > 0 and enemy["hp"] > 0:
                result = _run_battle_turn(player, enemy)
                if result == "fled":
                    return False

    if player.hp <= 0:
        return False

    # Vítězství
    gold = random.randint(*enemy["gold"])
    player.gold += gold
    player.gain_xp(enemy["xp"])
    player.kills += 1
    player.defeated_enemies.append(enemy["name"])  # <-- pro achievement drakobijce atd.
    update_quest(player, "kill", enemy["name"])
    check_achievements(player)                      # <-- achievement check po zabití
    slow_print(f"\n  🏆 Porazil jsi {enemy['name']}! Získal jsi {gold} zlatých a {enemy['xp']} XP.")
    return True


# ---------------------------------------------------------------------------
# Kouzelnický systém
# ---------------------------------------------------------------------------

def cast_spell(player: Player, enemy: dict):
    if not player.learned_spells:
        slow_print("  Nemáš žádná kouzla!")
        return
    slow_print("\n🔮 DOSTUPNÁ KOUZLA:")
    for i, spell_name in enumerate(player.learned_spells, 1):
        spell = SPELLS[spell_name]
        status_note = f" | ☠ Efekt: {spell['status']}" if spell.get("status") else ""
        print(f"  {i}. {spell_name} {spell['rarity']} – {spell['desc']}{status_note}")
        print(f"      Poškození: {spell['damage']} | Mana: {spell['mana']}")
    print(f"\n  💧 Tvoje mana: {player.mana}/{player.max_mana}")
    print("  (Enter = zpět)")
    choice = input("  > ").strip()
    if not choice.isdigit():
        return
    idx = int(choice) - 1
    if idx < 0 or idx >= len(player.learned_spells):
        return
    spell_name = player.learned_spells[idx]
    spell = SPELLS[spell_name]
    if player.mana < spell["mana"]:
        slow_print(f"  ❌ Nemáš dostatek many! Potřebuješ {spell['mana']}, máš {player.mana}")
        return
    player.mana -= spell["mana"]
    dmg = random.randint(*spell["damage"])
    enemy["hp"] -= dmg
    slow_print(f"  ✨ Seslal jsi {spell_name}! Způsobil jsi {dmg} magického poškození!")
    if spell.get("status"):
        apply_enemy_status(enemy, spell["status"])


def spell_shop(player: Player):
    slow_print("\n🔮 KOUZELNICKÝ OBCHOD!")
    slow_print("  Můžeš se naučit nová kouzla:\n")
    available_spells = [s for s in SPELLS.keys() if s not in player.learned_spells]
    if not available_spells:
        slow_print("  Znáš už všechna dostupná kouzla!")
        return
    options = []
    for i, spell_name in enumerate(available_spells, 1):
        spell = SPELLS[spell_name]
        price = (i * 30) + 20
        options.append((spell_name, price, spell))
        print(f"  {i}. {spell_name} {spell['rarity']}")
        print(f"     {spell['desc']}")
        print(f"     Poškození: {spell['damage']} | Mana: {spell['mana']} | Cena: {price} zlatých")
        print()
    print(f"  Máš {player.gold} zlatých. (Enter = odejít)")
    choice = input("  > ").strip()
    if not choice.isdigit() or not (1 <= int(choice) <= len(options)):
        return
    spell_name, price, _ = options[int(choice) - 1]
    if player.gold < price:
        slow_print("  Nemáš dost zlatých!")
        return
    player.gold -= price
    player.learned_spells.append(spell_name)
    slow_print(f"  ✅ Naučil jsi se kouzlo: {spell_name}!")
    check_achievements(player)  # <-- achievement za kouzla


def mystic_chest(player: Player):
    slow_print("\n📦 Našel jsi starou mystickou truhlu!")
    choice = input("  Otevřít truhlu? (Enter = ano, n = ne): ").strip().lower()
    if choice == "n":
        slow_print("  Opatrně ji obcházíš a pokračuješ dál.")
        return
    if random.random() < 0.75:
        reward_type = random.choice(["gold", "potion", "artifact"])
        if reward_type == "gold":
            gold = random.randint(25, 60)
            player.gold += gold
            update_quest(player, "gold", gold)
            check_achievements(player)
            slow_print(f"  💰 Truhla obsahovala {gold} zlatých!")
        elif reward_type == "potion":
            potion = random.choice(list(POTIONS.keys()))
            player.inventory[potion] = player.inventory.get(potion, 0) + 1
            slow_print(f"  🧪 Našel jsi {potion} v truhle!")
        else:
            artifact = random.choice(list(ARTIFACTS.keys()))
            if artifact not in player.artifacts:
                player.artifacts.append(artifact)
                slow_print(f"  💎 Truhla obsahovala artefakt: {artifact} {ARTIFACTS[artifact]['rarity']}!")
                synergies = player.get_active_synergies()
                if synergies:
                    slow_print(f"\n✨ NOVÁ SYNERGIE AKTIVOVÁNA: {', '.join(synergies)}!")
                check_achievements(player)
            else:
                gold = random.randint(20, 40)
                player.gold += gold
                slow_print(f"  Artefakt jsi již měl. Truhla ti místo něj dala {gold} zlatých.")
    else:
        trap_damage = random.randint(10, 25)
        player.hp = max(1, player.hp - trap_damage)
        slow_print(f"  ⚠️ Je to past! Utrpěl jsi {trap_damage} poškození.")
        slow_print(f"  Tvoje HP: {player.hp}/{player.max_hp}")


# ---------------------------------------------------------------------------
# Obchod
# ---------------------------------------------------------------------------

def shop(player: Player):
    slow_print("\n🛒 Vítej v obchodě!\n")
    options = []
    for name, info in WEAPONS.items():
        if name != player.weapon:
            price = list(WEAPONS.keys()).index(name) * 20 + 15
            options.append(("weapon", name, price, f"Zbraň: {name} (poškození {info['damage']})"))
    for armor_name, defense in ARMORS.items():
        if armor_name != player.armor:
            price = (defense - 1) * 40 + 50
            options.append(("armor", armor_name, price, f"Zbroj: {armor_name} (obrana +{defense})"))
    for potion, heal in POTIONS.items():
        price = heal // 2
        options.append(("potion", potion, price, f"Lektvar: {potion} (léčí {heal} HP)"))
    for i, (_, name, price, desc) in enumerate(options, 1):
        print(f"  {i}. {desc} – {price} zlatých")
    print(f"\n  Máš {player.gold} zlatých. (Enter = odejít)")
    choice = input("  > ").strip()
    if not choice.isdigit() or not (1 <= int(choice) <= len(options)):
        return
    kind, name, price, _ = options[int(choice) - 1]
    if player.gold < price:
        slow_print("  Nemáš dost zlatých mincí!")
        return
    player.gold -= price
    if kind == "weapon":
        player.weapon = name
    elif kind == "armor":
        player.armor = name
    else:
        player.inventory[name] = player.inventory.get(name, 0) + 1
    slow_print(f"  Koupil jsi {name}!")
    check_achievements(player)  # <-- achievement za zlato (po utrácení)


# ---------------------------------------------------------------------------
# Správa vybavení
# ---------------------------------------------------------------------------

def equipment_manager(player: Player):
    while True:
        slow_print("\n⚙️  SPRÁVA VYBAVENÍ")
        slow_print(f"\n  Aktuálně vybaveno:")
        slow_print(f"    ⚔️  Zbraň: {player.weapon}")
        slow_print(f"    🛡️  Zbroj: {player.armor}")
        slow_print(f"\n  [1] Přepnout zbraň  [2] Přepnout zbroj  [3] Zpět")
        choice = input("  > ").strip()
        if choice == "1":
            available_weapons = list(WEAPONS.keys())
            slow_print("\n  Dostupné zbraně:")
            for i, weapon in enumerate(available_weapons, 1):
                marker = "✓" if weapon == player.weapon else " "
                print(f"    [{marker}] {i}. {weapon} (poškození {WEAPONS[weapon]['damage']})")
            try:
                w_choice = int(input("\n  Vyber (číslo): ").strip())
                if 1 <= w_choice <= len(available_weapons):
                    player.weapon = available_weapons[w_choice - 1]
                    slow_print(f"  ✓ Vybral si {player.weapon}!")
            except Exception:
                slow_print("  Neplatný výběr!")
        elif choice == "2":
            available_armors = list(ARMORS.keys())
            slow_print("\n  Dostupné zbroje:")
            for i, armor in enumerate(available_armors, 1):
                marker = "✓" if armor == player.armor else " "
                defense = ARMORS[armor]
                print(f"    [{marker}] {i}. {armor} (obrana +{defense})")
            try:
                a_choice = int(input("\n  Vyber (číslo): ").strip())
                if 1 <= a_choice <= len(available_armors):
                    player.armor = available_armors[a_choice - 1]
                    slow_print(f"  ✓ Vybral si {player.armor}!")
            except Exception:
                slow_print("  Neplatný výběr!")
        elif choice == "3":
            break
        else:
            slow_print("  Neplatná volba!")


# ---------------------------------------------------------------------------
# Quest systém
# ---------------------------------------------------------------------------

def new_quest(player: Player):
    player.quest = random.choice(QUESTS).copy()
    player.quest_progress = 0
    slow_print("\n📜 Nový quest!")
    if player.quest["type"] == "kill":
        slow_print(f"  Zabij {player.quest['amount']}x {player.quest['target']}")
    elif player.quest["type"] == "rooms":
        slow_print(f"  Navštiv {player.quest['amount']} místností")
    elif player.quest["type"] == "gold":
        slow_print(f"  Získej {player.quest['amount']} zlata")


def update_quest(player: Player, event_type: str, value=None):
    if not player.quest:
        return
    q = player.quest
    if q["type"] == "kill" and event_type == "kill":
        if value == q["target"]:
            player.quest_progress += 1
    elif q["type"] == "rooms" and event_type == "room":
        player.quest_progress += 1
    elif q["type"] == "gold" and event_type == "gold":
        player.quest_progress += value
    check_quest_complete(player)


def check_quest_complete(player: Player):
    q = player.quest
    if not q:
        return
    if player.quest_progress >= q["amount"]:
        slow_print("\n🏆 QUEST SPLNĚN!")
        player.gold += q["reward_gold"]
        player.gain_xp(q["reward_xp"])
        slow_print(f"  Odměna: {q['reward_gold']} gold, {q['reward_xp']} XP")
        player.quest = None
        player.quest_progress = 0
        new_quest(player)


# ---------------------------------------------------------------------------
# Statistiky a ukládání
# ---------------------------------------------------------------------------

def save_stats(player: Player, survived: bool):
    import json
    stats_file = "game_stats.json"
    stats = {
        "jméno": player.name,
        "úroveň": player.level,
        "zabití_nepřátelé": player.kills,
        "navštívené_místnosti": player.rooms_visited,
        "zlato": player.gold,
        "přežil": survived,
        "achievementy": player.achievements,           # <-- uložení achievementů
        "achievementy_počet": len(player.achievements),
    }
    try:
        with open(stats_file, "r", encoding="utf-8") as f:
            all_stats = json.load(f)
    except Exception:
        all_stats = []
    all_stats.append(stats)
    with open(stats_file, "w", encoding="utf-8") as f:
        json.dump(all_stats, f, ensure_ascii=False, indent=2)


def save_game(player: Player):
    import json
    save_file = "save_game.json"
    save_data = {
        "name": player.name,
        "hp": player.hp,
        "max_hp": player.max_hp,
        "gold": player.gold,
        "xp": player.xp,
        "level": player.level,
        "weapon": player.weapon,
        "inventory": player.inventory,
        "kills": player.kills,
        "rooms_visited": player.rooms_visited,
        "armor": player.armor,
        "quest": player.quest,
        "quest_progress": player.quest_progress,
        "artifacts": player.artifacts,
        "companion": player.companion,
        "mana": player.mana,
        "max_mana": player.max_mana,
        "learned_spells": player.learned_spells,
        "last_stand_used": player.last_stand_used,
        "prophecies_count": player.prophecies_count,
        "achievements": player.achievements,          # <-- nové
        "defeated_enemies": player.defeated_enemies,  # <-- nové
    }
    with open(save_file, "w", encoding="utf-8") as f:
        json.dump(save_data, f, ensure_ascii=False, indent=2)
    slow_print("  💾 Hra uložena!")


def load_game():
    import json
    save_file = "save_game.json"
    try:
        with open(save_file, "r", encoding="utf-8") as f:
            save_data = json.load(f)
        player = Player(save_data["name"])
        player.hp = save_data["hp"]
        player.max_hp = save_data["max_hp"]
        player.gold = save_data["gold"]
        player.xp = save_data["xp"]
        player.level = save_data["level"]
        player.weapon = save_data["weapon"]
        player.inventory = save_data["inventory"]
        player.kills = save_data["kills"]
        player.rooms_visited = save_data["rooms_visited"]
        player.armor = save_data["armor"]
        player.quest = save_data["quest"]
        player.quest_progress = save_data["quest_progress"]
        player.artifacts = save_data["artifacts"]
        player.companion = save_data["companion"]
        player.mana = save_data["mana"]
        player.max_mana = save_data["max_mana"]
        player.learned_spells = save_data["learned_spells"]
        player.last_stand_used = save_data["last_stand_used"]
        player.prophecies_count = save_data["prophecies_count"]
        player.achievements = save_data.get("achievements", [])         # <-- nové
        player.defeated_enemies = save_data.get("defeated_enemies", []) # <-- nové
        slow_print("  📂 Hra načtena!")
        return player
    except FileNotFoundError:
        slow_print("  ❌ Žádná uložená hra nebyla nalezena!")
        return None
    except Exception as e:
        slow_print(f"  ❌ Chyba při načítání hry: {e}")
        return None


def show_stats():
    import json
    stats_file = "game_stats.json"
    try:
        with open(stats_file, "r", encoding="utf-8") as f:
            all_stats = json.load(f)
    except Exception:
        slow_print("\n  Žádné statistiky zatím nejsou!")
        return
    if not all_stats:
        slow_print("\n  Žádné statistiky zatím nejsou!")
        return
    sorted_stats = sorted(all_stats, key=lambda x: x["úroveň"], reverse=True)
    slow_print("\n📊 TOP 5 NEJLEPŠÍCH SKÓRE:")
    for i, stat in enumerate(sorted_stats[:5], 1):
        status = "✓ PŘEŽIL" if stat["přežil"] else "✗ Padl"
        achs = stat.get("achievementy_počet", 0)
        slow_print(f"  {i}. {stat['jméno']:15} | Úroveň {stat['úroveň']:3} | Zabití: {stat['zabití_nepřátelé']:3} | 🏅 {achs}/{len(ACHIEVEMENTS)} | {status}")


# ---------------------------------------------------------------------------
# Hlavní smyčka
# ---------------------------------------------------------------------------

def main():
    clear()
    slow_print("=" * 50)
    slow_print("        🗡️   DUNGEON QUEST   🗡️")
    slow_print("=" * 50)
    while True:
        slow_print("\n  [1] Nová hra")
        slow_print("  [2] Načíst hru")
        slow_print("  [3] Zobrazit statistiky")
        slow_print("  [4] Konec")
        menu_choice = input("  > ").strip()
        if menu_choice == "1":
            break
        elif menu_choice == "2":
            player = load_game()
            if player:
                slow_print(f"\nVítej zpět, {player.name}! Pokračuješ v dungeonu...\n")
                time.sleep(1)
                game_loop(player)
                return
        elif menu_choice == "3":
            show_stats()
        elif menu_choice == "4":
            slow_print("\n  Nashledanou!")
            return

    name = input("\nZadej jméno svého hrdiny: ").strip() or "Hrdina"
    player = Player(name)
    new_quest(player)
    slow_print(f"\nVítej, {player.name}! Vstupuješ do dungeonů...\n")
    time.sleep(1)
    game_loop(player)


def game_loop(player: Player):
    while player.hp > 0:
        room = random.choice(ROOMS)
        player.rooms_visited += 1
        update_quest(player, "room")
        slow_print(f"\n🚪 Vstoupil jsi do: {room.upper()}")

        for artifact in player.artifacts:
            if "hp_regen" in ARTIFACTS[artifact]:
                regen = ARTIFACTS[artifact]["hp_regen"]
                old_hp = player.hp
                player.hp = min(player.hp + regen, player.max_hp)
                if player.hp > old_hp:
                    slow_print(f"  ✨ {artifact} tě regeneruje o {player.hp - old_hp} HP!")

        player.status()
        check_achievements(player)  # <-- achievement check po každé místnosti

        roll = random.random()

        if roll < 0.01 and player.level >= 5:
            survived = battle(player, SECRET_BOSS)
            if not survived and player.hp <= 0:
                break
        elif roll < 0.55:
            enemy = random.choice(ENEMIES)
            survived = battle(player, enemy)
            if not survived and player.hp <= 0:
                break
        elif roll < 0.70:
            slow_print("\n🏪 Narazil jsi na obchodníka!")
            shop(player)
        elif roll < 0.78:
            slow_print("\n🔮 Narazil jsi na kouzelníka!")
            spell_shop(player)
        elif roll < 0.95:
            gold = random.randint(10, 30)
            player.gold += gold
            update_quest(player, "gold", gold)
            check_achievements(player)
            slow_print(f"\n💰 Našel jsi {gold} zlatých na zemi!")
        elif roll < 0.97:
            artifact = random.choice(list(ARTIFACTS.keys()))
            if artifact not in player.artifacts:
                player.artifacts.append(artifact)
                slow_print(f"\n💎 LEGENDÁRNÍ ARTEFAKT! Našel jsi: {artifact} {ARTIFACTS[artifact]['rarity']}")
                synergies = player.get_active_synergies()
                if synergies:
                    slow_print(f"\n✨ NOVÁ SYNERGIE AKTIVOVÁNA: {', '.join(synergies)}!")
                check_achievements(player)
            else:
                player.gold += 50
                slow_print(f"\n💎 Artefakt jsi již měl. Dostals 50 zlatých.")
        elif roll < 0.98:
            slow_print("\n🌊 Narazil jsi na mystickou fontánu!")
            restored_hp = min(30, player.max_hp - player.hp)
            restored_mana = min(20, player.max_mana - player.mana)
            player.hp += restored_hp
            player.mana += restored_mana
            slow_print(f"  ✓ Obnovil jsi {restored_hp} HP a {restored_mana} many.")
            if restored_hp == 0 and restored_mana == 0:
                slow_print("  Fontána ti nic nedala, ale její klid tě uklidnil.")
        elif roll < 0.99:
            mystic_chest(player)
        else:
            if not player.companion:
                companion = random.choice(list(COMPANIONS.keys()))
                player.companion = companion
                comp = COMPANIONS[companion]
                slow_print(f"\n🦸 NOVÝ SPOLEČNÍK! Připojil se k tobě: {companion} {comp['rarity']}")
                slow_print(f"   {comp['desc']}")
                check_achievements(player)
            else:
                gold = random.randint(15, 40)
                player.gold += gold
                slow_print(f"\n💰 Našel jsi {gold} zlatých v trávě!")

        cont = input("\nPokračovat dál? (Enter = ano, s = uložit, q = konec): ").strip().lower()
        if cont == "q":
            break
        elif cont == "s":
            save_game(player)

    # Konec hry
    slow_print("\n" + "=" * 50)
    survived = player.hp > 0
    if not survived:
        slow_print("💀 Byl jsi poražen! Hra skončila.")
    else:
        slow_print("🏰 Opustil jsi dungeon.")
    slow_print(f"\n📜 Statistiky hrdiny {player.name}:")
    slow_print(f"   Úroveň:               {player.level}")
    slow_print(f"   Zabití nepřátelé:     {player.kills}")
    slow_print(f"   Navštívené místnosti: {player.rooms_visited}")
    slow_print(f"   Zlaté:                {player.gold}")

    # Výpis achievementů
    slow_print(f"\n🏅 ACHIEVEMENTY ({len(player.achievements)}/{len(ACHIEVEMENTS)}):")
    if player.achievements:
        for key in player.achievements:
            ach = ACHIEVEMENTS[key]
            slow_print(f"   {ach['name']}  —  {ach['desc']}")
    else:
        slow_print("   Žádné achievementy tentokrát. Zkus to znovu!")

    slow_print("=" * 50)
    save_stats(player, survived)


if __name__ == "__main__":
    main()