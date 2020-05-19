# Pokeapi Wrapper Python

<!-- ![Pokeapi](https://raw.githubusercontent.com/PokeAPI/media/master/logo/pokeapi_256.png) -->
<!-- ![Pokeapi](https://img1.gratispng.com/20171220/ofe/pokeball-png-5a3ab8044b97e7.8086813315137976363096.jpg) -->

<a href="https://pokeapi.co/"><img src="https://raw.githubusercontent.com/PokeAPI/media/master/logo/pokeapi_256.png" title="PokeApi" alt="PokeApi"></a>

<!-- <a href="http://fvcproductions.com"><img src="https://avatars1.githubusercontent.com/u/4284691?v=3&s=200" title="FVCproductions" alt="FVCproductions"></a> -->

## Description
A simple **Python** application using **Flask** that simplies the Pokeapi result set when you search for a Pokémon. 

## Motivation
I always loved pokémons and now my babies love them too, so I had to do something about it. 

## Requirements
For development, you will need [Python](https://www.python.org/downloads/release/python-382/) installed in your environement and the modules that are included in the requirements.txt in the root path of the project. 
    
## Installation

### Project
    $ git clone https://github.com/brworkit/pokeapi-wrapper-python.git
    $ cd pokeapi-wrapper-python
    $ pip install -r requirements.txt --user
    
## Usage

Start the server after everything is installed.

## Run server locally
    
    $ export FLASK_APP=app.py _(setting the started file for running this application)_
    $ export FLASK_RUN_PORT=8500 _(setting the port you want the server running)_
    $ export FLASK_ENV=development _(setting the environment)_
    $ flask run (really starts the server)

After running these commands you will see in your prompt

    * Serving Flask app "app.py" (lazy loading)
    * Environment: development
    * Debug mode: on
    * Restarting with stat
    * Debugger is active!
    * Debugger PIN: 593-473-503
    * Running on http://127.0.0.1:8500/ (Press CTRL+C to quit)


## API

### GET /pokemons/<id>
    {
        "result": {
            "id"
            "order"
            "name":
            "weight"
            "height"
            "color"
            "base_experience"
            "image"
            "types": [
                {
                    "name"
                    "color"
                }
            ],
            "abilities": [
                {
                    "name"
                }
            ]
        }
    }

### GET /pokemons/<id>/sprites
    {
        "result": {
            "back_default"
            "back_shiny"
            "front_default"
            "front_shiny"
        }
    }

## Contributing
[PokeApi](https://pokeapi.co/) with their awesome set of data.  

## License
[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org)
[MIT License.](https://opensource.org/licenses/MIT)    
Copyright (c) 2020 **brworkit**.
