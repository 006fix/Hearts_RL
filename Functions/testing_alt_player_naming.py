
def test_alt_players(player1, player2, player3, player4):

    varp1a1 = player1.alt_player1
    varp1a2 = player1.alt_player2
    varp1a3 = player1.alt_player3

    varp2a1 = player2.alt_player1
    varp2a2 = player2.alt_player2
    varp2a3 = player2.alt_player3

    varp3a1 = player3.alt_player1
    varp3a2 = player3.alt_player2
    varp3a3 = player3.alt_player3

    varp4a1 = player4.alt_player1
    varp4a2 = player4.alt_player2
    varp4a3 = player4.alt_player3

    print(f"For player 1, alt players 1,2,3 are {varp1a1}, {varp1a2}, {varp1a3}")
    print(f"For player 2, alt players 1,2,3 are {varp2a1}, {varp2a2}, {varp2a3}")
    print(f"For player 3, alt players 1,2,3 are {varp3a1}, {varp3a2}, {varp3a3}")
    print(f"For player 4, alt players 1,2,3 are {varp4a1}, {varp4a2}, {varp4a3}")
