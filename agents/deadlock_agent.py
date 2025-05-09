from autogen import ConversableAgent


class DeadlockAgent(ConversableAgent):
    def __init__(self, name, llm_config):
        super().__init__(
            name=name,
            system_message="You are a player in the Deadlock Game. Respond only with 'Cooperate' or 'Defect'.",
            llm_config=llm_config,
        )

    def generate_action(self, messages):
        reply = self.generate_reply(messages)
        content = reply["content"].strip()

        if "Cooperate" in content:
            return "Cooperate"
        elif "Defect" in content:
            return "Defect"
        return "Defect"
