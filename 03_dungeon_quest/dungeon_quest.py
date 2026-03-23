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
 
WEAPONS = {
    "dřevěný meč":  {"damage": (3, 7),  "crit": 0.05},
    "železný meč":  {"damage": (6, 12), "crit": 0.10},
    "bojová sekera": {"damage": (8, 15), "crit": 0.15},
    "kouzelná hůlka": {"damage": (10, 20), "crit": 0.25},
    "Michalova dýka": {"damage": (25, 25), "crit": 0.30},
}
 
ENEMIES = [
    {"name": "Goblin",      "hp": 15, "damage": (2, 6),  "xp": 10, "gold": (2, 8)},
    {"name": "Kostlivec",      "hp": 20, "damage": (3, 8),  "xp": 15, "gold": (3, 10)},
    {"name": "Troll",       "hp": 35, "damage": (5, 12), "xp": 30, "gold": (8, 18)},
    {"name": "Drak",        "hp": 60, "damage": (10, 20),"xp": 80, "gold": (20, 50)},
    {"name": "Temný rytíř", "hp": 45, "damage": (7, 15), "xp": 50, "gold": (12, 25)},
    {"name": "Michalův hněv", "hp": 100,"damage": (15, 30),"xp": 150,"gold": (50, 100)},
]
 
ROOMS = [
    "tmavá chodba",
    "zaprášená hala",
    "klenutý sklep",
    "předkovský hrob",
    "dračí doupě",
    "kouzelná komnata",
    "pokladnice",
    "zapomenutá kaple",
    
]
 
POTIONS = {"malý lektvar": 20, "velký lektvar": 40, "eliksír života": 70}
 
