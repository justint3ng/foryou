/*
 * game.h
 *
 * Author: Jarrod Bennett, Cody Burnett
 *
 * Function prototypes for game functions available externally. You may wish
 * to add extra function prototypes here to make other functions available to
 * other files.
 */


#ifndef GAME_H_
#define GAME_H_

#include <stdint.h>

// Initialise the game by resetting the grid and beat
void initialise_game(void);

// flash the cursor
void flash_cursor(void);

// move the cursor in the x and/or y direction
void move_cursor(int8_t dx, int8_t dy);

// Returns 1 if the game is over, 0 otherwise.
uint8_t is_game_over(void);

#define SEA 0
#define CARRIER 1
#define CRUISER 2
#define DESTROYER 3
#define FRIGATE 4
#define CORVETTE 5
#define SUBMARINE 6
#define SHIP_MASK 7
#define SHIP_END 8
#define HORIZONTAL 16

#endif
