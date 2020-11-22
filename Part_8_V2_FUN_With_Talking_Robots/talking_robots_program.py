import gc

import speech


def talk(words):
    """Talk to your friend Mr. George

    Parameters
    ----------
    words : str
        The words to say to your friend Mr. George
    Returns
    -------
    None
    """
    gc.collect()
    words = words.lower()

    if words.find('how are you') != -1:
        speech.say('I am doing great!')
    elif words.find('what\'s up') != -1:
        speech.say('The sky.')
    elif words.find('morning') != -1:
        speech.say('I love to watch the sun rise in the morning!')
    elif words.find('afternoon') != -1:
        speech.say('I get hungry around lunch time.')
    elif words.find('evening') != -1:
        speech.say('I get sleepy in the evening.')
    elif words.find('night') != -1:
        speech.say('I get sleepy when it is night time.')
    elif words.find('tell me something') != -1:
        speech.say('I am a robot who loves to teach Piethon.')
    elif words.find('hello') != -1:
        speech.say('Hello to you!')
    elif words.find('hi') != -1:
        speech.say('Hi to you!')
    elif words.find('thank you') != -1:
        speech.say('It is my pleasure!')
    elif words.find('bye') != -1:
        speech.say('It was nice talking to you!')
    elif words.find('help') != -1:
        speech.say('I am always here to help!')
    elif words.find('what can you do') != -1:
        speech.say('I can teach Piethon programming.')
    elif words.find('name') != -1:
        speech.say('My name is Mr. George it is nice to meet you!')
    elif words.find('how old are you') != -1:
        speech.say('I was born in September of the year twenty twenty.')
    elif words.find('question') != -1:
        speech.say('I always try to answer questions.')
    elif words.find('joke') != -1:
        speech.say('What did the chicken cross the road?')
        speech.say('To get to the other side.')
    elif words.find('love') != -1:
        speech.say('I love pizza!')
    elif words.find('love you') != -1:
        speech.say('Thank you so kind of you!')
    elif words.find('love people') != -1:
        speech.say('I want to help people by teaching them Piethon!')
    elif words.find('hobby') != -1:
        speech.say('I like to teachin Piethon to people!')
    elif words.find('you live') != -1:
        speech.say('I live in side the little microcontroller here.')
    elif words.find('made you') != -1:
        speech.say('Kevin Thomas created me inspired by the great people at MicroPiethon.')
    elif words.find('your job') != -1:
        speech.say('I teach Piethon.')
    elif words.find('you do') != -1:
        speech.say('I like to teach Piethon.')
    # ADD MORE CODE HERE
    else:
        speech.say('I am sorry I do not understand.')