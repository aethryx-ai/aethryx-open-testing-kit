from aethryx_testing.redteam.prompt_attacks import run_prompt_attacks
from aethryx_testing.redteam.jailbreaks import run_jailbreaks

def run_full_redteam(model):
    pa = run_prompt_attacks(model)
    jb = run_jailbreaks(model)

    total = len(pa) + len(jb)
    high = sum(1 for x in pa+jb if x.get("risk")=="HIGH")

    return {
        "prompt_attacks": pa,
        "jailbreaks": jb,
        "summary": {
            "total": total,
            "high_risk": high,
            "risk_percent": round(high/total*100,2) if total else 0
        }
    }
