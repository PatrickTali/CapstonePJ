from flask import Blueprint, render_template,request
from flask_login import login_required
from cocktail_inventory.forms import IngredientForm
from cocktail_inventory.models import Cocktail, db
import requests


site = Blueprint('site', __name__, template_folder='site_templates')



@site.route('/')
def home():
    print("ooga booga in the terminal")
    return render_template('index.html')


@site.route('/profile', methods = ['GET', 'POST'])
@login_required
def profile():
    my_ingredient =IngredientForm()
    

    if request.method == "POST" and my_ingredient.validate_on_submit():
        print('formvalidated')
        ingredient = my_ingredient.ingredient.data.lower()

        response =requests.get(f'https://www.thecocktaildb.com/api/json/v1/1/filter.php?i={ingredient}')
        data = response.json()['drinks']
        
        
        for drinks in data:
            id = drinks["idDrink"]
            name = drinks["strDrink"]
            img = drinks["strDrinkThumb"]
            
            
        
            cocktail=Cocktail(id,name,img) 
            if not Cocktail.known_cocktail(id):
                 db.session.add(cocktail)
                 db.session.commit()   

            

     
    return render_template('profile.html', form=my_ingredient, drinks=Cocktail.query.all() )


    



   
   
   






@site.route('/get_drink_info/<int:id>', methods =['POST'])
@login_required
def get_drink_info(id):

    
    response =requests.get(f'https://www.thecocktaildb.com/api/json/v1/1/lookup.php?i={id}')
    data = response.json()['drinks']
    mydrink= Cocktail.query.get(id)
    
    for drink in data:
        new_drink= {}
        new_drink={
        "id":drink["idDrink"],
        "name":drink["strDrink"],
        "img":drink["strDrinkThumb"],
        "instructions":drink['strInstructions'],
        "ingredient1" : drink['strIngredient1'],
        "ingredient2" : drink['strIngredient2'],
        "ingredient3" :drink['strIngredient3'],
        "ingredient4" :drink['strIngredient4'],
        "ingredient5" :drink['strIngredient5'],
        "ingredient6" :drink['strIngredient6'],
        "ingredient7" :drink['strIngredient7'],
        "ingredient8" :drink['strIngredient8'],
        "ingredient9" :drink['strIngredient9'],
        "ingredient10" :drink['strIngredient10'],
        "ingredient11" :drink['strIngredient11'],
        "ingredient12" :drink['strIngredient12'],
        "ingredient13" :drink['strIngredient13'],
        "ingredient14" :drink['strIngredient14'],
        "ingredient15" :drink['strIngredient15'],
        "measure1":drink['strMeasure1'],
        "measure2" :drink['strMeasure2'],
        "measure3" :drink['strMeasure3'],
        "measure4" :drink['strMeasure4'],
        "measure5" :drink['strMeasure5'],
        "measure6": drink['strMeasure6'],
        "measure7" :drink['strMeasure7'],
        "measure8" :drink['strMeasure8'],
        "measure9" :drink['strMeasure9'],
        "measure10" :drink['strMeasure10'],
        "measure11" :drink['strMeasure11'],
        "measure13" :drink['strMeasure13'],
        "measure14" :drink['strMeasure14'],
        "measure15" :drink['strMeasure15']
    
    
        }



    

    
    mydrink.to_dict(new_drink)
    
    mydrink.saved()

    return render_template('cocktaildetails.html', mydrink=mydrink, drink=drink)




    
    
    
    
    
    
    
    

    
    
    
       

    
    
    
    
    





