# JP0030

import random

def ek_machli_pani_mein_gayi():
    fish_count = random.randint(0, 50) 
    print("Shuru ho gayi 'Ek Machli Pani Mein Gayi'...")
    print(f"Shuru mein {fish_count} machliyan hain.\n")

    while fish_count > 0:
        machli_to_remove = int(input("Kitni machliyan bacha ni hee?: "))
        if machli_to_remove < 1 or machli_to_remove > 3:
            print("Galat ! Sirf 1 se 3 machliyan bacha sakte ho.")
            continue

        fish_count -= machli_to_remove
        if fish_count <= 0:
            print("\nHaar gaye ! machli pahelese hi mari hui hee . \nPura machliyon ka khandan khatam ho gaya. !!🤣!!")
        else:
            print(f"\n{fish_count} machliyan baaki hain.\n")
            computer_move = random.randint(1, min(3, fish_count))
            print(f"Ab computer ne {computer_move} machliyan utha li.")
            fish_count -= computer_move
            if fish_count <= 0:
                print("\nHaar gaye😂! Computer ne sab machliyan utha li.")
            else:
                print(f"\n{fish_count} machliyan baaki hain.\n")

if __name__ == "__main__":
    ek_machli_pani_mein_gayi()
