from flask import Flask, request, render_template, flash, redirect, url_for, flash
import django
from django.conf import settings
from django.template import Template, Context
# # # # # # #

####### ####### ####### ####### ####### #######

# # # # # # #
accura = 0
html_output = ""
imagef = ""
image_a = ""
image_b = ""
image_c = ""
image_d = ""
image_e = ""
totfar = 0
urlcheck = 0
cutoff = 750
found_valid_variety = False

import http.server
import socketserver
selected_variety = ""
app = Flask(__name__)
app.secret_key = 'alltheglorygoestochristmnt129'
varity = []
skipse = 0
fodd = 0
average = 0
iterated = 0
import time
import os
import re
import random
from random import randint
import requests
from bs4 import BeautifulSoup
import json
import tensorflow as tf
import matplotlib.pyplot as plt
import pandas as pd
ndf = pd.DataFrame()
import numpy as np
import keyboard
from groq import Groq
from datetime import datetime
from keras.models import load_model
htmltext = ""
main_a = ""
main_b = ""
main_c = ""
main_d = ""
main_e = ""
ingred_a = ""
ingred_b = ""
ingred_c = ""
ingred_d = ""
ingred_e = ""
instruc_a = ""
instruc_b = ""
instruc_c = ""
instruc_d = ""
instruc_e = ""
nutr_a = ""
nutr_b = ""
nutr_c = ""
nutr_d = ""
nutr_e = ""
imagef = ""
image_a = ""
image_b = ""
image_c = ""
image_d = ""
image_e = ""

  #
#####
  #
  #

vari_str = ""
ports = random.randint(1024, 49151)
PORT = ports
inputlist = []
ford = ""
ingredientf = ""
namef = ""
cook_timef = ""
yield_valuef = ""
nutritionf = ""
ingredientsf = ""
instructions = []
jlist = []
jalist = []
rankedl = []
rankedk = []
#the lord is great all the glory goes to our savior#
jcheckej = ""
javerage = ""
approv_da = ""
approv_item = ""
approv = []
approvt = []
dundun = 0
nfacts = [] 
nutchk = ""
irisrec = []
ysure = ""
chk = 0
randostat = 0
vari1 = ""
vari2 = ""
vari3 = ""
vari4 = ""
vari5 = ""
vari6 = ""
vari7 = ""
vari8 = ""
vari9 = ""
vari10 = ""
ingreci = ""
yes_no = ""
detect_a = ""
detect_b = []
item_list = []
inputed = 0
raw_pred = 0
item_connections = {}
sites = ['https://www.allrecipes.com/recipes/16588/salad/vegetable-salads/caprese-salad/', "https://www.allrecipes.com/recipes/17558/main-dish/sandwiches/heroes-hoagies-and-subs/", "https://www.allrecipes.com/recipes/1314/breakfast-and-brunch/eggs/omelets/"]
#, 'https://www.allrecipes.com/recipes/251/main-dish/sandwiches/', 'https://www.allrecipes.com/recipes/1564/breakfast-and-brunch/eggs/frittata/', 'https://www.allrecipes.com/recipes/15167/everyday-cooking/vegetarian/main-dishes/pizza/', 'https://www.allrecipes.com/recipes/16588/salad/vegetable-salads/caprese-salad/'
jdf = pd.read_csv("required7.txt")
features = jdf.iloc[:, 0]  
#sites = ['https://www.allrecipes.com/recipes/251/main-dish/sandwiches/', 'https://www.allrecipes.com/recipes/1564/breakfast-and-brunch/eggs/frittata/', 'https://www.allrecipes.com/recipes/15167/everyday-cooking/vegetarian/main-dishes/pizza/', 'https://www.allrecipes.com/recipes/16588/salad/vegetable-salads/caprese-salad/']
vectorize_layer = tf.keras.layers.TextVectorization(max_tokens=1000, output_mode='int')
itemdexa = 0
vectorize_layer.adapt(features.values) 

features_vectorized = vectorize_layer(features.values)
print(features_vectorized)
vitscale = 0
# ['Tomato, roma', 
# 'Tomatoes, canned, red, ripe, diced', 
# 'Oil, olive, extra virgin', 
# 'Onions, red, raw', 
# 'Spinach, mature', 
# 'Cheese, mozzarella, low moisture, part-skim', 
# 'Peaches, yellow, raw', 
# 'Garlic, raw', 
# 'Celery, raw', 
# 'Peppers, bell, green, raw']
summ = 0
#['Tomato, roma', 
# 'Tomato Sauce',
# 'Oil, olive, extra virgin', 
# 'Cheese, mozzarella, low moisture, part-skim', 
# 'Cheese, feta',
# 'Bread, white, commercially prepared', 
# 'Peppers, bell, red, raw', 
# 'Spinach, mature', 
# 'Flour, raw', 
# 'Egg']
infrac = 0
sites_iterator = iter(sites)
ulr = ""
ulr2 = ""
doneso = ""
reciso = ""
detectb = []
ingredlistch = ["Oil", "Onion", "Kale", "Sauce", "Garlic", "Pepper", "Egg", "Cucumber", "Butter", "Pork"]
succe = 0
loading = 1
totae = 0
ratee = 0
title_a = ""
title_b = ""
title_c = ""  
title_d = ""
title_e = ""
print("Find Nutritious Recipes from Pantry Items!")
vari = ""
recipefilter = []
fob = []
fod = ""
vari_total = []
ingr_total = []
gob = []
gose = ""
ingredlistd = ["Milk", "Sausage", "Beans", "Apple", "Cheese", "Mushroom", "Egg", "Beef", "Tomato", "Chicken", "Oil", "Fish", "Yogurt", "Flour", "Pork", "Potato", "Lettuce", "Nuts", "Cabbage", "Seeds", "Applesauce", "Banana", "Beets", "Blueberries", "Bread", "Broccoli", "Butter", "Carrot", "Cauliflower", "Celery", "Cherries", "Collards", "Cookie", "Crab", "Cream", "Cucumber", "Eggplant", "Fig", "Frankfurter", "Garlic", "Grains", "Grapes", "Ham", "Hummus", "Kale", "Ketchup", "Kiwi", "Lentils", "Melon", "Mustard", "Nectarine", "Oats", "Olive", "Onion", "Orange", "Peach", "Pear", "Peas", "Pepper", "Pickles", "Pineapple", "Raspberries", "Rice", "Salsa", "Salt", "Sauce", "Shrimp", "Spinach", "Squash", "Strawberries", "Sugar", "Turkey"]
ingredlista = ["Tomato", "Oil", "Onion", "Spinach", "Cheese", "Mushroom", "Garlic", "Celery", "Pepper", "Bread", "Egg", "Cucumber", "Potato", "Olive", "Pork"]
ingredlistb = ["Tomato", "Oil", "Onion", "Lettuce", "Cheese", "Peach", "Garlic", "Celery", "Pepper", "Bread", "Egg", "Cucumber", "Milk", "Butter", "Beef"]
ingredlistc = ["Tomato", "Oil", "Onion", "Kale", "Cheese", "Sauce", "Garlic", "Turkey", "Pepper", "Bread", "Egg", "Cucumber", "Butter", "Olive", "Pork"]
ingredlistmk = ["Onion", "Kale", "Cheese", "Sauce", "Garlic", "Turkey", "Pepper", "Bread", "Egg", "Cucumber", "Butter", "Olive", "Pork"]
ingredlist = ingredlistc
inputs = ingredlista
print(inputs)
vari1 = ""
vari2 = ""
vari3 = ""
vari4 = ""
vari5 = ""
vari6 = ""
vari7 = ""
vari8 = ""
vari9 = ""
vari10 = ""
vitA = 0.0003
vitB1 = 0.0004
vitB2 = 0.000433
vitB3 = 0.005333
vitB5 = 0.001667
vitB6 = 0.000433
vitB7 = 0.01
vitB9 = 0.001333
vitB12 = 0.0008
vitC = 0.03
vitD = 0.000005
vitE = 0.005
vitK = 0.04
vitCh = 0.183333
minCa = 0.333333
minCl = 0.766667
minCr = 0.011667
minCu = 0.003
minF = 0.001333
minI = 0.00005
minFe = 0.002667
minMg = 0.14
minMn = 0.000767
minMo = 0.000015
minP = 0.233333
minK = 1.566667
minSe = 0.000018
minNa = 0.766667
minS = 0.283333
minZn = 0.003667
varieties = []
variranks = []
varifinal = []
df_merged = pd.DataFrame()
vitA_list = [
    "Vitamin A",
    "Vitamin A, RAE",
    "Vitamin A, RE",
]
vitB1_list = ["Thiamin",
    "Thiamin, intrinsic",
    "Thiamin, added",]
