# 1
class MusicPlayer:
    def __init__(self, song):
        self.song = song

    def play(self):
        print(f"{self.song} chalinyapti")

    def stop(self):
        print("To‘xtatildi")


player = MusicPlayer("Song.mp3")
player.play()
player.stop()



# 2
class Fan:
    def __init__(self, speed):
        self.speed = speed

    def increase(self):
        print(f"{self.speed}, tezlik oshdi")

    def decrease(self):
        print(f"{self.speed}, tezlik kamaydi")
x = Fan(50)
x.increase()
x.decrease()


3
class TV:
    def __init__(self, channel):
        self.channel = channel

    def next_channel(self):
        print(f"{self.channel}, Keyingi kanal")

    def prev_channel(self):
        print(f"{self.channel}, Oldingi kanal")
x = TV("sevimli")
x.next_channel()
x.next_channel()



# 4
class ShopItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def show(self):
        print(f"{self.name}, -  {self.price}, som")

    def discount(self):
        print(f" 50  Chegirma ")
x = ShopItem("Olma", 50)
x.show()
x.discount()

# 5
class Alarm:
    def __init__(self, time):
        self.time = time

    def set_alarm(self):
        print(f"{self.time} ga o'rnatildi ")

    def ring(self):
        print(f" jiring!!!!!!!!!! ")
x = Alarm("07 : 00")
x.set_alarm()
x.ring()
