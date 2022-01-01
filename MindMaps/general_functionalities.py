class ParseLearnFunction:
    @staticmethod
    def parse_learn(steps, device, function_name: str):
            with steps.start(f'Learning {function_name}',continue_=True) as step:
                try:
                    return device.learn(function_name).info
                except Exception as e:
                    step.failed('Could not learn it correctly\n{e}'.format(e=e))
                    return None 