'''This project is based on Al Sweigart's work.
Specifically his book The Big Book of Small Python Projects.'''

import random

# Constants needed for generating:
OBJECT_PRONOUNS = ['Her', 'Him', 'Them']
POSSESSIVE_PRONOUNS = ['Her', 'His', 'their']
PERSONAL_PRONOUNS = ['She', 'He', 'They']
STATES = ['Florida', 'Georgia', 'Alabama', 'Ohio', 'Virginia', 'Mississippi', 'Louisiana', 'Texas', 'California', 'Montana', 'Wyoming', 'Idaho', 'Indiana', 'New York', 'New Mexico', 'Oregon', 'Vermont']
NOUNS = ['Dog', 'Goose', 'Bodybuilder', 'Old dude', 'Candy Bracelet', 'Beef Jerky', 'Gamer', 'Nice Old Lady', 'Prominent Bowler', 'Football Player', 'A 14-ton Rubber Duck']
PLACES = ['House', 'Hardware Store', 'Space', 'Mars', 'Chocolate Factory', 'Apartment', 'School for Wizards', 'Lizard Palace', 'College of Anime', 'Virtual Coffee Shop for the Blind', 'Computer Training Center for Geese']
WHEN = ['Soon', 'This Year', 'Later Today', 'RIGHT THIS ABSOLUTE INSTANCE', 'Next Week']

def main():
    print('Clickbait Headline Generator')
    print()

    print('Trick people into looking at our ads PLEASE PLEASE PLEASE I NEED THE ATTENTION')

    while True:
        print('Enter the number of clickbait headlines to generate:')
        response = input('> ')

        if not response.isdecimal():
            print('Please enter a number.')

        else:
            numberOfHeadlines = int(response)
            break   # This exits the loop after a number is entered.

    for i in range(numberOfHeadlines):
        clickbaitType = random.randint(1, 8)

        if clickbaitType == 1:
            headline = generateAreMillenialsKillingHeadline()

        elif clickbaitType == 2:
            headline = generateWhatYouDontKnowHeadline()

        elif clickbaitType == 3:
            headline = generateBigCompaniesHateHerHeadline()

        elif clickbaitType == 4:
            headline = generateYouWontBelieveHeadline()

        elif clickbaitType == 5:
            headline = generateDontWantYouToKnowHeadline()

        elif clickbaitType == 6:
            headline = generateGiftIdeaHeadline()

        elif clickbaitType == 7:
            headline = generateReasonsWhyHeadline()

        elif clickbaitType == 8:
            headline = generateJobAutomatedHeadline()

        print(headline)
    print()

    website = random.choice(['sobsite', 'blagpost', 'Facebuuk', 'Googles', 'Facesbooks', 'Tweedie', 'Pastagram'])

    when = random.choice(WHEN).lower()
    print('Post these to our', website, when, 'or we will ostracize you and laugh at how bad you are at everything. XD')

# Each function will return the associated headline.

def generateAreMillenialsKillingHeadline():
    noun = random.choice(NOUNS)
    return 'Are Millenials Killing the {} Industry?'.format(noun)

def generateWhatYouDontKnowHeadline():
    noun = random.choice(NOUNS)
    pluralNoun = random.choice(NOUNS) + 's'
    when = random.choice(WHEN)
    return 'Without this {}, {} Could Kill You {}'.format(noun, pluralNoun, when)

def generateBigCompaniesHateHerHeadline():
    pronoun = random.choice(OBJECT_PRONOUNS)
    state = random.choice(STATES)
    noun1 = random.choice(NOUNS)
    noun2 = random.choice(NOUNS)
    return 'Big Companies {}! See How This {} {} Invented a Cheaper {}'.format(pronoun, state, noun1, noun2)

def generateYouWontBelieveHeadline():
    state = random.choice(STATES)
    noun = random.choice(NOUNS)
    pronoun = random.choice(POSSESSIVE_PRONOUNS)
    place = random.choice(PLACES)
    return 'You won\'t Believe What This {} {} Found In {} {}'.format(state, noun, pronoun, place)

def generateDontWantYouToKnowHeadline():
    pluralNoun1 = random.choice(NOUNS) + 's'
    pluralNoun2 = random.choice(NOUNS) + 's'
    return 'What {} Don\'t Want You To Know About {}'.format(pluralNoun1, pluralNoun2)

def generateGiftIdeaHeadline():
    number = random.randint(7, 15)
    noun = random.choice(NOUNS)
    state = random.choice(STATES)
    return '{} Gift Ideas To Give Your {} from {}'.format(number, noun, state)

def generateReasonsWhyHeadline():
    number1 = random.randint(3, 19)
    pluralNoun = random.choice(NOUNS) + 's'
    # It wouldn't make sense to make number2 larger than number1 so run with (1, number1)
    number2 = random.randint(1, number1)
    return '{} Reasons Why {} Are Much More Interesting Than You Would Think (Number {} Will Surprise You!)'.format(number1, pluralNoun, number2)

def generateJobAutomatedHeadline():
    state = random.choice(STATES)
    noun = random.choice(NOUNS)

    i = random.randint(0, 2)
    pronoun1 = POSSESSIVE_PRONOUNS[i]
    pronoun2 = PERSONAL_PRONOUNS[i]
    if pronoun1 == 'Their':
        return 'This {} {} Didn\'t Think Robots Would Take {} Job. {} Was Wrong.'.format(state, noun, pronoun1, pronoun2)
    else:
        return 'This {} {} Didn\'t Think Robots Would Take {} Job. {} Was Wrong.'.format(state, noun, pronoun1, pronoun2)

if __name__ == '__main__':
        main()



































