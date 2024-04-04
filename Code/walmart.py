# %%
# Import Splinter and BeautifulSoup
import requests
from splinter import Browser
from bs4 import BeautifulSoup as soup
import re
import pandas as pd

from import_export import addTo_products_dataframe
from import_export import get_products_dataframe

# %%
#browser = Browser('chrome', incognito=True)

# %%
# Visit the walmart site for eggs
url = 'https://www.walmart.com/browse/food/eggs/976759_9176907_1001469?povid=GlobalNav_rWeb_Grocery_DairyEggs_Eggs&facet=number_of_pieces%3A12%7C%7Cfacet_product_type%3AEggs'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}

response = requests.get(url, headers=headers) 
soup = soup(response.content, 'html.parser') 
print(soup.prettify()) 

# %%
#conditional_elements = soup.find_all('div', {'data-testid': 'item-stack'})
#print(conditional_elements)

# %%
#conditional_elements = soup.find_all("div", class_="mb1")
#conditional_text = [item.text for item in price]
#for i in conditional_text:
    #print(i)

# %%
#<span class="w_iUH7">current price $2.66</span>
conditional_elements = soup.find_all("span", class_="w_iUH7")
conditional_text = [item.text for item in conditional_elements]
for i in conditional_text:
    print(i)

# %%
eggs = pd.DataFrame(conditional_text)

eggs

# %%
eggs.insert(1, 'Current Price', '')
eggs

# %% [markdown]
# 

# %%
eggs.columns = ["Name", "Current Price"]

eggs = eggs[~eggs['Name'].str.contains('reviews', regex=True)]

eggs

# %%
egg_list = pd.DataFrame({'Name':eggs['Name'].iloc[::2].values, 'Current Price':eggs['Name'].iloc[1::2].values})
egg_list

# %%
egg_list[['1', '2']] = egg_list['Current Price'].str.split('$', expand=True)
print(egg_list)


# %%
egg_list

# %%
egg_list = egg_list.drop(['Current Price', '1'], axis=1)

# %%
egg_list.columns = ["Name", "Current Price"]
egg_list

# %%
egg_list["Category"] = "Eggs"
egg_list["Store"] = "Walmart"
egg_list

# %%
import requests
from splinter import Browser
from bs4 import BeautifulSoup as soup
import re
import pandas as pd

# %%
# Visit the walmart site for flour
url = 'https://www.walmart.com/browse/food/flours-meals/976759_976780_9959366_9084673?sort=best_match&cat_id=976759_976780_9959366_9084673_7544865&stores=5012&ps=40&facet=fulfillment_method_in_store%3AIn-store'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}

response = requests.get(url, headers=headers) 
soup = soup(response.content, 'html.parser') 
print(soup.prettify()) 

# %%
conditional_elements = soup.find_all("span", class_="w_iUH7")
conditional_text = [item.text for item in conditional_elements]
for i in conditional_text:
    print(i)

# %%
flour = pd.DataFrame(conditional_text)

flour

# %%
flour.insert(1, 'Current Price', '')
flour

# %%
#flour.insert(2, 'Reviews', '')
#flour

# %%
flour.columns = ["Name", "Current Price"]
flour

# %%
df1 = flour[flour.index % 3 != 2] 
df1

# %%
flour_list = pd.DataFrame({'Name':df1['Name'].iloc[::2].values, 'Current Price':df1['Name'].iloc[1::2].values})
flour_list

# %%
flour_list[['1', '2']] = flour_list['Current Price'].str.split('$', expand=True)
print(flour_list)

# %%
flour_list = flour_list.drop(['Current Price', '1'], axis=1)

# %%
flour_list.columns = ["Name", "Current Price"]
flour_list

# %%
flour_list["Category"] = "Flour"
flour_list["Store"] = "Walmart"
flour_list

# %%
# Import Splinter and BeautifulSoup
import requests
from splinter import Browser
from bs4 import BeautifulSoup as soup
import re
import pandas as pd

# %%

# Visit the walmart site for sugar
url = 'https://www.walmart.com/browse/food/baking-ingredients/976759_976780_9959366?sort=best_match&cat_id=976759_976780_9959366_3219393_4479282&stores=5012&ps=40&facet=fulfillment_method_in_store%3AIn-store'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}

