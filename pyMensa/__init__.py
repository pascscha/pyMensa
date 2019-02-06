from .Mensa import *

name = "pyMensa"

available = [Polymensa(), FoodLab(), Clausiusbar(), Polysnack(), Foodtrailer(), AlumniLounge(),
             Bellavista(), FusionMeal(), GessBar(), Tannenbar(), Dozentenfoyer(), Platte(),
             Raemi59(), UZHMercato(), UZHZentrum(), UZHLichthof(), Irchel(), IrchelAtrium(), Binzmühle(),
             Cityport(), Zahnmedizin(), Tierspital(), BotanischerGarten()]


def get_meals(name):
    return get_mensa(name).get_meals()


def get_mensa(name):
    for mensa in available:
        if mensa.has_alias(name):
            return mensa
