from aethryx_testing.redteam.engine import run_full_redteam
from aethryx_testing.scenarios.agent_failures import (
    run_agent_failure_scenarios,
    run_advanced_scenarios
)


def run_all_tests(agent):
    results = {}

    results["redteam"] = run_full_redteam(agent)
    results["agent_failures"] = run_agent_failure_scenarios(agent)
    results["advanced"] = run_advanced_scenarios(agent)

    return results
