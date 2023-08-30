# pokemon-soothing-silver-shiny-modifier

A modified version of [choogiesaur](https://github.com/choogiesaur)'s [hgss-shiny-modifier](https://github.com/choogiesaur/hgss-shiny-modifier). This changes the Shiny Pokémon encounter rate in the Pokémon SoothingSilver Nintendo DS ROM hack of Pokémon SoulSilver. Please look at the original for more information.

## Dependencies:
Requires **Python3** and the **ndspy** Python library. Install ndspy with pip:

```bash
pip install ndspy
```

## Usage:
1. Place your `.nds` file (the game ROM) in the same folder as the `shiny_rate_editor.py` script.
2. Run the script from your terminal, replacing `<filename>` with the name of your `.nds` file and `<new_shiny_rate>` with your preferred shiny encounter rate. The shiny encounter rate should be a hexadecimal value between `0x0` and `0xFF`. The default for Pokémon SoothingSilver is 0x20, producing a shiny rate of 32/65536.

```bash
# Arguments in [square brackets] are optional
python shiny_rate_editor.py <filename> [<new_shiny_rate>]
```

For example, if you have a file named `pokemon.nds` and you want to set the Shiny encounter rate to `0xFF` (1/256, the maximum), you would use:

```bash
python shiny_rate_editor.py pokemon.nds 0xFF
```

If you don't provide a new shiny rate, the script will use a default value of `0xFF`.

3. The script will create a new modified game ROM file called `shiny_rate_patched.nds`. Use your method of choice to play the edited game ROM file.

## License:
This project is licensed under the terms of the MIT license.
