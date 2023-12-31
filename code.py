#!/usr/bin/env python3


# Created by: Ismaila
# Created on: December 2023
# This program is the "Space Aliens" programs on the Badge
import ugame
import stage

import constants 


def game_scene():
    # this function is the main game game_scene

    #image banks for cicuitpython
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")
    #set the background to image 0 in the image bank
    #  and the size (10x8 tiles of size 16x16)


    background = stage.Grid(image_bank_background, 10, 8)

    ship = stage.Sprite(image_bank_sprites, 5, 75, constants.SCREEN_Y - (2 * constants.SPRITE_SIZE))

    # create a stage for the background to show up on
    #  and set the frame rate to 60 fps
    game = stage.Stage(ugame.display,60)
    # set the layers of all sprites, items show up in order
    game.layers = [ship] + [background]
    # render all sprites
    #  most likley you will only render the background once per game scene
    game.render_block()
    print("\n\n\n") # 3 blank lines
    print("Hello, Ismaila!")


    # repeat forever, game loop
    while True:
          # get user input
          keys = ugame.buttons.get_pressed()
          # redraw sprites
          game.render_sprites([ship])
          game.tick()
          #get user input
          keys = ugame.buttons.get_pressed()
          if keys & ugame.K_X:
               print ("A")
          if keys & ugame.K_O:
            print("B")
          if keys & ugame.K_START:
            print("start")
          if keys & ugame.K_SELECT:
            print("select")
          if keys & ugame. K_RIGHT:
            ship.move(ship.x +1, ship.y)
          if keys & ugame.K_LEFT:
            ship.move(ship.x -1, ship.y)
          if keys & ugame.K_UP:
            ship.move(ship.x, ship.y - 1)
          if keys & ugame.K_DOWN:
            ship.move(ship.x, ship.y + 1)
            pass # just a placeholder for now


    # redraw sprites
          game.render_sprites([ship])
          game.tick()

   
if __name__ == "__main__":
    game_scene()