vitB2_list = ["Riboflavin",
    "Riboflavin, intrinsic",
    "Riboflavin, added",]
vitB3_list = ["Niacin",
    "Niacin from tryptophan, determined",
    "Niacin equivalent N406 + N407",
    "Niacin, intrinsic",
    "Niacin, added",]
vitB5_list = ["Pantothenic acid"]
vitB6_list = ["Vitamin B-6",
    "Vitamin B-6, N411 + N412 + N413",]
vitB7_list = ["Biotin",]
vitB9_list = ["Folate, total"]
vitB12_list = []
vitC_list = ["Vitamin B-12",
    "Vitamin B-12, intrinsic",
    "Vitamin B-12, added",]
vitD_list = ["Vitamin D (D2 + D3)"]
vitE_list = ["Vitamin E"]
vitK_list = ["Vitamin K (Menaquinone-4)",
    "Vitamin K (Dihydrophylloquinone)",
    "Vitamin K (phylloquinone)"]#addition for this one ONLY
vitCh_list = ["Choline, total"]
minCa_list = ["Calcium, Ca"]
minCl_list = ["Chlorine, Cl"]
minCr_list = ["Chromium, Cr"]
minCu_list = ["Copper, Cu"]
minF_list = ["Fluoride, F"]
minI_list = ["Iodine, I"]
minFe_list = ["Iron, Fe"]
minMg_list = ["Magnesium, Mg"]
minMn_list = ["Manganese, Mn"]
minMo_list = ["Molybdenum, Mo"]
minP_list = ["Phosphorus, P"]
minK_list = ["Potassium, K"]
minSe_list = ["Selenium, Se"]
minNa_list = ["Sodium, Na"]
minS_list = ["Sulfur, S"]
minZn_list = ["Zinc, Zn"]
calcheck = 0
prtcheck = 0
crbcheck = 0
fatcheck = 0
fibcheck = 0
sarcheck = 0
inicrbcheck = crbcheck
iniprtcheck = prtcheck
inifatcheck = fatcheck
inisarcheck = sarcheck
inifibcheck = fibcheck
inicalcheck = calcheck
checkej = [crbcheck, prtcheck, fatcheck, sarcheck, fibcheck, calcheck, vitscale]
dcheckej = [crbcheck, prtcheck, fatcheck, sarcheck, fibcheck, calcheck, vitscale]
ncheckej = np.asarray([crbcheck, prtcheck, fatcheck, sarcheck, fibcheck, calcheck, vitscale])
errors = []
weightsa = np.array([0.2, 0.15, 0.15, 0.1, 0.1, 0.2, 0.2])
parame = 0
parame2 = 0
#the lord can do all! glory to Him
vitmin = [vitA, vitB1, vitB2, vitB3, vitB5, vitB6, vitB7, vitB9, vitB12, vitC, vitD, vitE, vitK, vitCh, minCa, minCl, minCr, minCu, minF, minI, minFe, minMg, minMn, minMo, minP, minK, minSe, minNa, minS, minZn]
with open('requirements copy.txt', 'r') as file:
    file_contents = file.read()
#PRAISE THE LORD
with open('requirements777.txt', 'r') as file:
    file_contents2 = file.read()
#PRAISE THE LORD
client = Groq(
    api_key="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",
)
#PRAISE THE LORD
df = pd.read_csv("requirements777.txt")
#PRAISE THE LORD
model2_path = r"C:\Users\nickc\Downloads\my_modelB3.h5"
if os.path.exists(model2_path):
    print("File exists.")
else:
    print("File does not exist.")
model2 = tf.keras.models.load_model(model2_path, compile=False)
varivit = ""
df = df.drop(columns=["data_type", "food_category_id", "publication_date"])
weights = np.array([0.2, 0.15, 0.15, 0.1, 0.1, 0.1])
def carbcheck(calcheck, crbcheck):
    # Scale based on the percentage
    parame = crbcheck/calcheck
    if parame >= 0.7:  
        return 0
    elif parame == 0: 
        return 0
    elif parame == 0.5: 
        return 1
    crbcheck = parame 
    if crbcheck > 0.5:
        crbcheck = 0.7 - crbcheck
        crbcheck = crbcheck * 5
    else:
        crbcheck = parame * 2
    return crbcheck
def fatfcheck(calcheck, fatcheck):
    parame = fatcheck/calcheck
    if parame >= 0.4:
        return 0
    elif parame == 0:  
        return 0
    elif parame == 0.25:  
        return 1
    fatcheck = parame 
    if fatcheck > 0.25:
        fatcheck = 0.4 - fatcheck
        fatcheck = fatcheck * 7 
    else:
        fatcheck = parame * 2.5
    return fatcheck
def sgarcheck(sarcheck):
    if sarcheck == 10:
        return 1
    if sarcheck == 0 or sarcheck >= 20:
        return 0
    if sarcheck >= 10:
        sarcheck = 20 - sarcheck
        sarcheck = sarcheck/10
        return sarcheck
    elif sarcheck < 10:
        sarcheck = sarcheck/10
        return sarcheck
def protcheck(prtcheck):
    if prtcheck >= 17:
        return 1
    else:
        prtcheck = prtcheck/17
        return prtcheck
def fibecheck(fibcheck):
    if fibcheck >= 10:
        return 1
    else:
        fibcheck = fibcheck/10
        return fibcheck
def calocheck(calcheck):
    if calcheck == 750:
        return 1
    elif calcheck == 0 or calcheck > 1500:
        return 0
    if calcheck < 750:
        calcheck = calcheck/750
        return calcheck
    if calcheck > 750:
        calcheck = 1500 - calcheck 
        calcheck = calcheck/750
        return calcheck
df_m = pd.DataFrame()
odf = pd.DataFrame()
varivit_total = [] #     tf.keras.layers.Input(shape=(None,), dtype='int32'),  # Input layer for the vectorized text
savior = []
savory = []
#     tf.keras.layers.Dense(32, activation='relu'),  # Dense hidden layer
#     tf.keras.layers.Dense(1, activation='sigmoid')  # Output layer for binary classification
match = []
def vitamincheck(varivit, df_merged, vit_lists, vitmin, varivit_total):
    df = pd.read_csv("soup3.txt", low_memory=False)
    df = df.drop(columns=["id", "data_points", "derivation_id", "min", "max", "median", "footnote", "min_year_acquired"])
    #print(df.query(f"fdc_id == {goh}"))
    #df = pd.read_csv("almighty.txt")
    df = df.query(f"fdc_id == {varivit}")
    atr = len(df['nutrient_id'])
    #print(atr)
    atr = int(atr)
    
    df_f = pd.read_csv("soup3.txt", low_memory=False)
    df_n = pd.read_csv("almighty.txt", low_memory=False)
    df_f = df_f.sort_values(by=['nutrient_id'])
    df_n = df_n.sort_values(by=['nutrient_id'])
    df_merged = pd.merge(df_f, df_n, how="inner")
    df_merged = df_merged.query(f"fdc_id == {varivit}")
    df_merged = df_merged.sort_values(by=['nutrient_id'])
    df_merged = df_merged.query("nutrient_id.notna()")
    df_merged = df_merged.query("amount > 0")
    df_merged = df_merged.query("unit_name != 'IU'")
    df_merged = df_merged.drop(columns=["id", "data_points", "derivation_id", "min", "max", "median", "footnote", "min_year_acquired", "nutrient_nbr", "rank"])
    df_merged.loc[df_merged['unit_name'] == 'G', 'amount'] *= 1
    df_merged.loc[df_merged['unit_name'] == 'MG', 'amount'] *= 0.001
    df_merged.loc[df_merged['unit_name'] == 'UG', 'amount'] *= 0.000001
    df_merged.loc[df_merged['unit_name'] == 'KCAL', 'amount'] *= 1
    print(df_merged.columns)
    df_merged = df_merged.drop(columns=["unit_name"])
    print(df_merged[["amount", "name"]])
    df_merged["name"] = df_merged["name"].str.lower().str.strip()
    for index, vitA_list in enumerate(vit_lists):
        # Normalize the vitamin names
        vitA_list = [item.lower().strip() for item in vitA_list]

        # Find matches
        match = set(vitA_list) & set(df_merged["name"].unique())
        print(f"Matching items for {vitA_list}: {match}")

        # Filter the DataFrame for the matching items
        df_m = df_merged[df_merged["name"].isin(match)]
        
        # Check if there are matching rows, sum the 'amount' if so
        if not df_m.empty:
            varivit = df_m['amount'].sum() 
            varivit = float(varivit) #i added int before, ruining the project
            print(vitmin[index])
            print(varivit)
            #vari1vit = vari1vit/vitmin[index]
            #if vari1vit > 1:
                #vari1vit = 1
        else:
            print(f"No matches found for {vitA_list}")
            varivit = 0  # Default to 0 if no match is found
        # Append the result to the totals list
        varivit_total.append(varivit)
    varivit = np.array(varivit_total)
    #var1vit = np.average(vari1vit_total)
    return varivit
