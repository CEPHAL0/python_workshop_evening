# Useful Dunder Method
# __repr__, __str__


class Bird:
    # Constructor Method
    def __init__(self, c, w, mb, nh):
        self.color = c
        self.weight = w
        self.migration_behavior = mb
        self.native_homeland = nh

    def __repr__(self):
        output = f"""
        ---------------------
            Color: {self.color}
            Weight: {self.weight}
            Migration Behavior: {self.migration_behavior}
            Native Homeland: {self.native_homeland}
        ---------------------
        """
        return output


pigeon = Bird("Gray", 3, "S2S", "Asia")
danfe = Bird("Red", 4, "North to North", "Nepal")
print(pigeon)
print(danfe)
