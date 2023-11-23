import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
st.title('Bienvenu sur notre page festive!')

st.write("sur cette page vous pouvez choisir le mode du jeux qui vous attend")

#df= pd.read_csv('data.csv', sep=',')
#df
pt = pd.read_csv('pt.csv', sep=',', index_col = 0)
#pt

def game(nom_pays='France'):
    try:
        if pt[pt['Country']==str(nom_pays).lower()]['Dec'].values[0]>=20:
            return "hot"
        elif pt[pt['Country']==str(nom_pays).lower()]['Dec'].values[0]<20:
            return "cold"
        else:
            return "erreur"
    except:
        return "Veuillez rentrer le pays en anglais et sans fautes de frappe"

#game('France')

#town_name = st.text_input("Rntrer le nom de votre ville:")
country_name = st.text_input("Rentrer le nom de votre pays (en anglais):")
st.write(game(country_name))


# Simple pygame program

# Import and initialize the pygame library
import pygame
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([500, 500])

# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((255, 255, 255))

    # Draw a solid blue circle in the center
    pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()
