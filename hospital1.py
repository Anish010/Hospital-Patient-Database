import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random
import time
import datetime
import mysql.connector

root = Tk()
root.title("Hospital Management System")
# root.geometry("1500x900+0+0")
root.state("zoomed")


def ilogout():
    import Login
    root.destroy()
    Login.main()


def fetch_data():
    con = mysql.connector.connect(
        host="localhost", user="root", password="12345678", database="patientdata", auth_plugin='mysql_native_password')
    my_cursor = con.cursor()
    my_cursor.execute("select * from hospital")
    rows = my_cursor.fetchall()
    if len(rows) != 0:
        hospital_table.delete(* hospital_table.get_children())
        for i in rows:
            hospital_table.insert("", END, values=i)
            con.commit()
        con.close()


ref = StringVar()
RoomNo = StringVar()
NameOfTablets = StringVar()
Dose = StringVar()
Phone = StringVar()
IssueDate = StringVar()
BloodPressure = StringVar()
Medication = StringVar()
PatientId = StringVar()
AadharNo = StringVar()
DoctorName = StringVar()
FirstName = StringVar()
LastName = StringVar()
Age = StringVar()
dob = StringVar()
PatientAddress = StringVar()

# ====== BUTTON FUNCTIONS ================================


def check_all_details_inserted():
    if room_no_entry.get() == "" or reference_no_entry.get() == "" or issue_date_entry.get() == "" or patient_id_entry.get() == "" or aadhar_no_entry.get() == "" or doctor_name_entry.get() == "" or patient_first_name_entry.get() == "" or patient_last_name_entry.get() == "" or age_entry.get() == "" or address_entry.get() == "":
        return True
    else:
        return False


def prescription_details():
    if check_all_details_inserted():
        messagebox.showerror("Error", "All fields are required")
    else:
        con = mysql.connector.connect(
            host="localhost", user="root", password="12345678", database="patientdata", auth_plugin='mysql_native_password')
        my_cursor = con.cursor()
        my_cursor.execute("insert into hospital values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
            ref.get(),
            RoomNo.get(),
            NameOfTablets.get(),
            Dose.get(),
            DoctorName.get(),
            IssueDate.get(),
            BloodPressure.get(),
            Medication.get(),
            PatientId.get(),
            AadharNo.get(),
            Phone.get(),
            FirstName.get(),
            LastName.get(),
            Age.get(),
            dob.get(),
            PatientAddress.get()
        ))
        con.commit()
        fetch_data()
        con.close()
        messagebox.showinfo("Success", "All Data inserted successfully")


def get_cursor(event=""):
    cursor_row = hospital_table.focus()
    content = hospital_table.item(cursor_row)
    row = content['values']
    ref.set(row[0]),
    RoomNo.set(row[1]),
    NameOfTablets.set(row[2]),
    Dose.set(row[3]),
    DoctorName.set(row[4]),
    IssueDate.set(row[5]),
    BloodPressure.set(row[6]),
    Medication.set(row[7]),
    PatientId.set(row[8]),
    AadharNo.set(row[9]),
    Phone.set(row[10]),
    FirstName.set(row[11]),
    LastName.set(row[12]),
    Age.set(row[13]),
    dob.set(row[14]),
    PatientAddress.set(row[15])


def update_data():
    con = mysql.connector.connect(host="localhost", user="root", password="12345678",
                                  database="patientdata", auth_plugin='mysql_native_password')
    my_cursor = con.cursor()
    my_cursor.execute("update hospital set Room_No=%s, Name_of_Tablets=%s,Dose=%s ,Doctor_Name=%s, Issue_Date=%s, Blood_Pressure=%s, Medication=%s, Patient_Id=%s, Aadhar_No=%s, Phone_No=%s, First_Name=%s, Last_Name=%s, Age=%s, Date_Of_Birth=%s, Address=%s where Reference_No=%s", (
        RoomNo.get(),
        NameOfTablets.get(),
        Dose.get(),
        DoctorName.get(),
        IssueDate.get(),
        BloodPressure.get(),
        Medication.get(),
        PatientId.get(),
        AadharNo.get(),
        Phone.get(),
        FirstName.get(),
        LastName.get(),
        Age.get(),
        dob.get(),
        PatientAddress.get(),
        ref.get()
    ))

    con.commit()
    fetch_data()
    con.close()
    messagebox.showinfo("Success", "Data updated successfully")


