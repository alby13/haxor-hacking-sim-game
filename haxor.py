import os
import random
import time
import math
from datetime import datetime

# --- ASCII Art and Visual Elements ---
TITLE_ART = """
██╗  ██╗ █████╗ ██╗  ██╗███████╗██████╗ 
██║  ██║██╔══██╗╚██╗██╔╝██╔════╝██╔══██╗
███████║███████║ ╚███╔╝ █████╗  ██████╔╝
██╔══██║██╔══██║ ██╔██╗ ██╔══╝  ██╔══██╗
██║  ██║██║  ██║██╔╝ ██╗███████╗██║  ██║
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
Created by alby13 - Hack the system!!!
"""

LOADING_BARS = [
    "▱▱▱▱▱▱▱▱▱▱",
    "▰▱▱▱▱▱▱▱▱▱",
    "▰▰▱▱▱▱▱▱▱▱",
    "▰▰▰▱▱▱▱▱▱▱",
    "▰▰▰▰▱▱▱▱▱▱",
    "▰▰▰▰▰▱▱▱▱▱",
    "▰▰▰▰▰▰▱▱▱▱",
    "▰▰▰▰▰▰▰▱▱▱",
    "▰▰▰▰▰▰▰▰▱▱",
    "▰▰▰▰▰▰▰▰▰▱",
    "▰▰▰▰▰▰▰▰▰▰"
]

# --- Game Data ---
class GameState:
    def __init__(self):
        self.current_location = "home"
        self.experience = 0
        self.reputation = 0
        self.money = 1000
        self.inventory = []
        self.missions_completed = []
        self.discovered_exploits = []
        self.active_mission = None

user_data = {
    "username": "guest",
    "password": "password",
    "level": 1,
    "firewall": 1,
    "encryption": 1,
    "stealth": 1
}

# Extended network with more interesting locations and challenges
network = {
    "home": {
        "type": "local",
        "files": ["notes.txt", "personal.info", "mission_board.txt"],
        "password": None,
        "ascii_art": """
        🏠 HOME SYSTEM
        ├── Documents
        ├── Tools
        └── Config
        """
    },
    "server1": {
        "type": "server",
        "files": ["login.log", "system.cfg"],
        "password": "securepass",
        "required_level": 2,
        "ascii_art": """
        📡 SERVER 1
        ├── Logs
        ├── Config
        └── Data
        """
    },
    "sidenet": {
        "type": "marketplace",
        "files": ["market.dat", "vendors.list"],
        "password": "sh4d0w",
        "required_level": 3,
        "firewall": 2,
        "ascii_art": """
        🕶️ SIDENET
        ├── Market
        ├── Forums
        └── Exchange
        """
    },
    "corp_network": {
        "type": "corporate",
        "files": ["employees.db", "projects.dat", "finances.xls"],
        "password": "corp123",
        "required_level": 4,
        "firewall": 3,
        "ascii_art": """
        🏢 CORPORATE NET
        ├── HR
        ├── Finance
        └── Projects
        """
    },
    "bank": {
        "type": "server",
        "files": ["accounts.data", "transactions.log"],
        "password": "supersecurepassword",
        "required_level": 5,
        "firewall": 4,
        "ascii_art": """
        🏦 BANK
        ├── Accounts
        ├── Transactions
        └── Security
        """
    }
}

# Available tools and upgrades in the marketplace
shop_items = {
    "password_cracker": {
        "name": "Password Cracker v2.0",
        "cost": 2000,
        "description": "Improves password cracking success rate by 20%",
        "type": "tool"
    },
    "vpn": {
        "name": "Secure VPN",
        "cost": 1500,
        "description": "Reduces trace detection chance by 30%",
        "type": "defense"
    },
    "firewall_boost": {
        "name": "Firewall Booster",
        "cost": 3000,
        "description": "Increases firewall effectiveness by 25%",
        "type": "defense"
    }
}

# Random events that can occur during gameplay
random_events = [
    {
        "name": "System Update",
        "description": "A sudden system update has temporarily weakened the target's security!",
        "effect": "security_decrease"
    },
    {
        "name": "Security Scan",
        "description": "The system is running a security scan. Increased chance of detection!",
        "effect": "detection_increase"
    },
    {
        "name": "Network Maintenance",
        "description": "Network maintenance has created a temporary backdoor!",
        "effect": "backdoor_available"
    }
]

