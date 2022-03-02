import io
import logging

def log_model_summary(model):
    with io.StringIO() as stream:
        model.summary(a = lambda x: stream.write(f'{x}\n') )
        summary_str = stream.getvalue()
    return summary_str