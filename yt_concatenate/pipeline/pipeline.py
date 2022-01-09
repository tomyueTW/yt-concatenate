from yt_concatenate.pipeline.steps.step import StepException

class Pipeline:
    def __init__(self, steps):
        self.steps = steps

    def run(self, inputs):
        data = None
        for step in self.steps:
            try:
                print(step.process(data, inputs))
            except StepException as err:
                print(f'Exception happened: {err}')
                break