# Available missions
missions = {
    "data_heist": {
        "name": "Corporate Data Heist",
        "description": "Infiltrate the corporate network and steal sensitive data",
        "target": "corp_network",
        "reward": 5000,
        "min_level": 3
    },
    "bank_hack": {
        "name": "Bank Security Test",
        "description": "Test the bank's security by attempting to access their system",
        "target": "bank",
        "reward": 10000,
        "min_level": 5
    }
}

known_ips = {
    "home": "127.0.0.1",
    "server1": "192.168.1.100",
    "sidenet": "10.31.337.1",
    "corp_network": "203.0.113.45",
    "bank": "10.0.0.5"
}

cracked_systems = []
game_state = GameState()

# --- Visual Effects ---
def display_loading_bar(duration=1, steps=10):
    for i in range(steps + 1):
        progress = LOADING_BARS[int((i/steps) * 10)]
        print(f"\rProgress: {progress} {i*10}%", end="", flush=True)
        time.sleep(duration/steps)
    print()

def display_hacking_animation():
    hacking_frames = [
        "⠋ HACKING",
        "⠙ HACKING",
        "⠹ HACKING",
        "⠸ HACKING",
        "⠼ HACKING",
        "⠴ HACKING",
        "⠦ HACKING",
        "⠧ HACKING",
        "⠇ HACKING",
        "⠏ HACKING"
    ]
    for _ in range(10):
        for frame in hacking_frames:
            print(f"\r{frame}", end="", flush=True)
            time.sleep(0.1)
    print()

# --- Enhanced Helper Functions ---
def display_prompt():
    location_type = network[game_state.current_location]["type"].upper()
    print(f"\n[{datetime.now().strftime('%H:%M:%S')}] {user_data['username']}@{known_ips[game_state.current_location]} ({location_type})$ ", end="")

def type_effect(text, speed=0.03):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(speed)
    print()

def calculate_success_chance(target_system):
    base_chance = 0.6
    level_bonus = user_data['level'] * 0.05
    tool_bonus = len(game_state.inventory) * 0.02
    return min(0.95, base_chance + level_bonus + tool_bonus)

def trigger_random_event():
    if random.random() < 0.15:  # 15% chance of random event
        event = random.choice(random_events)
        type_effect(f"\n🎲 RANDOM EVENT: {event['name']}")
        type_effect(f"📢 {event['description']}")
        return event
    return None

def display_system_info(system_name):
    system = network[system_name]
    print("\n" + system["ascii_art"])
    print(f"System Type: {system['type'].upper()}")
    print(f"Security Level: {'🔒' * system.get('required_level', 1)}")
    if system.get('firewall'):
        print(f"Firewall: {'🛡️' * system['firewall']}")
    print(f"Files: {len(system['files'])}")
    print(f"Status: {'🔓 CRACKED' if system_name in cracked_systems else '🔒 SECURED'}")

# --- Enhanced Command Functions ---
def cmd_help(args):
    help_text = """
🔧 Available Commands:
  help      - Show this help message
  ls        - List files in current directory
  cat       - View file contents
  connect   - Connect to a remote system
  disconnect- Return to home system
  crack     - Attempt to crack system security
  scan      - Scan for available networks
  upgrade   - Upgrade your skills
  shop      - Access the digital black market
  mission   - View or accept available missions
  status    - Display your hacker status
  clear     - Clear the terminal
  map       - Display network map
  inventory - Show your tools and items
  exit      - Quit the game.
"""
    print(help_text)

def cmd_status(args):
    status = f"""
╔══════════ HACKER STATUS ══════════╗
║ Level: {user_data['level']}                        
║ Experience: {game_state.experience}                  
║ Reputation: {game_state.reputation}   
║ Yen: ¥{game_state.money}                   
║                                  
║ SKILLS                          
║ ├── Firewall: {user_data['firewall']}              
║ ├── Encryption: {user_data['encryption']}           
║ └── Stealth: {user_data['stealth']}                
╚══════════════════════════════════╝
"""
    print(status)

def cmd_shop(args):
    if game_state.current_location != "sidenet":
        type_effect("❌ Error: Shop only accessible through sidenet connection!")
        return

    print("\n🏪 Welcome to the Digital Black Market!")
    print("Available Items:")
    for item_id, item in shop_items.items():
        print(f"\n{item['name']} (${item['cost']})")
        print(f"└── {item['description']}")

    if args and args[0] == "buy" and len(args) > 1:
        item_id = args[1]
        if item_id in shop_items:
            item = shop_items[item_id]
            if game_state.money >= item['cost']:
                game_state.money -= item['cost']
                game_state.inventory.append(item_id)
                type_effect(f"✅ Successfully purchased {item['name']}!")
            else:
                type_effect("❌ Insufficient funds!")
        else:
            type_effect("❌ Invalid item!")

