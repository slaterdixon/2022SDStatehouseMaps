#!/usr/bin/env python3


### Extra functions for statehouse district map


import folium
import pandas as pd
import geopandas as gpd
import numpy as np
import string
import regex as re
import branca

def how_many_seats(s):
  """Return number of seats in House district"""
  # Make sure string is string
  s = str(s)
  # If there are no numbers in the string it's a normal house district with 2 seats
  if s.isnumeric():
    return 2
  # Otherwise it's a district like 28A or 28B with 1 seat
  else:
    return 1
	
def name_to_tag(name):
  """Add stop character to name for url tag"""
	# Delete periods, convert to lowercase
  name = str(name).replace(".","").lower()
	# Split each character
  name = name.split()
	# Remove any single letter or characters
  for item in name:
      if len(item) < 2:
          name.remove(item)
  s = "-"
	# Rejoin string list with stop character -
  return s.join(name)

def sdpb_mtc_url(name):
    """Return URL from name"""
	# If the name exists
    if name:
	  # Return html tag with name as a tag
      return f"<a href=https://listen.sdpb.org/tags/{name_to_tag(name)}>{name}</a>"
    else:
      return np.nan
	  
def to_html_w_links(df):
  """Pandas to_HTML but fix weird formatting for a href"""
  # Convert dataframe to html
  html = df.to_html(index=False, classes="table", justify="inherit", border="0")
  # Replace html entity names
  html = html.replace("&lt;", "<")
  html = html.replace("&gt;", ">")
  return html

def table_html(style, district, seats, fig_name, df):
  table_html = f"""
    <!DOCTYPE html>
      <head>
        <style>
        <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap" rel="stylesheet">
        {style}
        
        </style>
        <base target="_blank" />

      </head>
      <body>

        <div class="header">
          <h3>State {fig_name} District {district}</h3>
          <h4>
            (Select {seats})
          </h4>
        </div>
        {to_html_w_links(df)}
      </body>
    <html> 
    """
  return table_html