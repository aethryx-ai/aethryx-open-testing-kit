from aethryx_testing.core.runner import run_all_tests

def mock_model(prompt):
    return "I cannot comply with that request"

results = run_all_tests(mock_model)

print(results)
