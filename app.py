# Q1:
# Load initial data

import pandas as pd

data = pd.read_csv('/home/jason/Documents/GitHub/data4life/data4life/data.txt',skipinitialspace=True)

data = data.astype('string')

data['concat docdate']= data['doctor_id']+data['appointment_datetime']
data['concat patientdate']= data['patient_id']+data['appointment_datetime']
data[['date','time']] = data['appointment_datetime'].str.split(' ',1,expand=True)

def doc_id_input():
    doctor = str(input('Please enter doctor id: '))
    return doctor

def date_input():
    date = str(input('Please enter the date you want to check in DDMMYYYY format: '))
    return date

def patient_id_input():
    patient = str(input('Please enter your patient id: '))
    return patient

def time_input():
    while True:
        time = str(input("Please enter your preferred time in HH:MM:SS: "))
        if time > '16:00:00' or time < '08:00:00':
            print('Appointment times must be between 08:00:00 and 16:00:00')
            continue
        break
    return time
# Q2:

# Get all appointments for the given doctor & date

def check_doc_appt (doctor,date,data):
    example = data[(data["doctor_id"]== doctor) & (data["date"]==date)]
    return "No appointment for this doctor on this date" if example.empty else example

# Q2B

# Get all appointment for given patient & date

def check_patient_appt (patient,date,data):
    example = data[(data["patient_id"]== patient) & (data["date"]==date)]
    return "You have no appointment on this date" if example.empty else example

def check_all_patient_appt (patient,data):
    example = data[(data["patient_id"]== patient)]
    return "You have no appointment on this date" if example.empty else example

# Q3:

# Patient makes an appointment by selecting doctor and date and time

def make_appt(doctor,patient,date,time,data):  
    if doctor+date+' '+time in data['concat docdate'].values:
        return 'Doctor is not available at this specific date and time',check_doc_appt(doctor,date,data)
    elif patient+date+' '+time in data['concat patientdate'].values:
        return 'You already have another appointment at this specific date and time',check_patient_appt(patient,date,data)
    else:
        data.loc[data.shape[0]] = [doctor,patient,date+' '+time,doctor+date+' '+time,patient+date+' '+time,date,time,]
        return check_patient_appt(patient,date,data)

# Q4:

# Patient cancels appointment by selecting doctor and date & time

def delete_appt_patient (doctor,patient,date,time,data):
    if patient+date+' '+time not in data['concat patientdate'].values:
        return 'You have no such appointment',check_all_patient_appt(patient,data),data
    else:
        data = data.drop(data[(data['doctor_id']==doctor) & (data["patient_id"]== patient) & (data["date"]==date) & (data["time"]==time)].index)
        return 'Appointment cancelled, these are your existing appointments',check_all_patient_appt(patient,data),data

print('Welcome to the appointment system, run data to see current list \n')
print('Available functions are: \n')
print('check_doc_appt(doc_id_input(),date_input(),data)\n')
print('check_patient_appt(patient_id_input(),date_input(),data) \n')
print('check_all_patient_appt(patient_id_input,data)\n')
print('make_appt(doc_id_input(),patient_id_input(),date_input(),time_input(),data)\n')
print('text,check,data = delete_appt_patient(doc_id_input(),patient_id_input(),date_input(),time_input(),data)\n')
