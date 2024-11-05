class Player:
    def __init__(self, playerName, playerPosition):
        self.playerName = playerName
        self.playerPosition = playerPosition

    def __str__(self):
        return f"{self.playerName} - ({self.playerPosition})"

class Team:
    def __init__(self, teamName):
        self.teamName = teamName
        self.players = []

    def addPlayer(self, player):
        self.players.append(player)

    def displayTeamAndPlayers(self):
        print(f"Your new Football Team is: 'The {self.teamName}'")
        print()
        print(f"Your players are: \n")
        for player in self.players:
            print(player)


quarterBack = Player("Joe Montana", "QB")
runningBack = Player("Barry Sanders", "RB")
wideReceiver = Player("Jerry Rice", "WR")
kicker = Player("Graham Gano", "K")

playerList = [quarterBack, runningBack, wideReceiver, kicker]

gatorsTeam = Team("Florida Gators")

def addPlayerToTeam():
    for player in playerList:
        gatorsTeam.addPlayer(player)

addPlayerToTeam()

gatorsTeam.displayTeamAndPlayers()


