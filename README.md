# Smart Door Access System for UMaT

This repository contains a Python implementation of a **Smart Door Access System** designed for UMaT admin staff. The system utilizes Object-Oriented Programming (OOP) concepts, specifically **encapsulation**, to secure sensitive access codes from direct, unauthorized modification.

## Features
- **Encapsulated Attributes**: Uses a public attribute for the staff name (`s_name`) and a private attribute for the access code (`__access_code`).
- **Property Decorators**: Implements `@property` and `@access_code.setter` to manage access code retrieval and updates seamlessly without traditional getter/setter syntax.
- **Validation**: Enforces strict validation (e.g., length checking) before updating any user's access code.

## File Structure
- `smart_door_system.py`: Main class definition and demonstration script.
- `README.md`: Documentation of the system.

## How to Run
Ensure you have Python installed, then run:
```bash
python smart_door_system.py