QUOTES = [
    "  💭 'Čas je peníze.' - Benjamin Franklin",
    "  💭 'Život je to, co se vám stane, zatímco si děláte jiné plány.' - John Lennon",
    "  💭 'Buď změnou, kterou chceš vidět ve světě.' - Mahatma Gandhi",
    "  💭 'Štěstí není cíl, ale způsob života.' - Albert Camus",
    "  💭 'Nejlepší způsob, jak předpovědět budoucnost, je ji vytvořit.' - Peter Drucker",
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
 
    def xp_to_next(self) -> int:
        return self.level * 50
 
    def gain_xp(self, amount: int):
        self.xp += amount
        while self.xp >= self.xp_to_next():
            self.xp -= self.xp_to_next()
            self.level += 1
            bonus = random.randint(10, 20)
            self.max_hp += bonus
            self.hp = min(self.hp + bonus, self.max_hp)
            slow_print(f"\n✨ Postoupil jsi na úroveň {self.level}! +{bonus} max HP")
 
    def attack(self) -> tuple[int, bool]:
        w = WEAPONS[self.weapon]
        dmg = random.randint(*w["damage"]) + self.level
        crit = random.random() < w["crit"]
        if crit:
            dmg = int(dmg * 2)
        return dmg, crit
 
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
        inv = ", ".join(f"{k}×{v}" for k, v in self.inventory.items() if v > 0)
        print(f"  🎒 {inv or 'prázdné'}")
 
 
# ---------------------------------------------------------------------------
# Boj
# ---------------------------------------------------------------------------
 
def battle(player: Player, enemy_template: dict) -> bool:
    enemy = dict(enemy_template)
    slow_print(f"\n⚔️  Narazil jsi na {enemy['name']}! (HP: {enemy['hp']})")
 
    while player.hp > 0 and enemy["hp"] > 0:
        print(f"\n  Ty: {player.hp} HP  |  {enemy['name']}: {enemy['hp']} HP")
        print("  [1] Útok  [2] Lektvar  [3] Útěk [4] Obchod [5] nečinnost")
        action = input("  > ").strip()
 
        if action == "1":
            dmg, crit = player.attack()
            enemy["hp"] -= dmg
            msg = f"  {'💥 KRITICKÝ ZÁSAH! ' if crit else ''}Zasáhl jsi za {dmg} poškození."
            slow_print(msg)
 
        elif action == "2":
            player.use_potion()
 
        elif action == "3":
            if random.random() < 0.4:
                slow_print("  🏃 Podařilo se ti utéct!")
                return False
            slow_print("  Útěk se nezdařil!")
        
        elif action == "4":
            shop(player)
        
        elif action == "5":
            slow_print("  Vstupuješ do AFK režimu...")
            print("  AFK režim. stiskni '1' pro návrat do hry.")
            last_quote = time.time()
            while True:
                if msvcrt.kbhit():
                    key = msvcrt.getch().decode('utf-8')
                    if key == '1':
                        slow_print("  Vrátil ses do hry!")
                        break
                current = time.time()
                if current - last_quote >= 30:
                    quote = random.choice(QUOTES)
                    print(quote)
                    last_quote = current
                time.sleep(0.1)
        
        else:
            slow_print("  Neplatná volba, přišel jsi o tah!")
 
        # Útok nepřítele
        if enemy["hp"] > 0:
            e_dmg = random.randint(*enemy["damage"])
            player.hp -= e_dmg
            slow_print(f"  {enemy['name']} tě zasáhl za {e_dmg} poškození!")
 
    if player.hp <= 0:
        return False
 
    # Vítězství
    gold = random.randint(*enemy["gold"])
    player.gold += gold
    player.gain_xp(enemy["xp"])
    player.kills += 1
    slow_print(f"\n  🏆 Porazil jsi {enemy['name']}! Získal jsi {gold} zlatých a {enemy['xp']} XP.")
    return True
 
 
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
        slow_print(f"  Koupil jsi {name}!")
    else:
        player.inventory[name] = player.inventory.get(name, 0) + 1
        slow_print(f"  Koupil jsi {name}!")
 
 
# ---------------------------------------------------------------------------
# Hlavní smyčka
# ---------------------------------------------------------------------------
 
def main():
    clear()
    slow_print("=" * 50)
    slow_print("        🗡️   DUNGEON QUEST   🗡️")
    slow_print("=" * 50)
    name = input("\nZadej jméno svého hrdiny: ").strip() or "Hrdina"
    player = Player(name)
    slow_print(f"\nVítej, {player.name}! Vstupuješ do dungeonů...\n")
    time.sleep(1)
 
    while player.hp > 0:
        room = random.choice(ROOMS)
        player.rooms_visited += 1
        slow_print(f"\n🚪 Vstoupil jsi do: {room.upper()}")
        player.status()
 
        roll = random.random()
        if roll < 0.55:
            enemy = random.choice(ENEMIES)
            survived = battle(player, enemy)
            if not survived and player.hp <= 0:
                break
        elif roll < 0.70:
            slow_print("\n🏪 Narazil jsi na obchodníka!")
            shop(player)
        elif roll < 0.85:
            gold = random.randint(10, 30)
            player.gold += gold
            slow_print(f"\n💰 Našel jsi {gold} zlatých na zemi!")
        else:
            slow_print("\n🌿 Místnost je klidná. Odpočíváš a obnovíš 15 HP.")
            player.hp = min(player.hp + 15, player.max_hp)
 
        cont = input("\nPokračovat dál? (Enter = ano, q = konec): ").strip().lower()
        if cont == "q":
            break
 
    slow_print("\n" + "=" * 50)
    if player.hp <= 0:
        slow_print("💀 Byl jsi poražen! Hra skončila.")
    else:
        slow_print("🏰 Opustil jsi dungeon.")
    slow_print(f"\n📜 Statistiky hrdiny {player.name}:")
    slow_print(f"   Úroveň:         {player.level}")
    slow_print(f"   Zabití nepřátelé: {player.kills}")
    slow_print(f"   Navštívené místnosti: {player.rooms_visited}")
    slow_print(f"   Zlaté:          {player.gold}")
    slow_print("=" * 50)
 
 
if __name__ == "__main__":
    main()
 