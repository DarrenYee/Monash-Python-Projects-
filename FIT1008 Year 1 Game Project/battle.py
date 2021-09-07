from army import Army
class Battle:
    def gladiatorial_combat (self, player_one: str, player_two: str ) -> int:
        army1 = army()
        army2 = army()
        army1.name = player_one
        army2.name = player_two
        conduct_combat(army1,army2,0)



    def fairer_combat(self, player_one :str ,player_two: str) -> None:
       army1 = army()
       army2 = army()
       army1.name = player_one
       army2.name = player_two
       conduct_combat(army1,army2,1)

    def __conduct_combat (self , army1: Army, army2:Army, formation: int) -> int:
        draw = 1
        expgain = 1
        while army1.force.is_empty() is False and army2.force.is_empty is False:
            if formation == 1:
                u1 = army1.force.serve()
                u2 = army2.force.serve()
            else:
                u1 = army1.force.pop()
                u2 = army2.force.pop()

            if u1.getspeed() > u2.getspeed():
                damagedealtu1 = u1.attack_damage()
                u2.defend(damagedealtu1)
                if u2.is_alive():
                    damagedealtu2=u2.attack_damage()
                    u1.defend(damagedealtu2)
            elif u2.getspeed() < u2.getspeed():
                damagedealtu2 = u2.attck_damage()
                u1.defend(damagedealtu2)
                if u1.is_alive():
                    damagedealtu1=u1.attack_damage()
                    u2.defend(damagedealtu1)
            else:
                damagedealtu1 = u1.attack_damage
                damagedealtu2 = u2.attack_damage
                u1.defend(damagedealtu2)
                u2.defend(damagedealtu1)

            if u1.is_alive() == True and u2.is_alive == True:
                u1.lose_life(draw)
                u2.lose_life(draw)
                if u1.is_alive() == True:
                    if formation == 1:
                        army1.force.append(u1)
                    else:
                        army1.force.push(u1)
                if u2.is_alive() == True:
                    if formation == 1:
                        army2.force.append(u2)
                    else:
                        army2.force.push(u2)
            elif u1.is_alive() == True and u2.is_alive == False:
                u1.gain_experience(expgain)
                if formation == 1:
                    army1.force.append(u1)
                else:
                    army2.force.push(u2)

            elif u1.is_alive == False and u2.is_alive == True:
                u2.gain_experience(expgain)
                if formation == 1:
                    army2.force.append(u2)
                else:
                    army2.force.push(u2)

        if army1.force.is_empty() == True and army2.force.is_empty() ==False:
            return 2
        elif army1.force.is_empty() == False and army2.force.is_empty() == True:
            return 1
        else:
            return 0













