class CreateUomController():
    
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def save(self, uom_name, is_active, is_deleted):
        self.model.save(uom_name, is_active, is_deleted)

    def update(self, uom_name, is_active, is_deleted, uom_id):
        self.model.update(uom_name, is_active, is_deleted, uom_id)

    def uom_list(self, parent):
        self.model.uom_list(parent)