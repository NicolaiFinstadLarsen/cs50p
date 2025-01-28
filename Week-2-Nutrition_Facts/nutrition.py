def main():
    fruit = input("Fruit: ").strip()
    kcal = get_kcal(fruit)

    if kcal:
        print(kcal)
    else:
        # Since the pset said to ignore input that was not a fruit.
        # exit() is frowned upon, or so i heard..
        return


def get_kcal(choosen_fruit):
    fruit_dict = {"apple": 130,
                  "avocado": 50,
                  "banana": 110,
                  "cantaloupe": 140,
                  "grapefruit": 60,
                  "grapes": 90,
                  "honeydew melon": 50,
                  "kiwifruit": 90,
                  "lemon": 15,
                  "lime": 20,
                  "nectarine": 60,
                  "orange": 80,
                  "peach": 60,
                  "pear": 100,
                  "pinapple": 50,
                  "plums": 70,
                  "strawberries": 50,
                  "sweet cherries": 100,
                  "tangerine": 50,
                  "watermelon": 80,
                  }

    return fruit_dict.get(choosen_fruit.lower())

    # for k, v in fruit_dict.items():
    #     # print(k)
    #     if choosen_fruit.lower() == k:
    #         # print(v)
    #         return v


main()
