import random
from agents.deadlock_agent import DeadlockAgent
from game.deadlock_game import DeadlockGame


def run_deadlock_match(agent1, agent2, rounds=5):
    game = DeadlockGame()
    history = []

    for i in range(rounds):
        msg_to_p1 = [
            {"role": "system", "content": "Round %d. Choose action." % (i + 1)}
        ]
        msg_to_p2 = [
            {"role": "system", "content": "Round %d. Choose action." % (i + 1)}
        ]

        action1 = agent1.generate_reply(msg_to_p1)
        action2 = agent2.generate_reply(msg_to_p2)

        reward = game.play(action1, action2)
        history.append(reward)
    result = game.evaluate()
    game.plot_metrics(
        result,
        save_path=f"results/deadlock_match_{agent1.name}_vs_{agent2.name}.png",
    )
    return result
