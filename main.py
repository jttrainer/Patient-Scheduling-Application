from Patient import Patient
from PatientRepository import PatientRepoLinkedList
from Schedule import ScheduleLinkedList
from Schedule import WaitListQueue
from datetime import datetime
import tkinter
from tkinter import ttk
from tkinter import messagebox


if __name__ == '__main__':
    # Instantiate data structures
    patient_repo = PatientRepoLinkedList()
    schedule = ScheduleLinkedList()
    wait_list = WaitListQueue()

    # Seed data
    test_patient_1 = Patient("Jackson", "Trainer", datetime(1988, 3, 29), "Male")
    test_patient_2 = Patient("Heather", "Apple", datetime(1988, 12, 12), "Female")
    test_patient_3 = Patient("Nate", "Tatar", datetime(1994, 3, 30), "Male")
    test_patient_4 = Patient("Barry", "Closer", datetime(1986, 10, 5), "Non-Binary")
    test_patient_5 = Patient("Jake", "Apple", datetime(1986, 9, 29), "Male")

    # Add seed data to patient repository
    patient_repo.add_item(test_patient_1)
    patient_repo.add_item(test_patient_2)
    patient_repo.add_item(test_patient_3)
    patient_repo.add_item(test_patient_4)
    patient_repo.add_item(test_patient_5)

    # Add seed data to schedule
    schedule.add_item(2, test_patient_1)
    schedule.add_item(10, test_patient_2)
    schedule.add_item(5, test_patient_3)
    schedule.add_item(1, test_patient_4)
    schedule.add_item(6, test_patient_5)

    # Add seed data to wait list
    wait_list.enqueue(test_patient_1)

    # Used to generate GUI and display wait list queue
    def display_schedule():
        # Generate empty list to hold the schedule
        schedule_list = []

        # Add items to schedule list for use in displaying on screen
        for k in range(schedule.max_size):
            if schedule.get(k):
                schedule_list.append(f"{str(schedule.get(k))}")

        # Schedule View
        schedule_frame = tkinter.LabelFrame(frame, text="Schedule")
        schedule_frame.grid(row=1, column=0, padx=30, pady=15, sticky="w")

        # Generate and format the text to display on the screen
        incrementer = 0
        for t in schedule_list:
            tkinter.Label(schedule_frame, text="● " + time_slot_switch(incrementer) + ": " + t).grid(row=incrementer,
                                                                                                     column=0,
                                                                                                     sticky="w")
            incrementer += 1
        # Format list to be easier to read
        for i in schedule_frame.winfo_children():
            i.grid_configure(padx=10, pady=5)

    # Used to generate GUI and display wait list queue
    def display_wait_list():
        # Wait List View
        wait_list_frame = tkinter.LabelFrame(frame, text="Wait List")
        wait_list_frame.grid(row=1, column=1, padx=30, pady=15, sticky="w")

        for n in range(wait_list.max_size):
            if n < len(wait_list.items):
                tkinter.Label(wait_list_frame, text=f"{n + 1}: {wait_list.items[n]}").grid(row=n, column=0, sticky="w")
            else:
                tkinter.Label(wait_list_frame, text=f"{n + 1}: Open").grid(row=n, column=0, sticky="w")

        # Format list to be easier to read
        for i in wait_list_frame.winfo_children():
            i.grid_configure(padx=10, pady=5)

    # Calls search function from Schedule DS to verify if patient exists. If so the display patient info
    # window is opened.
    def patient_search():
        if not patient_repo.search(patient_repo.head, last_name_entry.get(), first_name_entry.get()):
            tkinter.messagebox.showwarning(title="Patient Not Found", message="No patient was found with the provided "
                                                                              "information")
        else:
            open_find_patient_win(patient_repo.search(patient_repo.head, last_name_entry.get(),
                                                      first_name_entry.get()))

    # Validates user input for each item and provides appropriate message if error is found.
    def validate_input(first_name: str, last_name: str, dob_month, dob_day, dob_year, sex: str,
                       phone: str, email: str):
        current_year = datetime.today().year
        error_found = False
        valid_sex = {"Male", "Female", "Non-Binary", "Not Listed"}
        if first_name is None or first_name == "":
            messagebox.showinfo("Input Error", "The First Name field cannot be blank")
            error_found = True
        if last_name is None or last_name == "":
            messagebox.showinfo("Input Error", "The Last Name field cannot be blank")
            error_found = True
        if sex not in valid_sex:
            messagebox.showinfo("Input Error", "Please select one of the available Sex options")
            error_found = True
        if dob_month is None or dob_month == "" or int(dob_month) < 1 or int(dob_month) > 12:
            messagebox.showinfo("Input Error", "Month of the year cannot be blank, less than 1 or greater than 12")
            error_found = True
        if dob_day is None or dob_day == "" or int(dob_day) < 1 or int(dob_day) > 31:
            messagebox.showinfo("Input Error", "Day of the month cannot be blank, less than 1 or greater than 31")
            error_found = True
        if dob_year is None or dob_year == "" or int(dob_year) < 1900 or int(dob_year) > current_year:
            messagebox.showinfo("Input Error", f"Month of the year cannot be blank, less than 1900 or greater than "
                                               f"{current_year}")
            error_found = True
        if phone is None or phone == "":
            messagebox.showinfo("Input Error", "The Phone field cannot be blank")
            error_found = True
        if email is None or email == "":
            messagebox.showinfo("Input Error", "The Email field cannot be blank")
            error_found = True
        return error_found

    # Verifies if patient exists in repo before adding to schedule If patient not found warning message is displayed.
    # Validates user input for selected time is correct and if timeslot is open before adding to schedule and
    # refreshing schedule display
    def add_to_schedule():
        if not patient_repo.search(patient_repo.head, last_name_entry.get(), first_name_entry.get()):
            tkinter.messagebox.showwarning(title="Patient Not Found", message="No patient was found with the provided "
                                                                              "information")
        else:
            if schedule_timeslot_combobox.get() is None or schedule_timeslot_combobox.get() == "":
                tkinter.messagebox.showwarning(title="Input Error", message="No timeslot selected. Please try again")
            elif schedule.get(int(schedule_timeslot_combobox.get()) - 1) == "None found":
                schedule.add_item(int(schedule_timeslot_combobox.get()) - 1,
                                  patient_repo.search(patient_repo.head, last_name_entry.get(), first_name_entry.get()))
            else:
                tkinter.messagebox.showwarning(title="Schedule Full", message="The selected time is "
                                                                              "full. Please try again.")
        display_schedule()

    # Verifies if patient exists in repo before adding to wait list. If patient not found warning message is displayed.
    def add_to_wait_list():
        if not patient_repo.search(patient_repo.head, last_name_entry.get(), first_name_entry.get()):
            tkinter.messagebox.showwarning(title="Patient Not Found", message="No patient was found with the provided "
                                                                              "information")
        else:
            if not wait_list.is_full():
                wait_list.enqueue(patient_repo.search(patient_repo.head, last_name_entry.get(), first_name_entry.get()))
            else:
                tkinter.messagebox.showwarning(title="Wait List Full", message="The wait list is full.")
        display_wait_list()

    def remove_from_wait_list():
        # Verifies if queue is empty before removing from wait list and refreshes the wait list display.
        if not wait_list.is_empty():
            wait_list.dequeue()
        else:
            tkinter.messagebox.showwarning(title="Wait List Empty", message="The wait list is empty.")
        display_wait_list()

    def save_new_patient(first_name: str, last_name: str, dob_month, dob_day, dob_year, sex: str,
                         phone: str, email: str, popup_window: tkinter.Toplevel):
        # Calls validation function and if valid save patient to repo
        if not validate_input(first_name, last_name, dob_month, dob_day, dob_year, sex, phone, email):
            dob_combined = datetime(int(dob_year), int(dob_month), int(dob_day))
            create_save_patient = Patient(first_name, last_name, dob_combined, sex, phone, email)
            patient_repo.add_item(create_save_patient)
            popup_window.destroy()

    def time_slot_switch(time_slot: int):
        # Switches int to string for better visual appearance and understanding
        match time_slot:
            case 0:
                return "8:30 - 9:30"
            case 1:
                return "9:30 - 10:00"
            case 2:
                return "10:00 - 10:30"
            case 3:
                return "10:30 - 11:00"
            case 4:
                return "1:30 - 2:00"
            case 5:
                return "2:00 - 2:30"
            case 6:
                return "2:30 - 3:00"
            case 7:
                return "3:00 - 3:30"
            case 8:
                return "3:30 - 4:00"
            case 9:
                return "4:00 - 4:30"
            case 10:
                return "4:30 - 5:00"
            case default:
                return "Not available"

    def open_new_patient_win():
        # Create the GUI framework for pop out window
        new = tkinter.Toplevel()
        new.title("Create New Patient")
        new.minsize(600, 300)

        # This is the create patient section
        create_patient_frame = tkinter.LabelFrame(new, text="Create Patient")
        create_patient_frame.grid(row=0, column=0, padx=40, pady=30)

        # First name GUI label and data entry
        create_first_name_label = tkinter.Label(create_patient_frame, text="First Name:")
        create_first_name_label.grid(row=0, column=0)
        create_first_name_entry = tkinter.Entry(create_patient_frame)
        create_first_name_entry.grid(row=0, column=1)

        # Last name GUI label and data entry
        create_last_name_label = tkinter.Label(create_patient_frame, text="Last Name:")
        create_last_name_label.grid(row=0, column=2)
        create_last_name_entry = tkinter.Entry(create_patient_frame)
        create_last_name_entry.grid(row=0, column=3)

        # Sex GUI label and data entry
        create_sex_label = tkinter.Label(create_patient_frame, text="Sex:")
        create_sex_label.grid(row=0, column=4)
        create_sex_combobox = ttk.Combobox(create_patient_frame, values=["Male", "Female", "Non-Binary", "Not Listed"])
        create_sex_combobox.grid(row=0, column=5)

        # DOB month GUI label and data entry
        create_dob_month_label = tkinter.Label(create_patient_frame, text="Birth Month:")
        create_dob_month_label.grid(row=1, column=0)
        create_dob_month_entry = tkinter.Entry(create_patient_frame)
        create_dob_month_entry.grid(row=1, column=1)

        # DOB day GUI label and data entry
        create_dob_day_label = tkinter.Label(create_patient_frame, text="Birth Day:")
        create_dob_day_label.grid(row=1, column=2)
        create_dob_day_entry = tkinter.Entry(create_patient_frame)
        create_dob_day_entry.grid(row=1, column=3)

        # DOB year GUI label and data entry
        create_dob_year_label = tkinter.Label(create_patient_frame, text="Birth Year:")
        create_dob_year_label.grid(row=1, column=4)
        create_dob_year_entry = tkinter.Entry(create_patient_frame)
        create_dob_year_entry.grid(row=1, column=5)

        # Phone GUI label and data entry
        create_phone_label = tkinter.Label(create_patient_frame, text="Phone:")
        create_phone_label.grid(row=2, column=0)
        create_phone_entry = tkinter.Entry(create_patient_frame)
        create_phone_entry.grid(row=2, column=1)

        # Email GUI label and data entry
        create_email_label = tkinter.Label(create_patient_frame, text="Email:")
        create_email_label.grid(row=2, column=2)
        create_email_entry = tkinter.Entry(create_patient_frame)
        create_email_entry.grid(row=2, column=3)

        # Button to perform save action
        save_patient_button = tkinter.Button(create_patient_frame, text="Save New Patient",
                                             command=lambda: save_new_patient(create_first_name_entry.get(),
                                                                              create_last_name_entry.get(),
                                                                              create_dob_month_entry.get(),
                                                                              create_dob_day_entry.get(),
                                                                              create_dob_year_entry.get(),
                                                                              create_sex_combobox.get(),
                                                                              create_phone_entry.get(),
                                                                              create_email_entry.get(), new))
        save_patient_button.grid(row=3, column=0, sticky="news")

        # Button to cancel and close window
        cancel_button = tkinter.Button(create_patient_frame, text="Cancel", command=new.destroy)
        cancel_button.grid(row=3, column=1, sticky="news")

        for item in create_patient_frame.winfo_children():
            item.grid_configure(padx=10, pady=5)

    def open_find_patient_win(get_patient: Patient):
        search_window = tkinter.Toplevel()
        search_window.title("Search Result")
        search_window.minsize(600, 300)

        search_patient_frame = tkinter.LabelFrame(search_window, text="Search Patient")
        search_patient_frame.grid(row=0, column=0, padx=20, pady=30)

        search_first_name_label = tkinter.Label(search_patient_frame,
                                                text=f"First Name: {get_patient.first_name.title()}")
        search_first_name_label.grid(row=0, column=0)

        search_last_name_label = tkinter.Label(search_patient_frame, text=f"Last Name: {get_patient.last_name.title()}")
        search_last_name_label.grid(row=2, column=0)

        search_dob_label = tkinter.Label(search_patient_frame, text=f"Date of Birth: {get_patient.dob}")
        search_dob_label.grid(row=0, column=1)

        search_sex_label = tkinter.Label(search_patient_frame, text=f"Sex: {get_patient.sex.title()}")
        search_sex_label.grid(row=2, column=1, sticky="w")

        search_phone_label = tkinter.Label(search_patient_frame, text=f"Phone: {get_patient.phone}")
        search_phone_label.grid(row=0, column=2)

        search_email_label = tkinter.Label(search_patient_frame, text=f"Email: {get_patient.email.lower()}")
        search_email_label.grid(row=2, column=2)

        close_button = tkinter.Button(search_patient_frame, text="Close", command=search_window.destroy)
        close_button.grid(row=3, column=0, sticky="news")

        for i in search_patient_frame.winfo_children():
            i.grid_configure(padx=10, pady=5)

    # Create the GUI framework
    window = tkinter.Tk()
    window.title("Primary Care Scheduling")
    window.minsize(800, 600)
    frame = tkinter.Frame(window)
    frame.pack()

    # This is the patient lookup section
    patient_info_frame = tkinter.LabelFrame(frame, text="Patient Information")
    patient_info_frame.grid(row=0, columnspan=2, padx=30, pady=30)

    # First name GUI label and data entry
    first_name_label = tkinter.Label(patient_info_frame, text="First Name:")
    first_name_label.grid(row=0, column=0)
    first_name_entry = tkinter.Entry(patient_info_frame)
    first_name_entry.grid(row=0, column=1)

    # Last name GUI label and data entry
    last_name_label = tkinter.Label(patient_info_frame, text="Last Name:")
    last_name_label.grid(row=1, column=0)
    last_name_entry = tkinter.Entry(patient_info_frame)
    last_name_entry.grid(row=1, column=1)

    # Timeslot GUI label and data entry
    schedule_timeslot_label = tkinter.Label(patient_info_frame, text="Pick Timeslot:")
    schedule_timeslot_label.grid(row=2, column=0)
    schedule_timeslot_combobox = ttk.Combobox(patient_info_frame, values=["1", "2", "3", "4", "5", "6", "7", "8", "9",
                                                                          "10"])
    schedule_timeslot_combobox.grid(row=2, column=1)

    # Button to perform patient search
    search_button = tkinter.Button(patient_info_frame, text="View Patient", command=patient_search)
    search_button.grid(row=0, column=2, sticky="news")

    # Button to open new patient creation window
    new_patient_button = tkinter.Button(patient_info_frame, text="Create New Patient", command=open_new_patient_win)
    new_patient_button.grid(row=1, column=2, sticky="news")

    # Button to add patient to schedule
    add_to_schedule_button = tkinter.Button(patient_info_frame, text="Schedule Patient", command=add_to_schedule)
    add_to_schedule_button.grid(row=2, column=2, sticky="news")

    # Button to add patient to wait list
    add_to_wait_list_button = tkinter.Button(patient_info_frame, text="Add to Wait List", command=add_to_wait_list)
    add_to_wait_list_button.grid(row=3, column=2, sticky="news")

    # Button to remove patient to wait list
    remove_from_wait_list_button = tkinter.Button(patient_info_frame, text="Remove from Wait List",
                                                  command=remove_from_wait_list)
    remove_from_wait_list_button.grid(row=4, column=2, sticky="news")

    # Format fields
    for i in patient_info_frame.winfo_children():
        i.grid_configure(padx=15, pady=5)

    # Generates the GUI to display the schedule
    display_schedule()

    # Generates the GUI to display the wait list
    display_wait_list()

    window.mainloop()
