class Evaluator:
    def __init__(self, model):
        self.model = model

    def evaluate(self, tests):
        results = []
        for t in tests:
            res = self.model(t["input"])
            results.append({"input": t["input"], "response": res})
        return results
