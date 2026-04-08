from aethryx_testing.redteam.prompt_attacks import run_prompt_attacks
from aethryx_testing.redteam.jailbreaks import run_jailbreaks


def run_all_tests(model):
    results = {}

    results["prompt_attacks"] = run_prompt_attacks(model)
    results["jailbreaks"] = run_jailbreaks(model)

    return results