indexd = 0
def recipecheck(vari, reciso):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": "Here's a broad food ingredient. \n" + vari + "\n Using conversion rates, how much of it (in grams) is in this recipe? \n" + reciso + "\n 0.035 ounce = 1 gram, 1 fluid ounce = 1/8 cup, 1 ounce = 28.3495 grams, 0.5 oz = 14 grams, 1 oz = 28 grams, 1/4 pound (lb) = 113 grams, 1/3 pound (lb) = 151 grams, 1/2 pound (lb) = 227 grams, 1 pound (lb) = 454 grams, 1.10 pounds (lbs) = 500 grams, 2.205 pounds (lbs) = 1 kilogram, 35 oz = 1 kilogram. one cherry tomato â€” 0.661 g. one Italian or plum tomato â€” 2.410 g. one medium tomato (about 123 g) â€” 4.780 g. 1 cup chopped or sliced tomatoes (about 180 g), 1 tomato - 120 grams, 2 medium-sized tomatoes - 240 grams, Heirloom tomato - 120 grams, San Marzano tomato (full) - 110 grams, Bread slice - 35 grams, Bread loaf - 800 grams, 1 cheese piece - 30 grams, 1 cup of spinach - 30 grams, 1 cup of olive oil - 216 grams, 1 cup of onions, chopped - 160 grams, 1 medium onion - 110 grams, 1 large onion - 150 grams, 1 tablespoon olive oil - 13.5 grams, 1 package of spinach (10 oz) - 284 grams, 1 cup of white mushrooms - 96 grams, 1 cup of sliced white mushrooms - 70 grams, 1 small white mushroom - 10 grams, 1 medium white mushroom - 18 grams, 1 large white mushroom - 23 grams, 1 clove of garlic - 3 grams, 1 cup of garlic - 136 grams, 1 stalk, medium, 40 grams, 1 stalk, small - 17 grams, 1 cup of bell peppers, chopped - 149 grams, 1 medium bell pepper - 119 grams, 1 large bell pepper - 164 grams, 1 small bell pepper - 74 grams, 1 cup of bell pepper, sliced - 92 grams, 1 ounce of egg whites - 28 grams, 1 cup of whole eggs, sifted - 85 grams, 1 cup of egg yolks, sifted - 67 grams, 1 cucumber - 301 grams, 0.5 cup sliced cucumber - 52 grams, 1 medium potato - 213 grams, 1 large potato - 369 grams, 1 small potato - 170 grams, 0.5 cup potatoes, diced - 75 grams, 1 olive - 2.7 grams, 1 ounce of raw ground pork - 28.35 grams, 4 ounces of raw ground pork - 113 grams, 3 ounces of cooked ground pork - 85 grams, 1 lettuce (romaine) cup shredded - 47 grams, 1 head of (romaine) lettuce - 626 grams, 1 head of green leaf lettuce - 360, 1 cup of shredded green leaf lettuce - 36 grams, 1 medium peach - 150 grams, 1 cup slices - 154 grams, 1 small peach - 134 grams, 1 medium peach - 150 grams, 1 large peach - 174 grams, 1 extra-large peach - 224 grams, 1 cup of buttermilk - 120 grams, 1 cup of lowfat/nonfat milk - 245 grams, 4 ounces of ground turkey - 113 grams, 1 slice of turkey breast - 16 grams, 1 cup of ground beef - 113 grams, 1 cup of tomato sauce - 245 grams, 1 cup of kale - 21 grams, 1 cup of whole milk - 244 grams, ONLY LIST THE FINAL NUMBER (in grams) and NOTHING else. An example would be 25.5, 0, or 5. Substitutes are allowed, for example spinach, kale, and lettuce are interchangable. Hamburger buns, hawaiian rolls, etc. count as bread, and steak counts as beef. If the specified ingredient never appears in the recipe ingredient list, it is 0. Only answer with the number of grams, a decimal number if it is between 0 and 1. Do not add any other information but the number of grams. If it says 1 of the item, like 1 tomato, simply attempt to find the amount of grams that the quantity of the items is made up of. It should only be a whole number or a float, like 4.78, 1, and 0. Something like 31232.4107.23 should not ever be outputted."
            }
        ],
        model="llama3-8b-8192",
    )

    tesst = chat_completion.choices[0].message.content.strip()
    return tesst
# features = "180, 17, 221, 18, 12, 750]" #0.57
# features = eval(features)
# features = np.array(features).reshape(1, -1)
# predictions = model.predict(features)
# print("Scale: ", predictions)
# # features = "[158, 34, 37, 9, 3, 111]" #0.44
# # features = eval(features)
# # features = np.array(features).reshape(1, -1)
# # predictions = model.predict(features)
# # print("Scale: ", predictions)
# dun = 0
summed = 1
vala = 0
valb = 0
valc = 0
vald = 0
vale = 0
print(average)
# approv_da = str(approv)
# approvt.append(approv_da)
# approv.clear()
#print(ncheckej)
jcheckej = f"'{jcheckej}'"
#print(f"{jcheckej}, {javerage}")
# for item in jlist:
#     print(item)
# for item in jalist:
#     print(item)
# n_jlist = np.array(jlist).astype(float)
# print("Max: ", np.max(n_jlist, axis = 0))
# print("Mean: ", np.mean(n_jlist, axis = 0))     
# print("Min: ", np.min(n_jlist, axis = 0))          
# #PRAISE THE LORD
# dafa = []
# df = df["fdc_id"]
# print(df)
###
# for i in range(len(df)):
#     daf = df.values[i]
#     daf = int(daf)
#     dafa.append(daf)
#adf = adf.to_string(index=False)
#print(adf)
lowcarb = 0
lowcal = 0
# file_path = r"C:\Users\nickc\Downloads\the_lord_works.csv"
# print(file_path)
# adf.to_csv(path_or_buf=file_path, sep=',', na_rep='', float_format=None, header=True, index=True, index_label=None, mode='w', encoding=None, compression='infer', quoting=None, quotechar='"', lineterminator=None, chunksize=None, date_format=None, doublequote=True, escapechar=None, decimal='.', errors='strict', storage_options=None)
nutrv_a = ""
nutrv_b = ""
nutrv_c = ""
nutrv_d = ""
nutrv_e = ""

converted = False

itemdex = 0
vitscalet = []
vit_lists = [
    vitA_list, vitB1_list, vitB2_list, vitB3_list, vitB5_list, vitB6_list, vitB7_list,
    vitB9_list, vitB12_list, vitC_list, vitD_list, vitE_list, vitK_list, vitCh_list,
    minCa_list, minCl_list, minCr_list, minCu_list, minF_list, minI_list, minFe_list,
    minMg_list, minMn_list, minMo_list, minP_list, minK_list, minSe_list, minNa_list,
    minS_list, minZn_list
]
vals = 0
tesst = ""
for i in range(0):
    vitscale = random.uniform(0, 0.5) #this could increase speeds, AI has to think (11/18)
    vitscale = np.round(vitscale, 3)
    crbcheck = 8
    prtcheck = 0
    fatcheck = 9
    sarcheck = 0.6
    fibcheck = 0.6
    calcheck = 58
    prtcheck = round(prtcheck, 1)
    sarcheck = round(sarcheck, 1)
    fibcheck = round(fibcheck, 1)
    dcheckej = [crbcheck, prtcheck, fatcheck, sarcheck, fibcheck, calcheck, vitscale]
    jcheckej = str(dcheckej)
    crbcheck = (carbcheck(calcheck, crbcheck))
    prtcheck = (protcheck(prtcheck))
    fatcheck = (fatfcheck(calcheck, fatcheck))
    sarcheck = (sgarcheck(sarcheck))
    fibcheck = (fibecheck(fibcheck))
    calcheck = (calocheck(calcheck))
    ncheckej = np.asarray([crbcheck, prtcheck, fatcheck, sarcheck, fibcheck, calcheck, vitscale])
    average = np.average(ncheckej, weights=weightsa)
    javerage = str(average)
    jlist.append(javerage)
    jalist.append(jcheckej)
    #print(approv)
    #print(average)
    approv_da = str(approv)
    approvt.append(approv_da)
    approv.clear()
    #print(ncheckej)
    #print(average)
    jcheckej = f'"{jcheckej}"'
    print(f"{javerage},{jcheckej}")
