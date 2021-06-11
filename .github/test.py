# content of test_sample.py
def inc(x):
    return x + 1


def test_answer():
    assert inc(3) == 5


# def model_regression():
#     model = getModel()
#     regression_examples = []
#     regression_output = []
#     for example, output in zip(regression_examples, regression_output):
#         assert(model.forward(regression_examples) == regression_output)