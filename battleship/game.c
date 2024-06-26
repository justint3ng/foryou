/*
 * game.c
 *
 * Functionality related to the game state and features.
 *
 * Author: Jarrod Bennett, Cody Burnett
 */ 

#include "game.h"
#include <stdlib.h>
#include <stdio.h>
#include <stdint.h>
#include "display.h"
#include "ledmatrix.h"
#include "terminalio.h"

uint8_t human_grid[GRID_NUM_ROWS][GRID_NUM_COLUMNS];
uint8_t computer_grid[GRID_NUM_ROWS][GRID_NUM_COLUMNS];
uint8_t cursor_x, cursor_y;
uint8_t cursor_on;

// Initialise the game by resetting the grid and beat
void initialise_game(void)
{
	// clear the splash screen art
	ledmatrix_clear();
	
	// see "Human Turn" feature for how ships are encoded
	// fill in the grid with the ships
	uint8_t initial_human_grid[GRID_NUM_ROWS][GRID_NUM_COLUMNS] =
		{{SEA,                  SEA,                            SEA,                            SEA,                SEA,                SEA,                            SEA,                            SEA                 },
		 {SEA,                  CARRIER|HORIZONTAL|SHIP_END,    CARRIER|HORIZONTAL,             CARRIER|HORIZONTAL, CARRIER|HORIZONTAL, CARRIER|HORIZONTAL,             CARRIER|HORIZONTAL|SHIP_END,    SEA                 },
		 {SEA,                  SEA,                            SEA,                            SEA,                SEA,                SEA,                            SEA,                            SEA                 },
		 {SEA,                  SEA,                            CORVETTE|SHIP_END,              SEA,                SEA,                SUBMARINE|SHIP_END,             SEA,                            SEA                 },
		 {DESTROYER|SHIP_END,   SEA,                            CORVETTE|SHIP_END,              SEA,                SEA,                SUBMARINE|SHIP_END,             SEA,                            FRIGATE|SHIP_END    },
		 {DESTROYER,            SEA,                            SEA,                            SEA,                SEA,                SEA,                            SEA,                            FRIGATE             },
		 {DESTROYER|SHIP_END,   SEA,                            CRUISER|HORIZONTAL|SHIP_END,    CRUISER|HORIZONTAL, CRUISER|HORIZONTAL, CRUISER|HORIZONTAL|SHIP_END,    SEA,                            FRIGATE|SHIP_END    },
		 {SEA,                  SEA,                            SEA,                            SEA,                SEA,                SEA,                            SEA,                            SEA                 }};
	uint8_t initial_computer_grid[GRID_NUM_ROWS][GRID_NUM_COLUMNS] =
		{{SEA,                  SEA,                            SEA,                            SEA,                SEA,                SEA,                            SEA,                            SEA                 },
		 {DESTROYER|SHIP_END,   SEA,                            CRUISER|HORIZONTAL|SHIP_END,    CRUISER|HORIZONTAL, CRUISER|HORIZONTAL, CRUISER|HORIZONTAL|SHIP_END,    SEA,                            FRIGATE|SHIP_END    },
		 {DESTROYER,            SEA,                            SEA,                            SEA,                SEA,                SEA,                            SEA,                            FRIGATE             },
		 {DESTROYER|SHIP_END,   SEA,                            CORVETTE|SHIP_END,              SEA,                SEA,                SUBMARINE|SHIP_END,             SEA,                            FRIGATE|SHIP_END    },
		 {SEA,                  SEA,                            CORVETTE|SHIP_END,              SEA,                SEA,                SUBMARINE|SHIP_END,             SEA,                            SEA                 },
		 {SEA,                  SEA,                            SEA,                            SEA,                SEA,                SEA,                            SEA,                            SEA                 },
		 {SEA,                  CARRIER|HORIZONTAL|SHIP_END,    CARRIER|HORIZONTAL,             CARRIER|HORIZONTAL, CARRIER|HORIZONTAL, CARRIER|HORIZONTAL,             CARRIER|HORIZONTAL|SHIP_END,    SEA                 },
		 {SEA,                  SEA,                            SEA,                            SEA,                SEA,                SEA,                            SEA,                            SEA                 }};
	for (uint8_t i=0; i<GRID_NUM_COLUMNS; i++)
	{
		for (uint8_t j=0; j<GRID_NUM_COLUMNS; j++)
		{
			human_grid[j][i] = initial_human_grid[j][i];
			computer_grid[j][i] = initial_computer_grid[j][i];
			if (human_grid[j][i] & SHIP_MASK)
			{
				ledmatrix_draw_pixel_in_human_grid(i, j, COLOUR_ORANGE);
			}
		}
	}
	cursor_x = 3;
	cursor_y = 3;
	cursor_on = 1;
}

void flash_cursor(void)
{
	cursor_on = 1-cursor_on;
	if (cursor_on)
	{
		ledmatrix_draw_pixel_in_computer_grid(cursor_x, cursor_y, COLOUR_YELLOW);
	}
	else if (0) // test for hit ship here, then duplicate and modify to test for sunken ship
	{
		ledmatrix_draw_pixel_in_computer_grid(cursor_x, cursor_y, COLOUR_RED);
	}
	else
	{
		ledmatrix_draw_pixel_in_computer_grid(cursor_x, cursor_y, COLOUR_BLACK);
	}
}

// moves the position of the cursor by (dx, dy) such that if the cursor
// started at (cursor_x, cursor_y) then after this function is called,
// it should end at ( (cursor_x + dx) % WIDTH, (cursor_y + dy) % HEIGHT)
// the cursor should be displayed after it is moved as well
void move_cursor(int8_t dx, int8_t dy) {
	//YOUR CODE HERE
	/*suggestions for implementation:
	 * 1: remove the display of the cursor at the current location
	 *		(and replace it with whatever piece is at that location)
	 * 2: update the positional knowledge of the cursor, this will include
	 *		variables cursor_x, cursor_y and cursor_visible. Make sure you
	 *		consider what should happen if the cursor moves off the board.
	 * 3: display the cursor at the new location
	 * 4: reset the cursor flashing cycle. See project.c for how the cursor
	 *		is flashed.
	 */
	
}


// Returns 1 if the game is over, 0 otherwise.
uint8_t is_game_over(void)
{
	// YOUR CODE HERE
	// Detect if the game is over i.e. if a player has won.
	return 0;
}
