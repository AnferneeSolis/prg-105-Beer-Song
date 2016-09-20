def math(num_beers):
    while num_beers > 0:
        print(str(num_beers) + " bottles of beer on the wall")
        print(str(num_beers) + " bottles of beer,")
        print("If one of those bottles should happen to fall")
        print(str(num_beers - 1) + " bottle of beer on the wall!\n")

        num_beers = num_beers - 1
    return 0

math(int(10))
