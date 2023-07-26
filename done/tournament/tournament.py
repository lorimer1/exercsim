HEADER = "Team                           | MP |  W |  D |  L |  P"
NAME_WIDTH = 31
VALUE_WIDTH = 3
TEAM_DATA_DICT = {"MP": 0, "W": 0, "D": 0, "L": 0, "P": 0}


def tally(rows: list) -> list:
    if not rows:
        return [HEADER]

    teams_set = set()
    teams = dict()
    games = []

    for row in rows:
        game = row.split(";")
        games.append(game)
        teams_set.add(game[0])
        teams_set.add(game[1])

    for team in teams_set:
        teams[team] = TEAM_DATA_DICT.copy()

    for game in games:
        team1, team2, outcome = game[0], game[1], game[2]
        teams[team1]["MP"] += 1
        teams[team2]["MP"] += 1
        if outcome == "win":
            teams[team1]["W"] += 1
            teams[team2]["L"] += 1
            teams[team1]["P"] += 3
        elif outcome == "loss":
            teams[team2]["W"] += 1
            teams[team1]["L"] += 1
            teams[team2]["P"] += 3
        elif outcome == "draw":
            teams[team1]["D"] += 1
            teams[team2]["D"] += 1
            teams[team1]["P"] += 1
            teams[team2]["P"] += 1

    sorted_teams = dict(
        sorted(teams.items(), key=lambda item: (-item[1]["P"], item[0]))
    )
    result = [
        f'{k:<{NAME_WIDTH}}|{v["MP"]:>{VALUE_WIDTH}} |{v["W"]:>{VALUE_WIDTH}} |{v["D"]:>{VALUE_WIDTH}} |{v["L"]:>{VALUE_WIDTH}} |{v["P"]:>{VALUE_WIDTH}}'
        for k, v in sorted_teams.items()
    ]

    return [HEADER] + result


if __name__ == "__main__":
    results = ["Allegoric Alaskans;Blithering Badgers;win"]
    print(tally(results))
