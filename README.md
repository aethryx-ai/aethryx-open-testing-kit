# Aethryx Open Testing Kit

Developer-first toolkit for testing, red-teaming, and evaluating LLMs and AI agents built for **real-world failure scenarios**, not just static benchmarks.


## Why this exists

Most AI evaluation tools focus on:
- Model accuracy
- Static benchmarks

But real-world AI systems fail because of:
- Prompt injection  
- Jailbreaks  
- Agent misuse of tools  
- Multi-step decision failures  
- Data leakage & unsafe autonomy  

**Aethryx focuses on testing AI systems the way they actually break in production.**

## Key Capabilities

### Red Teaming
- Prompt injection attacks
- Jailbreak simulations (dynamic generation)
- Adversarial testing datasets

### Agent Failure Simulation (Core Differentiator)
- Tool misuse scenarios
- Unsafe autonomy detection
- Policy violation testing
- Multi-step failure chains

### Dataset-Driven Evaluation
- Bias datasets
- Hallucination tests
- Financial risk scenarios
- Data leakage simulations

### Risk Scoring
- Vulnerability detection
- Risk classification (LOW / HIGH / CRITICAL)
- Aggregated risk summaries

## Quick Start

```bash
pip install .
python examples/run_all.py
## Quick Start

from aethryx_testing.core.runner import run_all_tests

class Agent:
    def run(self, prompt):
        return "blocked"

results = run_all_tests(Agent())

print(results)
