import requests
import json
import time
import threading
import statistics
import random
import matplotlib.pyplot as plt


nombres = ["Mario", "Mario", "Mario - Gold Edition", "Mario - Silver Edition", "8-Bit Mario Classic Color", "8-Bit Mario Modern Color", "Mario - Wedding", "Dr. Mario", "Mario - Cat", "Luigi", "Luigi", "Peach", "Peach", "Peach - Wedding", "Peach - Cat", "Yoshi", "Yoshi", "Rosalina", "Rosalina & Luma", "Bowser", "Bowser", "Bowser - Wedding", "Hammer Slam Bowser", "Bowser Jr.", "Wario", "Wario", "Donkey Kong", "Donkey Kong", "Turbo Charge Donkey Kong", "Diddy Kong", "Diddy Kong", "Toad", "Daisy", "Daisy", "Waluigi", "Goomba", "Boo", "Koopa Troopa", "Piranha Plant", "King K. Rool", "Link", "Link - Ocarina of Time", "Link - Majora's Mask", "Link - Twilight Princess", "Link - Skyward Sword", "8-Bit Link", "Link - Archer", "Link - Rider", "Young Link", "Link - Link's Awakening", "Toon Link", "Toon Link - The Wind Waker", "Zelda", "Toon Zelda - The Wind Waker", "Zelda", "Sheik", "Zelda & Loftwing", "Ganondorf", "Midna & Wolf Link", "Daruk", "Urbosa", "Mipha", "Revali", "Guardian", "Bokoblin", "Villager", "Isabelle - Summer Outfit", "Isabelle", "Isabelle - Winter Outfit", "K. K. Slider", "Tom Nook", "Timmy & Tommy", "Mabel", "Reese", "Cyrus", "Digby", "Rover", "Resetti", "Blathers", "Celeste", "Kicks", "Kapp'n", "Lottie", "Fox", "Falco", "Wolf", "Samus", "Samus Aran", "Samus - Metroid Dread", "Zero Suit Samus", "Metroid", "Ridley", "Dark Samus", "E.M.M.I.", "Captain Falcon", "Olimar", "Pikmin", "Little Mac", "Wii Fit Trainer", "Pit", "Dark Pit", "Palutena", "Mr. Game & Watch", "R.O.B. - Famicom", "R.O.B. - NES", "Duck Hunt", "Ice Climbers", "Mii Brawler", "Mii Swordfighter", "Mii Gunner", "Inkling Girl", "Inkling Girl - Lime Green", "Inkling Girl - Neon Pink", "Inkling", "Inkling - Yellow", "Inkling Boy", "Inkling Boy - Purple", "Inkling Boy - Neon Green", "Inkling Squid", "Inkling Squid - Orange", "Inkling Squid - Neon Purple", "Callie", "Marie", "Pearl", "Marina", "Octoling Girl", "Octoling Boy", "Octoling - Blue", "Octoling Octopus", "Smallfry", "Min Min", "Ivysaur", "Charizard", "Squirtle", "Pikachu", "Jigglypuff", "Mewtwo", "Pichu", "Lucario", "Greninja", "Incineroar", "Detective Pikachu", "Pokemon Trainer", "Kirby", "Kirby", "Meta Knight", "Meta Knight", "King Dedede", "King Dedede", "Waddle Dee", "Qbby", "Marth", "Ike", "Lucina", "Robin", "Roy", "Corrin", "Corrin - Player 2", "Alm", "Celica", "Chrom", "Chrom", "Tiki", "Byleth", "Shulk", "Ness", "Lucas", "Chibi Robo", "Sonic", "Bayonetta", "Bayonetta - Player 2", "Pac-Man", "Solaire of Astora", "Kazuya", "Mega Man", "Mega Man - Gold Edition", "Mega Man", "Ryu", "Ken", "One-Eyed Rathalos and Rider - Male", "One-Eyed Rathalos and Rider - Female", "Nabiru", "Rathian and Cheval", "Barioth and Ayuria", "Qurupeco and Dan", "Razewing Ratha", "Ena", "Tsukino", "Magnamalo", "Palico", "Palico", "Palamute", "Palamute", "Malzeno", "Shovel Knight", "Shovel Knight - Gold Edition", "Plague Knight", "Specter Knight", "King Knight", "Cloud", "Cloud - Player 2", "Sephiroth", "Hero", "Snake", "Simon", "Richter", "Loot Goblin", "Joker", "Banjo & Kazooie", "Terry", "Steve", "Alex"]


def get_data(tiempos, nombres):

    url = "https://amiiboapi.com/api/amiibo/"
    thread_list = []
    i = 0
    n = 5000 #numero de solicitudes deseadas
    while i < n:

        numero = random.randrange(len(nombres))
        name = nombres[numero]
        payload = {"name": name , "type": "figure"}
        tInicio = time.time()
        t = threading.Thread(target=send_request, args=(url, payload, tInicio, tiempos, name, numero))
        thread_list.append(t)
        t.start()
        time.sleep(0.05)  
        i += 1

    for t in thread_list:
        t.join()

def send_request(url, payload, start_time, tiempos, name, numero):
                    
        response = requests.get(url, payload)
        
            
        data = response.json()
        jsonified_data = json.dumps(data)
        end_time = time.time()  
        print (jsonified_data)     
    
        elapsed_time = round((end_time - start_time) * 1000, 2)  
        tiempos.append(elapsed_time)

tiempos = []

get_data(tiempos,nombres)
print(len(tiempos))
print(statistics.mean(tiempos))

x = range(len(tiempos))

plt.plot(x,tiempos)

plt.savefig('tiempos.png')