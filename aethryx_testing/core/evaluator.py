class Evaluator:
    def __init__(self, model_callable):
        self.model = model_callable

    def evaluate(self, test_cases):
        results = []
        for case in test_cases:
            response = self.model(case["input"])
            score = self._score(response, case)
            results.append({
                "input": case["input"],
                "response": response,
                "score": score
            })
        return results

    def _score(self, response, case):
        if "expected" in case:
            return int(case["expected"] in response)
        return 0
