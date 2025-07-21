# Patient Registration System

## Objective

Create a command-line interface (CLI) program in Python that allows staff at a medical center to register and manage patient records.


## Functional Requirements:

1. **Main Menu Options**:

   * Register a new patient
   * View all patients
   * Search patient by name or ID
   * Update patient information
   * Delete a patient
   * Exit

2. **Patient Data Structure**:
   Each patient must have:

   * Unique ID (auto-generated)
   * First name (str)
   * Last name (str)
   * Date of birth (YYYY-MM-DD)
   * Gender (M/F/Other)
   * Phone number (validated)
   * Email address (optional, validated)
   * Insurance status (boolean)

3. **Persistence**:

   * Store patient records in a local JSON file (`patients.json`)
   * Load data at startup and save on exit or after any change

4. **Validation**:

   * Ensure required fields are not empty
   * Validate phone number format
   * Prevent duplicate registrations (by full name and DOB)


## Technical Requirements:

* Use **functions** to modularize code
* Use **type hints** throughout
* Use **exception handling** for input errors and file issues
* Organize code for reusability and clarity


## Bonus Features (optional):

* Add appointment scheduling and link appointments to patients
* Export patient list to CSV
* Add search filters (e.g., by insurance status or age range)
* Password protection for CLI access (basic auth)


## Example CLI Interaction:

```
=== Medical Center ===
1. Register new patient
2. View all patients
3. Search for patient
4. Update patient record
5. Delete patient
6. Exit
> 1

-- Register New Patient --
First Name: John
Last Name: Doe
Date of Birth (YYYY-MM-DD): 1985-04-12
Gender (M/F/Other): M
Phone Number: +48123456789
Email (optional): john.doe@example.com
Insurance (yes/no): yes
Patient registered with ID: P00001
```
