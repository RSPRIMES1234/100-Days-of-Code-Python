import random
import os
blank_list=[]
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')
hangman_words="about, above, abuse, accept, accident, accuse, across, activist, actor, administration, admit, adult, advertise, advise, affect, afraid, after, again, against, agency, aggression, agree, agriculture, force, airplane, airport, album, alcohol, alive, almost, alone, along, already, although, always, ambassador, amend, ammunition, among, amount, anarchy, ancestor, ancient, anger, animal, anniversary, announce, another, answer, apologize, appeal, appear, appoint, approve, archeology, argue, around, arrest, arrive, artillery, assist, astronaut, astronomy, asylum, atmosphere, attach, attack, attempt, attend, attention, automobile, autumn, available, average, avoid, awake, award, balance, balloon, ballot, barrier, battle, beauty, because, become, before, begin, behavior, behind, believe, belong, below, betray, better, between, biology, black, blame, bleed, blind, block, blood, border, borrow, bottle, bottom, boycott, brain, brave, bread, break, breathe, bridge, brief, bright, bring, broadcast, brother, brown, budget, build, building, bullet, burst, business, cabinet, camera, campaign, cancel, cancer, candidate, capital, capture, career, careful, carry, catch, cause, ceasefire, celebrate, center, century, ceremony, chairman, champion, chance, change, charge, chase, cheat, cheer, chemicals, chemistry, chief, child, children, choose, circle, citizen, civilian, civil, rights, claim, clash, class, clean, clear, clergy, climate, climb, clock, close, cloth, clothes, cloud, coalition, coast, coffee, collapse, collect, college, colony, color, combine, command, comment, committee, common, communicate, community, company, compare, compete, complete, complex, compromise, computer, concern, condemn, condition, conference, confirm, conflict, congratulate, Congress, connect, conservative, consider, constitution, contact, contain, container, continent, continue, control, convention, cooperate, correct, corruption, cotton, count, country, court, cover, crash, create, creature, credit, crime, criminal, crisis, criticize, crops, cross, crowd, crush, culture, curfew, current, custom, customs, damage, dance, danger, daughter, debate, decide, declare, decrease, defeat, defend, deficit, define, degree, delay, delegate, demand, democracy, demonstrate, denounce, depend, deplore, deploy, depression, describe, desert, design, desire, destroy, detail, detain, develop, device, dictator, different, difficult, dinner, diplomat, direct, direction, disappear, disarm, disaster, discover, discrimination, discuss, disease, dismiss, dispute, dissident, distance, divide, doctor, document, dollar, donate, double, dream, drink, drive, drown, during, early, earth, earthquake, ecology, economy, education, effect, effort, either, elect, electricity, embassy, embryo, emergency, emotion, employ, empty, enemy, energy, enforce, engine, engineer, enjoy, enough, enter, environment, equal, equipment, escape, especially, establish, estimate, ethnic, evaporate, event, every, evidence, exact, examine, example, excellent, except, exchange, excuse, execute, exercise, exile, exist, expand, expect, expel, experience, experiment, expert, explain, explode, explore, export, express, extend, extra, extraordinary, extreme, extremist, factory, false, family, famous, father, favorite, federal, female, fence, fertile, field, fierce, fight, final, financial, finish, fireworks, first, float, flood, floor, flower, fluid, follow, force, foreign, forest, forget, forgive, former, forward, freedom, freeze, fresh, friend, frighten, front, fruit, funeral, future, gather, general, generation, genocide, gentle, glass, goods, govern, government, grain, grass, great, green, grind, ground, group, guarantee, guard, guerrilla, guide, guilty, happen, happy, harvest, headquarters, health, heavy, helicopter, hijack, history, holiday, honest, honor, horrible, horse, hospital, hostage, hostile, hotel, house, however, human, humor, hunger, hurry, husband, identify, ignore, illegal, imagine, immediate, immigrant, import, important, improve, incident, incite, include, increase, independent, individual, industry, infect, inflation, influence, inform, information, inject, injure, innocent, insane, insect, inspect, instead, instrument, insult, intelligence, intelligent, intense, interest, interfere, international, Internet, intervene, invade, invent, invest, investigate, invite, involve, island, issue, jewel, joint, judge, justice, kidnap, knife, knowledge, labor, laboratory, language, large, laugh, launch, learn, leave, legal, legislature, letter, level, liberal, light, lightning, limit, liquid, listen, literature, little, local, lonely, loyal, machine, magazine, major, majority, manufacture, march, market, marry, material, mathematics, matter, mayor, measure, media, medicine, member, memorial, memory, mental, message, metal, method, microscope, middle, militant, military, militia, mineral, minister, minor, minority, minute, missile, missing, mistake, model, moderate, modern, money, month, moral, morning, mother, motion, mountain, mourn, movement, movie, murder, music, mystery, narrow, nation, native, natural, nature, necessary, negotiate, neighbor, neither, neutral, never, night, noise, nominate, normal, north, nothing, nowhere, nuclear, number, object, observe, occupy, ocean, offensive, offer, office, officer, official, often, operate, opinion, oppose, opposite, oppress, orbit, order, organize, other, overthrow, paint, paper, parachute, parade, pardon, parent, parliament, partner, party, passenger, passport, patient, peace, people, percent, perfect, perform, period, permanent, permit, person, persuade, physical, physics, picture, piece, pilot, place, planet, plant, plastic, please, plenty, point, poison, police, policy, politics, pollute, popular, population, position, possess, possible, postpone, poverty, power, praise, predict, pregnant, present, president, press, pressure, prevent, price, prison, private, prize, probably, problem, process, produce, profession, professor, profit, program, progress, project, promise, propaganda, property, propose, protect, protest, prove, provide, public, publication, publish, punish, purchase, purpose, quality, question, quick, quiet, radar, radiation, radio, railroad, raise, reach, react, ready, realistic, reason, reasonable, rebel, receive, recent, recession, recognize, record, recover, reduce, reform, refugee, refuse, register, regret, reject, relations, release, religion, remain, remains, remember, remove, repair, repeat, report, represent, repress, request, require, rescue, research, resign, resist, resolution, resource, respect, responsible, restaurant, restrain, restrict, result, retire, return, revolt, right, river, rocket, rough, round, rubber, rural, sabotage, sacrifice, sailor, satellite, satisfy, school, science, search, season, second, secret, security, seeking, seize, Senate, sense, sentence, separate, series, serious, serve, service, settle, several, severe, shake, shape, share, sharp, sheep, shell, shelter, shine, shock, shoot, short, should, shout, shrink, sickness, signal, silence, silver, similar, simple, since, single, sister, situation, skeleton, skill, slave, sleep, slide, small, smash, smell, smoke, smooth, social, soldier, solid, solve, sound, south, space, speak, special, speech, speed, spend, spill, spirit, split, sport, spread, spring, square, stand, start, starve, state, station, statue, steal, steam, steel, stick, still, stone, store, storm, story, stove, straight, strange, street, stretch, strike, strong, structure, struggle, study, stupid, subject, submarine, substance, substitute, subversion, succeed, sudden, suffer, sugar, suggest, suicide, summer, supervise, supply, support, suppose, suppress, surface, surplus, surprise, surrender, surround, survive, suspect, suspend, swallow, swear, sweet, sympathy, system, target, taste, teach, technical, technology, telephone, telescope, television, temperature, temporary, tense, terrible, territory, terror, terrorist, thank, theater, theory, there, these, thick, thing, think, third, threaten, through, throw, tired, today, together, tomorrow, tonight, torture, total, touch, toward, trade, tradition, traffic, tragic, train, transport, transportation, travel, treason, treasure, treat, treatment, treaty, trial, tribe, trick, troops, trouble, truce, truck, trust, under, understand, unite, universe, university, unless, until, urgent, usual, vacation, vaccine, valley, value, vegetable, vehicle, version, victim, victory, video, village, violate, violence, visit, voice, volcano, volunteer, wages, waste, watch, water, wealth, weapon, weather, weigh, welcome, wheat, wheel, where, whether, which, while, white, whole, willing, window, winter, withdraw, without, witness, woman, wonder, wonderful, world, worry, worse, worth, wound, wreck, wreckage, write, wrong, yellow, yesterday, young"
life_0=r"""      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / \
     |
    _|___"""
