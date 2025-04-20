import telebot

name = 'cat'
energy = 100
satiety = 50
happiness = 100
thirst = 0
intelligence = 10

bot = telebot.TeleBot('7408306461:AAE7ojR0FIrCIa_rGTSkE9EaplMmDMf3VlM')

def dead():
   global satiety, energy, thirst, happiness, intelligence
   satiety += 100
   energy -= 100
   thirst -= 100
   happiness -= 100
   intelligence -= 100
   

def drink():
   global satiety, energy, thirst
   satiety -= 10
   energy += 10
   thirst -= 50 

def listen_to_music():
    global energy, happiness
    energy -= 10
    happiness += 10
    
def feed():
   global satiety, energy, thirst
   satiety += 10
   energy += 10
   thirst += 20
    

def walk():
   global satiety, energy, happiness, thirst
   satiety -= 10
   energy -= 50
   happiness += 50
   thirst += 30

def play():
   global satiety, happiness, energy, thirst
   satiety -= 10
   energy -= 20
   happiness += 100
   thirst += 50

def sleep():
   global satiety, happiness, energy
   satiety -= 50
   happiness -= 10
   energy += 100

def read():
   global intelligence, happiness, energy
   intelligence += 10
   happiness += 10
   energy -= 20

def send_a_letter():
    global intelligence, happiness
    intelligence += 10
    happiness += 10
    
def check(message):
  global satiety, energy, happiness
  if satiety <= 10:
      bot.send_message(message.chat.id, f'{name} is died')

  elif satiety >= 100:
      bot.send_message(message.chat.id, f'{name} is full!')
  if happiness < 10:
      bot.send_message(message.chat.id, f'{name} is died!')
  elif happiness > 100:
      bot.send_message(message.chat.id, f'{name} is happy!')
  if energy < 10:
      bot.send_message(message.chat.id, f'{name} is died!')
  elif energy > 100:
      bot.send_message(message.chat.id, f'{name} got enough sleep!')
  if thirst >= 100:
      bot.send_message(message.chat.id, f'{name} is died!')
  elif thirst > 50:
      bot.send_message(message.chat.id, f'{name} needs to quench its thirst!')
  if  intelligence >= 100:
        bot.send_message(message.chat.id, f'{name} is smart!')
  elif intelligence <= 0:
        bot.send_message(message.chat.id, f'{name} jumped under the car!')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, 'Hi, I am [NuiI]! [переведено] напишите /help для получения списка команд')
    
@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, '/walk \n /feed \n /play \n /sleep \n /drink \n /start \n /help \n /music \n /read \n /letter \n /photo \n love your pets! \n /dead')

@bot.message_handler(commands=['feed'])
def feed_handler(message):
    feed()
    bot.send_message(message.chat.id, '🍽')
    check(message)

@bot.message_handler(commands=['play'])
def play_handler(message):
    play()
    bot.send_message(message.chat.id, '👾🏐')
    check(message)

@bot.message_handler(commands=['sleep'])
def sleep_handler(message):
    sleep()
    bot.send_message(message.chat.id, '☁️')
    check(message)

@bot.message_handler(commands=['drink'])
def drink_handler(message):
    drink()
    bot.send_message(message.chat.id, '☕️')
    check(message)

@bot.message_handler(commands=['walk'])
def walk_handler(message):
    walk()
    bot.send_message(message.chat.id, '⛸')
    check(message)

@bot.message_handler(commands=['music'])
def music_handler(message):
    listen_to_music()
    bot.send_message(message.chat.id, '🎧')
    check(message)

@bot.message_handler(commands=['read'])
def read_handler(message):
    read()
    bot.send_message(message.chat.id, '💻')
    check(message)

@bot.message_handler(commands=['letter'])
def send_a_letter_handler(message):
    send_a_letter()
    bot.send_message(message.chat.id, '✉️')
    check(message)

@bot.message_handler(commands=['dead'])
def dead_handler(message):
    dead()
    bot.send_message(message.chat.id, '')
    check(message)

@bot.message_handler(commands=['photo'])
def send_photo(message):
    photo_url = "https://ae04.alicdn.com/kf/S08b090d7a1984216a4323c2d32366e1aR.jpg_480x480.jpg"
    bot.send_photo(message.chat.id, photo_url, caption='It is your pet!')

bot.polling()