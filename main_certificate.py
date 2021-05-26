#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
from certificate import *
from docx import Document
import csv
from docx2pdf import convert


# create output folder if not exist
try:
    os.makedirs("Output/Doc")
    os.makedirs("Output/PDF")
except OSError:
    pass


def get_participants(f):
    data = [] # create empty list
    with open(f, mode="r", encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            data.append(row) # append all results
    return data

def create_docx_files(filename, list_participate, ambassador):

    for participate in list_participate:
        # use original file everytime
        doc = Document(filename)

        name = participate["Name Surname"]
        event = participate["Workshop"]

        replace_participant_name(doc, name)
        replace_event_name(doc, event)
        replace_ambassador_name(doc, ambassador)
        doc.save('Output/Doc/{}.docx'.format(name))
        print("Output/{}.pdf Creating".format(name))
        convert('Output/Doc/{}.docx'.format(name), 'Output/Pdf/{}.pdf'.format(name))

    
# get certificate temple path
certificate_file = "Data Template/Event Certificate Template.docx"
# get participants path
participate_file = "Data Template/Event Participate Template.csv"

# get ambassador name
ambassador_name = "Ayşegül Aydoğan"

# get participants
list_participate = get_participants(participate_file);

# process data
create_docx_files(certificate_file, list_participate, ambassador_name)



