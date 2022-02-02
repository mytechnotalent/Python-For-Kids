class FileManager:
    """
    Class to implement file access to store inventory if
    power lost or reset to maintain persistence
    """
    def write_inventory_file(self, inventory_item):
        """
        Method to write inventory item to inventory file upon picking it up

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
                inventory = file.read()
                return inventory
        except OSError:
            return False

    def clear_inventory_file(self):
        """
        Method to clear inventory file after winning a game

        Returns:
            bool
        """
        try:
            with open('inventory', 'w') as file:
                file.write('')
                return True
        except OSError:
            return False