life_1="""      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / 
     |
    _|___"""
life_2="""      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      
     |
    _|___"""
life_3="""      _______
     |/      |
     |      (_)
     |      \|/
     |       
     |      
     |
    _|___"""
life_4="""      _______
     |/      |
     |      (_)
     |      \|
     |       
     |      
     |
    _|___"""
life_5=r"""      _______
     |/      |
     |      (_)
     |      \
     |       
     |      
     |
    _|___"""
life_6="""      _______
     |/      |
     |      (_)
     |      
     |       
     |       
     |
    _|___"""
life_7="""      _______
     |/      |
     |      
     |      
     |       
     |      
     |
    _|___"""
hangman_ascii_list=[life_0,life_1,life_2,life_3,life_4,life_5,life_6,life_7]








hangman_words=hangman_words.split(", ")
guess_word=random.choice(hangman_words)
guess_word = list(guess_word)
for _ in range(len(guess_word)):
    blank_list.append("_")
print(r""" _
| |
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |
                   |___/                    """)
guess_right_left=len(guess_word)
lifes=7
while (guess_right_left>0) and (lifes>0):
    user_guess=input("Guess a letter:")
    clear_console()
    user_guess=user_guess.lower()
    if user_guess in guess_word:
        while user_guess in guess_word:
            index=guess_word.index(user_guess)
            blank_list[index]=user_guess
            guess_word.remove(user_guess)
            guess_right_left-=1

        print("".join(blank_list))
        print(hangman_ascii_list[lifes])
    elif user_guess not in guess_word and user_guess in blank_list:
        print(f"You've already guessed {user_guess}")
        print("".join(blank_list))
        print(hangman_ascii_list[lifes])
    elif user_guess not in guess_word and user_guess not in blank_list and lifes!=1:
        print(f"You guessed {user_guess}, that's not in the word. You lose a life.")
        lifes-=1
        print("".join(blank_list))
        print(hangman_ascii_list[lifes])
    elif user_guess not in guess_word and user_guess not in blank_list and lifes==1:
        print(f"You guessed {user_guess}, that's not in the word. You lost all of your life.Gameover.")
        lifes -= 1
        print("".join(blank_list))
        print(hangman_ascii_list[lifes])








