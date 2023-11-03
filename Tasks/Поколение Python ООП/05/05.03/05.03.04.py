from functools import total_ordering

@total_ordering
class Version:
    def __init__(self, version):
        version = (list(map(int, version.split("."))) + [0, 0])[:3]
        self.version = version 
        
    def __repr__(self):
        return f"Version('{'.'.join(map(str, self.version))}')"
    
    def __str__(self):
        return f"{'.'.join(map(str, self.version))}"
    
    def __eq__(self, other):
        if isinstance(other, Version):
            return self.version == other.version
        return NotImplemented
    
    def __lt__(self, other):
        if isinstance(other, Version):
            return self.version < other.version
        return NotImplemented