def iPrescription():
    text_prescription.insert(
        END, "Ref. No :\t"+ref.get()+"\n")
    text_prescription.insert(
        END, "Patient Id :\t"+PatientId.get()+"\n")
    text_prescription.insert(END, "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    text_prescription.insert(END, "Doctor Name :\tDr. "+DoctorName.get()+"\n")
    text_prescription.insert(END, "Patient Name :\t" +
                             FirstName.get()+" "+LastName.get()+"\n")
    text_prescription.insert(END, "Age : "+Age.get() +
                             "\t\t    "+"DOB : "+dob.get()+"\n\n")
    text_prescription.insert(
        END, "Issue Date :\t"+IssueDate.get()+"\n")
    text_prescription.insert(
        END, "Phone No :\t"+Phone.get()+"\n")
    text_prescription.insert(END, "Room No :\t"+RoomNo.get() + "\n\n")
    text_prescription.insert(
        END, "Blood Pressure :\t"+BloodPressure.get()+"\n")
    text_prescription.insert(END, "Medication :\t"+Medication.get()+"\n")
    text_prescription.insert(
        END, "Name of Tablets :\t"+NameOfTablets.get()+"\n")
    text_prescription.insert(END, "Dose :\t"+Dose.get()+"\n")


label_title = Label(root, bd=20, bg="red", relief=RIDGE,
                    text="HOSPITAL PATIENT DATABASE", fg="white",
                    font=("impact", 32, "bold"))
label_title.pack(side=TOP, fill=X)

# NAV BAR
nav_frame = Frame(root, bd=20, relief=RIDGE, borderwidth=7)
nav_frame.place(x=0, y=88, width=1280, height=54)

# Dataframe
data_frame = Frame(root, bd=20, relief=RIDGE, borderwidth=7)
data_frame.place(x=0, y=142, width=1280, height=333)

patient_information = LabelFrame(data_frame, bd=10, relief=RIDGE, borderwidth=5, padx=10, font=(
    "times new roman", 12, "bold"), text="Patient Information")
patient_information.place(x=2, y=5, width=845, height=315)

prescription = LabelFrame(data_frame, bd=10, relief=RIDGE, borderwidth=5, padx=10, font=(
    "times new roman", 12, "bold"), text="Prescription Information")
prescription.place(x=855, y=5, width=400, height=315)

# details frame
details_frame = Frame(root, bd=20, relief=RIDGE, borderwidth=7)
details_frame.place(x=0, y=505, width=1280, height=108)

# BUTTON FRAME
button_frame = Frame(root, bd=20, relief=RIDGE, borderwidth=7)
button_frame.place(x=0, y=610, width=1280, height=54)

# Patient Information frame

# Patient Information frame
# ====Labels======

# Reference No
reference_no = Label(patient_information, text="Reference No :",
                     font=("arial", 12, "bold"), padx=2)
reference_no.grid(row=0, column=0, sticky=W)

# roomn no
room_no = Label(patient_information, text="Room no :", font=(
    "arial", 12, "bold"), padx=2, pady=6)
room_no.grid(row=1, column=0, sticky=W)

# Name of Tablets
name_of_tablets = Label(patient_information, text="Name of Tablets :", font=(
    "arial", 12, "bold"), padx=2, pady=6)
name_of_tablets.grid(row=2, column=0, sticky=W)

# dose
dose = Label(patient_information, text="Dose :",
             font=("arial", 12, "bold"), padx=2, pady=6)
dose.grid(row=3, column=0, sticky=W)

# Doctor Name
doctor_name = Label(patient_information, text="Doctor Name :",
                    font=("arial", 12, "bold"), padx=2, pady=6)
doctor_name.grid(row=4, column=0, sticky=W)

# issue date
issue_date = Label(patient_information, text="Issue Date :",
                   font=("arial", 12, "bold"), padx=2, pady=6)
issue_date.grid(row=5, column=0, sticky=W)

# Blood pressure
blood_pressure = Label(patient_information, text="Blood Pressure :", font=(
    "arial", 12, "bold"), padx=2, pady=6)
blood_pressure.grid(row=6, column=0, sticky=W)

# Medication
medication = Label(patient_information, text="Medication :",
                   font=("arial", 12, "bold"), padx=2, pady=6)
medication.grid(row=7, column=0, sticky=W)

# Aadhar No
aadhar_no = Label(patient_information, text="Aadhar No :",
                  font=("arial", 12, "bold"), padx=2, pady=6)
aadhar_no.grid(row=0, column=4, sticky=W, padx=(10, 0))

# Phone Number
phone = Label(patient_information, text="Phone No :", font=(
    "arial", 12, "bold"), padx=2, pady=6)
phone.grid(row=1, column=4, sticky=W, padx=(10, 0))

# Patient First Name
patient_first_name = Label(patient_information, text="First Name :", font=(
    "arial", 12, "bold"), padx=2, pady=6)
patient_first_name.grid(row=2, column=4, sticky=W, padx=(10, 0))

# Patient Last Name
patient_last_name = Label(patient_information, text="Last Name :", font=(
    "arial", 12, "bold"), padx=2, pady=6)
patient_last_name.grid(row=3, column=4, sticky=W, padx=(10, 0))

# Age
age = Label(patient_information, text="Age :",
            font=("arial", 12, "bold"), padx=2, pady=6)
age.grid(row=4, column=4, sticky=W, padx=(10, 0))
# Date of Birth
date_of_birth = Label(patient_information, text="DOB :",
                      font=("arial", 12, "bold"), padx=2, pady=6)
date_of_birth.grid(row=5, column=4, sticky=W, padx=(10, 0))
# Address
address = Label(patient_information, text="Address :",
                font=("arial", 12, "bold"), padx=2, pady=6)
address.grid(row=6, column=4, sticky=W, padx=(10, 0))

# Patient id
patient_id = Label(patient_information, text="Patient Id :",
                   font=("arial", 12, "bold"), padx=2, pady=6)
patient_id.grid(row=7, column=4, sticky=W, padx=(10, 0))

# ====Entry=====
reference_no_entry = Entry(patient_information, font=(
    "arial", 13, "bold"), width=30, textvariable=ref)
reference_no_entry.grid(row=0, column=1, sticky=W)

room_no_entry = Entry(patient_information, font=(
    "arial", 13, "bold"), width=30, textvariable=RoomNo)
room_no_entry.grid(row=1, column=1, sticky=W)

name_of_tablets_entry = Entry(patient_information, font=(
    "arial", 13, "bold"), width=30, textvariable=NameOfTablets)
name_of_tablets_entry.grid(row=2, column=1, sticky=W)

dose_entry = Entry(patient_information, font=(
    "arial", 13, "bold"), width=30, textvariable=Dose)
dose_entry.grid(row=3, column=1, sticky=W)

doctor_name_entry = Entry(patient_information, font=(
    "arial", 13, "bold"), width=30, textvariable=DoctorName)
doctor_name_entry.grid(row=4, column=1, sticky=W)

issue_date_entry = Entry(patient_information, font=(
    "arial", 13, "bold"), width=30, textvariable=IssueDate)
issue_date_entry.grid(row=5, column=1, sticky=W)

blood_pressure_entry = Entry(
    patient_information, font=("arial", 13, "bold"), width=30, textvariable=BloodPressure)
blood_pressure_entry.grid(row=6, column=1, sticky=W)

medication_entry = Entry(patient_information, font=(
    "arial", 13, "bold"), width=30, textvariable=Medication)
medication_entry.grid(row=7, column=1, sticky=W)

aadhar_no_entry = Entry(patient_information, font=(
    "arial", 13, "bold"), width=30, textvariable=AadharNo)
aadhar_no_entry.grid(row=0, column=5, sticky=W)

phone_entry = Entry(patient_information, font=(
    "arial", 13, "bold"), width=30, textvariable=Phone)
phone_entry.grid(row=1, column=5, sticky=W)

patient_first_name_entry = Entry(patient_information, font=(
    "arial", 13, "bold"), width=30, textvariable=FirstName)
patient_first_name_entry.grid(row=2, column=5, sticky=W)

patient_last_name_entry = Entry(patient_information, font=(
    "arial", 13, "bold"), width=30, textvariable=LastName)
patient_last_name_entry.grid(row=3, column=5, sticky=W)

age_entry = Entry(patient_information, font=(
    "arial", 13, "bold"), width=30, textvariable=Age)
age_entry.grid(row=4, column=5, sticky=W)

date_of_birth_entry = Entry(patient_information, font=(
    "arial", 13, "bold"), width=30, textvariable=dob)
date_of_birth_entry.grid(row=5, column=5, sticky=W)

address_entry = Entry(patient_information, font=(
    "arial", 13, "bold"), width=30, textvariable=PatientAddress)
address_entry.grid(row=6, column=5, sticky=W)

patient_id_entry = Entry(patient_information, font=(
    "arial", 13, "bold"), width=30, textvariable=PatientId)
patient_id_entry.grid(row=7, column=5, sticky=W)

# Prescription
text_prescription = Text(prescription, font=(
    "arial", 8, "bold"), width=58, height=12)
text_prescription.grid(row=0, column=0)


# Buttons - Botton
# # Prescription
text_prescription = Text(prescription, font=(
    "arial", 12, "bold"), width=39, height=15)
text_prescription.grid(row=0, column=0)

# Prescription Button
button_prescription = Button(button_frame, text="Prescription", font=(
    "arial", 9, "bold"), width=30, height=2, bg="green", fg="white", anchor=CENTER, command=iPrescription)
button_prescription.grid(row=0, column=1)

# Prescription Save Button
button_prescription_details = Button(button_frame, text="Prescription Save", font=(
    "arial", 9, "bold"), width=30, height=2, bg="green", fg="white", anchor=CENTER, command=prescription_details)
button_prescription_details.grid(row=0, column=2)

# Update Button
button_update = Button(button_frame, text="Update", font=("arial", 9, "bold"),
                       width=30, height=2, bg="green", fg="white", anchor=CENTER, command=update_data)
button_update.grid(row=0, column=3)

# Delete Button
button_delete = Button(button_frame, text="Delete", font=(
    "arial", 9, "bold"), width=30, height=2, bg="green", fg="white", anchor=CENTER)
button_delete.grid(row=0, column=4)

# Clear Button
button_clear = Button(button_frame, text="Clear", font=(
    "arial", 9, "bold"), width=30, height=2, bg="green", fg="white", anchor=CENTER)
button_clear.grid(row=0, column=5)

# Exit Button
button_exit = Button(button_frame, text="Exit", font=(
    "arial", 9, "bold"), width=22, height=2, bg="red", fg="white", anchor=CENTER)
button_exit.grid(row=0, column=6)

# Nav Bar

# Doctor
button_Home = Button(nav_frame, text="Home", font=(
    "arial", 9, "bold"), width=35, height=2, bg="#2916f5", fg="white", anchor=CENTER)
button_Home.grid(row=0, column=0)

# Doctor
button_doctor = Button(nav_frame, text="Doctor",  font=(
    "arial", 9, "bold"), width=35, height=2, bg="#2916f5", fg="white", anchor=CENTER)
button_doctor.grid(row=0, column=1)

# Patient
button_patient = Button(nav_frame, text="Patient", font=(
    "arial", 9, "bold"), width=35, height=2, bg="#2916f5", fg="white", anchor=CENTER)
button_patient.grid(row=0, column=2)

# Appointments
button_appointment = Button(nav_frame, text="Appointments", font=(
    "arial", 9, "bold"), width=35, height=2, bg="#2916f5", fg="white", anchor=CENTER)
button_appointment.grid(row=0, column=3)

# Logout
button_logout = Button(nav_frame, text="Logout", font=("arial", 9, "bold"),
                       width=34, height=2, bg="#2916f5", fg="white", anchor=CENTER, command=ilogout)
button_logout.grid(row=0, column=4)

# Table
# Scroll

scroll_x = ttk.Scrollbar(details_frame, orient=HORIZONTAL)
scroll_y = ttk.Scrollbar(details_frame, orient=VERTICAL)

hospital_table = ttk.Treeview(details_frame, column=("ref", "room_no", "name_of_tablets", "dose", "doctor_name", "issue_dt", "blood_pressure",
                                                     "medication", "patient_id", "aadhar_no", "phone", "first_name", "last_name", "age", "dob", "address"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

scroll_x.pack(side=BOTTOM, fill=X)
scroll_y.pack(side=RIGHT, fill=Y)

scroll_x.config(command=hospital_table.xview)
scroll_y.config(command=hospital_table.yview)

hospital_table.heading("ref", text="Reference No")
hospital_table.heading("room_no", text="Room No")
hospital_table.heading("name_of_tablets", text="Name of Tablets")
hospital_table.heading("dose", text="Dose")
hospital_table.heading("doctor_name", text="Doctor Name")
hospital_table.heading("issue_dt", text="Issue Date")
hospital_table.heading("blood_pressure", text="Blood Pressure")
hospital_table.heading("medication", text="Medication")
hospital_table.heading("patient_id", text="Patient Id")
hospital_table.heading("aadhar_no", text="Aadhar No")
hospital_table.heading("phone", text="Phone No")
hospital_table.heading("first_name", text="First Name")
hospital_table.heading("last_name", text="Last Name")
hospital_table.heading("age", text="Age")
hospital_table.heading("dob", text="Date of Birth")
hospital_table.heading("address", text="Address")
hospital_table["show"] = "headings"
hospital_table.pack(fill=BOTH, expand=1)
hospital_table.bind("<ButtonRelease-1>", get_cursor)
fetch_data()


mainloop()
