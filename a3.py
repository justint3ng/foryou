import tkinter
import tkinter as tk
from tkinter import filedialog # For masters task
from typing import Callable, Union, Optional
from a3_support import *
from model import *
from constants import *

# Implement your classes here
class InfoBar(AbstractGrid):
    INFO_BAR_ROWS = 2
    INFO_BAR_COLS = 3
    INFO_BAR_HEIGHT = "1c"
    INFO_BAR_WIDTH = "1c"

    def __init__(self, master: Union[tk.Tk, tk.Frame]) -> None:
        size = (
            int(self.INFO_BAR_WIDTH[:-1]),
            int(self.INFO_BAR_HEIGHT[:-1])
        )
        width = self.INFO_BAR_COLS * size[0]
        height = self.INFO_BAR_ROWS * size[1]
        super().__init__(master, (self.INFO_BAR_ROWS, self.INFO_BAR_COLS), (width, height))

    def redraw(self, day: int, money: int, energy: int) -> None:
        for label in self.grid_slaves():
            label.grid_forget()

            # Create the day label
        day_label = tk.Label(self, text=f"Day: {day}")
        day_label.grid(row=0, column=0)

        # Create the money label
        money_label = tk.Label(self, text=f"Money: {money}")
        money_label.grid(row=0, column=1)

        # Create the energy label
        energy_label = tk.Label(self, text=f"Energy: {energy}")
        energy_label.grid(row=0, column=2)

class FarmView(AbstractGrid):
    def __init__(self, master: tk.Tk | tk.Frame, dimensions: tuple[int, int], size: tuple[int, int], **kwargs):
        super().__init__(master, dimensions, size, **kwargs)
        self.image_cache = {}

    def redraw(self, ground: list[str], plants: dict[tuple[int, int], 'Plant'], player_position: tuple[int, int], player_direction: str):
        self.clear()

        # Create images for ground
        for i, row in enumerate(ground):
            for j, ground_type in enumerate(row):
                image = get_image(soil.png)
                self.create_image((j, i), image)

        # Create images for plants
        for position, plant in plants.items():
            plant_type = plant.get_type()
            stage = plant.get_stage()
            image_filename = f"stage_{stage}.png"  # Modified image filename construction
            image = get_image(image_filename)
            self.create_image(position, image)

            # Create image for player
        player_image = get_image(f"player_{player_direction}.png")
        self.create_image(player_position, player_image)

class ItemView(tk.Frame):
    def __init__(self, master: tk.Frame, item_name: str, amount: int, select_command: Optional[Callable[[str], None]] = None, sell_command: Optional[Callable[[str], None]] = None, buy_command: Optional[Callable[[str], None]] = None):
        super().__init__(master)
        self.item_name = item_name
        self.amount = amount

        # Create the labels
        self.item_label = tk.Label(self, text=f"{self.item_name}: ")
        self.amount_label = tk.Label(self, text=f"Amount: {self.amount}")
        self.sell_price_label = tk.Label(self, text=f"Sell price: ${SELL_PRICES[self.item_name]}")

        # Create the buy button
        if buy_command and self.item_name in BUY_PRICES:
            self.buy_button = tk.Button(
                self,
                text=f"Buy price: ${BUY_PRICES[self.item_name]}",
                command=lambda: buy_command(self.item_name)
            )
        else:
            self.buy_button = tk.Button(self, text="")

        # Create the sell button
        if sell_command:
            self.sell_button = tk.Button(
                self,
                text="Sell",
                command=lambda: sell_command(self.item_name)
            )
        else:
            self.sell_button = tk.Button(self, text="")

        # Bind the select command to the frame and label
        if select_command:
            self.bind("<Button-1>", lambda event: select_command(self.item_name))
            self.item_label.bind("<Button-1>", lambda event: select_command(self.item_name))

        # Position the widgets using grid layout
        self.item_label.grid(row=0, column=0)
        self.amount_label.grid(row=0, column=1)
        self.sell_price_label.grid(row=0, column=2)
        self.buy_button.grid(row=0, column=3)
        self.sell_button.grid(row=0, column=4)

    def update(self, amount: int, selected: bool = False) -> None:
        self.amount = amount
        self.amount_label.config(text=f"Amount: {self.amount}")

        if selected:
            self.configure(bg="lightblue")
        else:
            self.configure(bg="white")