def cmd_mission(args):
    if not args:
        print("\n📋 Available Missions:")
        for mission_id, mission in missions.items():
            if mission_id not in game_state.missions_completed:
                print(f"\n{mission['name']}")
                print(f"└── {mission['description']}")
                print(f"└── Reward: ${mission['reward']}")
                print(f"└── Required Level: {mission['min_level']}")
        return

    if args[0] == "accept" and len(args) > 1:
        mission_id = args[1]
        if mission_id in missions:
            mission = missions[mission_id]
            if user_data['level'] >= mission['min_level']:
                game_state.active_mission = mission_id
                type_effect(f"✅ Accepted mission: {mission['name']}")
            else:
                type_effect("❌ Level too low for this mission!")
        else:
            type_effect("❌ Invalid mission ID!")

def cmd_map(args):
    map_art = """
    🏠 HOME ──────┐
                 ├── 📡 SERVER1
                 ├── 🕶️ SIDENET
                 ├── 🏢 CORP_NETWORK
                 └── 🏦 BANK
    """
    print(map_art)
    print("\nNetwork Status:")
    for system in network:
        status = "🔓 CRACKED" if system in cracked_systems else "🔒 SECURED"
        print(f"{system}: {status}")

def cmd_inventory(args):
    if not game_state.inventory:
        type_effect("📦 Your inventory is empty!")
        return

    print("\n📦 Inventory:")
    for item_id in game_state.inventory:
        item = shop_items[item_id]
        print(f"└── {item['name']}: {item['description']}")

def cmd_ls(args):
    current_system = network[game_state.current_location]
    print("\n📁 Files in current system:")
    for file in current_system['files']:
        print(f"  └── {file}")

def cmd_cat(args):
    if not args:
        type_effect("❌ Usage: cat <filename>")
        return
    filename = args[0]
    current_system = network[game_state.current_location]
    if filename in current_system['files']:
        if filename == "notes.txt":
            type_effect("📝 This is your personal notebook. You can store useful information here.")
        elif filename == "personal.info":
            type_effect(f"👤 Name: {user_data['username']}\n   Level: {user_data['level']}")
        elif filename == "mission_board.txt":
            cmd_mission([])
        elif filename == "login.log":
            type_effect("🔐 Access logs. Looks like someone tried to access this system recently...")
        elif filename == "system.cfg":
            type_effect("⚙️ System configuration file. Contains sensitive system settings.")
        elif filename == "market.dat":
            type_effect("🛒 Sidenet market data. Contains product listings and vendor information.")
        elif filename == "vendors.list":
            type_effect("👥 List of vendors on the sidenet. Be careful who you trust.")
        elif filename == "employees.db":
            type_effect("💼 Employee database. Contains personal and professional information.")
        elif filename == "projects.dat":
            type_effect("📊 Project data. Confidential information about ongoing projects.")
        elif filename == "finances.xls":
            type_effect("💰 Financial records. Highly sensitive financial data.")
        elif filename == "accounts.data":
            type_effect("🏦 Bank account details. Accessing this could be lucrative but risky.")
        elif filename == "transactions.log":
            type_effect("💸 Transaction logs. Detailed records of financial transactions.")
        else:
            type_effect("📄 Generic file. No specific content.")
    else:
        type_effect("❌ File not found!")

def cmd_connect(args):
    global game_state
    if not args:
        type_effect("❌ Usage: connect <system_name>")
        return
    system_name = args[0]
    if system_name in network:
        if system_name == game_state.current_location:
            type_effect("❌ You are already connected to this system!")
            return
        if system_name in cracked_systems or network[system_name]['password'] is None:
            game_state.current_location = system_name
            display_system_info(system_name)
        elif user_data['level'] >= network[system_name].get('required_level', 1):
            if system_name not in cracked_systems:
                type_effect(f"🔐 Attempting to connect to {system_name}...")
                display_loading_bar(2)
                if random.random() < calculate_success_chance(network[system_name]):
                    type_effect(f"✅ Connection successful! System '{system_name}' is now accessible.")
                    cracked_systems.append(system_name)
                    game_state.current_location = system_name
                    display_system_info(system_name)
                else:
                    type_effect(f"❌ Connection failed! System '{system_name}' security is too strong.")
            else:
                game_state.current_location = system_name
                display_system_info(system_name)
        else:
            type_effect("❌ Your hacking level is too low to connect to this system!")
    else:
        type_effect("❌ Unknown system!")

