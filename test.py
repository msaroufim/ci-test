# content of test_sample.py
class TestClass:
    def inc(self,x):
        return x + 1

    def test_answer(self):
        assert self.inc(3) == 5


# def model_regression():
#     model = getModel()
#     regression_examples = s[]
#     regression_output = []
#     for example, output in zip(regression_examples, regression_output):
#         assert(model.forward(regression_examples) == regression_output)