# Foobar is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Foobar is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Foobar.  If not, see <http://www.gnu.org/licenses/>.

import colorama
from colorama import Fore, Style
colorama.init()

import random

print(Fore.RED + "  __                  __                      ")
print(" / /__    _____ ___  / /___ __  ___  ___  ___ ")
print("/ __/ |/|/ / -_) _ \/ __/ // / / _ \/ _ \/ -_)")
print("\__/|__,__/\__/_//_/\__/\_, /  \___/_//_/\__/ ")
print("                       /___/                  " + Style.RESET_ALL)

print(Fore.YELLOW + "             |-----------------|")
print("             | 1 - Начать игру |")
print("             | 2 - Об игре     |")
print("             |-----------------|")
print(Fore.RED + "                 Версия 1.0a    " + Fore.YELLOW)

koloda = random.randint(2, 10)

while True:
    menu = input(">> ")

    if menu == "r":
        continue

    if menu == "1":
        print("     Игрок 1, пишите \"1\", если вам нужны")
        print("     карты или \"2\", если вам достаточно.")
        while True:
            player1 = input(">> ")
            if player1 == "1":
                print(f"      Вам попалась карта с номиналом: {koloda}")
                koloda = random.randint(2, 10)
            if player1 == "2":
                koloda = random.randint(2, 10)
                print(" Итак, вы собрали свои карты, теперь Игрок 2!")
                print("     Игрок 2, пишите \"1\", если вам нужны")
                print("     карты или \"2\", если вам достаточно.")
                while True:
                    player2 = input(">> ")
                    if player2 == "1":
                        print(f"      Вам попалась карта с номиналом: {koloda}")
                        koloda = random.randint(2, 10)
                    if player2 == "2":
                        print("  Игра завершена! Считайте итоговый номинал.")
                        print("    Напишите \"1\", дабы начать игру заново.")
                        break
                break
        continue
        break

    if menu == "2":
        print(" |-----------------------------------------|")
        print(" |               Игру написал              |")
        print(" |Конышев Юрий aka Yura_FX на языке Python.|")
        print(" |        https://github.com/YuraFX        |")
        print(" |                  (2023)                 |")
        print(" |-----------------------------------------|")
        print("                                            ")
        print(" |-----------------------------------------|")
        print(" |              Правила игры:              |")
        print(" | 1. Играют два игрока.                   |")
        print(" | 2. Цель игры - набрать 21 очко или      |")
        print(" | приблизиться к этой цифре, не перебрав. |")
        print(" | 3. Игрок, набравший 21 очко точно,      |")
        print(" | побеждает. Если кто-то перебирает сумму |")
        print(" | более 21, он проигрывает.               |")
        print(" |-----------------------------------------|")