def cmd_disconnect(args):
    global game_state
    if game_state.current_location != "home":
        game_state.current_location = "home"
        type_effect("✅ Disconnected. Returning to home system.")
    else:
        type_effect("❌ You are already in your home system!")
        
def cmd_crack(args):
    if game_state.current_location == "home":
        type_effect("❌ You cannot crack your own system!")
        return

    target_system = network[game_state.current_location]
    if target_system.get('password'):
        type_effect("🔐 Initiating password cracking sequence...")
        display_hacking_animation()

        success_chance = calculate_success_chance(target_system)
        if random.random() < success_chance:
            type_effect(f"✅ Password cracked: {target_system['password']}")
            cracked_systems.append(game_state.current_location)
            if target_system['type'] == 'server':
                game_state.reputation += 5
            elif target_system['type'] == 'corporate':
                game_state.reputation += 10
            elif target_system['type'] == 'bank':
                game_state.reputation += 20
            
            # Check for mission completion
            if game_state.active_mission:
                mission = missions[game_state.active_mission]
                if mission['target'] == game_state.current_location:
                    type_effect(f"🎉 Mission '{mission['name']}' completed!")
                    game_state.money += mission['reward']
                    game_state.missions_completed.append(game_state.active_mission)
                    game_state.active_mission = None

        else:
            type_effect("❌ Password cracking failed!")
            type_effect("🚨 Intrusion attempt detected! Trace initiated.")
            # Implement trace logic here if you want a more complex system
    else:
        type_effect("❌ This system does not require a password to access.")

def cmd_scan(args):
    type_effect("📡 Scanning for available networks...")
    display_loading_bar(3)
    for system_name, system_data in network.items():
        if system_name != game_state.current_location:
            print(f"└── {system_name} ({known_ips[system_name]}) - {system_data['type'].upper()}")

def cmd_upgrade(args):
    print("\n💪 Available Upgrades:")
    print("  1. Firewall (Cost: ¥1000, Current Level: {}, Description: Increases firewall strength, reducing chances of being detected)".format(user_data['firewall']))
    print("  2. Encryption (Cost: ¥1500, Current Level: {}, Description: Improves encryption, making your data more secure)".format(user_data['encryption']))
    print("  3. Stealth (Cost: ¥2000, Current Level: {}, Description: Enhances stealth capabilities, allowing for quieter operations)".format(user_data['stealth']))

    if args:
        try:
            choice = int(args[0])
            if choice == 1:
                if game_state.money >= 1000:
                    game_state.money -= 1000
                    user_data['firewall'] += 1
                    type_effect("✅ Firewall upgraded!")
                else:
                    type_effect("❌ Insufficient funds!")
            elif choice == 2:
                if game_state.money >= 1500:
                    game_state.money -= 1500
                    user_data['encryption'] += 1
                    type_effect("✅ Encryption upgraded!")
                else:
                    type_effect("❌ Insufficient funds!")
            elif choice == 3:
                if game_state.money >= 2000:
                    game_state.money -= 2000
                    user_data['stealth'] += 1
                    type_effect("✅ Stealth upgraded!")
                else:
                    type_effect("❌ Insufficient funds!")
            else:
                type_effect("❌ Invalid choice!")
        except ValueError:
            type_effect("❌ Invalid input!")
    else:
        type_effect("Enter the number of the upgrade you want to purchase.")

# --- Main Game Loop ---
def main():
    global game_state
    os.system('cls' if os.name == 'nt' else 'clear')
    print(TITLE_ART)
    type_effect("Game Story: You're a hacker.")
    type_effect("Type 'help' to see available commands.")

    while True:
        display_prompt()
        command = input().strip()
        parts = command.split()
        if not parts:
            continue

        command_name = parts[0].lower()
        command_args = parts[1:]

        # Execute corresponding command
        command_map = {
            "help": cmd_help,
            "ls": cmd_ls,
            "cat": cmd_cat,
            "connect": cmd_connect,
            "disconnect": cmd_disconnect,
            "crack": cmd_crack,
            "scan": cmd_scan,
            "upgrade": cmd_upgrade,
            "shop": cmd_shop,
            "mission": cmd_mission,
            "status": cmd_status,
            "map": cmd_map,
            "inventory": cmd_inventory,
            "clear": lambda _: os.system('cls' if os.name == 'nt' else 'clear')
        }

        if command_name == "exit":
            type_effect("👋 Thanks for playing! Goodbye!")
            break
        elif command_name in command_map:
            command_map[command_name](command_args)
        else:
            type_effect("❌ Unknown command!")

if __name__ == "__main__":
    main()
