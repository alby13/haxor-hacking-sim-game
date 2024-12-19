# Haxor Hacking Simulator Text Game
This code implements a text-based hacker simulation game where you play as a hacker navigating a virtual network, trying to infiltrate systems, complete missions, and upgrade your skills. Here's a breakdown of the game:

Core Gameplay:

Objective: The main goal is to become a renowned hacker by completing missions, cracking systems, and accumulating wealth and reputation.

Exploration: You navigate a network of interconnected systems, each with its own type, security level, files, and potential challenges.

Hacking: You can attempt to "crack" systems to gain access. This involves a chance-based mechanic influenced by your level, tools, and the target system's security.

Missions: The game offers missions with specific objectives, such as stealing data from a corporate network or testing the security of a bank. Completing missions rewards you with money and reputation.

Progression: You earn experience and money, which can be used to upgrade your skills (firewall, encryption, stealth) and purchase tools from a black market.

Risk and Reward: Your actions carry risks. Failed hacking attempts can trigger alerts or traces. Successfully cracking systems and completing missions increases your reputation and rewards.

Key Features:

Command-Line Interface: The game is entirely text-based, using commands like ls, cat, connect, crack, shop, mission, etc., to interact with the game world.

ASCII Art and Visuals: Uses ASCII art to depict systems (home, server, darknet, etc.) and loading bars to enhance the visual experience.

Typing Effect: A typing effect simulates the feel of interacting with a terminal.

Network Map: A map command provides a visual representation of the interconnected systems and their status (cracked or secured).

Inventory System: You can buy items from the shop on the 'sidenet', and they are stored in your inventory. These items enhance your hacking abilities.

Upgrade System: You can upgrade your core hacking skills: Firewall, Encryption, and Stealth, which improve your chances of success and reduce detection risks.

Random Events: The game includes random events that can impact gameplay, such as system updates that weaken security or security scans that increase the chance of detection.

Mission System: The mission command allows you to view and accept missions, which provide clear objectives and rewards.

Status and Information: The status command displays your current level, experience, money, and skill levels. The ls and cat commands allow you to explore files within systems.

Game World:

Home: Your base of operations.

Server1: A basic server with some security.

Sidenet: A marketplace where you can buy tools and upgrades.

Corp_Network: A corporate network with higher security and valuable data.

Bank: The most secure system, representing a high-risk, high-reward target.

How to Play:

Run the Python code.

Use commands to interact:

help: Get a list of available commands.

connect <system_name>: Try to connect to a system.

ls: List files in the current system.

cat <filename>: View the contents of a file.

crack: Attempt to crack the current system's password.

disconnect: Return to your home system.

scan: Discover available networks.

upgrade: Improve your skills.

shop: Buy items (only accessible from the sidenet).

mission: View and accept missions.

status: Check your progress.

map: View the network map.

inventory: See your purchased items.

clear: Clear the terminal screen.

exit: Quit the game.

Example Gameplay:

Start at home.

scan to find available systems.

connect server1 to try to access the server.

ls to see what files are there.

crack to try to gain full access.

If successful, explore with ls and cat.

connect sidenet to visit the shop.

shop to see what's available.

shop buy password_cracker to purchase a tool (if you have enough money).

mission to view missions.

mission accept data_heist to start a mission.

connect corp_network to target the corporate network.

...and so on.

Overall:

The game offers a fun and engaging text-based experience for those interested in hacking and cybersecurity themes. It combines elements of exploration, strategy, risk management, and character progression to create a challenging and rewarding gameplay loop. The code is well-structured and relatively easy to understand, making it a good starting point for those interested in learning about text-based game development in Python.

.

Gameplay and Code Structure

The game's flow can be broken down into several key systems and loops, all driven by the Python code:

1. Game Initialization and Data Structures:

GameState Class: This class (class GameState) holds the player's current state:

current_location: The system the player is currently connected to.

experience, reputation, money: Player's progress metrics.

inventory: Tools purchased from the shop.

missions_completed, discovered_exploits: Tracks completed objectives.

active_mission: The currently selected mission.

user_data Dictionary: Stores core player attributes:

username, password: For login (currently basic).