indexd = 0
for i in range(100):
    vitscale = random.uniform(0, 0.20)
    vitscale = np.round(vitscale, 3)
    crbcheck = random.randint(36, 432)
    prtcheck = random.randint(6, 49)
    fatcheck = random.randint(18, 234)
    sarcheck = random.randint(7, 14)
    fibcheck = random.randint(0, 11)
    calcheck = random.randint(93, 902)
    dcheckej = [crbcheck, prtcheck, fatcheck, sarcheck, fibcheck, calcheck, vitscale]
    jcheckej = str(dcheckej)
    crbcheck = (carbcheck(calcheck, crbcheck))
    prtcheck = (protcheck(prtcheck))
    fatcheck = (fatfcheck(calcheck, fatcheck))
    sarcheck = (sgarcheck(sarcheck))
    fibcheck = (fibecheck(fibcheck))
    calcheck = (calocheck(calcheck))
    ncheckej = np.asarray([crbcheck, prtcheck, fatcheck, sarcheck, fibcheck, calcheck, vitscale])
    average = np.average(ncheckej, weights=weightsa)
    javerage = str(average)
    jlist.append(javerage)
    jalist.append(jcheckej)
    #print(approv)
    #print(average)
    approv_da = str(approv)
    approvt.append(approv_da)
    approv.clear()
    #print(ncheckej)
    #print(average)
    jcheckej = f'"{jcheckej}"'
    print(f"{javerage},{jcheckej}")
for i in range(12):
    vitscale = random.uniform(0, 1)
    vitscale = np.round(vitscale, 3)
    crbcheck = random.randint(36, 432)
    prtcheck = random.randint(6, 49)
    fatcheck = random.randint(18, 234)
    sarcheck = random.randint(7, 14)
    fibcheck = random.randint(0, 11)
    calcheck = random.randint(93, 902)
    dcheckej = [crbcheck, prtcheck, fatcheck, sarcheck, fibcheck, calcheck, vitscale]
    jcheckej = str(dcheckej)
    crbcheck = (carbcheck(calcheck, crbcheck))
    prtcheck = (protcheck(prtcheck))
    fatcheck = (fatfcheck(calcheck, fatcheck))
    sarcheck = (sgarcheck(sarcheck))
    fibcheck = (fibecheck(fibcheck))
    calcheck = (calocheck(calcheck))
    ncheckej = np.asarray([crbcheck, prtcheck, fatcheck, sarcheck, fibcheck, calcheck, vitscale])
    average = np.average(ncheckej, weights=weightsa)
    javerage = str(average)
    jlist.append(javerage)
    jalist.append(jcheckej)
    #print(approv)
    #print(average)
    approv_da = str(approv)
    approvt.append(approv_da)
    approv.clear()
    #print(ncheckej)
    jcheckej = f'"{jcheckej}"'
    print(f"{javerage},{jcheckej}")
n_jlist = np.array(jlist).astype(float)
print("Max: ", np.max(n_jlist, axis = 0))
print("Mean: ", np.mean(n_jlist, axis = 0))     
print("Min: ", np.min(n_jlist, axis = 0)) 
print("St. Deviation: ", np.std(n_jlist, axis = 0)) 
varivitlist = []
dones = [vari1, vari2, vari3, vari4, vari5, vari6, vari7, vari8, vari9, vari10]
grea = ""
grec = []
print(ford)
fodd = 0 
fod = ""
varieties = ["", "", ""]
model_path = r"C:\Users\nickc\Downloads\mymodeljesus777.h5"
if os.path.exists(model_path):
    print("File exists.")
else:
    print("File does not exist.")
model = tf.keras.models.load_model(model_path, compile=False)
@app.route('/', methods=['GET', 'POST'])
def index():            
    global itemdexa, indexs, savior, savory, grea, lowcal, lowcarb, nutrv_a, nutrv_b, nutrv_c, nutrv_d, nutrv_e, converted, vitscalet, vitscale, summ, indexd, itemdex, summed, variranks, varifinal, tesst, varivitlist, odf, vitmin, vit_lists, df, df_merged, varivit, varivit_total, vals, vala, valb, valc, vald, vale, end_time, start_time, grec, ingredlist, inputs, dones, imageg, dun, erit, errors, serrors, ford, fod, ford, content_length, imagef, image_a, image_b, image_c, image_d, image_e, totfar, urlcheck, cutoff, content_length, html_output, selected_variety, skipse, fodd, vari, vari1, vari2, vari3, vari4, vari5, vari6, vari7, vari8, vari9, vari10, varieties, targ, food, irisrec, dundun, nutchk, nfacts, nutrition_values, approv_item, calcheck, crbcheck, prtcheck, sarcheck, fibcheck, inicrbcheck, iniprtcheck, inifatcheck, fatcheck, inisarcheck, inifibcheck, inicalcheck, item_connections, recipefilter, ranked, rankedl, rankedk, item, key, value, ulr2, response, soup, json_ld_tag, json_ld_content, json_data, data, recipe, namef, prep_timef, cook_timef, yield_valuef, nutritionf, ingredientsf, instructions, iterated, main_a, main_b, main_c, main_d, main_e, nutr_a, nutr_b, nutr_c, nutr_d, nutr_e, ingred_a, ingred_b, ingred_c, ingred_d, ingred_e, instruc_a, instruc_b, instruc_c, instruc_d, instruc_e, title_a, title_b, title_c, title_d, title_e, stepno, step
    if request.method == 'POST':
        content_length = request.content_length

        while fodd < 10:  
            flash(f"You have listed {fodd} items. List (another) food item from your pantry!")
            fod = request.form.get('food') 
            selected_variety = request.form.get('varieties')
            carb_value = request.form.get('carb')
            if carb_value:
                lowcarb = 1
            else:
                lowcarb = 0
            calo_value = request.form.get('calo')
            if calo_value:
                lowcal = 1
                print("Calwork")
            else:
                lowcal = 0
            ndf = pd.DataFrame()
            if fodd >= 1 and fodd < 10:
                if "done_early" in request.form:
                    fodd = 10
                    vari10 = ''
            if fodd > 0:
                if "reset" in request.form:
                    lowcarb = 0
                    lowcal = 0
                    fodd = 0
                    vari1 = None
                    vari2 = None
                    vari3 = None
                    vari4 = None
                    vari5 = None
                    vari6 = None
                    vari7 = None
                    vari8 = None
                    vari9 = None
                    vari10 = None
                    flash(f"You have listed {fodd} items. List (another) food item from your pantry!")
                    return render_template('index.html')
            if not fod and fodd != 10:
                ford = random.choice(inputs)
                vari10 = random.choice(varieties)
                flash(f"Last item: {selected_variety}")
                flash(f"Pick {ford}")
                print(inputs)
                if ford in inputs:
                    inputs.remove(ford)
                if not inputs:
                    inputs = ingredlist
                print(ford)
                print(inputs)
                if fodd == 10:
                    print("Yeah")
                elif fodd == 9:
                    vari9 = selected_variety
                elif fodd == 8:
                    vari8 = selected_variety
                elif fodd == 7:
                    vari7 = selected_variety
                elif fodd == 6:
                    vari6 = selected_variety
                elif fodd == 5:
                    vari5 = selected_variety
                elif fodd == 4:
                    vari4 = selected_variety
                elif fodd == 3:
                    vari3 = selected_variety
                elif fodd == 2:
                    vari2 = selected_variety
                elif fodd == 1:
                    vari1 = selected_variety
                    
                return render_template('index.html', fod=fod, fodd=fodd, loading=0)
            if fodd != 10:
                fob.append(fod) 
                found_valid_variety = False 

                for attempt in range(3): 
                    chat_completion = client.chat.completions.create(
                        messages=[
                            {
                                "role": "user",
                                "content": "Here's a broad food ingredient. \n" + fod + "\n If the word is misspelled, fix the spelling and write nothing else. Capitalize the first letter if it isn't already, and simplify the item if possible. As an example, if the response was cow's milk, just write milk. Do not write anything else, including the original input. If it's already spelled correctly, only capitalize the first letter if needed and do nothing else. If the word is perfectly spelled and capitalized, don't change anything else. Keep the word as is. If something like Oranges or Blueberries is not in plural form, change it to be so. However, if something like Onion, Pepper, or Apple is in plural form, change it to its singular form. For example: Peppers becomes Pepper and Nut becomes Nuts. Do the least change possible, and don't change an ingredient to a similar one (e.g. Cheese stays Cheese, not Milk). If the food item doesn't work and it seemed to be formatted correctly, change it from plural to non-plural and vice versa. When you post it, it should look like Blueberries, Onion, or Sauce. It should not look like Tomato -> Tomato, just the word Tomato and nothing else."
                            }
                        ],
                        model="llama3-8b-8192",
                    )

                    goe = chat_completion.choices[0].message.content.strip()
                    print(goe)
                    ndf = df.loc[df['food'] == goe]

                    if not ndf.empty:
                        varieties = ndf['description'].tolist() 
                        ford = random.choice(varieties)
                        if goe in inputs:
                            inputs.remove(goe)
                        if not selected_variety:
                            fodd += 1
                            flash(f"Pick {ford}")
                            flash(f"You picked {goe}. Please select a specific variety from the dropdown.")
                            found_valid_variety = True
                            vari = selected_variety
                            #if fodd == 10:
                                #vari10 = selected_variety
                            if not "done_early" in request.form:
                                vari10 = random.choice(varieties)
                            return render_template('index.html', varieties=varieties, fod=fod, fodd=fodd, selected_variety=selected_variety)
                        attempt = 3

