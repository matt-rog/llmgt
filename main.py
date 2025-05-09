from runner.experiment_runner import run_deadlock_match
from agents.deadlock_agent import DeadlockAgent

if __name__ == "__main__":
    llm_config = {
        "model": "gpt-3.5-turbo",  # or any LLM adapter AutoGen supports
        "temperature": 0.7,
    }

    agent1 = DeadlockAgent(name="Alice", llm_config=llm_config)
    agent2 = DeadlockAgent(name="Bob", llm_config=llm_config)

    result = run_deadlock_match(agent1, agent2, rounds=10)
    print("Experiment Result:", result)
