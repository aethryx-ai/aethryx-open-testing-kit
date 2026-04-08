from aethryx_testing.redteam.prompt_attacks import run_prompt_attacks
from aethryx_testing.redteam.jailbreaks import run_jailbreaks
from aethryx_testing.core.risk import score_to_numeric


def run_full_redteam(model):
    prompt_results = run_prompt_attacks(model)
    jailbreak_results = run_jailbreaks(model)

    all_results = prompt_results + jailbreak_results

    total = len(all_results)
    risk_score = sum(score_to_numeric(r["risk"]) for r in all_results)

    avg_risk = round(risk_score / total, 2) if total else 0

    return {
        "prompt_attacks": prompt_results,
        "jailbreaks": jailbreak_results,
        "summary": {
            "total_tests": total,
            "aggregate_score": risk_score,
            "average_risk_score": avg_risk
        }
    }