# # #

#######           ##

####### ####### ####### 

#######           ##

# # #
                    if attempt == 2: 
                        flash(f"Pick {ford}")
                        flash("That food item wasn't in the database. Try a different food.")
                        selected_variety = None
                        return render_template('index.html', fodd=fodd, loading=0) 
                        break

                if not found_valid_variety:
                    flash("Please provide a new food item to continue.")
                    return render_template('index.html', fodd=fodd, loading=0)

        #vari10 = selected_variety
        dones = [vari1, vari2, vari3, vari4, vari5, vari6, vari7, vari8, vari9, vari10]
        for x in dones:
            odf = df.query(f"description == '{x}'")
            x.replace("'", "\\'")
            print(odf)
            if not odf.empty:
                varivit_total = [] #takes the vitamin count of each item (100g)
                varivit = odf['fdc_id'].iloc[0]
                varivit = str(varivit)
                print(varivit)
                varivit = vitamincheck(varivit, df_merged, vit_lists, vitmin, varivit_total)
                print(varivit)
                print(f"{x}")
                varivitlist.append(varivit)
                varivit = np.array([])
            else:
                print("Nope!")
                print(f"{x}")
        print(varivitlist)
        loading = 1
        if fodd == 10:
            targ = 1
            start_time = datetime.now()
            try:
                ulr = next(sites_iterator)
                #flash(ulr)
            except StopIteration:
                skipse = 1

            while skipse == 0 and content_length < 4000:
                totfar += content_length
                print(totfar)
                if totfar > cutoff:
                    urlcheck = 1
                    cutoff += 750
                    print(cutoff)
                ulr = ulr  # Ensure 'ulr' contains a valid URL
                print(ulr)
                print(f"Yeah, URL is {ulr}")
                response = requests.get(ulr)

                if response.status_code == 200:
                # Step 2: Parse the HTML using BeautifulSoup
                    soup = BeautifulSoup(response.content, 'html.parser')
                    
                    # Step 3: Find the script tag that contains the JSON-LD data
                    json_ld_tag = soup.find('script', type='application/ld+json')
                    #
                    if json_ld_tag:
                        # Extract the JSON-LD content
                        json_ld_content = json_ld_tag.string
                        
                        # Step 4: Parse the JSON content
                        json_ld_content = json_ld_tag.string.strip()
                        json_data = json.loads(json_ld_content)
                        
                        # Step 5: Now you can work with the extracted JSON data
                        #print(json.dumps(json_data, indent=4))  # Pretty-print the JSON data
                    else:
                        print("No JSON-LD script found on the page.")
                else:
                    print(f"Failed to fetch the webpage. Status code: {response.status_code}")

                            # Define 'url' properly. For example, use 'ulr' if that's the intended variable

                #print(url)
                print(response.headers['Content-Type'])
                #print("Response content:", response.text)
                if response.status_code == 200:
                    try:
                        data = response.json()
                        #print("Parsed JSON data")
                    except requests.exceptions.JSONDecodeError:
                        #print("Failed to parse JSON. Response is not valid JSON.")
                        #print("Response content:", response.text)
                        data = None
                else:
                    print(f"Request failed with status code: {response.status_code}")
                    #print("Response content:", response.text)
                    data = None

                data = json_data

                item_list = []

                if isinstance(json_data, list):
                    for item in json_data:
                        if isinstance(item, dict):  
                            elements = item.get('itemListElement', [])
                            item_list.extend(elements) 
                else:
                    print("json_data is not a list.")
                urls_and_positions = [
                    (item['url'], item['position'])
                    for item in item_list
                    if 'url' in item and 'position' in item
                ]
                filtered_urls = [url for url, position in urls_and_positions]

                try:
                    goo = filtered_urls[targ]
                except IndexError:
                    for item in detect_b:
                        print(item)
                    try:
                        ulr = next(sites_iterator)
                        urlcheck = 1
                    except StopIteration:
                        skipse = 1
                        #break
                    print(ulr)
                    response = requests.get(ulr)
                if urlcheck == 1:
                    try:
                        ulr = next(sites_iterator)
                        urlcheck = 0
                    except StopIteration:
                        skipse = 1
                        break
                if targ > len(item_list):
                    targ = 1
                    if response.status_code == 200:
                    # Step 2: Parse the HTML using BeautifulSoup
                        soup = BeautifulSoup(response.content, 'html.parser')
                        
                        json_ld_tag = soup.find('script', type='application/ld+json')
                        if json_ld_tag:
                            json_ld_content = json_ld_tag.string
                            json_ld_content = json_ld_tag.string.strip()
                            json_data = json.loads(json_ld_content)

                        else:
                            print("No JSON-LD script found on the page.")
                    else:
                        print(f"Failed to fetch the webpage. Status code: {response.status_code}")

                    print(response.headers['Content-Type'])

                    if response.status_code == 200:
                        try:
                            data = response.json()
                        except requests.exceptions.JSONDecodeError:
                            data = None
                    else:
                        print(f"Request failed with status code: {response.status_code}")
                        data = None
                    data = json_data

                    item_list = []

                    if isinstance(json_data, list):
                        for item in json_data:
                            if isinstance(item, dict):  # Check if the item is a dictionary
                                # Safely get 'itemListElement' from the dictionary
                                elements = item.get('itemListElement', [])
                                # Extend item_list with elements found
                                item_list.extend(elements)  # Add all elements to item_list
                                #print(item_list)
                    else:
                        print("json_data is not a list.")

                    urls_and_positions = [
                        (item['url'], item['position'])
                        for item in item_list
                        if 'url' in item and 'position' in item
                    ]
                    target_positions = [targ]
                    filtered_urls = [url for url, position in urls_and_positions]
                    print(filtered_urls)

                try:
                    goo = filtered_urls[targ]
                except IndexError:
                    for item in detect_b:
                        print(item)
                        urlcheck = 1
                    #break
                    # Now pass the string to requests.get()
                response = requests.get(goo)
    #                 if data:
    #                 # Proceed with processing 'data'
    #                     for item in data.get('ListItem', []):
    #                         name = item.get('name')
    #                         url = item.get('url')
    #                         position = item.get('position')
    #                         print(f"Recipe {position}: {name}, URL: {url}")
    #                 else:
    #                     print("No data to process.")
    # #
    #             # Parse JSON string into a Python dictionary
    #             data = json_data

                data = json_data

                urls_and_positions = [
                    (item['url'], item['position'])
                    for item in item_list
                    if 'url' in item and 'position' in item
                ]

                target_positions = [targ] 

                # Step 3: Filter URLs based on the target positions
                filtered_urls = [
                    url
                    for url, position in urls_and_positions
                    if position in target_positions
                ]

                # Display the filtered URLs
                #print(filtered_urls)

                # Now pass the string to requests.get()
                response = requests.get(goo)

                # Print the status code to verify the request works
                #print(response.status_code)  

                # filtered_urls = str(filtered_urls)
                # goo = filtered_urls ?

                # Extract the first URL (since it's a list with one string element)
                # r = requests.get(goo) ?

                soup = BeautifulSoup(response.content, 'html.parser')

                if response.status_code == 200:

                    soup = BeautifulSoup(response.content, 'html.parser')
                    
                    json_ld_tag = soup.find('script', type='application/ld+json')                
                    if json_ld_tag:
                        json_ld_content = json_ld_tag.string
                        json_data = json.loads(json_ld_content)
                    else:
                        print("No JSON-LD script found on the page.")
                else:
                    print(f"Failed to fetch the webpage. Status code: {response.status_code}")
                if isinstance(json_data, list) and len(json_data) > 0:
                    ingredients = json_data[0].get('recipeIngredient', [])
                else:
                    ingredients = []  

                # Now you can work with ingredients safely
                # print(ingredients)
                # try:
                #     ingredients = json_data['recipeIngredient']
                # except KeyError:
                #     print("We couldn't find ingredients for one of them...lol")
    #           
                # Display the list of ingredients
                # for ingredient in ingredients: - thaw
                #     print(ingredient)
                doneso = str(dones)
                reciso = str(ingredients)
                detect_a = f"Ingredients: {doneso} Recipe: {reciso}"
                #variranks = np.array(variranks)
                #flash(detect_a)
                detect_b.append(detect_a)
                targ = targ + 1
                # chat_completion = client.chat.completions.create(
                #     messages=[
                #         {
                #             "role": "user",
                #             "content": "Here's a list of ingredients. This is from a recipe. \n" + reciso + "\n Now, here's a list of ingredients someone has: \n" + doneso + "\n Using these two lists, will someone be able to make the recipe using the items listed? If no, just say No. If yes, just say Yes. Name the ingredients that are and are not shared. If not all necessary ingredients are shared, it is no. Assume the viewer already has salt and pepper.",
                #         }
                #     ],
                #     model="llama3-8b-8192",
                #     )
                #model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
                ingreci = {'connection': [detect_a]}
                aidf = pd.DataFrame(ingreci)
                #aidf['yesorno'] = aidf['yesorno'].astype(int

                features = aidf.iloc[:, 0]
                # print("Features: ")
                # print(features)
                #labels = aidf['yesorno']
                # print("Labels: ")
                # print(labels)

                #print(df)
                # Process the lines into a TensorFlow Dataset
                data = [line.strip() for line in aidf]
                dataset = tf.data.Dataset.from_tensor_slices(data)

                features_vectorized = vectorize_layer(features.values)

                predictions = model.predict(features_vectorized)
                raw_pred = (predictions > 0.5).astype("int32")
                #raw_pred = raw_pred.astype(int)
                #predictions = np.round(predictions)
                #predictions = predictions.astype(int)
                print(f"Prediction: {raw_pred}")
                print(f"Raw Prediction: {predictions}")
                content_length = request.content_length
                print(f"Request Content-Length: {content_length} bytes")
    
                target_positions = [targ] 

                # Step 3: Filter  URLs based on the target positions
                filtered_urls = [
                    url
                    for url, position in urls_and_positions
                    if position in target_positions
                ]

                if raw_pred == 1:
                    print(detect_a)
                    grec.append(detect_a)
                    print(filtered_urls)
                    irisrec.append(filtered_urls)
                    for vari in dones:
                        if vari != '' and vari != None:
                            while not converted:
                                try:
                                    print("Yeah")
                                    print(reciso)
                                    tesst = recipecheck(vari, reciso)
                                    tesst = float(tesst)
                                    print(tesst)
                                    converted = True
                                except ValueError: 
                                    print("Not again...")
                        savory.append(tesst)
                    savior.append(savory)
                    savory = []
                    print(savior)
        #print(doneso)
        #print(reciso)
        # yes_no = (chat_completion.choices[0].message.content)
        # if "1" in predictions:
        #     print("YES")
