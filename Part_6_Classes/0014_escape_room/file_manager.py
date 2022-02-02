class FileManager:
    """
    Class to implement file access to store inventory if
    power lost or reset to maintain persistence
    """

    def write_inventory_file(self, inventory_item):
        """
        Method to write inventory item to inventory file upon picking it up
        """
        try:
            with open('inventory', 'w') as file:
                file.write(inventory_item)
        except OSError:
            pass

    def read_inventory_file(self):
        """
        Method to read inventory file and return its contents

        Return:
            str
        """
        try:
            with open('inventory', 'r') as file:
                inventory = file.read()
                return inventory
        except OSError:
            pass

    def clear_inventory_file(self):
        """
        Method to clear inventory file after winning a game
        """
        try:
            with open('inventory', 'w') as file:
                file.write('')
        except OSError:
            pass
