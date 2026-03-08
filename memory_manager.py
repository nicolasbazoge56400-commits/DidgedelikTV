class MemoryManager:
    def __init__(self):
        self.memory = {}
        self.context = None

    def add_to_memory(self, key, value):
        """Add a value to the memory with the associated key."""
        self.memory[key] = value

    def get_from_memory(self, key):
        """Retrieve a value from memory using the key."""
        return self.memory.get(key, None)

    def set_context(self, context):
        """Set the current context for the conversation."""
        self.context = context

    def get_context(self):
        """Retrieve the current context."""
        return self.context

    def clear_memory(self):
        """Clear the entire memory store."""
        self.memory.clear()
        self.context = None

    def memory_dump(self):
        """Return a full dump of memory for debugging purposes."""
        return self.memory