level: Determines access to systems.

firewall, encryption, stealth: Core skills that can be upgraded.

network Dictionary: Defines the game world's network topology:

Each key (e.g., "home", "server1") is a system.

Each system has attributes: type, files, password, required_level, ascii_art, and sometimes firewall. This dictionary dictates the layout of the network, security levels, and content of each system.

shop_items Dictionary: Lists items available for purchase on the darknet:

name, cost, description, type (e.g., "tool", "defense").

missions Dictionary: Defines the available missions:

name, description, target (system to hack), reward, min_level.

known_ips Dictionary: Maps system names to their "IP addresses" for flavor.

cracked_systems List: Tracks systems the player has successfully cracked.

2. Main Game Loop (main() function):

Initialization: Clears the screen, displays the game title, and prints a welcome message.

Command Input and Processing:

display_prompt(): Shows the player's current location and waits for input.

The loop continuously takes player input (commands).

Input is split into command_name and command_args.

command_map (a dictionary) links command names (strings) to their corresponding functions (e.g., "help": cmd_help).

Command Execution: The appropriate command function is executed based on the player's input.

3. Command Functions (e.g., cmd_help, cmd_ls, cmd_connect, etc.):

These functions implement the core gameplay mechanics.

Navigation (cmd_connect, cmd_disconnect):

cmd_connect checks if the target system exists, if the player has access (level, cracked status), and then simulates a connection attempt, updating game_state.current_location. It leverages calculate_success_chance() and random chance for success or failure.

cmd_disconnect returns the player to the "home" system.

System Interaction (cmd_ls, cmd_cat):

cmd_ls lists files in the files list of the current system (from the network dictionary).

cmd_cat displays the content of a specified file. File content is currently hardcoded within the cmd_cat function based on the filename.

Hacking (cmd_crack):

Simulates password cracking using display_hacking_animation() for visual effect.

Uses calculate_success_chance() based on player level, tools, and system security.

Success adds the system to cracked_systems, potentially granting reputation and completing missions.

Failure can trigger intrusion alerts.

Progression (cmd_upgrade, cmd_shop):

cmd_upgrade allows spending game_state.money to increase firewall, encryption, or stealth in user_data.

cmd_shop (only accessible on "darknet") lets the player buy items from shop_items, deducting game_state.money and adding the item to game_state.inventory.

Missions (cmd_mission):

Displays available missions from the missions dictionary.

Allows accepting missions, setting game_state.active_mission.

Mission completion is checked within cmd_crack if the cracked system matches the mission target.

Information (cmd_status, cmd_map, cmd_inventory):

cmd_status shows player stats.

cmd_map displays a text-based map of the network and system status (cracked/secured).

cmd_inventory lists purchased items.

Utility (cmd_help, cmd_clear, cmd_scan):

cmd_help shows available commands.

cmd_clear clears the terminal screen.

cmd_scan lists discoverable systems and their types.

cmd_exit: Terminates the game loop.

4. Helper Functions:

display_loading_bar(): Creates an animated loading bar.

display_hacking_animation(): Displays a spinning hacking animation.

display_prompt(): Shows the current location and user in the command prompt.

type_effect(): Simulates typing text to the screen.

calculate_success_chance(): Calculates the probability of a successful hack based on player attributes and target system security.

trigger_random_event(): Has a chance to trigger a random event that modifies gameplay.

display_system_info(): Prints information about a system, including its ASCII art.

Gameplay Paths and Loops:

Exploration Loop: scan -> connect -> ls -> cat -> disconnect

Hacking Loop: connect -> crack (success/failure) -> (potential mission completion)

Progression Loop: (Complete missions/crack systems) -> Earn money/reputation -> upgrade skills / shop for items -> (Become more powerful)

Mission Loop: mission -> mission accept -> (Navigate to target) -> crack (target system) -> (Complete mission) -> (Rewards)

Code Structure Summary:

The game is built around a central loop that processes player commands. These commands trigger functions that interact with the game's data structures (representing the player, network, items, and missions). Helper functions enhance the visual presentation and calculate game mechanics. The interaction between these elements creates the dynamic gameplay experience of exploration, hacking, progression, and mission completion.
