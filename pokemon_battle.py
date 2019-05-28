pokemon_elegido = input("contra que pokemon quieres luchar(planta/fuego/agua):")
pikachu_life = 100
if pokemon_elegido == "planta":
    enemy_lp = 100
    enemy_at = 10
elif pokemon_elegido == "fuego":
    enemy_lp = 180
    enemy_at = 14
elif pokemon_elegido == "agua":
    enemy_lp = 90
    enemy_at = 9
while pikachu_life > 0 and enemy_lp > 0:
    wich_attack = input("que ataque vas a usar?")
    if wich_attack == "1":
        p_power_atack = 10
    elif wich_attack == "2":
        p_power_atack = 12
    enemy_lp = enemy_lp - p_power_atack
    pikachu_life = pikachu_life - enemy_at
    print ("pikachu_lvida de pikachu {}".format(pikachu_life))
    print("vida del enemigo {}".format(enemy_lp))


if pikachu_life <= 0:
    print("perdiste")
else:
    print("ganaste")



