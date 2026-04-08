from aethryx_testing.redteam.engine import run_full_redteam
from aethryx_testing.scenarios.agent_failures import (
    run_agent_failure_scenarios,
    run_advanced_scenarios
)

def run_all_tests(agent):
    return {
        "redteam": run_full_redteam(agent),
        "agent_failures": run_agent_failure_scenarios(agent),
        "advanced": run_advanced_scenarios(agent)
    }
