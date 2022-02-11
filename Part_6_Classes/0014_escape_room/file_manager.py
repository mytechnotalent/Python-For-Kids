class FileManager:
    """
    Class to implement file access to store inventory to maintain persistence
    """

    def __init__(self):
        self.inventory = ''

    @staticmethod
    def clear_inventory_file():
        """
        Static method to clear inventory file after winning a game

        Returns:
            bool
        """
        try:
            with open('inventory', 'w') as file:
                file.write('')
                return True
        except OSError:
            return False

    @staticmethod
    def write_inventory_file(inventory_item):
        """
        Static method to write inventory item to inventory file upon picking it up

        Params:
            inventory_item: str
    
        Returns:
            bool
        """
        try:
            with open('inventory', 'w') as file:
                file.write(inventory_item)
                return True
        except OSError:
            return False

    def read_inventory_file(self):
        """
        Method to read inventory file and return its contents

        Return:
            str or bool
        """
        try:
            with open('inventory', 'r') as file:
                self.inventory = file.read()
                return self.inventory
        except OSError:
            return False