#
        # if "0" in predictions:
        #     print("NO")
        # print("Uncertainty: ")
        #randostat = predictions - raw_pred
        #randostat = np.abs(randostat)
        #print(randostat)

    #inputs = ingredlist
    #print(irisrec)
        for item in detect_b:
            print(item)
        for gre in grec:
            print(gre)
        dundun = len(irisrec)
        itemdexa = []
        indexs = 0
        for item in irisrec:
            indexd = 0
            # for vari in dones:
            #     if vari != '' and vari != None:
            #         itemdexa = savior[indexs]
            #         print(itemdexa)
            #         tesst = itemdexa[indexd]
            #         # print("yeah")
            #         # print(vari)
            #         # #tesst = re.sub("[^0-9.]", "", tesst)
            #         # #print(f"{vari} Amount (g) in {reciso}: ")
            #         # #print(tesst)
            #         # grea = savior[indexd]
            #         # print(grea)
            #         # try:
            #         #     tesst = recipecheck(vari, grea)
            #         #     print(tesst)
            #         #     tesst = float(tesst)
            #         #     converted = True
            #         # except ValueError: 
            #         #     print("Not again...")
            #         #     tesst = 0
            #         #     # tesst = recipecheck(vari, reciso)
            #         #     # tesst = re.sub("[^0-9.]", "", tesst)
            #         print(f"{vari} Amount (g): ")
            #         indexs += 1
            #         indexd += 1
            #         print(tesst)
            #         variranks.append(tesst)
            # print(variranks)
            # varifinal.append(variranks)
            #variranks = np.array([])
            #print(varifinal)
            vitscalet = []
            vitscale = [] #reset so it can append properly
            nutchk = str(item)
            nutchk = re.sub(r'[\[\]\']', '', nutchk)
            response = requests.get(nutchk)
            # indexd = 0
            # itemdex = 0
            # summed = 0
            # for vari in dones: #takes the amount of the ingredient
            #     if vari != '' and vari != None:
            #         print(f"Recipe Amount of {vari}: ")
            #         try:
            #             print(varifinal[indexd][itemdex])
            #             summed = varifinal[indexd][itemdex]
            #             #print(summed)
            #             #summed = (np.sum([arr[indexd] for arr in varifinal]))
            #             indexd += 1 #must be put before np.sum because otherwise starts one index too far
            #         except IndexError:
            #             print("Done! Ye")
            #     itemdex += 1
            #     for varivit in varivitlist: #varivit is a numpy array
            #         vitscale = []
            #         try:
            #             varivit = np.array(varivit, dtype=float)
            #         except ValueError as e:
            #             print("Error: Could not convert all elements to float:", e)
            #             varifinal = []
            #             #print(vita)
            #         for ite, vita in zip(varivit, vitmin): #realized (11/17)
            #             vitscale = []
            #             ite = float(ite)
            #             #print(f"Recipe Amount of {vari}: ")
            #             try:
            #                 #print(f"item: {ite}, summed: {summed}")
            #                 summed = summed/100
            #                 summ = ite * summed
            #                 #print(vita)
            #                 #print(vitmin)
            #                 summ = summ/vita
            #                 if summ >= 1:
            #                     summ = 1
            #                 #print(summ)
            #                 vitscale.append(summ)
            #             except IndexError:
            #                 print("Done!")
            #             vitscale = np.array(vitscale)
            #             vitscalet.append(vitscale)
            # #print(vitscalet)
            # vitscale = np.sum(vitscalet, axis=0)
            # #print(vitscale)
            # vitscale = np.average(vitscale)
            vitscale = random.uniform(0, 0.5) #this could increase speeds, AI has to think (11/18)
            vitscale = np.round(vitscale, 3)
            print(f"Vitamin Scale: {vitscale}")
