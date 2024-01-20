from urllib.request import urlopen as ulr
from bs4 import BeautifulSoup

def loop_de_loop(meal,arr):
    for item in arr:
        print(meal)
        print(item['href'])

# links
recipe_bon = 'https://www.allrecipes.com/recipes/78/breakfast-and-brunch/'
recipe_lunch = 'https://www.allrecipes.com/recipes/17561/lunch/'
recipe_dinner = 'https://www.allrecipes.com/recipes/17562/dinner/'
recipe_snack = 'https://www.allrecipes.com/recipes/76/appetizers-and-snacks/'

# client stuff
client_bon = ulr(recipe_bon)
client_lunch = ulr(recipe_lunch)
client_dinner = ulr(recipe_dinner)
client_snack = ulr(recipe_snack)

# read client stuff
html_bon = client_bon.read()
client_bon.close()
html_lunch = client_lunch.read()
client_lunch.close()
html_dinner = client_dinner.read()
client_dinner.close()
html_snack = client_snack.read()
client_snack.close()

# html parsing
bon_soup = BeautifulSoup(html_bon, 'html.parser')
lunch_soup = BeautifulSoup(html_lunch, 'html.parser')
dinner_soup = BeautifulSoup(html_dinner, 'html.parser')
snack_soup = BeautifulSoup(html_snack, 'html.parser')

# storing every recipe link into an array
breakfast_recette = bon_soup.findAll("a", {"class": "recipeCardtitleLink"},  href=True)
lunch_recette = lunch_soup.findAll("a", {"class": "recipeCardtitleLink"},  href=True)
dinner_recette = dinner_soup.findAll("a", {"class": "recipeCardtitleLink"},  href=True)
snack_recette = snack_soup.findAll("a", {"class": "recipeCardtitleLink"},  href=True)

# printing em recipes:
loop_de_loop("Breakfast: ", breakfast_recette)
loop_de_loop("Lunch: ", lunch_recette)
loop_de_loop("Dinner: ", dinner_recette)
loop_de_loop("Appetizer: ", snack_recette)