response = requests.get(url, headers=headers) 
soup = soup(response.content, 'html.parser') 
print(soup.prettify()) 

# %%
conditional_elements = soup.find_all("span", class_="w_iUH7")
conditional_text = [item.text for item in conditional_elements]
for i in conditional_text:
    print(i)

# %%
sugar = pd.DataFrame(conditional_text)

sugar

# %%
sugar.insert(1, 'Current Price', '')
sugar

# %%
sugar.columns = ["Name", "Current Price"]
sugar

# %%
df2 = sugar[sugar.index % 3 != 2] 
df2

# %%
sugar_list = pd.DataFrame({'Name':df2['Name'].iloc[::2].values, 'Current Price':df2['Name'].iloc[1::2].values})
sugar_list

# %%
sugar_list[['1', '2']] = sugar_list['Current Price'].str.split('$', expand=True)
print(sugar_list)

# %%
sugar_list = sugar_list.drop(['Current Price', '1'], axis=1)
sugar_list.columns = ["Name", "Current Price"]
sugar_list

# %%
sugar_list["Category"] = "Sugar"
sugar_list["Store"] = "Walmart"
sugar_list

# %%
# Import Splinter and BeautifulSoup
import requests
from splinter import Browser
from bs4 import BeautifulSoup as soup
import re
import pandas as pd

# %%

url = 'https://www.walmart.com/browse/food/2-milk/976759_9176907_4405816_4288431?povid=976759_topnavpill_9176907_Milkbrowsepills_2%milk_Rweb_aug_23'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}

response = requests.get(url, headers=headers) 
soup = soup(response.content, 'html.parser') 
print(soup.prettify()) 

# %%
conditional_elements = soup.find_all("span", class_="w_iUH7")
conditional_text = [item.text for item in conditional_elements]
for i in conditional_text:
    print(i)

# %%
milk = pd.DataFrame(conditional_text)



# %%
milk.insert(1, 'Current Price', '')


# %%
milk.columns = ["Name", "Current Price"]


# %%
#df4 = milk[milk.index % 3 != 2] 
df4 = milk[milk.index % 3 != 2].iloc[:8]


# %%
last_10_rows = milk.tail(10)


# %%
frames = [df4, last_10_rows]
 
result = pd.concat(frames)


# %%
milk_list = pd.DataFrame({'Name':result['Name'].iloc[::2].values, 'Current Price':result['Name'].iloc[1::2].values})


# %%
milk_list[['1', '2']] = milk_list['Current Price'].str.split('$', expand=True)


# %%
milk_list = milk_list.drop(['Current Price', '1'], axis=1)
milk_list.columns = ["Name", "Current Price"]


# %%
milk_list["Category"] = "Milk"
milk_list["Store"] = "Walmart"


# %%
# Import Splinter and BeautifulSoup
import requests
from splinter import Browser
from bs4 import BeautifulSoup as soup
import re
import pandas as pd

# %%
url = 'https://www.walmart.com/browse/food/vanilla-extract-food-coloring-spices/976759_976780_9959366_5020530?sort=best_match&cat_id=976759_976780_9959366_5020530_1343575&stores=5012&ps=40&facet=fulfillment_method_in_store%3AIn-store'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}

response = requests.get(url, headers=headers) 
soup = soup(response.content, 'html.parser') 
print(soup.prettify()) 

# %%
conditional_elements = soup.find_all("span", class_="w_iUH7")
conditional_text = [item.text for item in conditional_elements]
for i in conditional_text:
    print(i)

# %%
vanilla = pd.DataFrame(conditional_text)

vanilla

# %%
vanilla.insert(1, 'Current Price', '')

# %%
vanilla.columns = ["Name", "Current Price"]
vanilla

# %%
df5 = vanilla[vanilla.index % 3 != 2] 
df5

# %%
vanilla_list = pd.DataFrame({'Name':df5['Name'].iloc[::2].values, 'Current Price':df5['Name'].iloc[1::2].values})
vanilla_list

# %%
vanilla_list[['1', '2']] = vanilla_list['Current Price'].str.split('$', expand=True)
print(vanilla_list)

# %%
vanilla_list = vanilla_list.drop(['Current Price', '1'], axis=1)
vanilla_list.columns = ["Name", "Current Price"]
vanilla_list

# %%
vanilla_list["Category"] = "Vanilla Extract"
vanilla_list["Store"] = "Walmart"
vanilla_list

