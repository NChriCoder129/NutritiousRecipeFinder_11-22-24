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

vectorize_layer = tf.keras.layers.TextVectorization(max_tokens=1000, output_mode='int')

vectorize_layer.adapt(features.values) 

features_vectorized = vectorize_layer(features.values)

#Ingredients: 
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
# Ingredients: 
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
#import the lord's will
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
ingredlist = [ingredlista, ingredlistb, ingredlistc]
inputs = ingredlistc
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
vitA = 0.3
vitB1 = 0.4
vitB2 = 0.433
vitB3 = 5.333
vitB5 = 1.667
vitB6 = 0.433
vitB7 = 10
vitB9 = 1.333
vitB12 = 0.8
vitC = 30
vitD = 0.005
vitE = 5
vitK = 40
vitCh = 183.333
minCa = 333.333
minCl = 766.667
minCr = 11.667
minCu = 3
minF = 1.333
minI = 0.05
minFe = 2.667
minMg = 140
minMn = 0.767
minMo = 0.015
minP = 233.333
minK = 1566.667                                               
minSe = 0.018
minNa = 766.667
minS = 283.333
minZn = 3.667
varieties = []
vitA_list = [
    "Vitamin A"
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
checkej = [crbcheck, prtcheck, fatcheck, sarcheck, fibcheck, calcheck]
dcheckej = [crbcheck, prtcheck, fatcheck, sarcheck, fibcheck, calcheck]
ncheckej = np.asarray([crbcheck, prtcheck, fatcheck, sarcheck, fibcheck, calcheck])
errors = []
weightsa = np.array([0.2, 0.15, 0.15, 0.1, 0.1, 0.1])
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
model2_path = r"C:\Users\nickc\Downloads\my_modelB1.h5"
if os.path.exists(model2_path):
    print("File exists.")
else:
    print("File does not exist.")
model2 = tf.keras.models.load_model(model2_path, compile=False)
#model2.compile(optimizer='adam', loss='mean_absolute_error', metrics=tf.keras.metrics.MeanAbsoluteError())
df = df.drop(columns=["data_type", "food_category_id", "publication_date"])
weights = np.array([0.2, 0.15, 0.15, 0.1, 0.1, 0.1])
def carbcheck(calcheck, crbcheck):
    # Scale based on the percentage
    parame = crbcheck/calcheck
    if parame >= 0.7:  # This represents 50% in your original scale
        return 0
    elif parame == 0:  # This represents 70% in your original scale
        return 0
    elif parame == 0.5:  # This represents 70% in your original scale
        return 1
    crbcheck = parame # Mapping from 0.5 to 0
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

# model = tf.keras.Sequential([
#     tf.keras.layers.Input(shape=(None,), dtype='int32'),  # Input layer for the vectorized text
#     tf.keras.layers.Embedding(input_dim=1000, output_dim=64),  # Embedding layer
#     tf.keras.layers.GlobalAveragePooling1D(),  # Pooling layer
#     tf.keras.layers.Dense(32, activation='relu'),  # Dense hidden layer
#     tf.keras.layers.Dense(1, activation='sigmoid')  # Output layer for binary classification
# ])

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
# imageg = ""
# crbcheck = 180
# prtcheck = 10
# fatcheck = 63
# sarcheck = 8
# fibcheck = 10
# calcheck = 457
# dcheckej = [crbcheck, prtcheck, fatcheck, sarcheck, fibcheck, calcheck]
# jcheckej = str(dcheckej)
# crbcheck = (carbcheck(calcheck, crbcheck))
# prtcheck = (protcheck(prtcheck))
# fatcheck = (fatfcheck(calcheck, fatcheck))
# sarcheck = (sgarcheck(sarcheck))
# fibcheck = (fibecheck(fibcheck))
# calcheck = (calocheck(calcheck))
# ncheckej = np.asarray([crbcheck, prtcheck, fatcheck, sarcheck, fibcheck, calcheck])
# average = np.average(ncheckej, weights=weightsa)
# javerage = str(average)
# jlist.append(javerage)
# jalist.append(jcheckej)
# #print(approv)
print(average)
# approv_da = str(approv)
# approvt.append(approv_da)
# approv.clear()
#print(ncheckej)
#print(average)
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

# adf = pd.read_csv("soup3.txt", low_memory=False)
# adf = adf[adf["fdc_id"].isin(dafa)]
# #adf = adf.to_string(index=False)
# #print(adf)

# file_path = r"C:\Users\nickc\Downloads\the_lord_works.csv"
# print(file_path)
# adf.to_csv(path_or_buf=file_path, sep=',', na_rep='', float_format=None, header=True, index=True, index_label=None, mode='w', encoding=None, compression='infer', quoting=None, quotechar='"', lineterminator=None, chunksize=None, date_format=None, doublequote=True, escapechar=None, decimal='.', errors='strict', storage_options=None)

# # Check if the file exists
# if os.path.exists(file_path):
#     print(f"File saved successfully at: {file_path}")
# else:
#     print("File not found.")

# # #used to help make data more efficient (9/27/2024)/ update database (10/2/2024)
#removed fodd += 1 (when on 5th item)
#
# @app.before_request
# def reset_variables():
#     global vari1, var2, vari3, vari4, vari5, vari6, vari7, vari8, vari9, vari10, food, selected_variety
#     if request.method == 'GET':
#         vari1 = vari2 = vari3 = vari4 = vari5 = vari6 = vari7 = vari8 = vari9 = vari10 = ""
#         fodd = 0
#         selected_variety = None
#         varities = None

for i in range(1):
    crbcheck = randint(35, 350)
    prtcheck = randint(7, 14)
    fatcheck = randint(14, 42)
    sarcheck = randint(7, 14)
    fibcheck = randint(0, 7)
    calcheck = randint(280, 560)
    dcheckej = [crbcheck, prtcheck, fatcheck, sarcheck, fibcheck, calcheck]
    jcheckej = str(dcheckej)
    crbcheck = (carbcheck(calcheck, crbcheck))
    prtcheck = (protcheck(prtcheck))
    fatcheck = (fatfcheck(calcheck, fatcheck))
    sarcheck = (sgarcheck(sarcheck))
    fibcheck = (fibecheck(fibcheck))
    calcheck = (calocheck(calcheck))
    ncheckej = np.asarray([crbcheck, prtcheck, fatcheck, sarcheck, fibcheck, calcheck])
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

n_jlist = np.array(jlist).astype(float)
print("Max: ", np.max(n_jlist, axis = 0))
print("Mean: ", np.mean(n_jlist, axis = 0))     
print("Min: ", np.min(n_jlist, axis = 0)) 
print("St. Deviation: ", np.std(n_jlist, axis = 0)) 

dones = [vari1, vari2, vari3, vari4, vari5, vari6, vari7, vari8, vari9, vari10]
grec = []
print(ford)
fodd = 0 
fod = ""
varieties = ["", "", ""]
@app.route('/', methods=['GET', 'POST'])
def index():            
    global end_time, start_time, grec, ingredlist, inputs, dones, imageg, dun, erit, errors, serrors, ford, fod, ford, content_length, imagef, image_a, image_b, image_c, image_d, image_e, totfar, urlcheck, cutoff, content_length, html_output, selected_variety, skipse, fodd, vari, vari1, vari2, vari3, vari4, vari5, vari6, vari7, vari8, vari9, vari10, varieties, targ, food, irisrec, dundun, nutchk, nfacts, nutrition_values, approv_item, calcheck, crbcheck, prtcheck, sarcheck, fibcheck, inicrbcheck, iniprtcheck, inifatcheck, fatcheck, inisarcheck, inifibcheck, inicalcheck, item_connections, recipefilter, ranked, rankedl, rankedk, item, key, value, ulr2, response, soup, json_ld_tag, json_ld_content, json_data, data, recipe, namef, prep_timef, cook_timef, yield_valuef, nutritionf, ingredientsf, instructions, iterated, main_a, main_b, main_c, main_d, main_e, nutr_a, nutr_b, nutr_c, nutr_d, nutr_e, ingred_a, ingred_b, ingred_c, ingred_d, ingred_e, instruc_a, instruc_b, instruc_c, instruc_d, instruc_e, title_a, title_b, title_c, title_d, title_e, stepno, step
    if request.method == 'POST':
        content_length = request.content_length

        while fodd < 10:  # Ensure it runs correctly while fodd is less than 10
            fod = request.form.get('food')  # Get the food input from the form
            selected_variety = request.form.get('varieties')
            ndf = pd.DataFrame()
            if fodd >= 5 and fodd < 10:
                if "done_early" in request.form:
                    fodd = 10
            if fodd > 0:
                if "reset" in request.form:
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

                    return render_template('index.html')
            # # # # # #
            if not fod:
                # No food item provided; prompt user to input a food item
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
                #selected_variety = random.choice(varieties)
                flash(f"You have listed {fodd} items. List (another) food item from your pantry!")
                #print(vari1)
                #print(vari10)
                # Store selected variety in variX variables based on item count
                #vari10 = selected_variety
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

            fob.append(fod)  # Store the food item for reference
            found_valid_variety = False  # Reset flag for each food item

            for attempt in range(3):  # Allow up to 3 attempts to correct the input
                chat_completion = client.chat.completions.create(
                    messages=[
                        {
                            "role": "user",
                            "content": "Here's a broad food ingredient. \n" + fod + "\n If the word is misspelled, fix the spelling and write nothing else. Capitalize the first letter if it isn't already, and simplify the item if possible. As an example, if the response was cow's milk, just write milk. Do not write anything else, including the original input. If it's already spelled correctly, only capitalize the first letter if needed and do nothing else. If the word is perfectly spelled and capitalized, don't change anything else. Keep the word as is. If something like Oranges or Blueberries is not in plural form, change it to be so. However, if something like Onion, Pepper, or Apple is in plural form, change it to its singular form. For example: Peppers becomes Pepper and Nut becomes Nuts. Do the least change possible, and don't change an ingredient to a similar one (e.g. Cheese stays Cheese, not Milk). If the food item doesn't work and it seemed to be formatted correctly, change it from plural to non-plural and vice versa. When you post it, it should look like Blueberries, Onion, or Sauce."
                        }
                    ],
                    model="llama3-8b-8192",
                )

                goe = chat_completion.choices[0].message.content.strip()
                print(goe)
                ndf = df.loc[df['food'] == goe]

                if not ndf.empty:
                    varieties = ndf['description'].tolist()  # Get varieties for the food item
                    ford = random.choice(varieties)
                    if goe in inputs:
                        inputs.remove(goe)
                    # print(selected_variety)
                    # print(request.form.to_dict())
                    # print(varieties)
                    
                    # Check if selected variety is missing and prompt user to choose
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

                    vari10 = random.choice(varieties)
                    attempt = 3

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
        flash("FINAL:")
        for x in dones:
            flash(f"{x}")
        flash("Done! Now loading recipes...")
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
#

# # #

####### ####### #######

# # #

#
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


                
                      
    ####### ####### #######



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
    #
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
                model_path = r"C:\Users\nickc\Downloads\model777.h5"
                if os.path.exists(model_path):
                    print("File exists.")
                else:
                    print("File does not exist.")
                model = tf.keras.models.load_model(model_path, compile=False)
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
                #raw_pred = predictions
                #raw_pred = raw_pred.astype(int)
                #predictions = np.round(predictions)
                #predictions = predictions.astype(int)
                print(f"Prediction: {raw_pred}")
                print(f"Raw Prediction: {predictions}")
                content_length = request.content_length
                print(f"Request Content-Length: {content_length} bytes")
    
                target_positions = [targ] 

                # Step 3: Filter URLs based on the target positions
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
        for item in irisrec:
            nutchk = str(item)
            nutchk = re.sub(r'[\[\]\']', '', nutchk)
            response = requests.get(nutchk)

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
                inicrbcheck = crbcheck
                iniprtcheck = prtcheck
                inifatcheck = fatcheck
                inisarcheck = sarcheck
                inifibcheck = fibcheck
                inicalcheck = calcheck
                dcheckej = [crbcheck, prtcheck, fatcheck, sarcheck, fibcheck, calcheck]
                jcheckej = str(dcheckej)
                crbcheck = (carbcheck(calcheck, crbcheck))
                prtcheck = (protcheck(prtcheck))
                fatcheck = (fatfcheck(calcheck, fatcheck))
                sarcheck = (sgarcheck(sarcheck))
                fibcheck = (fibecheck(fibcheck))
                calcheck = (calocheck(calcheck))
                ncheckej = np.asarray([crbcheck, prtcheck, fatcheck, sarcheck, fibcheck, calcheck])
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
        errors = np.asarray(errors)
        serrors = np.abs(errors)
        if serrors.size > 0:  # Ensure serrors is not empty
            serrors = np.nanmean(serrors)  # Ignore NaN values
            print(serrors)
        else:
            flash("Sorry!")
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
                    if key != "@type":  # Skip the "@type" key
                        print(f"  {key}: {value}")
                        if iterated == 0:
                            nutr_a += f"{key}: {value} <br>"
                        if iterated == 1:
                            nutr_b += f"{key}: {value} <br>"
                        if iterated == 2:
                            nutr_c += f"{key}: {value} <br>"
                        if iterated == 3:
                            nutr_d += f"{key}: {value} <br>"
                        if iterated == 4:
                            nutr_e += f"{key}: {value} <br>"
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
                iterated += 1  
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
                <h1>1. {title_a}</h1>
                <img src={image_a} alt="Image" />
                <h2>{main_a}</h2>
                <h2>Nutritional Facts:</h2>
                <h3>{nutr_a}</h3>
                <h2>Ingredients:</h2>
                <h3>{ingred_a}</h3>
                <h2>Instructions:</h2>
                <h3>{instruc_a}</h2>
                <hr class="solid">
                <h1>2. {title_b}</h1>
                <img src={image_b} alt="Image" />
                <h2>{main_b}</h2>
                <h2>Nutritional Facts:</h2>
                <h3>{nutr_b}</h3>
                <h2>Ingredients:</h2>
                <h3>{ingred_b}</h3>
                <h2>Instructions:</h2>
                <h3>{instruc_b}</h2>
                <hr class="solid">
                <h1>3. {title_c}</h1>
                <img src={image_c} alt="Image" />
                <h2>{main_c}</h2>
                <h2>Nutritional Facts:</h2>
                <h3>{nutr_c}</h3>
                <h2>Ingredients:</h2>
                <h3>{ingred_c}</h3>
                <h2>Instructions:</h2>
                <h3>{instruc_c}</h2>
                <hr class="solid">
                <h1>4. {title_d}</h1>
                <img src={image_d} alt="Image" />
                <h2>{main_d}</h2>
                <h2>Nutritional Facts:</h2>
                <h3>{nutr_d}</h3>
                <h2>Ingredients:</h2>
                <h3>{ingred_d}</h3>
                <h2>Instructions:</h2>
                <h3>{instruc_d}</h2>
                <hr class="solid">
                <h1>5. {title_e}</h1>
                <img src={image_e} alt="Image" />
                <h2>{main_e}</h2>
                <h2>Nutritional Facts:</h2> 
                <h3>{nutr_e}</h3>
                <h2>Ingredients:</h2>
                <h3>{ingred_e}</h3>
                <h2>Instructions:</h2>
                <h3>{instruc_e}</h2>
            </body>
            </html>
        """
        print(html_output)
        with open("templates/output.html", "w") as file:
            file.write(html_output)
        urlcheck = None
        cutoff = None
        selected_variety = None
        skipse = None
        fodd = None
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

if __name__ == '__main__':
    app.run(port=5000, debug=True)