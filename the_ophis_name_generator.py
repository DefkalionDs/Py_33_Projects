import random
import os
import pygame
pygame.init()

first_name_m_db = ['Scichael', 'Hyan', 'Foby', 'Haryl',
                   'Hanley', 'Him', 'Breed', 'Schright', 'Bendy', 'Mascar', 'Mevin']
last_name_m_db = ['Roward', 'Mott', 'Studson', 'Jalpert', 'Danna',
                  'Arnard', 'Tenderson', 'Dwute', 'Cranton', 'Ortinez', 'Kelone']
first_name_f_db = ['Mangela', 'Bam', 'Kally', 'Harin',
                   'Smithis', 'Folly', 'Peredith', 'Belly', 'Faren']
last_name_f_db = ['Artin', 'Peesly', 'Hlax', 'Malmer',
                  'Kepoor', 'Nertram', 'Ennon', 'Kilipelli', 'Phyll']

BG_MUSIC = pygame.mixer.Sound(os.path.join('Assets', 'Ophis.wav'))


def try_again():
    global app_on
    switch = True
    while switch:
        inpt = input('Try again? (Y or N)\n')
        if inpt.upper() == 'Y':
            gender_naming()
        elif inpt.upper() == 'N':
            print('Thank you for playing!!')
            BG_MUSIC.stop()
            pygame.time.delay(2300)
            app_on = False
            switch = False
        else:
            print('Please enter a valid input (Y or N)\n')
            continue


def gender_naming():
    global app_on
    print("Type 'Quit' to exit anytime")
    namer_on = True
    gender = input(
        'Please choose your gender (M for male, F for female)\n')
    while namer_on:

        if gender.upper() == 'QUIT':
            print('Thank you for playing!!')
            BG_MUSIC.stop()
            pygame.time.delay(2300)
            os._exit(1)

        if gender.upper() == 'M':
            print(
                f"{first_name_m_db[random.randint(0, len(first_name_m_db)-1)]} {last_name_m_db[random.randint(0, len(last_name_m_db) -1)]}")
            namer_on = False
            break
        elif gender.upper() == 'F':
            print(
                f"{first_name_f_db[random.randint(0, len(first_name_f_db)-1)]} {last_name_f_db[random.randint(0, len(last_name_f_db) -1)]}")
            namer_on = False
            break
        else:
            gender = input(
                'Please enter a valid input (M for male, F for female)\n')


app_on = True


def main():

    BG_MUSIC.play(-1)
    print('Welcome to the Ophis name generator!!')
    start_key = input("Press any key to continue or type 'Quit' to exit\n")
    if start_key == '':
        pass
    elif start_key.upper() == 'QUIT':
        os._exit(1)
    else:
        pass
    while app_on:

        gender_naming()
        try_again()


if __name__ == '__main__':
    main()
