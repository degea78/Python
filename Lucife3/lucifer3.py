import random

player = {
    'name': 'Necro',
    'health': 100,
    'heal': 16,
    'attack': 12
}
enemy = {
    'name': 'Monster',
    'health': 120,
    'attack': 14
}
game_running = True

while game_running:
    print ('==========================')
    print ('   L U C I F E R   III')
    print ('==========================')

    player['name'] = input('Your name please: ')
    print ('Wellcome in Hell', player['name'])
    print ('__________________________')
    print ('You enter in the forest and the first Monster appear in front of you')
    print ('Monster have ' + str(enemy['health']) + ' health')
    print ('What do you whant to do ' + player['name'] + ' ?')
    print ('1 for Attack')
    print ('2 for Heal')
    attack_or_heal = input ('What do you whant to do?: ')

    if attack_or_heal == str('1'):
        enemy['health'] = enemy['health'] - player['attack']
        player['health'] = player['health'] - enemy['attack']
        print ('Monster remainig heal: ' + str(enemy['health']))
        print ('Your remainig heal: ' + str(player['health']))
    
    elif attack_or_heal == str('2'):
        player['health'] = player['health'] + player['heal']
        if (player['health'] > 100):
            player['health'] = 100
            print ('Your healt is now : ' + str(player['health']))




    game_running = False