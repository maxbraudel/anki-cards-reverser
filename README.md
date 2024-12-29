# Anki Cards Reverser

An Anki addon that allows users to dynamically switch between normal (front to back) and reversed (back to front) card order while studying, without modifying the original cards.

## Features

- Toggle between normal and reversed card order on the fly
- Visual indicator showing when cards are in reversed mode
- Seamless integration with Anki's interface
- Support for both normal cards and "type the answer" cards
- No modification to your original cards or note types
- Clean and intuitive user interface

## Technologies Used

- Python
- Anki Add-on API
- Qt for the user interface (via PyQt)
- HTML/CSS for card templates

## Installation

1. Download the `cards-reverser.ankiaddon` file from the `/Addon File/` folder
2. Open Anki
3. Navigate to Tools > Add-ons
4. Click "Install from File..."
5. Select the downloaded `cards-reverser.ankiaddon` file
6. Restart Anki

## Card Template Setup

### For Basic Cards (Normal)

1. Navigate to: Tools > Manage Note Types 
2. Select "Basic"
3. Click "Fields..." and ensure you have the following fields:
   - Front
   - Back
   - Hint
4. Click "Cards"
5. Replace the templates with the provided files from `/Card templates/Normal/`:
   - Front Template
   - Back Template
   - Styling (CSS)

### For Type the Answer Cards

1. Follow the same steps as above but use templates from `/Card templates/Type the Answer/`

## Usage

1. A new menu "Card Order" will appear in the Anki menu bar
2. Choose between:
   - "Normal (Front > Back)" - standard front to back order
   - "Reversed (Back > Front)" - reversed back to front order
3. A green indicator will appear when in reversed mode

## License

This addon is released under the [MIT License](LICENSE).

Copyright 2024 [Max Braudel](https://github.com/maxbraudel)