# %%
# Import Splinter and BeautifulSoup
import requests
from splinter import Browser
from bs4 import BeautifulSoup as soup
import re
import pandas as pd

# %%
url = 'https://www.walmart.com/browse/food/unsalted-butter/976759_9176907_1001467_5254440?povid=976759_nup_9176907_ButterBrowseNup_UnsaltedButter_Rweb_2_15_2024'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}

response = requests.get(url, headers=headers) 
soup = soup(response.content, 'html.parser') 
print(soup.prettify()) 

# %%
conditional_elements = soup.find_all("span", class_="w_iUH7")
conditional_text = [item.text for item in conditional_elements]
for i in conditional_text:
    print(i)

# %%
butter = pd.DataFrame(conditional_text)

butter

# %%
butter.insert(1, 'Current Price', '')

# %%
butter.columns = ["Name", "Current Price"]
butter

# %%
df6 = butter[butter.index % 3 != 2].iloc[:2]
df6


# %%
last_rows = butter.tail(8)
last_rows

# %%
frames2 = [df6, last_rows]
 
result2 = pd.concat(frames2)
display(result2)

# %%
butter_list = pd.DataFrame({'Name':result2['Name'].iloc[::2].values, 'Current Price':result2['Name'].iloc[1::2].values})
butter_list

# %%
butter_list[['1', '2']] = butter_list['Current Price'].str.split('$', expand=True)
print(butter_list)

# %%
butter_list = butter_list.drop(['Current Price', '1'], axis=1)
butter_list.columns = ["Name", "Current Price"]
butter_list

# %%
butter_list["Category"] = "Butter"
butter_list["Store"] = "Walmart"
butter_list

# %%
# Import Splinter and BeautifulSoup
import requests
from splinter import Browser
from bs4 import BeautifulSoup as soup
import re
import pandas as pd

# %%

url = 'https://www.walmart.com/browse/food/chocolate-chips-cocoa/976759_976780_9959366_2710937?sort=best_match&cat_id=976759_976780_9959366_2710937_6862428&stores=5012&ps=40&facet=fulfillment_method%3AIn-store'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}

response = requests.get(url, headers=headers) 
soup = soup(response.content, 'html.parser') 
print(soup.prettify()) 

# %%
conditional_elements = soup.find_all("span", class_="w_iUH7")
conditional_text = [item.text for item in conditional_elements]
for i in conditional_text:
    print(i)

# %%
chips = pd.DataFrame(conditional_text)
chips

# %%
chips.insert(1, 'Current Price', '')

# %%
chips.columns = ["Name", "Current Price"]
chips

# %%
df7 = chips[chips.index % 3 != 2]
df7

# %%
chips_list = pd.DataFrame({'Name':df7['Name'].iloc[::2].values, 'Current Price':df7['Name'].iloc[1::2].values})
chips_list

# %%
chips_list[['1', '2']] = chips_list['Current Price'].str.split('$', expand=True)
print(chips_list)

# %%
chips_list = chips_list.drop(['Current Price', '1'], axis=1)
chips_list.columns = ["Name", "Current Price"]
chips_list

# %%
chips_list["Category"] = "Chocolate Chips"
chips_list

# %%
chips_list["Store"] = "Walmart"
chips_list

# %%
# Import Splinter and BeautifulSoup
import requests
from splinter import Browser
from bs4 import BeautifulSoup as soup
import re
import pandas as pd

# %%
url = 'https://www.walmart.com/browse/food/brown-sugar/976759_976780_9959366_3087979_2203492?povid=976759_LHNCP_976780_Categories_SugarsandSweeteners_BrownSugar_Jun_2&facet=brand%3ADomino%7C%7Cbrand%3AGreat+Value%7C%7Cbrand%3ADulce+Cana'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}

response = requests.get(url, headers=headers) 
soup = soup(response.content, 'html.parser') 
print(soup.prettify())

# %%
conditional_elements = soup.find_all("span", class_="w_iUH7")
conditional_text = [item.text for item in conditional_elements]
for i in conditional_text:
    print(i)

# %%
bsugar = pd.DataFrame(conditional_text)

bsugar

# %%
bsugar.insert(1, 'Current Price', '')
bsugar

# %%
bsugar.columns = ["Name", "Current Price"]
bsugar

