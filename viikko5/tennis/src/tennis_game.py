class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name

        self.player1_game_score = 0
        self.player2_game_score = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.player1_game_score = self.player1_game_score + 1
        else:
            self.player2_game_score = self.player2_game_score + 1

    def score_when_tied(self):
        if self.player1_game_score == self.player2_game_score:
            if self.player1_game_score == 0:
                return "Love-All"
            if self.player1_game_score == 1:
                return "Fifteen-All"
            if self.player1_game_score == 2:
                return "Thirty-All"
            if self.player1_game_score == 3:
                return "Forty-All"
            return "Deuce"

    def score_when_chance_to_win_game(self):
        minus_result = self.player1_game_score - self.player2_game_score
        if minus_result == 1:
            return "Advantage player1"
        if minus_result == -1:
            return "Advantage player2"
        if minus_result >= 2:
            return "Win for player1"
        return "Win for player2"

    def score_if_not_tied_and_no_chance_to_win(self):
        score = ""
        temp_score = 0
        for pelaaja in range(1, 3):
                if pelaaja == 1:
                    temp_score = self.player1_game_score
                else:
                    score = score + "-"
                    temp_score = self.player2_game_score

                if temp_score == 0:
                    score = score + "Love"
                elif temp_score == 1:
                    score = score + "Fifteen"
                elif temp_score == 2:
                    score = score + "Thirty"
                elif temp_score == 3:
                    score = score + "Forty"
        return score

    def get_score(self):
        if self.player1_game_score == self.player2_game_score:
            score = self.score_when_tied()

        elif self.player1_game_score >= 4 or self.player2_game_score >= 4:
            score = self.score_when_chance_to_win_game()

        else:
            score = self.score_if_not_tied_and_no_chance_to_win()


        return score
