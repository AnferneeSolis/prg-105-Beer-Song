def math(num_beers):
    if num_beers > 0:
        print(str(num_beers) + " bottles of beer no the wall")
        print(str(num_beers) + " bottles of beer")
        print("If one of those bottles should ahppen to fall")
        print(str(num_beers - 1) + " bottle of beer on the wall!\n")

        math(num_beers - 1)
    else:
        print("FIN")

math(int(99))
