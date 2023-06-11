<h2>

```
                            ____     __       __  
     ____  ___  ____  ___  / __/__  / /______/ /_ 
    / __ \/ _ \/ __ \/ _ \/ /_/ _ \/ __/ ___/ __ \
   / /_/ /  __/ /_/ /  __/ __/  __/ /_/ /__/ / / /
  / .___/\___/ .___/\___/_/  \___/\__/\___/_/ /_/ 
 /_/        /_/                                   
```

</h2>

## 📜 My attempt to replicate the [neofetch](https://github.com/dylanaraps/neofetch) in python  

# 🔧 Installation

First of all, install these dependencies:

```bash
pip3 install colored requests
```

Now clone the repository:  

```bash
git clone https://github.com/PepeBigotes/pepefetch
```

Congrats! you are now ready to execute `main.py` to use the tool:  

```bash
cd pepefetch && py -3 main.py
```

## 🖌 Customization

You can easily customize and configure this tool through the next files:

- `config.py`: Configuration file to set parameters like colors, symbols, custom variables, formats, etc.  
- `infos.py`: Script that calls all the info() functions so you can easily reorder or enable/disable these 'infos' as you like. You can also put your own prints here.  
