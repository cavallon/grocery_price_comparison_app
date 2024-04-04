# grocery_comparison_project
  April Holmes
  Christopher Avallon
  Lucas Barber

Description: Interactive website to compare grocery prices across several grocery stores.

# OVERVIEW:

"If only there was a way to compare all grocery store prices for a recipe"
    -- Christopher Avallon, 2024

The purpose of this project is to create an application which compares grocery prices across several grocery stores, querying a database for the minumim price.
Due to the potentially enormous scope of this endeavor, we've limited this application to the ingredients necessary for baking cookies.
Our stores are Kroger, Walmart, and Aldi. The end result is a flask script which displays the cheapest ingredient results for all three stores.

This project is a system made up of the following parts:

  # -- Data Gathering
      Files: 
        aldi_web_scraping.ipynb
        walmart.ipynb
        kroger.ipynb

      We used webscraping for Aldi and Walmart to retrieve search results and store them in dataframes. Regular expressions were used to filter.
      Kroger data was obtained via an API
      The end result are three dataframes for each store, which are exported to to an sqlite database.
      The file Cookie_calculator_app.ipynb is an additional way of verifying data integrity by merging dataframes.

  # -- Database
      Files: 
        import_export.py
        sqlite_setup.py
        grocery.sqlite
        grocery_comparison_diagram.png
      
      Import_export.py uses sqlalchemy to import the final dataframes from each store and export them to our sqlite database, grocery.sqlite.
      All grocery data is stored in grocery.sqlite.

  # -- Results
      Files:
        cookie_flask
        cookie_html.html
        cookie_css.css
        totals_by_date.png
        store_tot_barchart.html
      
      cookie_flask queries grocery.sqlite for the minimum price per ingredient for each store, and displays the results of the query in html.
      No hardcoding in html is required, as the classes are automatically populated with the results of the query.
      cookie_flask includes routes to html to render both bar charts.

# HOW IT WORKS

Simply run the cookie_flask script and connect to the local server. Follow to /allstores and you will have your cheapest cookie per store results!
This system is set up in such a way where you don't need to web scrape each time you want results. 
The database is automatically updated each time you run the data gathering/api scripts. Ultimately, this system is entirely scalable if datetime querying is implemented.

  # -- Full chain of events:
      1 - Data is gathered, rendered as dataframes, and filtered in data gathering/api scripts
      2 - Data is exported to sqlite database
      3 - Database is queried to return results of minimum ingredient cost and minimum sum cost per store
      4 - Query results are dynamically displayed in HTML


# ETHICAL CONDSIDERATIONS

While scraping the websites for Aldi and Walmart has an overall minimal impact on their traffic, it's not how these websites were designed or intended to be used.
Therefore, it was important to us to have as little impact as possible, which is why we've set this system to only webscrape when we need to update the database. \

# KNOWN ISSUE
Walmart website has changed while working on this project, causing data collection to fail in the past. We've worked to fix the issue, but longevity isn't necessarily guranteed.
Further updates to the website could cause issues in the future.



# Data Resources
  Kroger APIs
    https://developer.kroger.com/documentation/public/getting-started/quick-start
    Walmart.com (search results)
    Aldi.com (search results)
