class Phone:

    # Constructor overloading is not directly supported in Python.
    # We can use default arguments to achieve similar behavior.
    def __init__(self, brand=None, model=None, color=None,
                 ram=0, rom=0, btry=0):

        self.brand = brand
        self.model = model
        self.color = color
        self.ram = ram
        self.rom = rom
        self.btry = btry

        # Similar to Java's instance initialization block
        print(self)

    # -----------------------------------------
    # Display object inside the class
    # -----------------------------------------
    def display_obj(self):

        result = "inside class display()\n"

        result += "Brand: " + str(self.brand) + "\n"
        result += "Model: " + str(self.model) + "\n"
        result += "Color: " + str(self.color) + "\n"
        result += "RAM: " + str(self.ram) + "GB\n"
        result += "ROM: " + str(self.rom) + "GB\n"
        result += "Battery: " + str(self.btry) + "mAh\n"
        result += "\n"

        return result

    # -----------------------------------------
    # Similar to Java's toString()
    # -----------------------------------------
    def __str__(self):

        result = "With __str__()\n"

        result += "Brand: " + str(self.brand) + "\n"
        result += "Model: " + str(self.model) + "\n"
        result += "Color: " + str(self.color) + "\n"
        result += "RAM: " + str(self.ram) + "GB\n"
        result += "ROM: " + str(self.rom) + "GB\n"
        result += "Battery: " + str(self.btry) + "mAh\n"
        result += "\n"

        return result


# -----------------------------------------
# Display outside the class
# -----------------------------------------
def display_out(ph):

    result = "outside class display()\n"

    result += "Brand: " + str(ph.brand) + "\n"
    result += "Model: " + str(ph.model) + "\n"
    result += "Color: " + str(ph.color) + "\n"
    result += "RAM: " + str(ph.ram) + "GB\n"
    result += "ROM: " + str(ph.rom) + "GB\n"
    result += "Battery: " + str(ph.btry) + "mAh\n"

    return result


# -----------------------------------------
# main
# -----------------------------------------

p1 = Phone("Google Pixel", "10 pro xl", "gray", 0, 256, 6000)

print(p1.display_obj())

print(display_out(p1))

print(p1)