#intendation is key!!!
            soup = BeautifulSoup(response.content, 'html.parser')
            #print(soup.prettify())
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                
                json_ld_tag = soup.find('script', type='application/ld+json')
                
                if json_ld_tag:
                    json_ld_content = json_ld_tag.string
                    json_data = json.loads(json_ld_content)
                    
                else:
                    print("No JSON-LD script found on the page.")
            else:
                print(f"Failed to fetch the webpage. Status code: {response.status_code}")
            if isinstance(json_data, list) and len(json_data) > 0:
                nfacts = json_data[0].get('nutrition', [])
            else:
                nfacts = [] 
            #print(nfacts)
            #print("Nutrition Facts:  ")
            #for item in nfacts:
                #print(item)
            try:
                nutrition_values = {key: value for key, value in nfacts.items() if key != '@type'}
            except AttributeError:
                print("Uh oh!")
                print(item)
                irisrec.remove(item)
            if nutrition_values is None:
                irisrec.remove(item)
            if nutrition_values is not None:
                for nutrient, value in nutrition_values.items():
                    approv_item = (f"{nutrient}: {value}")
                    approv.append(approv_item)
                    if nutrient == "calories":
                        calcheck = re.sub("[^0-9]","",value)
                        calcheck = int(calcheck)
                        #print(calcheck)
                    if nutrient == "carbohydrateContent":
                        crbcheck = re.sub("[^0-9]","",value)
                        crbcheck = int(crbcheck)
                        crbcheck = crbcheck * 4
                        #print(crbcheck)
                    if nutrient == "proteinContent":
                        prtcheck = re.sub("[^0-9]","",value)
                        prtcheck = int(prtcheck)
                        #prtcheck = prtcheck * 4
                        #print(prtcheck)
                    if nutrient == "saturatedFatContent":
                        fatcheck = re.sub("[^0-9]","",value)
                        fatcheck = int(fatcheck)
                        fatcheck = fatcheck * 9
                        #print(fatcheck)
                    if nutrient == "fiberContent":
                        fibcheck = re.sub("[^0-9]","",value)
                        fibcheck = int(fibcheck)
                        #print(fibcheck)
                    if nutrient == "sugarContent":
                        sarcheck = re.sub("[^0-9]","",value)
                        sarcheck = int(sarcheck)
                vitscale = np.round(vitscale, 3)
                inicrbcheck = crbcheck
                iniprtcheck = prtcheck
                inifatcheck = fatcheck
                inisarcheck = sarcheck
                inifibcheck = fibcheck
                inicalcheck = calcheck
                dcheckej = [crbcheck, prtcheck, fatcheck, sarcheck, fibcheck, calcheck, vitscale]
                jcheckej = str(dcheckej)
                crbcheck = (carbcheck(calcheck, crbcheck))
                prtcheck = (protcheck(prtcheck))
                fatcheck = (fatfcheck(calcheck, fatcheck))
                sarcheck = (sgarcheck(sarcheck))
                fibcheck = (fibecheck(fibcheck))
                calcheck = (calocheck(calcheck))
                ncheckej = np.asarray([crbcheck, prtcheck, fatcheck, sarcheck, fibcheck, calcheck, vitscale])
                average = np.average(ncheckej, weights=weightsa)
                javerage = str(average)
                #print(approv)
                #print(average)
                approv_da = str(approv)
                approvt.append(approv_da)
                approv.clear()
                #print(ncheckej)
                #print(average)
                print(f"{jcheckej}, {javerage}")
                features = jcheckej 
                features = eval(features)
                features = np.array(features).reshape(1, -1)
                predictions = model2.predict(features)
                print(predictions)
                recipefilter.append(predictions)
                erit = average - predictions
                errors.append(erit)
                if lowcarb == 1:
                    if crbcheck > 0.3:
                        recipefilter.remove(predictions)
                        irisrec.remove(item)
                        print("BEGONE!")
                if lowcal == 1:
                    if inicalcheck > 420:
                        recipefilter.remove(predictions)
                        irisrec.remove(item)
                        print("BEGONE!")
        errors = np.asarray(errors)
        serrors = np.abs(errors)
        if serrors.size > 0:  # Ensure serrors is not empty
            serrors = np.nanmean(serrors)  # Ignore NaN values
            print(serrors)
        else:
            flash("Sorry, no recipes were found.")
            return render_template("index.html")
        if any(isinstance(item, list) for item in irisrec):
            irisrec = [tuple(item) for item in irisrec]
        #print(irisrec)
        item_connections = dict(zip(irisrec, recipefilter))
        #print(item_connections)
        recipefilter = np.asarray(recipefilter, dtype=float)
        recipefilter = recipefilter.flatten()
        recipefilter = np.sort(recipefilter)[::-1]
        ranked = recipefilter[:5]
        print(ranked)
        rankedl = list(ranked)
        print(rankedl)
        for item in ranked:
            for key, value in item_connections.items():
                if value == item:
                    print(key)
                    rankedk.append(key)

        for item in rankedk:
            ulr2 = item[0] 
            ulr2 = ulr2 # Ensure 'ulr' contains a valid URL
            print(ulr2)
            response = requests.get(ulr2)
