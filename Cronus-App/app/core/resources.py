class ResourceManager:
    def __init__(self):
        self.resources = {}

    def add_resource(self, resource_type: str, amount: int):
        if resource_type in self.resources:
            self.resources[resource_type] += amount
        else:
            self.resources[resource_type] = amount

    def allocate_resource(self, resource_type: str, amount: int):
        if resource_type in self.resources and self.resources[resource_type] >= amount:
            self.resources[resource_type] -= amount
            return True
        return False