class FarmGame:
    def __init__(self, master: tk.Tk, map_file: str):
        self._master = master
        master.title("Farm Game")
        # Create the title banner
        banner_image = get_image('images/header.png', [700, BANNER_HEIGHT], ['images/header.png', ImageTk.PhotoImage])
        banner_label = tk.Label(master, image=banner_image)
        banner_label.pack()
        #create the InfoBar
        infobar = InfoBar(master)
        infobar.pack()

        #create the ItemView instances
        item_views = []
        item_names = ["Potato Seed", "Kale Seed", "Berry Seed", "Potato", "Kale", "Berry"]
        for item_name in item_names:
            item_view = ItemView(master, item_name=item_name, amount=0)
            item_view.pack()
            item_views.append(item_view)

        #create the FarmView instance
        """farmview = FarmView(master)
        farmview.pack()

        self.next_day_button = next_day_button
        self.item_views = item_views
        self.farm_view = farm_view"""

        # Create the Next Day button
        '''next_day_button = tk.Button(master, text="Next day", command=self.next_day)
        next_day_button.pack()'''

        # create the controller
        #self.controller = FarmGame()

        # Bind keypress event to handle_keypress function
        master.bind('<KeyPress>', self.handle_keypress)

        # create the menu
        #]self.create_menu()



    def redraw(self):
        self.InfoBar.redraw()
        self.ItemView.redraw()
        self.FarmView.redraw()
        self.window.update()

    def handle_keypress(self, event: tk.Event):
        key = event.keysym

        if key == 'w':
            # Player attempts to move up one square
            self.controller.move_player('w')
        elif key == 'a':
            # Player attempts to move left one square
            self.controller.move_player('a')
        elif key == 's':
            # Player attempts to move down one square
            self.controller.move_player('s')
        elif key == 'd':
            # Player attempts to move right one square
            self.controller.move_player('d')
        elif key == 'p':
            # Attempt to plant the selected seed
            self.controller.plant_selected_seed()
        elif key == 'h':
            # Attempt to harvest the plant at the player's position
            self.controller.harvest_plant()
        elif key == 'r':
            # Attempt to remove the plant at the player's position
            self.controller.remove_plant()
        elif key == 't':
            # Attempt to till the soil at the player's position
            self.controller.till_soil()
        elif key == 'u':
            # Attempt to untill the soil at the player's position
            self.controller.untill_soil()
            
        elif key == 'Button-1':
        #Left click on inventory item
            clicked_item = self.inventory.get_clicked_item(event.x, event.y)

            if clicked_item:
                self.controller.set_selected_item(clicked_item)
    
        # Handle buy and sell button presses if needed
        if key == 'Button-2':
            # Right click
            if self.inventory.is_buy_button_clicked(event.x, event.y):
                self.controller.buy_selected_item()
            elif self.inventory.is_sell_button_clicked(event.x, event.y):
                self.controller.sell_selected_item()
            
        self.update_view()
    def select_item(self, item_name: str):
        self.selectec_item = item_name
        self.view.redraw()

    def buy_item(self, item_name: str):
        if item_name in BUY_PRICES and self.player.money >= BUY_PRICES[item_name]:
            self.player.buy_item(item_name, BUY_PRICES[item_name])
            self.view.redraw()

    def sell_item(self, item_name: str):
        if item_name in SELL_PRICES and self.player.get_item_quantity(item_name) > 0:
            self.player.sell_item(item_name, SELL_PRICES[item_name])
        self.view.redraw()

def play_game(root: tk.Tk, map_file: str):
    controller = FarmGame(root, map_file)
    root.mainloop()
    return None

def main() -> None:
    """constructing the root to Tk instance"""
    root = tk.Tk()
    """calling the play_game function and passing in the newly created root instance"""
    play_game(root, 'maps/map1.txt')
    return None

if __name__ == '__main__':
    root = tk.Tk()
    app = FarmGame(root)
    root.mainloop()