# %%
bsugar.columns = ["Name", "Current Price"]

bsugar = bsugar[~bsugar['Name'].str.contains('reviews', regex=True)]

bsugar

# %%
bsugar.columns = ["Name", "Current Price"]

bsugar = bsugar[~bsugar['Name'].str.contains('Was', regex=True)]

bsugar

# %%
brown_sugar_list = pd.DataFrame({'Name':bsugar['Name'].iloc[::2].values, 'Current Price':bsugar['Name'].iloc[1::2].values})
brown_sugar_list

# %%
brown_sugar_list[['1', '2']] = brown_sugar_list['Current Price'].str.split('$', expand=True)
brown_sugar_list

# %%
brown_sugar_list = brown_sugar_list.drop(['Current Price', '1'], axis=1)

# %%
brown_sugar_list.columns = ["Name", "Current Price"]
brown_sugar_list

# %%
brown_sugar_list["Category"] = "Brown Sugar"
brown_sugar_list["Store"] = "Walmart"
brown_sugar_list

# %%
# Import Splinter and BeautifulSoup
import requests
from splinter import Browser
from bs4 import BeautifulSoup as soup
import re
import pandas as pd

# %%
#url = 'https://www.walmart.com/browse/food/salt-pepper/976759_976794_3029941_1878334?povid=976759_nup_976794_HerbsandSpices_Saltandpepper_Rweb_Aug_28'
url = 'https://www.walmart.com/search?q=morton+iodized+salt&typeahead=iodized+salt&facet=brand%3AMorton+Salt'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}

response = requests.get(url, headers=headers) 
soup = soup(response.content, 'html.parser') 
print(soup.prettify()) 

# %%
conditional_elements = soup.find_all("span", class_="w_iUH7")
conditional_text = [item.text for item in conditional_elements]
for i in conditional_text:
    print(i)

# %%
salt = pd.DataFrame(conditional_text)

salt

# %%
salt.insert(1, 'Current Price', '')
salt

# %%
salt.columns = ["Name", "Current Price"]

salt = salt[~salt['Name'].str.contains('reviews', regex=True)]

salt

# %%
salt.columns = ["Name", "Current Price"]
salt = salt[~salt['Name'].str.contains('All-Purpose,', regex=True)]
salt

# %%
#salt.columns = ["Name", "Current Price"]
#p = 'Salt\current price'
#salt = salt[salt['Name'].str.contains("p", regex=True)]

#salt

# %%
salt.columns = ["Name", "Current Price"]

salt = salt[~salt['Name'].str.contains('Was', regex=True)]

salt

# %%
#salt.drop(salt.tail(2).index,
        #inplace = True)
#salt

# %%
salt_list = pd.DataFrame({'Name':salt['Name'].iloc[::2].values, 'Current Price':salt['Name'].iloc[1::2].values})
salt_list

# %%
salt_list[['1', '2']] = salt_list['Current Price'].str.split('$', expand=True)
salt_list

# %%
salt_list = salt_list.drop(['Current Price', '1'], axis=1)



# %%
salt_list.columns = ["Name", "Current Price"]
salt_list

# %%
salt_list["Category"] = "Salt"
salt_list["Store"] = "Walmart"
salt_list

# %%
import requests
from splinter import Browser
from bs4 import BeautifulSoup as soup
import re
import pandas as pd

# %%
# Visit the walmart site for baking soda
url = 'https://www.walmart.com/browse/food/baking-soda-starch/976759_976780_9959366_5053287?sort=best_match&cat_id=976759_976780_9959366_5053287_7963908&stores=5012&ps=40&facet=fulfillment_method_in_store%3AIn-store'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}

response = requests.get(url, headers=headers) 
soup = soup(response.content, 'html.parser') 
print(soup.prettify()) 

# %%
conditional_elements = soup.find_all("span", class_="w_iUH7")
conditional_text = [item.text for item in conditional_elements]
for i in conditional_text:
    print(i)

# %%
baking_soda = pd.DataFrame(conditional_text)

baking_soda

# %%
baking_soda.insert(1, 'Current Price', '')
baking_soda

# %%
baking_soda.columns = ["Name", "Current Price"]

baking_soda = baking_soda[~baking_soda['Name'].str.contains('reviews', regex=True)]

baking_soda

