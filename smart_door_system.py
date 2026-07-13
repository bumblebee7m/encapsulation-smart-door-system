class Staff:
    def __init__(self, s_name: str, access_code: str):
        self.s_name = s_name
        self.access_code = access_code 

    @property
    def access_code(self) -> str:
        authorized = True  
        if authorized:
            return self.__access_code
        else:
            raise PermissionError("Access Denied: You are not authorized to view this code.")

    @access_code.setter
    def access_code(self, new_code: str):
        if not isinstance(new_code, str):
            raise TypeError("Access code must be a string.")
        
        if len(new_code) < 4:
            raise ValueError("Update Failed: Access code must be at least 4 characters long.")
            
        self.__access_code = new_code
        print(f"[System]: Access code for {self.s_name} successfully updated.")

    def display_info(self):
        print("\n--- Staff Information ---")
        print(f"Staff Name : {self.s_name}")
        print(f"Access Code: {self.access_code}")
        print("-------------------------\n")


if __name__ == "__main__":
    print("--- Initializing Staff ---")
    staff1 = Staff("Kofi Mensah", "A1b2C3d4")
    staff1.display_info()

    print("--- Attempting Invalid Update (Too Short) ---")
    try:
        staff1.access_code = "123"
    except ValueError as e:
        print(f"Error: {e}")

    print("\n--- Attempting Valid Update ---")
    staff1.access_code = "SecurePass2026"
    
    staff1.display_info()