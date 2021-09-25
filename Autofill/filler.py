import datetime
import os

from docxtpl import DocxTemplate, InlineImage
from docx.shared import Cm

from modifiers import converter
from modifiers.InfoContainers import Header


class Filler:

    def __init__(self, **kwargs):
        """
        1) passes the parameters to processMarker1() and processMarker2() to return a string to be replaced based on the
        grade
        2) this process is done by using grade borders lists as shown, and grade border handlers
        (replaceable strings in templates)

        this is done to ease the process of .render() as this method can only be
        used once, so all info must be processed first after passing it

        :param kwargs: takes grade, total marks, and number of slice (eg. lab 2, lab 1)
        """
        self.gradeBorders = [95, 82, 70, 66, 63, 60, 56, 53, 50, 45, 40, 0]
        self.gradeBorders2 = [100, 96, 93, 90, 89, 84, 79, 75, 74, 69, 64, 60, 59, 40, 20, 0]
        self.gradeBordersHandler = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
                                    "eleven", "twelve"]
        self.gradeBordersHandler2 = ["m", "m1", "m2", "m3", "a", "a1", "a2", "a3", "ad", "ad1", "ad2", "ad3", "i", "i1",
                                     "i2", "i3"]

        self.marker1 = self.processMarker1(kwargs["grade"], kwargs["total"])
        self.marker2 = self.processMarker2(kwargs["grade"], kwargs["total"])

    def processMarker1(self, grade, total):
        grade = int(grade)
        total = int(total)
        """
        this function passes the first marker (in the template) which specifies the student performance
        to the function called infoToReplace

        :param grade: takes grade of a subject object eg. lab, quiz...
        :param total: takes total mark of the same subject object
        :return: returns the string to be replaced in the template
        """
        for i in range(len(self.gradeBorders)):
            if grade / total >= (self.gradeBorders[i] / 100):
                return self.gradeBordersHandler[i]
            else:
                continue

    def processMarker2(self, grade, total):
        grade = int(grade)
        total = int(total)
        """
        this function passes the second marker (in the template) which specifies the student performance
        to the function called infoToReplace

        :param grade: takes grade of a subject object eg. lab, quiz...
        :param total: takes total mark of the same subject object
        :return: returns the string to be replaced in the template
        """

        for i in range(len(self.gradeBorders2)):
            if grade / total >= (self.gradeBorders2[i] / 100):
                return self.gradeBordersHandler2[i]
            else:
                continue

    def infoToReplace(self, subject, **kwargs):

        """
        takes all info to be replaced in a given template

        :param kwargs: takes all info including student, sunject and subject info to be replaced in the template and
        attempts this action using render() method
        :return: new generated documents of the student in a file --> Autofill/AutofillResults
        """

        doc = DocxTemplate(kwargs["template_name"])

        picture = InlineImage(doc, kwargs["picture"], Cm(5))
        context = {"name": kwargs["name"],
                   "picture": picture,
                   "program_name": kwargs["program_name"],
                   "ID": kwargs["ID"],
                   "UEL_ID": kwargs["UEL_ID"],
                   "semester": kwargs["semester"],
                   "academic_year": str(kwargs["academic_year"]),
                   "ASU_course_code": str(kwargs["ASU_course_code"]),
                   "UEL_module_code": str(kwargs["UEL_module_code"]),
                   "ASU_course_name": kwargs["ASU_course_name"],
                   "UEL_module_name": kwargs["UEL_module_name"],
                   "date": datetime.datetime.now().strftime('%m/%d/%Y'),
                   "grade": kwargs["grade"],
                   "num": kwargs["num"],
                   "instructor_signature": kwargs["instructor_signature"],
                   "assistant_signature": kwargs["assistant_signature"],
                   self.marker1: "*",
                   self.marker2: "*"}

        doc.render(context)
        if kwargs["template_name"] == 'Autofill/Templates and pictures/Header Template.docx':
            doc.save(f"Subjects/{subject.ASU_course_code}/My Header.docx")
            converter.convert_to_pdf([f"Subjects/{subject.ASU_course_code}/My Header.docx"])

        elif kwargs["template_name"] == 'Autofill/Templates and pictures/Assignment Template.docx':

            os.makedirs(os.path.dirname(f"Subjects/{subject.ASU_course_code}/ass/AssignmentCover"
                     +str(kwargs["num"]) + ".docx"), exist_ok=True)

            doc.save(f"Subjects/{subject.ASU_course_code}/ass/AssignmentCover"
                     + str(kwargs["num"]) + ".docx")

            converter.convert_to_pdf([f"Subjects/{subject.ASU_course_code}/ass/AssignmentCover"
                                      + str(kwargs["num"]) + ".docx"])

        elif kwargs["template_name"] == 'Autofill/Templates and pictures/Quiz Template.docx':

            os.makedirs(os.path.dirname(f"Subjects/{subject.ASU_course_code}/quizzes/QuizCover"
                     + str(kwargs["num"]) + ".docx"), exist_ok=True)

            doc.save(f"Subjects/{subject.ASU_course_code}/quizzes/QuizCover"
                     + str(kwargs["num"]) + ".docx")

            converter.convert_to_pdf([f"Subjects/{subject.ASU_course_code}/quizzes/QuizCover"
                                      + str(kwargs["num"]) + ".docx"])

        elif kwargs["template_name"] == 'Autofill/Templates and pictures/Lab Template.docx':

            os.makedirs(os.path.dirname(f"Subjects/{subject.ASU_course_code}/lab/LabCover"
                     + str(kwargs["num"]) + ".docx"), exist_ok=True)

            doc.save(f"Subjects/{subject.ASU_course_code}/lab/LabCover"
                     + str(kwargs["num"]) + ".docx")

            converter.convert_to_pdf([f"Subjects/{subject.ASU_course_code}/lab/LabCover"
                                      + str(kwargs["num"]) + ".docx"])

        elif kwargs["template_name"] == 'Autofill/Templates and pictures/Project Template.docx':

            os.makedirs(os.path.dirname(f"Subjects/{subject.ASU_course_code}/project/ProjectCover"
                     + str(kwargs["num"]) + ".docx"), exist_ok=True)

            doc.save(f"Subjects/{subject.ASU_course_code}/project/ProjectCover"
                     + str(kwargs["num"]) + ".docx")

            converter.convert_to_pdf([f"Subjects/{subject.ASU_course_code}/project/ProjectCover"
                                      + str(kwargs["num"]) + ".docx"])

        elif kwargs["template_name"] == 'Autofill/Templates and pictures/Midterm Template.docx':

            os.makedirs(os.path.dirname(f"Subjects/{subject.ASU_course_code}/midterm/MidtermCover"
                     + str(kwargs["num"]) + ".docx"), exist_ok=True)

            doc.save(f"Subjects/{subject.ASU_course_code}/midterm/MidtermCover"
                     + str(kwargs["num"]) + ".docx")
            converter.convert_to_pdf([f"Subjects/{subject.ASU_course_code}/midterm/MidtermCover"
                                      + str(kwargs["num"]) + ".docx"])


