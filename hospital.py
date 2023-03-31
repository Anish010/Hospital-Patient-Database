import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random
import time
import datetime
import mysql.connector


def main():
    root_ele = Tk()
    ob = Hospital(root_ele)
    root_ele.mainloop()


class Hospital:

    def fetch_data(self):
        con = mysql.connector.connect(
            host="localhost", user="root", password="12345678", database="patientdata", auth_plugin='mysql_native_password')
        my_cursor = con.cursor()
        my_cursor.execute("select * from hospital")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.hospital_table.delete(
                * self.hospital_table.get_children())
            for i in rows:
                self.hospital_table.insert("", END, values=i)
            con.commit()
        con.close()

    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Management System")
        # self.root.geometry("1500x900+0+0")
        self.root.state("zoomed")

        self.ref = StringVar()
        self.RoomNo = StringVar()
        self.NameOfTablets = StringVar()
        self.Dose = StringVar()
        self.Phone = StringVar()
        self.IssueDate = StringVar()
        self.BloodPressure = StringVar()
        self.Medication = StringVar()
        self.PatientId = StringVar()
        self.AadharNo = StringVar()
        self.DoctorName = StringVar()
        self.FirstName = StringVar()
        self.LastName = StringVar()
        self.Age = StringVar()
        self.dob = StringVar()
        self.PatientAddress = StringVar()

        # ====== BUTTON FUNCTIONS ================================

        def check_all_details_inserted():
            if room_no_entry.get() == "" or reference_no_entry.get() == "" or issue_date_entry.get() == "" or patient_id_entry.get() == "" or aadhar_no_entry.get() == "" or doctor_name_entry.get() == "" or patient_first_name_entry.get() == "" or patient_last_name_entry.get() == "" or age_entry.get() == "" or address_entry.get() == "":
                return True
            else:
                return False

        def Prescription_Details():
            if check_all_details_inserted() == True:
                messagebox.showerror("Error", "All fields are required")
            else:
                con = mysql.connector.connect(
                    host="localhost", user="root", password="12345678", database="patientdata", auth_plugin='mysql_native_password')
                my_cursor = con.cursor()
                my_cursor.execute("insert into hospital values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                    self.ref.get(),
                    self.RoomNo.get(),
                    self.NameOfTablets.get(),
                    self.Dose.get(),
                    self.DoctorName.get(),
                    self.IssueDate.get(),
                    self.BloodPressure.get(),
                    self.Medication.get(),
                    self.PatientId.get(),
                    self.AadharNo.get(),
                    self.Phone.get(),
                    self.FirstName.get(),
                    self.LastName.get(),
                    self.Age.get(),
                    self.dob.get(),
                    self.PatientAddress.get()
                ))
                con.commit()
                self.fetch_data()
                con.close()
                messagebox.showinfo(
                    "Success", "All Data inserted successfully")

        def get_cursor(event=""):
            cursor_row = self.hospital_table.focus()
            content = self.hospital_table.item(cursor_row)
            row = content['values']
            self.ref.set(row[0]),
            self.RoomNo.set(row[1]),
            self.NameOfTablets.set(row[2]),
            self.Dose.set(row[3]),
            self.DoctorName.set(row[4]),
            self.IssueDate.set(row[5]),
            self.BloodPressure.set(row[6]),
            self.Medication.set(row[7]),
            self.PatientId.set(row[8]),
            self.AadharNo.set(row[9]),
            self.Phone.set(row[10]),
            self.FirstName.set(row[11]),
            self.LastName.set(row[12]),
            self.Age.set(row[13]),
            self.dob.set(row[14]),
            self.PatientAddress.set(row[15])

        def update_data():
            con = mysql.connector.connect(
                host="localhost", user="root", password="12345678", database="patientdata", auth_plugin='mysql_native_password')
            my_cursor = con.cursor()

            my_cursor.execute("update hospital set Room_No=%s, Name_of_Tablets=%s,Dose=%s ,Doctor_Name=%s, Issue_Date=%s, Blood_Pressure=%s, Medication=%s, Patient_Id=%s, Aadhar_No=%s, Phone_No=%s, First_Name=%s, Last_Name=%s, Age=%s, Date_Of_Birth=%s, Address=%s where Reference_No=%s", (
                self.RoomNo.get(),
                self.NameOfTablets.get(),
                self.Dose.get(),
                self.DoctorName.get(),
                self.IssueDate.get(),
                self.BloodPressure.get(),
                self.Medication.get(),
                self.PatientId.get(),
                self.AadharNo.get(),
                self.Phone.get(),
                self.FirstName.get(),
                self.LastName.get(),
                self.Age.get(),
                self.dob.get(),
                self.PatientAddress.get(),
                self.ref.get()
            ))

            con.commit()
            self.fetch_data()
            con.close()
            messagebox.showinfo("Success", "Data updated successfully")

        def iPrescription():
            self.text_prescription.insert(
                END, "Ref. No :\t"+self.ref.get()+"\t\t"+"Patient Id :\t"+self.PatientId.get()+"\n")
            self.text_prescription.insert(
                END, "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

            self.text_prescription.insert(
                END, "Doctor Name :\tDr. "+self.DoctorName.get()+"\n")

            self.text_prescription.insert(
                END, "Patient Name :\t"+self.FirstName.get()+" "+self.LastName.get()+"\n")

            self.text_prescription.insert(
                END, "Age :\t"+self.Age.get()+"\t\t"+"DOB :\t"+self.dob.get()+"\n")

            self.text_prescription.insert(
                END, "Issue Date :\t"+self.IssueDate.get()+"\t  "+"Phone No :\t"+self.Phone.get()+"\n\n")

            self.text_prescription.insert(
                END, "Room No :\t"+self.RoomNo.get()+"\n")

            self.text_prescription.insert(
                END, "Blood Pressure :\t"+self.BloodPressure.get()+"\n")

            self.text_prescription.insert(
                END, "Medication :\t"+self.Medication.get()+"\n")

            self.text_prescription.insert(
                END, "Name of Tablets :\t"+self.NameOfTablets.get()+"\n")

            self.text_prescription.insert(
                END, "Dose :\t"+self.Dose.get()+"\n")

            self.text_prescription.insert(
                END, "Medication :\t"+self.ref.get()+"\n")

        def idelete():
            con = mysql.connector.connect(
                host="localhost", user="root", password="12345678", database="patientdata",
                auth_plugin='mysql_native_password')
            my_cursor = con.cursor()
            query = "delete from hospital where Reference_No=%s"
            value = (self.ref.get(),)
            my_cursor.execute(query, value)
            con.commit()
            con.close()
            self.fetch_data()
            messagebox.showinfo("Delete", "Record deleted successfully")

        def clear():
            self.ref.set(""),
            self.RoomNo.set(""),
            self.NameOfTablets.set(""),
            self.Dose.set(""),
            self.DoctorName.set(""),
            self.IssueDate.set(""),
            self.BloodPressure.set(""),
            self.Medication.set(""),
            self.PatientId.set(""),
            self.AadharNo.set(""),
            self.Phone.set(""),
            self.FirstName.set(""),
            self.LastName.set(""),
            self.Age.set(""),
            self.dob.set(""),
            self.PatientAddress.set("")

        def iexit():
            ext = messagebox.askyesno(
                "Hospitsal Management System", "Do you want to exit?")
            if ext > 0:
                root.destroy()

        label_title = Label(root, bd=20, bg="red", relief=RIDGE,
                            text="HOSPITAL PATIENT DATABASE", fg="white",
                            font=("impact", 32, "bold"))

        label_title.pack(side=TOP, fill=X)

        # NAV BAR
        nav_frame = Frame(root, bd=20, relief=RIDGE, borderwidth=7)
        nav_frame.place(x=0, y=88, width=1280, height=54)

        # Dataframe
        data_frame = Frame(root, bd=20, relief=RIDGE, borderwidth=7)
        data_frame.place(x=0, y=142, width=1280, height=340)

        patient_information = LabelFrame(data_frame, bd=10, relief=RIDGE, borderwidth=5, padx=10, font=(
            "times new roman", 12, "bold"), text="Patient Information")
        patient_information.place(x=2, y=5, width=845, height=320)

        prescription = LabelFrame(data_frame, bd=10, relief=RIDGE, borderwidth=5, padx=10, font=(
            "times new roman", 12, "bold"), text="Prescription Information")
        prescription.place(x=855, y=5, width=400, height=320)

        # details frame
        details_frame = Frame(root, bd=20, relief=RIDGE, borderwidth=7)
        details_frame.place(x=0, y=480, width=1280, height=130)

        # BUTTON FRAME
        button_frame = Frame(root, bd=20, relief=RIDGE, borderwidth=7)
        button_frame.place(x=0, y=610, width=1280, height=54)

        # Patient Information frame

        # Patient Information frame
        # ====Labels======

        # Reference No
        reference_no = Label(patient_information, text="Reference No :", font=(
            "arial", 12, "bold"), padx=2)
        reference_no.grid(row=0, column=0, sticky=W)

        # room no
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
        doctor_name = Label(patient_information, text="Doctor Name :", font=(
            "arial", 12, "bold"), padx=2, pady=6)
        doctor_name.grid(row=4, column=0, sticky=W)

        # issue date
        issue_date = Label(patient_information, text="Issue Date :", font=(
            "arial", 12, "bold"), padx=2, pady=6)
        issue_date.grid(row=5, column=0, sticky=W)

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

        # Phone Number
        phone = Label(patient_information, text="Phone No :", font=(
            "arial", 12, "bold"), padx=2, pady=6)
        phone.grid(row=2, column=4, sticky=W, padx=(10, 0))

        # Patient First Name
        patient_first_name = Label(patient_information, text="First Name :", font=(
            "arial", 12, "bold"), padx=2, pady=6)
        patient_first_name.grid(row=3, column=4, sticky=W, padx=(10, 0))
        # Patient Last Name
        patient_last_name = Label(patient_information, text="Last Name :", font=(
            "arial", 12, "bold"), padx=4, pady=6)
        patient_last_name.grid(row=4, column=4, sticky=W, padx=(10, 0))
        # Age
        age = Label(patient_information, text="Age :",
                    font=("arial", 12, "bold"), padx=2, pady=6)
        age.grid(row=5, column=4, sticky=W, padx=(10, 0))
        # Date of Birth
        date_of_birth = Label(patient_information, text="DOB :",
                              font=("arial", 12, "bold"), padx=2, pady=6)
        date_of_birth.grid(row=6, column=4, sticky=W, padx=(10, 0))
        # Address
        address = Label(patient_information, text="Address :",
                        font=("arial", 12, "bold"), padx=2, pady=6)
        address.grid(row=7, column=4, sticky=W, padx=(10, 0))

        # ====Entry=====
        reference_no_entry = Entry(patient_information, font=(
            "arial", 13, "bold"), width=30, textvariable=self.ref)
        reference_no_entry.grid(row=0, column=1, sticky=W)

        room_no_entry = Entry(patient_information, font=(
            "arial", 13, "bold"), width=30, textvariable=self.RoomNo)
        room_no_entry.grid(row=1, column=1, sticky=W)

        name_of_tablets_entry = Entry(patient_information, font=(
            "arial", 13, "bold"), width=30, textvariable=self.NameOfTablets)
        name_of_tablets_entry.grid(row=2, column=1, sticky=W)

        dose_entry = Entry(patient_information, font=(
            "arial", 13, "bold"), width=30, textvariable=self.Dose)
        dose_entry.grid(row=3, column=1, sticky=W)

        doctor_name_entry = Entry(patient_information, font=(
            "arial", 13, "bold"), width=30, textvariable=self.DoctorName)
        doctor_name_entry.grid(row=4, column=1, sticky=W)

        issue_date_entry = Entry(patient_information, font=(
            "arial", 13, "bold"), width=30, textvariable=self.IssueDate)
        issue_date_entry.grid(row=5, column=1, sticky=W)

        blood_pressure_entry = Entry(
            patient_information, font=("arial", 13, "bold"), width=30, textvariable=self.BloodPressure)
        blood_pressure_entry.grid(row=6, column=1, sticky=W)

        medication_entry = Entry(patient_information, font=(
            "arial", 13, "bold"), width=30, textvariable=self.Medication)
        medication_entry.grid(row=7, column=1, sticky=W)

        patient_id_entry = Entry(patient_information, font=(
            "arial", 13, "bold"), width=30, textvariable=self.PatientId)
        patient_id_entry.grid(row=0, column=5, sticky=W)

        aadhar_no_entry = Entry(patient_information, font=(
            "arial", 13, "bold"), width=30, textvariable=self.AadharNo)
        aadhar_no_entry.grid(row=1, column=5, sticky=W)

        phone_entry = Entry(patient_information, font=(
            "arial", 13, "bold"), width=30, textvariable=self.Phone)
        phone_entry.grid(row=2, column=5, sticky=W)

        patient_first_name_entry = Entry(
            patient_information, font=("arial", 13, "bold"), width=30, textvariable=self.FirstName)
        patient_first_name_entry.grid(row=3, column=5, sticky=W)

        patient_last_name_entry = Entry(
            patient_information, font=("arial", 13, "bold"), width=30, textvariable=self.LastName)
        patient_last_name_entry.grid(row=4, column=5, sticky=W)

        age_entry = Entry(patient_information, font=(
            "arial", 13, "bold"), width=30, textvariable=self.Age)
        age_entry.grid(row=5, column=5, sticky=W)

        date_of_birth_entry = Entry(patient_information, font=(
            "arial", 13, "bold"), width=30, textvariable=self.dob)
        date_of_birth_entry.grid(row=6, column=5, sticky=W)

        address_entry = Entry(patient_information, font=(
            "arial", 13, "bold"), width=30, textvariable=self.PatientAddress)
        address_entry.grid(row=7, column=5, sticky=W)

        # Prescription
        text_prescription = Text(prescription, font=(
            "arial", 12, "bold"), width=39, height=15)
        text_prescription.grid(row=0, column=0)

        # Buttons
        # Prescription
        self.text_prescription = Text(prescription, font=(
            "arial", 12, "bold"), width=39, height=15)
        self.text_prescription.grid(row=0, column=0)

        # Prescription Button
        self.button_prescription = Button(button_frame, text="Prescription", font=("arial", 9, "bold"),
                                          width=30, height=2, bg="green", fg="white", anchor=CENTER, command=iPrescription)
        self.button_prescription.grid(row=0, column=1)

        # Prescription Save Button
        self.button_prescription_details = Button(button_frame, text="Prescription Save", font=("arial", 9, "bold"),
                                                  width=30, height=2, bg="green", fg="white", anchor=CENTER, command=Prescription_Details)
        self.button_prescription_details.grid(row=0, column=2)

        # Update Button
        self.button_update = Button(button_frame, text="Update", font=("arial", 9, "bold"),
                                    width=30, height=2, bg="green", fg="white", anchor=CENTER, command=update_data)
        self.button_update.grid(row=0, column=3)

        # Delete Button
        self.button_delete = Button(button_frame, text="Delete", font=("arial", 9, "bold"),
                                    width=30, height=2, bg="green", fg="white", anchor=CENTER, command=idelete)
        self.button_delete.grid(row=0, column=4)
        self.button_delete.grid(row=0, column=4)

        # Clear Button
        self.button_clear = Button(button_frame, text="Clear", font=("arial", 9, "bold"),
                                   width=30, height=2, bg="green", fg="white", anchor=CENTER, command=clear)
        self.button_clear.grid(row=0, column=5)

        # Exit Button
        self.button_exit = Button(button_frame, text="Exit", font=("arial", 9, "bold"),
                                  width=22, height=2, bg="red", fg="white", anchor=CENTER, command=iexit)
        self.button_exit.grid(row=0, column=6)

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
                               width=34, height=2, bg="#2916f5", fg="white", anchor=CENTER)
        button_logout.grid(row=0, column=4)

        # Table
        # Scroll

        scroll_x = ttk.Scrollbar(details_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_frame, orient=VERTICAL)

        self.hospital_table = ttk.Treeview(details_frame, column=("ref", "room_no", "name_of_tablets", "dose", "doctor_name", "issue_dt", "blood_pressure",
                                           "medication", "patient_id", "aadhar_no", "phone", "first_name", "last_name", "age", "dob", "address"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.hospital_table.xview)
        scroll_y.config(command=self.hospital_table.yview)

        self.hospital_table.heading("ref", text="Reference No")
        self.hospital_table.heading("room_no", text="Room No")
        self.hospital_table.heading("name_of_tablets", text="Name of Tablets")
        self.hospital_table.heading("dose", text="Dose")
        self.hospital_table.heading("doctor_name", text="Doctor Name")
        self.hospital_table.heading("issue_dt", text="Issue Date")
        self.hospital_table.heading("blood_pressure", text="Blood Pressure")
        self.hospital_table.heading("medication", text="Medication")
        self.hospital_table.heading("patient_id", text="Patient Id")
        self.hospital_table.heading("aadhar_no", text="Aadhar No")
        self.hospital_table.heading("phone", text="Phone No")
        self.hospital_table.heading("first_name", text="First Name")
        self.hospital_table.heading("last_name", text="Last Name")
        self.hospital_table.heading("age", text="Age")
        self.hospital_table.heading("dob", text="Date of Birth")
        self.hospital_table.heading("address", text="Address")

        self.hospital_table["show"] = "headings"
        self.hospital_table.pack(fill=BOTH, expand=1)
        self.hospital_table.bind("<ButtonRelease-1>", get_cursor)
        self.fetch_data()


if __name__ == "__main__":
    main()
