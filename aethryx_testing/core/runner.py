from aethryx_testing.redteam.prompt_attacks import run_prompt_attacks

def run_all_tests(model):
    results = {}
    results["prompt_attacks"] = run_prompt_attacks(model)
    return results