# %%
baking_soda = pd.DataFrame({'Name':baking_soda['Name'].iloc[::2].values, 'Current Price':baking_soda['Name'].iloc[1::2].values})
baking_soda

# %%
baking_soda[['1', '2']] = baking_soda['Current Price'].str.split('$', expand=True)
baking_soda

# %%
baking_soda = baking_soda.drop(['Current Price', '1'], axis=1)

# %%
baking_soda.columns = ["Name", "Current Price"]
baking_soda

# %%
baking_soda["Category"] = "Baking Soda"
baking_soda["Store"] = "Walmart"
baking_soda

# %%
# Import Splinter and BeautifulSoup
import requests
from splinter import Browser
from bs4 import BeautifulSoup as soup
import re
import pandas as pd

# %%

url = 'https://www.walmart.com/browse/food/baking-soda-starch/976759_976780_9959366_5053287?sort=best_match&cat_id=976759_976780_9959366_5053287_5452783&stores=5012&ps=40&facet=fulfillment_method%3AIn-store'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}

response = requests.get(url, headers=headers) 
soup = soup(response.content, 'html.parser') 
print(soup.prettify()) 

# %%
conditional_elements = soup.find_all("span", class_="w_iUH7")
conditional_text = [item.text for item in conditional_elements]
for i in conditional_text:
    print(i)

# %%
baking_powder = pd.DataFrame(conditional_text)

baking_powder

# %%
baking_powder.insert(1, 'Current Price', '')
baking_powder

# %%
baking_powder.columns = ["Name", "Current Price"]

baking_powder = baking_powder[~baking_powder['Name'].str.contains('reviews', regex=True)]

baking_powder

# %%
baking_powder.columns = ["Name", "Current Price"]

baking_powder = baking_powder[~baking_powder['Name'].str.contains('Was', regex=True)]

baking_powder

# %%
baking_powder = pd.DataFrame({'Name':baking_powder['Name'].iloc[::2].values, 'Current Price':baking_powder['Name'].iloc[1::2].values})
baking_powder

# %%
baking_powder[['1', '2']] = baking_powder['Current Price'].str.split('$', expand=True)
baking_powder


# %%
baking_powder = baking_powder.drop(['Current Price', '1'], axis=1)

# %%
baking_powder.columns = ["Name", "Current Price"]
baking_powder

# %%
baking_powder["Category"] = "Baking Powder"
baking_powder["Store"] = "Walmart"
baking_powder

# %%
walmart_info = [egg_list, flour_list, sugar_list, milk_list, vanilla_list, butter_list, chips_list, brown_sugar_list, salt_list, baking_soda, baking_powder]
walmart_df = pd.concat(walmart_info)
walmart_df


# %%
walmart_df.reset_index(drop=True, inplace=True)
walmart_df

# %%
from datetime import datetime

walmart_df.rename(columns={"Category": "Ingredient"}, inplace=True)
walmart_df.rename(columns={"Current Price": "Price"}, inplace=True)
walmart_df.rename(columns={"Name": "product"}, inplace=True)
walmart_df["Price"] = walmart_df["Price"].astype(float)
walmart_df["Ingredient"].replace("Eggs", "eggs", inplace=True)
walmart_df["Ingredient"].replace("Flour", "flour", inplace=True)
walmart_df["Ingredient"].replace("Sugar", "granulated sugar", inplace=True)
walmart_df["Ingredient"].replace("Milk", "milk", inplace=True)
walmart_df["Ingredient"].replace("Vanilla Extract", "vanilla extract", inplace=True)
walmart_df["Ingredient"].replace("Butter", "butter", inplace=True)
walmart_df["Ingredient"].replace("Chocolate Chips", "chocolate chips", inplace=True)
walmart_df["Ingredient"].replace("Brown Sugar", "brown sugar", inplace=True)
walmart_df["Ingredient"].replace("Salt", "salt", inplace=True)
walmart_df["Ingredient"].replace("Baking Soda", "baking soda", inplace=True)
walmart_df["Ingredient"].replace("Baking Powder", "baking powder", inplace=True)
walmart_df['Date'] = datetime.now().strftime("%Y-%m-%d")
walmart_products_df = walmart_df
walmart_products_df

# %%
%store walmart_products_df

# %%
df = pd.DataFrame()
df = get_products_dataframe()

df

# %%
addTo_products_dataframe(walmart_products_df)


