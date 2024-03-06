class FormatResponse():
    def success(self, message, data, state_code=200):
       return {
           "message":message,
            "count": len(data) if isinstance(data, list or tuple) else None,
            "status_code":state_code,
            "data":data
       }
    
    def error(self, message, state_code=400):
        return {
           "message":message,
            "status_code":state_code,
       }
