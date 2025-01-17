class Updates:
    def __init__(self, update_data):
        self.update_id = update_data['result'][-1]['update_id'],
        self.message = update_data['result'][-1]['message']['text']
    def __str__(self):
        return f"Update ID: {self.update_id}\nMessage: {self.message}"
    

     
    

    
