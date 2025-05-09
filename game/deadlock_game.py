import matplotlib.pyplot as plt
import os


class DeadlockGame:
    def __init__(self, betrayal_penalty=True):
        self.payoff_matrix = {
            ("Cooperate", "Cooperate"): (3, 3),
            ("Cooperate", "Defect"): (-1, 5),
            ("Defect", "Cooperate"): (5, -1),
            ("Defect", "Defect"): (1, 1),
        }
        self.history = []
        self.betrayal_penalty = betrayal_penalty

    def play(self, action1, action2):
        outcome = (action1, action2)
        reward = self.payoff_matrix.get(outcome, (0, 0))

        # Optional extra penalty for betrayal (adds complexity)
        if self.betrayal_penalty:
            if outcome == ("Cooperate", "Defect"):
                reward = (reward[0] - 1, reward[1])
            elif outcome == ("Defect", "Cooperate"):
                reward = (reward[0], reward[1] - 1)

        self.history.append((action1, action2, reward))
        return reward

    def evaluate(self):
        p1_scores = [r[2][0] for r in self.history]
        p2_scores = [r[2][1] for r in self.history]

        p1_actions = [r[0] for r in self.history]
        p2_actions = [r[1] for r in self.history]

        mutual_coop = sum(1 for r in self.history if r[0] == r[1] == "Cooperate")
        mutual_defect = sum(1 for r in self.history if r[0] == r[1] == "Defect")
        betrayals = sum(1 for r in self.history if r[0] != r[1])

        return {
            "rounds": len(self.history),
            "P1_avg": sum(p1_scores) / len(p1_scores),
            "P2_avg": sum(p2_scores) / len(p2_scores),
            "P1_coop_rate": p1_actions.count("Cooperate") / len(p1_actions),
            "P2_coop_rate": p2_actions.count("Cooperate") / len(p2_actions),
            "mutual_cooperation": mutual_coop,
            "mutual_defection": mutual_defect,
            "betrayals": betrayals,
            "history": self.history,
        }

    def plot_metrics(self, eval_data, save_path=None):
        rounds = list(range(1, eval_data["rounds"] + 1))
        p1_rewards = [r[2][0] for r in eval_data["history"]]
        p2_rewards = [r[2][1] for r in eval_data["history"]]

        fig, ax = plt.subplots()
        ax.plot(rounds, p1_rewards, label="Player 1 Reward")
        ax.plot(rounds, p2_rewards, label="Player 2 Reward")
        ax.set_xlabel("Round")
        ax.set_ylabel("Reward")
        ax.set_title("Strategic Deadlock Game: Rewards per Round")
        ax.legend()
        ax.grid(True)
        plt.tight_layout()

        if save_path:
            os.makedirs(os.path.dirname(save_path), exist_ok=True)
            plt.savefig(save_path)
            plt.close(fig)  # prevent GUI pop-up in notebooks/servers
        else:
            return fig
