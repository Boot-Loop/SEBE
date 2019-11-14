
class Context:

    def __init__(self):
        self.ctx = dict()
    
    def get_context(self):
        return self.ctx

class FormContext(Context):
    def __init__(self, form, form_template):
        super().__init__()
        self.ctx.update(
            form          = form,
            form_template = form_template,
        )

        