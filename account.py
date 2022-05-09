from pydoc import doc
from xml.dom.minidom import Document


class Account:          # Class with its attributes and methods
    ID = int          # name attribute = datatype that it receives
    name = str
    document = str
    email = str
    password = str

    def __init__(self, name, document):             # Constructor method with its minimum parameters in this case it would be name and document. 
        self.name = name            # self.name call to attribute from Class Account inside method
        self.document = document
