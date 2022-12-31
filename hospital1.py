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
root.geometry("1500x900+0+0")


# ====== BUTTON FUNCTIONS ================================


def Prescription_Details():
    if name_of_tablets_entry.get() == "" or reference_no_entry.get() == "":
        messagebox.showerror("Error", "All fields are required")
    else:
        con = mysql.connector.connect(
            host="localhost", user="root", password="12345678", database="patientdata", auth_plugin='mysql_native_password')
        my_cursor = con.cursor()
        my_cursor.execute("insert into hospital values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
            NameOfTablets.get(),
            ref.get(),
            NoOfTablets.get(),
            IssueDate.get(),
            ExpDate.get(),
            DailyDose.get(),
            BloodPressure.get(),
            Medication.get(),
            PatientId.get(),
            AadharNo.get(),
            DoctorName.get(),
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


# HEADING
label_title = Label(root, bd=20, relief=RIDGE,
                    text="HOSPITAL PATIENT DATABASE", fg="red", bg="white",
                    font=("times new roman", 32, "bold"))
label_title.pack(side=TOP, fill=X)

# Dataframe
data_frame = Frame(root, bd=20, relief=RIDGE, borderwidth=7)
data_frame.place(x=0, y=88, width=1300, height=340)

patient_information = LabelFrame(data_frame, bd=10, relief=RIDGE, borderwidth=5, padx=10, font=(
    "times new roman", 12, "bold"), text="Patient Information")
patient_information.place(x=2, y=5, width=845, height=317)

prescription = LabelFrame(data_frame, bd=10, relief=RIDGE, borderwidth=5, padx=10, font=(
    "times new roman", 12, "bold"), text="Prescription Information")
prescription.place(x=855, y=5, width=380, height=317)

# BUTTON FRAME
button_frame = Frame(root, bd=20, relief=RIDGE, borderwidth=7)
button_frame.place(x=0, y=430, width=1280, height=64)

# details frame
details_frame = Frame(root, bd=20, relief=RIDGE, borderwidth=7)
details_frame.place(x=0, y=500, width=1280, height=160)

# PATIENT INFORMATION FRAME

# ====Labels======
# name of tablets
tablet_name = Label(patient_information, text="Name of Tablet :", font=(
    "arial", 12, "bold"), padx=2, pady=6)
tablet_name.grid(row=0, column=0)
# Reference No
reference_no = Label(patient_information, text="Reference No :", font=(
    "arial", 12, "bold"), padx=2)
reference_no.grid(row=1, column=0, sticky=W)
# dose
dose = Label(patient_information, text="Dose :",
             font=("arial", 12, "bold"), padx=2, pady=6)
dose.grid(row=2, column=0, sticky=W)
# No. of Tablets
no_of_tablets = Label(patient_information, text="No of Tablets :", font=(
    "arial", 12, "bold"), padx=2, pady=6)
no_of_tablets.grid(row=2, column=0, sticky=W)
# issue date
issue_date = Label(patient_information, text="Issue Date :", font=(
    "arial", 12, "bold"), padx=2, pady=6)
issue_date.grid(row=3, column=0, sticky=W)
# expiry date
expiry_date = Label(patient_information, text="Expiry Date :", font=(
    "arial", 12, "bold"), padx=2, pady=6)
expiry_date.grid(row=4, column=0, sticky=W)
# daily dose
daily_dose = Label(patient_information, text="Daily Dose :", font=(
    "arial", 12, "bold"), padx=2, pady=6)
daily_dose.grid(row=5, column=0, sticky=W)
# Blood pressure
blood_pressure = Label(patient_information, text="Blood Pressure :", font=(
    "arial", 12, "bold"), padx=2, pady=6)
blood_pressure.grid(row=6, column=0, sticky=W)
# Medication
medication = Label(patient_information, text="Medication :", font=(
    "arial", 12, "bold"), padx=2, pady=6)
medication.grid(row=7, column=0, sticky=W)
# Patient id
patient_id = Label(patient_information, text="Patient Id :", font=(
    "arial", 12, "bold"), padx=2, pady=6)
patient_id.grid(row=0, column=4, sticky=W, padx=(10, 0))
# Aadhar No
aadhar_no = Label(patient_information, text="Aadhar No :",
                  font=("arial", 12, "bold"), padx=2, pady=6)
aadhar_no.grid(row=1, column=4, sticky=W, padx=(10, 0))
# Doctor Name
doctor_name = Label(patient_information, text="Doctor Name :", font=(
    "arial", 12, "bold"), padx=2, pady=6)
doctor_name.grid(row=2, column=4, sticky=W, padx=(10, 0))
# Patient First Name
patient_first_name = Label(patient_information, text="First Name :", font=(
    "arial", 12, "bold"), padx=2, pady=6)
patient_first_name.grid(row=3, column=4, sticky=W, padx=(10, 0))
# Patient Last Name
patient_last_name = Label(patient_information, text="Last Name :", font=(
    "arial", 12, "bold"), padx=2, pady=6)
patient_last_name.grid(row=4, column=4, sticky=W, padx=(10, 0))
# Age
age = Label(patient_information, text="Age :",
            font=("arial", 12, "bold"), padx=2, pady=6)
age.grid(row=5, column=4, sticky=W, padx=(10, 0))
# Date of Birth
dob = Label(patient_information, text="DOB :",
            font=("arial", 12, "bold"), padx=2, pady=6)
dob.grid(row=6, column=4, sticky=W, padx=(10, 0))
# Address
address = Label(patient_information, text="Address :",
                font=("arial", 12, "bold"), padx=2, pady=6)
address.grid(row=7, column=4, sticky=W, padx=(10, 0))
# Prescription
text_prescription = Text(prescription, font=(
    "arial", 12, "bold"), width=39, height=15)
text_prescription.grid(row=0, column=0)

NameOfTablets = StringVar()
ref = StringVar()
Dose = StringVar()
NoOfTablets = StringVar()
IssueDate = StringVar()
ExpDate = StringVar()
DailyDose = StringVar()
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

# ====Entry=====
name_of_tablets_entry = Entry(patient_information, textvariable=NameOfTablets, font=(
    "arial", 13, "bold"), width=30)
name_of_tablets_entry.grid(row=0, column=1)

reference_no_entry = Entry(patient_information, textvariable=ref, font=(
    "arial", 13, "bold"), width=30)
reference_no_entry.grid(row=1, column=1)

dose_entry = Entry(patient_information, textvariable=Dose, font=(
    "arial", 13, "bold"), width=30)
dose_entry.grid(row=2, column=1)

no_of_tablets_entry = Entry(patient_information, textvariable=NoOfTablets, font=(
    "arial", 13, "bold"), width=30)
no_of_tablets_entry.grid(row=2, column=1)

issue_date_entry = Entry(patient_information, textvariable=IssueDate, font=(
    "arial", 13, "bold"), width=30)
issue_date_entry.grid(row=3, column=1)

expiry_date_entry = Entry(patient_information, textvariable=ExpDate, font=(
    "arial", 13, "bold"), width=30)
expiry_date_entry.grid(row=4, column=1)

daily_dose_entry = Entry(patient_information, textvariable=DailyDose, font=(
    "arial", 13, "bold"), width=30)
daily_dose_entry.grid(row=5, column=1)

blood_pressure_entry = Entry(
    patient_information, textvariable=BloodPressure, font=("arial", 13, "bold"), width=30)
blood_pressure_entry.grid(row=6, column=1)

medication_entry = Entry(patient_information, textvariable=Medication, font=(
    "arial", 13, "bold"), width=30)
medication_entry.grid(row=7, column=1)

patient_id_entry = Entry(patient_information, textvariable=PatientId, font=(
    "arial", 13, "bold"), width=30)
patient_id_entry.grid(row=0, column=5)

aadhar_no_entry = Entry(patient_information, font=(
    "arial", 13, "bold"), width=30, textvariable=AadharNo)
aadhar_no_entry.grid(row=1, column=5)

doctor_name_entry = Entry(patient_information, font=(
    "arial", 13, "bold"), width=30, textvariable=DoctorName)
doctor_name_entry.grid(row=2, column=5)

patient_first_name_entry = Entry(
    patient_information, font=("arial", 13, "bold"), width=30, textvariable=FirstName)
patient_first_name_entry.grid(row=3, column=5)

patient_last_name_entry = Entry(
    patient_information, font=("arial", 13, "bold"), width=30, textvariable=LastName)
patient_last_name_entry.grid(row=4, column=5)

age_entry = Entry(patient_information, font=(
    "arial", 13, "bold"), width=30, textvariable=Age)
age_entry.grid(row=5, column=5)

dob_entry = Entry(patient_information, font=(
    "arial", 13, "bold"), width=30, textvariable=dob)
dob_entry.grid(row=6, column=5)

address_entry = Entry(patient_information, font=(
    "arial", 13, "bold"), width=30, textvariable=PatientAddress)
address_entry.grid(row=7, column=5)

# Buttons

# Prescription Button
button_prescription = Button(button_frame, text="Prescription", font=("arial", 12, "bold"),
                             width=21, height=2, bg="green", fg="white", anchor=CENTER,)
button_prescription.grid(row=0, column=1)

# Prescription Details Button
button_prescription_details = Button(button_frame, text="Prescription Details", font=("arial", 12, "bold"),
                                     width=20, height=2, bg="green", fg="white", anchor=CENTER, command=Prescription_Details)
button_prescription_details.grid(row=0, column=2)

# Update Button
button_update = Button(button_frame, text="Update", font=("arial", 12, "bold"),
                       width=20, height=2, bg="green", fg="white", anchor=CENTER)
button_update.grid(row=0, column=3)

# Delete Button
button_delete = Button(button_frame, text="Delete", font=("arial", 12, "bold"),
                       width=20, height=2, bg="green", fg="white", anchor=CENTER)
button_delete.grid(row=0, column=4)

# Clear Button
button_clear = Button(button_frame, text="Clear", font=("arial", 12, "bold"),
                      width=20, height=2, bg="green", fg="white", anchor=CENTER)
button_clear.grid(row=0, column=5)

# Exit Button
button_exit = Button(button_frame, text="Exit", font=("arial", 12, "bold"),
                     width=20, height=2, bg="red", fg="white", anchor=CENTER)
button_exit.grid(row=0, column=6)

# Table
# Scroll

scroll_x = ttk.Scrollbar(details_frame, orient=HORIZONTAL)
scroll_y = ttk.Scrollbar(details_frame, orient=VERTICAL)

hospital_table = ttk.Treeview(details_frame, column=(
    "name_of_tablet", "ref", "dose", "no_of_tablets", "issue_dt", "expiry_dt", "daily_dose",
    "aadhar_no", "name", "doctor", "dob", "address"), xscrollcommand=scroll_x.set,
    yscrollcommand=scroll_y.set)

scroll_x.pack(side=BOTTOM, fill=X)
scroll_y.pack(side=RIGHT, fill=Y)

scroll_x.config(command=hospital_table.xview)
scroll_y.config(command=hospital_table.yview)

hospital_table.heading("name_of_tablet", text="Name of Tablet")
hospital_table.heading("ref", text="Reference No")
hospital_table.heading("dose", text="Dose")
hospital_table.heading("no_of_tablets", text="No of Tablets")
hospital_table.heading("issue_dt", text="Issue Date")
hospital_table.heading("expiry_dt", text="Expiry Date")
hospital_table.heading("daily_dose", text="Daily Dose")
hospital_table.heading("aadhar_no", text="Aadhar No")
hospital_table.heading("name", text="Name")
hospital_table.heading("doctor", text="Doctor Name")
hospital_table.heading("dob", text="Date of Birth")
hospital_table.heading("address", text="Address")

hospital_table["show"] = "headings"
hospital_table.pack(fill=BOTH, expand=1)

fetch_data()

mainloop()
