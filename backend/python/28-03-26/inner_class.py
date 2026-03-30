# Defining the outer class 'computer'
# This class acts as a primary container for the computer's general properties and its inner components.
class computer:
    
    # The __init__ constructor method for the outer 'computer' class
    # It accepts arguments to initialize both the computer itself and its internal parts. 
    def __init__(self, name, age, type, generation):
        # Assigning the passed 'name' (e.g., "8gb") to the outer instance variable
        self.name = name
        # Assigning the passed 'age' (e.g., "256gb") to the outer instance variable
        self.age = age
        
        # Creating an object of the inner 'Processor' class directly *inside* the outer class's constructor!
        # It immediately forwards the 'type' and 'generation' arguments into the inner class's constructor.
        self.processor = self.Processor(type, generation)
        
    # An instance method for the outer 'computer' class meant to display its total configuration
    def displayConfig(self):
        # Step 1: Prints out the outer class's own direct attributes (name and age)
        print(f"Computer Name: {self.name}, Age: {self.age}")
        
        # Step 2: Calls the inner class's completely separate displayConfig() method using the object created previously
        # This effectively delegates the task of printing processor details exclusively to the Processor object itself!
        self.processor.displayConfig()

    # --- INNER CLASS DEFINITION ---
    # Defining an inner class named 'Processor' strictly nested inside the 'computer' class.
    # This structurally represents a strong "Has-A" relationship: A Computer *has a* Processor.
    class Processor:
        
        # The constructor method solely for the inner 'Processor' class
        # It handles initializing only processor-specific attributes independent of the full computer
        def __init__(self, type, generation):
            # Assigning the processor's type (e.g., "Intel")
            self.type = type
            # Assigning the processor's generation (e.g., "12th Gen")
            self.generation = generation

        # An instance method living inside the inner 'Processor' class
        def displayConfig(self):
            # Prints out the inner processor's specific encapsulated attributes
            print(f"Processor Type: {self.type}, Generation: {self.generation}")

# --- Object Creation and Execution ---

# Creating a 'computer' object named comp1.
# Notice how we pass all arguments simultaneously to the outer class ("8gb", "256gb", "Intel", "12th Gen").
# The outer class logically catches them, keeps the first two, and forwards "Intel" and "12th Gen" inward!
comp1 = computer("8gb", "256gb", "Intel", "12th Gen")

# Calling the display method securely on the outer class object.
# This single call cascadingly triggers both the outer print, AND the inner print consecutively.
comp1.displayConfig()

# --- Example 2: Car and Engine (Composition) ---
# Defining an outer class 'Car'
class Car:
    # Outer class constructor taking brand, model, and engine specifics
    def __init__(self, brand, model, engine_type, fuel_capacity, mileage):
        # Setting outer class attributes
        self.brand = brand
        self.model = model
        
        # Creating an instance of the inner 'Engine' class and passing the engine details to it
        self.engine = self.Engine(engine_type, fuel_capacity, mileage)
        
    # Outer method to display the car's general details
    def show(self):
        print(f"Brand: {self.brand}, Model: {self.model}")

    # Inner class 'Engine' tightly coupled to the 'Car' wrapper
    class Engine:
        # Inner constructor defining properties unique to an Engine
        def __init__(self, engine_type, fuel_capacity, mileage):
            self.engine_type = engine_type
            self.fuel_capacity = fuel_capacity
            self.mileage = mileage
            
        # Inner method to display the engine's specifics
        def show(self):
            print(f"Engine Type: {self.engine_type}, Fuel Capacity: {self.fuel_capacity}, Mileage: {self.mileage}")

# Instantiating the Car object which automatically creates its own Engine object internally
car1 = Car("Toyota", "Camry", "Petrol", "50L", "20kmpl")
# Calling the outer class method
car1.show()
# Directly accessing the inner 'engine' object and calling its specific method
car1.engine.show()


# --- Example 3: University and College ---
# Defining an outer class 'University'
class University:
    # Outer class constructor taking details for both the University and the specific College
    def __init__(self, name, location, college, cetcode, type, no_of_students):
        self.name = name
        # [FIXED ERROR]: The 'location' argument wasn't being saved to the instance variable in the original code!
        self.location = location 
        
        # Initializing the inner 'College' class by forwarding all the granular details inward
        self.college = self.College(name, location, college, cetcode, type, no_of_students)
        
    # Outer method to display University details
    def info(self):
        # Now self.location correctly exists and will not throw an AttributeError
        print(f"\nUniversity Name: {self.name}, Location: {self.location}")
        # Delegating the rest of the display task to the inner College object
        self.college.info()
        
    # Inner class 'College' representing a specific college under the University umbrella
    class College:
        # Inner constructor setting up college-specific attributes
        def __init__(self, name, location, college, cetcode, type, no_of_students):
            self.name = name
            self.location = location
            self.college = college
            self.cetcode = cetcode
            self.type = type
            # [FIXED ERROR]: The 'no_of_students' argument wasn't being saved in the original code!
            self.no_of_students = no_of_students 
            
        # Inner method to display College details
        def info(self):
            # Now self.no_of_students correctly exists and can be printed safely
            print(f"College Details -> Name: {self.name}, Location: {self.location}, College: {self.college}, Cetcode: {self.cetcode}, Type: {self.type}, No of Students: {self.no_of_students}")

# Creating a 'University' object 'coll'. (Providing dummy data)
coll = University("Vtu", "Aicte", "AIT", "12345", "Private", "1000")
# Calling the outer object's info() method, which correctly cascades into the College's info() method
coll.info()