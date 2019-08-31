# BackendTest
design REST APIs using Django REST Framework


- python 3.6.5
- Django 2.2.4
- Markdown 3.1.1

Models:

 

- Design the User Model with username(unique field), email(unique field), first_name,
last_name,m password. (You can use the django inbuilt user model)
 

- Design A Step Model with step_text(string field, not null), Many to One relationship with
Recipe
 

- Design An Ingredient Model with text(not null, string), Many to One relationship with
Recipe
 

- Design A Recipe Model with name(string, not null), Foreign Key to User table(one to one
relationship), One to Many relationship with Step and Ingredient Model

superuser is :admin password:qazwsx123
- Show all recipes:(You can delete update and get the recipe)http://127.0.0.1:8000/api/v1/recipes/
![Image description](https://github.com/wangjinlong9788/BackendTest/blob/master/show/recipes.JPG)

- Show recipe according to user by user Id:(You can delete update and get the recipe by user id here)
![Image description](https://github.com/wangjinlong9788/BackendTest/blob/master/show/Byid.JPG)

- Show ingredient accordingly:(You can delete update and get the ingredient here)
![Image description](https://github.com/wangjinlong9788/BackendTest/blob/master/show/ingredient.JPG)

- Whole
![Image description](https://github.com/wangjinlong9788/BackendTest/blob/master/show/List%20Create%20Recipe%20%E2%80%93%20Django%20REST%20framework.png)

- Show recipe according to user by recipe Id:(You can delete update and get the recipe by recipe id here)
![Image description](https://github.com/wangjinlong9788/BackendTest/blob/master/show/recipe_id.JPG)


- Show steps accordingly.
![Image description](https://github.com/wangjinlong9788/BackendTest/blob/master/show/steps.JPG)

- show Login page(frond end page):
![Image description](https://github.com/wangjinlong9788/BackendTest/blob/master/show/login.JPG)
- show Register page(frond end page):
![Image description](https://github.com/wangjinlong9788/BackendTest/blob/master/show/register.JPG)

- show user admin recipe (frond end page):
![Image description](https://github.com/wangjinlong9788/BackendTest/blob/master/show/frondrecipes.JPG)