def createSubjectSliceMidterm(student, subject):
    """

    Creates a filler object to process grade markers and to replace all info passed in a given template

    :param student: takes student object to pass its parameter to infoToReplace method
    :param subject: takes subject object to pass its parameter to infoToReplace method
    :return: the results of infoToReplace
    """

    midterm_fill = Filler(grade=subject.midterms.grade, total=subject.midterms.total)

    midterm_fill.infoToReplace(subject=subject, template_name='Autofill/Templates and pictures/Midterm Template.docx',
                               name=student.name, picture=student.picture_name,
                               program_name=student.program_name, academic_year=student.academic_year,
                               ID=student.ID, UEL_ID=student.UEL_ID, ASU_course_code=subject.ASU_course_code,
                               UEL_module_code=subject.UEL_module_code, ASU_course_name=subject.ASU_course_name,
                               UEL_module_name=subject.UEL_module_name, semester=subject.semester,
                               grade=subject.midterms.grade,
                               instructor_signature=subject.instructor_signature,
                               assistant_signature=subject.assistant_signature, num=1)
    subject.midterms.file_paths.insert(0, f"Subjects/{subject.ASU_course_code}/midterm/MidtermCover1.pdf")


def createSubjectSliceAssignments(student, subject):
    for i in range(len(subject.assignments.file_paths)):
        ass_fill = Filler(grade=subject.assignments.grade, total=subject.assignments.total)

        ass_fill.infoToReplace(subject=subject,
                               template_name='Autofill/Templates and pictures/Assignment Template.docx',
                               name=student.name, picture=student.picture_name,
                               program_name=student.program_name, academic_year=student.academic_year,
                               ID=student.ID, UEL_ID=student.UEL_ID, ASU_course_code=subject.ASU_course_code,
                               UEL_module_code=subject.UEL_module_code, ASU_course_name=subject.ASU_course_name,
                               UEL_module_name=subject.UEL_module_name, semester=subject.semester,
                               grade=subject.assignments.grade,
                               instructor_signature=subject.instructor_signature,
                               assistant_signature=subject.assistant_signature, num=i + 1)

        subject.assignments.file_paths.insert((2*i), f"Subjects/{subject.ASU_course_code}"
                                                          f"/ass/AssignmentCover{i+1}.pdf")


