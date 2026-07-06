class FootballTeam:
    def __init__(self, team_name, coach):
        self.team_name = team_name
        self.coach = coach
        self.players = []

    def add_player(self, name, position, number, age, nationality):
        
        player = {
            "name": name,
            "position": position,
            "number": number,
            "age": age,
            "nationality": nationality

        }
        self.players.append(player)

    def remove_player(self, rem_num):
        for player in self.players:
            if player["number"] == rem_num:
                self.players.remove(player)
                return
    
    def plupdate(self, pl_num, key, value):
        for player in self.players:
            if player["number"] == pl_num:
                player[key] = value
                return
        
    
    def club_info(self):
        print(f"Team Name: {self.team_name}")
        print(f"Coach: {self.coach}")
        print(f"Players Squad: {self.players}")

    def plinfo(self, pl_num):
        for player in self.players:
            if player["number"] == pl_num:
                print(player)
                return

liver = FootballTeam("Liverpool", "Iraola")
liver.add_player("Messi", "forward", 10, 38, "Argentina")
liver.add_player("Ronaldo", "forward", 7, 40, "Portugal")
liver.club_info()
liver.plinfo(10)
liver.plupdate(10, "goal", 1)
liver.plinfo(10)
liver.remove_player(7)
liver.club_info()
