print("Welcome to Choose Your Own Destiny!")
name = input("Enter you name: ")
age = int(input("Enter your age: "))


health = 10


if age >= 18:
    print("You're old enough to play")
    wana_play = input("Do you want to play? ").lower()
    if wana_play == "yes":
        print("You are starting with", health, "health")
        print("Let's start the game!")

        left_or_right = input("First choice... Left or Right (left/right)? ").lower()
        if left_or_right == "left":
            ans = input(
                "Nice, you follow the path and reach a lake... Do you swim across or go around (across/around)? "
            ).lower()

            if ans == "around":
                print("You went around and reached the other side of the lake")

            elif ans == "across":
                print(
                    "You managed to get across, but were bit by a shark and lost 5 health"
                )
                health -= 5

            ans = input(
                "You notice a house and a river. Which do you go to (river/house)? "
            ).lower()
            if ans == "house":
                print(
                    "You go to the house and are greeteed by the owner... He doesn't like you and you lose 5 health"
                )
                health -= 5

                if health <= 0:
                    print(
                        "You now have 0 health and you lost the game.. Beter luck next time"
                    )
                else:
                    print("Yayyy! you survived")

            else:
                print("You fell in the river and lost...")

        else:
            print("You fell down and lost the game. Better luck next time")

    else:
        print("see you later...!")

else:
    print("You're not ond enough to play")
