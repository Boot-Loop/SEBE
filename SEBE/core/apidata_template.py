
## to create python dictionary for jsonresponse
## this dosen't contain status code only the body
class ApiDataTemplate:

    STATUS_INFO    = 'info'
    STATUS_SUCCESS = 'success'
    STATUS_ERROR   = 'error'

    def __init__(self, message="", status=STATUS_SUCCESS ):
        self.data = {
            'status' : status,
            'message': message,
        }
    
    def as_dict(self):
        return self.data
    