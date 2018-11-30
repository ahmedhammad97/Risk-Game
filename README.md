# Risk-Game
Risk is a strategic board game, where two or more players tend to dominate the whole map using their troops.

This project is an online simplified version of the game, we allow only two players in every game, we also skip fortifying step.

At the beginning, the user choose which two agents should play the game from the following options:
- **Human Agent**, where the user plays himself.
- **Passive Agent**, that only deploys, but never attacks.
- **Aggressive Agent**, that takes extreme choices.
- **Nearly Pacifist Agent**, that plays safe moves.
- **Greedy Agent**, that examines all possible moves and play the local best one.
- **A\* Agent**, that runs A* search for every turn to find the best move.
- **Real-time A\* Agent**, that does a search of depth one only.
- **Minimax Agent**, that assumes optimal moves for opponent, and act upon it.

## How it works
The client sends an AJAX request upon starting the game carrying the user choices of map and agents, which is validated by the view module, it then invokes the controller to create the model(`Game`, `Node`, `Agent`..etc.) if it is valid, and asynchronously render the map.

A WebSocket (Django channels) is opened after initial render is complete, allowing the server consumer the send initial random distribution of troops and territories.

The controller keeps track of the game turns, and calls `Deploy` and `Attack` functions for every agent in it's turn.

Rendering the new view after every update in the model, is done by few message passing between client and server consumer, except for the case of **Human Agent**, where the process of message passing is reversed in terms of order.

The controller checks for the winning state after every turn, and terminates the model, and send a winning message in the case of winning.


## Technologies
- Django 2.1.2
- Django Channels 2.1.5
- Jquery 3.3.1

## Screenshots
![ScreenShot1](https://github.com/ahmedhammad97/Risk-Game/blob/master/screenshots/home.png)
![ScreenShot2](https://github.com/ahmedhammad97/Risk-Game/blob/master/screenshots/playingUsa.gif)
![ScreenShot3](https://github.com/ahmedhammad97/Risk-Game/blob/master/screenshots/WinningEgypt.gif)
