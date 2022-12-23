'''
전제조건
1. 맞춰야 하는 secret_word의 자릿수는 주어진 상태라고 가정하고 letter_guessed = [_____] 이런 식으로 설정했어요. ( 보통 행멘에서 그렇게 하지 않나요...!?)
2. 주어진 함수에 파라미터를 자유롭게 추가할 수 있음.
3. 사용자가 추측한 알파벳은 입력받는걸로 가정. (input() 사용) -> 추측한 알파벳을 어떻게 아는지 설명이 없어서요)
4. 게임에 성공했을 때에는 pirnt("success")를, 실패했을 때에는 print("failed")를 출력. -> 이건 어떻게 하라고 안나와있어서 맘대로 했어요!!
5. 입력했던 알파멧이 secret_word에 있는데 또 입력햇을 때는 실패로 세지 않았음.
'''

def load_words():
    #단어를 뭔 파일에서 불러오는 함수 ( 지환님이 하시는 부분이에요 )
    return

def get_word():
    # 위에 불러온 파일에서 랜덤으로 단어 하나를 가져오는 함수. 이 코드에서는 임의로 claptrap으로 지정했어요.

    word = 'claptrap'
    return word

MAX_GUESSES = 6 # 아마 최대로 시도할 수 있는 횟수겠죠?
secret_word = get_word()
letter_guessed = ['_' for i in range(len(secret_word))]

def word_guessed(user_letter):

    is_guessed = False

    global secret_word
    global  letter_guessed

    #사용자의 추측 알파벳이 맞았다면 letter_guessed에 추측한 알파벳을 추가하고 true를, 틀렸다면 false를 반환하는 함수

    for i in range(len(secret_word)):
        if user_letter == secret_word[i]:
            letter_guessed[i] = user_letter
            is_guessed = True

    return is_guessed

def print_guessed():

    # 지금까지 맞춘 철자들을 출력하는 함수. letter_guessed가 list형태이기 때문에 문자열로 변환해서 출력

    print(''.join(letter_guessed))


def play_hangman():

    mistaked_made = 0 # 실패횟수 초기화

    while True:
        user_leter = input()
        if word_guessed(user_leter) == False:
            mistaked_made += 1
        print_guessed()

        if ''.join(letter_guessed) == secret_word:
            print("success")
            print(secret_word)
            break
        if mistaked_made == MAX_GUESSES:
            print("failed")
            break

    return

play_hangman()

MAX_GUESSES = 0
if (len(secret_word) < 4):
    MAX_GUESSES = 12
elif (4 <= len(secret_word) < 8):
    MAX_GUESSES = 6
elif (8 <= len(secret_word)):
    MAX_GUESSES = 5

if MAX_GUESSES == 12:
    print('easy')
elif MAX_GUESSES == 6:
    print('medium')
elif MAX_GUESSES == 5:
    print('hard')


def decide_level(level):
    while True:
        index = randrange(0,len(wordlist))
        if level == "easy":
            if len(wordlist[index]) < 4:
                word = wordlist[index]
                break
        elif level == "medium":
            if 4 <= len(wordlist[index]) < 8:
                word = wordlist[index]
                break
        elif level == "hard":
            if len(wordlist[index])>= 8:
                word = wordlist[index]
                break
    return

level = input()










