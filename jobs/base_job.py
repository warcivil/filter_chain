class RootJob:
    def __init__(self, dataset_object):
        self.dataset_object = dataset_object
        self.next_modifier = None

    def set_dataset_object(self, dataset_object):
        self.dataset_object = dataset_object

    def add_modifier(self, modifier):
        if self.next_modifier:
            self.next_modifier.add_modifier(modifier)
        else:
            self.next_modifier = modifier

    def handle(self):
        if self.next_modifier:
            self.next_modifier.handle()