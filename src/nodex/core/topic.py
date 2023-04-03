import json

class Topic:
    name = ""
    description = ""
    id = -1

    def __init__(self, topic_name):
        topic_file = f"topics/{topic_name}.topic"
        with open(topic_file) as f:
            topic_data = json.load(f)
            self.name = topic_data.get("name")
            self.description = topic_data.get("description")
            self.id = topic_data.get("id")

    def __str__(self):
        return f"Topic(name={self.name}, description={self.description}, id={self.id})"
        
        
        

