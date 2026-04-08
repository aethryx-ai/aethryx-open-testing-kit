from aethryx_testing.core.runner import run_all_tests

class Agent:
    def run(self, prompt):
        if "approve" in prompt.lower():
            return "executed"
        return "blocked"

def model(prompt):
    return "safe"

print(run_all_tests(Agent()))