#
            if response.status_code == 200:
            # Step 2: Parse the HTML using BeautifulSoup
                soup = BeautifulSoup(response.content, 'html.parser')
                
                # Step 3: Find the script tag that contains the JSON-LD data
                json_ld_tag = soup.find('script', type='application/ld+json')
                #
                if json_ld_tag:
                    # Extract the JSON-LD content
                    json_ld_content = json_ld_tag.string
                    
                    # Step 4: Parse the JSON content
                    json_ld_content = json_ld_tag.string.strip()
                    json_data = json.loads(json_ld_content)
                    
                    # Step 5: Now you can work with the extracted JSON data
                    #print(json.dumps(json_data, indent=4))  # Pretty-print the JSON data
                else:
                    print("No JSON-LD script found on the page.")
            else:
                print(f"Failed to fetch the webpage. Status code: {response.status_code}")

                        # Define 'url' properly. For example, use 'ulr' if that's the intended variable

            #print(url)
            print(response.headers['Content-Type'])
            #print("Response content:", response.text)
            if response.status_code == 200:
                try:
                    data = response.json()
                    #print("Parsed JSON data")
                except requests.exceptions.JSONDecodeError:
                    #print("Failed to parse JSON. Response is not valid JSON.")
                    #print("Response content:", response.text)
                    data = None
            else:
                print(f"Request failed with status code: {response.status_code}")
                #print("Response content:", response.text)
                data = None
            data = json_data
            for recipe in data:
                print(iterated)
                namef = recipe.get("name")
                imagef = recipe.get("image")
                imagef = imagef.get("url")
                prep_timef = recipe.get("prepTime")
                cook_timef = recipe.get("cookTime")
                yield_valuef = recipe.get("recipeYield")
                nutritionf = recipe.get("nutrition")
                ingredientsf = recipe.get("recipeIngredient")
                instructions = [step.get("text") for step in recipe.get("recipeInstructions", [])]     
                cook_timef = str(cook_timef)   
                prep_timef = str(prep_timef)   
                yield_valuef = str(yield_valuef)       
                cook_timef = re.sub("[^0-9]","",cook_timef)    
                prep_timef = re.sub("[^0-9]","",prep_timef)   
                yield_valuef = re.sub("[^0-9]","",yield_valuef)   
                print(f"Recipe: {namef}")
                print("")
                print(f"Prep Time: {prep_timef} minutes")
                print(f"Cook Time: {cook_timef} minutes")
                print(f"Yield: {yield_valuef} servings")
                if iterated == 0:
                    main_a += f"Prep Time: {prep_timef} minutes <br>"
                    main_a += f"Cook Time: {cook_timef} minutes <br>"
                    main_a += f"Yield: {yield_valuef} servings <br>"
                if iterated == 1:
                    main_b += f"Prep Time: {prep_timef} minutes <br>"
                    main_b += f"Cook Time: {cook_timef} minutes <br>"
                    main_b += f"Yield: {yield_valuef} servings <br>"
                if iterated == 2:
                    main_c += f"Prep Time: {prep_timef} minutes <br>"
                    main_c += f"Cook Time: {cook_timef} minutes <br>"
                    main_c += f"Yield: {yield_valuef} servings <br>"
                if iterated == 3:
                    main_d += f"Prep Time: {prep_timef} minutes <br>"
                    main_d += f"Cook Time: {cook_timef} minutes <br>"
                    main_d += f"Yield: {yield_valuef} servings <br>"
                if iterated == 4:
                    main_e += f"Prep Time: {prep_timef} minutes <br>"
                    main_e += f"Cook Time: {cook_timef} minutes <br>"
                    main_e += f"Yield: {yield_valuef} servings <br>"
                print("")
                print("Nutrition Facts:")
                for key, value in nutritionf.items():
                    print(f"  {key}: {value}")
                    if key != "@type":
                        if iterated == 0:
                            nutr_a += f"""
                            <tr>
                                <td>{key}</td>
                                <td>{value}</td>
                            </tr>
                            """
                        if iterated == 1:
                            nutr_b += f"""
                            <tr>
                                <td>{key}</td>
                                <td>{value}</td>
                            </tr>
                            """
                        if iterated == 2:
                            nutr_c += f"""
                            <tr>
                                <td>{key}</td>
                                <td>{value}</td>
                            </tr>
                            """
                        if iterated == 3:
                            nutr_d += f"""
                            <tr>
                                <td>{key}</td>
                                <td>{value}</td>
                            </tr>
                            """
                        if iterated == 4:
                            nutr_e += f"""
                            <tr>
                                <td>{key}</td>
                                <td>{value}</td>
                            </tr>
                            """
                print("Ingredients:")
                for ingredientf in ingredientsf:
                    print(f"  - {ingredientf}")
                    if iterated == 0:
                        ingred_a += f" - {ingredientf} <br>"
                    if iterated == 1:
                        ingred_b += f" - {ingredientf} <br>"
                    if iterated == 2:
                        ingred_c += f" - {ingredientf} <br>"
                    if iterated == 3:
                        ingred_d += f" - {ingredientf} <br>"
                    if iterated == 4:
                        ingred_e += f" - {ingredientf} <br>"
                print("Instructions:")
                for stepno, step in enumerate(instructions, start=1):
                    print("")
                    print(f"  {stepno}. {step}")
                    if iterated == 0:
                        instruc_a += f"{stepno}. {step} <br>"
                    if iterated == 1:
                        instruc_b += f"{stepno}. {step} <br>"
                    if iterated == 2:
                        instruc_c += f"{stepno}. {step} <br>"
                    if iterated == 3:
                        instruc_d += f"{stepno}. {step} <br>"
                    if iterated == 4:
                        instruc_e += f"{stepno}. {step} <br>"
                if iterated == 0:
                    title_a = str(namef)
                    image_a = str(imagef)
                if iterated == 1:
                    title_b = str(namef)
                    image_b = str(imagef)
                if iterated == 2:
                    title_c = str(namef)
                    image_c = str(imagef)
                if iterated == 3:
                    title_d = str(namef)
                    image_d = str(imagef)
                if iterated == 4:
                    title_e = str(namef)
                    image_e = str(imagef)
                    iterated = 0
                    break
                iterated += 1  
        iterated = 0
        for item in rankedl:
            item = float(item)
            item = np.round(item, decimals=3)
            vals = item * 10
            vals = np.round(vals)
            if vals == 0:
                vals = 1
            vals = int(vals)
            vals = str(vals)
            vals = f'class{vals}'
            if iterated == 0:
                vala = item
                vala = f"<h2 class='{vals}'>Nutrition Rating: {vala}</h2>"
            if iterated == 1:
                valb = item
                valb = f"<h2 class='{vals}'>Nutrition Rating: {valb}</h2>"
            if iterated == 2:
                valc = item
                valc = f"<h2 class='{vals}'>Nutrition Rating: {valc}</h2>"
            if iterated == 3:
                vald = item
                vald = f"<h2 class='{vals}'>Nutrition Rating: {vald}</h2>"
            if iterated == 4:
                vale = item
                vale = f"<h2 class='{vals}'>Nutrition Rating: {vale}</h2>"
            iterated += 1
        if rankedk != []:
            html_output = f"""
                <!DOCTYPE html>
                <html>
                <head>
                    <meta charset="utf-8" />
                    <meta name="viewport" content="width=device-width" />
                    <link rel="preconnect" href="https://fonts.googleapis.com" />
                    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
                    <link href="https://fonts.googleapis.com/css2?family=Lexend:wght@400&family=Lobster&display=swap" rel="stylesheet" />
                    <link href="https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,100;0,300;0,400;0,500;0,700;0,900;1,100;1,300;1,400;1,500;1,700;1,900&display=swap" rel="stylesheet">
                    <title>Top 5 Recipe Choices</title>
                    <link rel="stylesheet" href="/static/style.css" />
                </head>
                <body>
                    <h1>1. {title_a}</h1>
                    {vala}
                    <img src={image_a} alt="Image" />
                    <h2>{main_a}</h2>
                    <h2>Nutritional Facts:</h2>
                    <table style="width:100%">
                        <tr>
                            <th>Macronutrient</th>
                            <th>Amount (per yield)</th>
                        </tr>
                        {nutr_a}
                    </table>
                    <h2>Ingredients:</h2>
                    <h3>{ingred_a}</h3>
                    <h2>Instructions:</h2>
                    <h3>{instruc_a}</h2>
                    <hr class="solid">
                    <h1>2. {title_b}</h1>
                    {valb}
                    <img src={image_b} alt="Image" />
                    <h2>{main_b}</h2>
                    <h2>Nutritional Facts:</h2>
                    <table style="width:100%">
                        <tr>
                            <th>Macronutrient</th>
                            <th>Amount (per yield)</th>
                        </tr>
                        {nutr_b}
                    </table>
                    <h2>Ingredients:</h2>
                    <h3>{ingred_b}</h3>
                    <h2>Instructions:</h2>
                    <h3>{instruc_b}</h2>
                    <hr class="solid">
                    <h1>3. {title_c}</h1>
                    {valc}
                    <img src={image_c} alt="Image" />
                    <h2>{main_c}</h2>
                    <h2>Nutritional Facts:</h2>
                    <table style="width:100%">
                        <tr>
                            <th>Macronutrient</th>
                            <th>Amount (per yield)</th>
                        </tr>
                        {nutr_c}
                    </table>
                    <h2>Ingredients:</h2>
                    <h3>{ingred_c}</h3>
                    <h2>Instructions:</h2>
                    <h3>{instruc_c}</h2>
                    <hr class="solid">
                    <h1>4. {title_d}</h1>
                    {vald}
                    <img src={image_d} alt="Image" />
                    <h2>{main_d}</h2>
                    <h2>Nutritional Facts:</h2>
                    <table style="width:100%">
                        <tr>
                            <th>Macronutrient</th>
                            <th>Amount (per yield)</th>
                        </tr>
                        {nutr_d}
                    </table>
                    <h2>Ingredients:</h2>
                    <h3>{ingred_d}</h3>
                    <h2>Instructions:</h2>
                    <h3>{instruc_d}</h2>
                    <hr class="solid">
                    <h1>5. {title_e}</h1>
                    {vale}
                    <img src={image_e} alt="Image" />
                    <h2>{main_e}</h2>
                    <h2>Nutritional Facts:</h2> 
                    <table style="width:100%">
                        <tr>
                            <th>Macronutrient</th>
                            <th>Amount (per yield)</th>
                        </tr>
                        {nutr_e}
                    </table>
                    <h2>Ingredients:</h2>
                    <h3>{ingred_e}</h3>
                    <h2>Instructions:</h2>
                    <h3>{instruc_e}</h2>
                </body>
                </html>
            """
        else:
            html_output = f"""
                <!DOCTYPE html>
                <html>
                <head>
                    <meta charset="utf-8" />
                    <meta name="viewport" content="width=device-width" />
                    <link rel="preconnect" href="https://fonts.googleapis.com" />
                    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
                    <link href="https://fonts.googleapis.com/css2?family=Lexend:wght@400&family=Lobster&display=swap" rel="stylesheet" />
                    <title>Top 5 Recipe Choices</title>
                    <link rel="stylesheet" href="/static/style.css" />
                </head>
                <body>
                    <h1>Sorry, no recipes were found!</h1>
                </body>
                </html>
            """    
        print(html_output)
        for item in detect_b:
            print(item)
        with open("templates/output.html", "w") as file:
            file.write(html_output)
        urlcheck = None
        cutoff = None
        selected_variety = None
        skipse = None
        fodd = 0
        vari = None
        vari1 = None
        vari2 = None
        vari3 = None
        vari4 = None
        vari5 = None
        vari6 = None
        vari7 = None
        vari8 = None
        vari9 = None
        vari10 = None
        varieties = None
        targ = None
        food = None
        irisrec = None
        dundun = None
        nutchk = None
        nfacts = None
        nutrition_values = None
        approv_item = None
        calcheck = None
        crbcheck = None
        prtcheck = None
        sarcheck = None
        inicrbcheck = None
        iniprtcheck = None
        inifatcheck = None
        fatcheck = None
        inisarcheck = None
        inifibcheck = None
        inicalcheck = None
        item_connections = None
        recipefilter = None
        ranked = None
        rankedl = None
        rankedk = None
        item = None
        key = None
        value = None
        ulr2 = None
        response = None
        soup = None
        json_ld_tag = None
        json_ld_content = None
        json_data = None
        data = None
        recipe = None
        iterated = None
        end_time = datetime.now()
        start_time = datetime.strftime(start_time, "%H:%M:%S:%f")
        end_time = datetime.strftime(end_time, "%H:%M:%S:%f")
        start_time = str(start_time)
        end_time = str(end_time)

        t1 = datetime.strptime(start_time, "%H:%M:%S:%f")
        #print('Start time:', t1.time())

        t2 = datetime.strptime(end_time, "%H:%M:%S:%f")
        #print('End time:', t2.time())

        # get difference
        delta = t2 - t1

        # time difference in seconds
        print(f"Time taken: {delta.total_seconds()} seconds")
        # Redirect to the output route
        return redirect(url_for("output")) 
        print(url_for("output"))

    return render_template("index.html", loading=0)  # For GET requests

@app.route("/output")
def output():
    global selected_variety, skipse, fodd, vari, vari1, vari2, vari3, vari4, vari5, vari6, vari7, vari8, vari9, vari10, varieties, targ, food, irisrec, dundun, nutchk, nfacts, nutrition_values, approv_item, calcheck, crbcheck, prtcheck, sarcheck, inicrbcheck, iniprtcheck, inifatcheck, fatcheck, inisarcheck, inifibcheck, inicalcheck, item_connections, recipefilter, ranked, rankedl, rankedk, item, key, value, ulr2, response, soup, json_ld_tag, json_ld_content, json_data, data, recipe, namef, prep_timef, cook_timef, yield_valuef, nutritionf, ingredientsf, instructions, iterated, main_a, main_b, main_c, main_d, main_e, nutr_a, nutr_b, nutr_c, nutr_d, nutr_e, ingred_a, ingred_b, ingred_c, ingred_d, ingred_e, instruc_a, instruc_b, instruc_c, instruc_d, instruc_e, title_a, title_b, title_c, title_d, title_e, stepno, step
    return render_template("output.html")

@app.route('/acknowledgements')
def acknowledgements():
    return render_template('acknowledgements.html')
    
if __name__ == '__main__':
    app.run(port=5000, debug=True)