def createSubjectSliceLabs(student, subject):
    for i in range(len(subject.labs.file_paths)):
        lab_fill = Filler(grade=subject.labs.grade, total=subject.labs.total)

        lab_fill.infoToReplace(subject=subject, template_name='Autofill/Templates and pictures/Lab Template.docx',
                               name=student.name, picture=student.picture_name,
                               program_name=student.program_name, academic_year=student.academic_year,
                               ID=student.ID, UEL_ID=student.UEL_ID, ASU_course_code=subject.ASU_course_code,
                               UEL_module_code=subject.UEL_module_code, ASU_course_name=subject.ASU_course_name,
                               UEL_module_name=subject.UEL_module_name, semester=subject.semester,
                               grade=subject.labs.grade,
                               instructor_signature=subject.instructor_signature,
                               assistant_signature=subject.assistant_signature,
                               num=i + 1)
        subject.labs.file_paths.insert((2*i), f"Subjects/{subject.ASU_course_code}"
                                                      f"/lab/LabCover{i+1}.pdf")



def createSubjectSliceProject(student, subject):
    if bool(subject.project.file_paths):
        project_fill = Filler(grade=subject.project.grade, total=subject.project.total, num=1)

        project_fill.infoToReplace(subject=subject, template_name='Autofill/Templates and pictures/Project Template.docx',
                                   name=student.name, picture=student.picture_name,
                                   program_name=student.program_name, academic_year=student.academic_year,
                                   ID=student.ID, UEL_ID=student.UEL_ID, ASU_course_code=subject.ASU_course_code,
                                   UEL_module_code=subject.UEL_module_code, ASU_course_name=subject.ASU_course_name,
                                   UEL_module_name=subject.UEL_module_name, semester=subject.semester,
                                   grade=subject.project.grade,
                                   instructor_signature=subject.instructor_signature,
                                   assistant_signature=subject.assistant_signature,
                                   num=1)
        subject.project.file_paths.insert(0, f"Subjects/{subject.ASU_course_code}/project/ProjectCover1.pdf")


def createSubjectSliceQuizzes(student, subject):
    for i in range(len(subject.quizzes.file_paths)):
        quiz_fill = Filler(grade=subject.quizzes.grade[i], total=subject.quizzes.total[i])

        quiz_fill.infoToReplace(subject=subject, template_name='Autofill/Templates and pictures/Quiz Template.docx',
                                name=student.name, picture=student.picture_name,
                                program_name=student.program_name, academic_year=student.academic_year,
                                ID=student.ID, UEL_ID=student.UEL_ID, ASU_course_code=subject.ASU_course_code,
                                UEL_module_code=subject.UEL_module_code, ASU_course_name=subject.ASU_course_name,
                                UEL_module_name=subject.UEL_module_name, semester=subject.semester,
                                grade=subject.quizzes.grade[i],
                                instructor_signature=subject.instructor_signature,
                                assistant_signature=subject.assistant_signature,
                                num=i + 1)
        subject.quizzes.file_paths.insert(2*i,
                                           f"Subjects/{subject.ASU_course_code}/quizzes/QuizCover{i + 1}.pdf")


def createHeader(student, subject):
    try:
        header = Header()
        header_fill = Filler(grade=header.grade, total=header.total, num=header.num)

        header_fill.infoToReplace(subject=subject, template_name='Autofill/Templates and pictures/Header Template.docx',
                                  name=student.name, picture=student.picture_name,
                                  program_name=student.program_name, academic_year=student.academic_year,
                                  ID=student.ID, UEL_ID=student.UEL_ID, ASU_course_code=subject.ASU_course_code,
                                  UEL_module_code=subject.UEL_module_code, ASU_course_name=subject.ASU_course_name,
                                  UEL_module_name=subject.UEL_module_name, semester=subject.semester,
                                  grade=header.grade,
                                  instructor_signature=subject.instructor_signature,
                                  assistant_signature=subject.assistant_signature,
                                  num=1)
    except IOError:
        print("No Image Found"
              "your image has been replaced with a placeholder, you can edit it or regenerate your document after "
              "changing the file location to 'Autofill/Templates and pictures'")
        student.picture_name = 'Autofill/Templates and pictures/placeholder.png'
        createHeader(student, subject)


def createSubjectFiller(student, subject):
    """

    :param student: takes student object
    :param subject: takes subject object
    :return: returns all student documents and saves them in AutofillResults file
    """
    print("Please wait for a few seconds...")
    createHeader(student, subject)
    createSubjectSliceAssignments(student, subject)
    createSubjectSliceQuizzes(student, subject)
    createSubjectSliceLabs(student, subject)
    createSubjectSliceProject(student, subject)
    createSubjectSliceMidterm(student, subject)
    print("Your Documents are now ready! Please check them and edit if missing information")
