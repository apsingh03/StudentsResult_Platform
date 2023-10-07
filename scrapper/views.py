from django.http import HttpResponse
from django.shortcuts import render
import requests
from bs4 import BeautifulSoup


def checkOptionConditions(soup, qNo, optionA, optionB, optionC, optionD):
    questionNo = soup.find_all("td", attrs={"class": "rw"})
    answerStatus = soup.find_all("table", attrs={"class": "menu-tbl"})

    try:
        questionOption = questionNo[qNo].table.tbody.find_all("tr")
        answeredStatus = answerStatus[qNo].tbody.find_all("tr")

        rightAnsUrl = "/per/g27/pub/2207/touchstone/TempQPImagesStoreMode1/adcimages/1690372151428/tick.png"
        # print( "Q - " , qNo+1 ,  str( answeredStatus[1].text))
        if str(answeredStatus[1].text)[8:] == "Answered":
            # print(  "Q - " , qNo+1 , " option 1 -->  ",   questionOption[optionA].img["src"]  )

            # Option 1
            if questionOption[optionA].img["src"] == rightAnsUrl:
                if (
                    str(answeredStatus[2].text)[15:]
                    == str(questionOption[optionA].text)[3]
                ):
                    # print( "Q No - " , qNo+1 , " Correct Option A - " , str(questionOption[optionA].text)  )
                    return "Q No -{qNo}  #Correct Answer".format(qNo=qNo + 1)
                else:
                    # print( "Q No - " , qNo+1 , "Option A-> Wrong Answer your Option is " , str( answeredStatus[2].text )[15:]  )
                    return "Q No -{qNo}  #Wrong Answer".format(qNo=qNo + 1)

            # Option 2
            elif questionOption[optionB].img["src"] == rightAnsUrl:
                if (
                    str(answeredStatus[2].text)[15:]
                    == str(questionOption[optionB].text)[0]
                ):
                    # print( "Q No - " , qNo+1 , " Correct Option B - " , str(questionOption[optionB].text)  )
                    return "Q No -{qNo}  #Correct Answer".format(qNo=qNo + 1)
                else:
                    # print( "Q No - " , qNo+1 , "Option B-> Wrong Answer your Option is " , str( answeredStatus[2].text )[15:]  )
                    return "Q No -{qNo}  #Wrong Answer".format(qNo=qNo + 1)

            # Option 3
            elif questionOption[optionC].img["src"] == rightAnsUrl:
                if (
                    str(answeredStatus[2].text)[15:]
                    == str(questionOption[optionC].text)[0]
                ):
                    # print( "Q No - " , qNo+1 , " Correct Option C - " , str(questionOption[optionC].text)  )
                    return "Q No -{qNo}  #Correct Answer".format(qNo=qNo + 1)
                else:
                    # print( "Q No - " , qNo+1 , "Option C-> Wrong Answer your Option is " , str( answeredStatus[2].text )[15:]  )
                    return "Q No -{qNo}  #Wrong Answer".format(qNo=qNo + 1)

            # Option 4
            elif questionOption[optionD].img["src"] == rightAnsUrl:
                if (
                    str(answeredStatus[2].text)[15:]
                    == str(questionOption[optionD].text)[0]
                ):
                    # print( "Q No - " , qNo+1 , " Correct-> Option D - " , str(questionOption[optionD].text) )
                    return "Q No -{qNo}  #Correct Answer".format(qNo=qNo + 1)
                else:
                    # print( "Q No - " , qNo+1 , "Option D Wrong Answer your Option is " , str( answeredStatus[2].text )[15:]  )
                    return "Q No -{qNo}  #Wrong Answer".format(qNo=qNo + 1)

            else:
                print("ELSE CASE ", qNo + 1)

            # str( secondQuestionStatus[2].text )[15:]

        else:
            # print( "Q No - " , qNo + 1 , "# Not Answered" ,  )
            return "Q No -{qNo}  #Not Answered".format(qNo=qNo + 1)

    except Exception as e:
        print(" Exception Error at", qNo + 1, " --> ", e)


# Create your views here.
def home_View(request):
    URL = "https://ssc.digialm.com///per/g27/pub/2207/touchstone/AssessmentQPHTMLMode1//2207O23185/2207O23185S20D98078/16903723090571825/3205012168_2207O23185S20D98078E1.html#"
    r = requests.get(URL)
    # print(r.content)

    soup = BeautifulSoup(r.content, "html5lib")

    notAnswered = 0

    # print("-------- SECTION A ------------ ")

    sectionOneArray = {}

    for data in range(25):
        # print(data)
        if data == 5:
            questions = str(checkOptionConditions(soup, data, 4, 5, 6, 7)).split("#")[1]
        else :
            questions = str(checkOptionConditions(soup, data, 3, 4, 5, 6)).split("#")[1]

        sectionOneArray["q"+str(data)] = questions
    
    # print("data" , sectionOneArray)

    sectionA_notAttempted = 0
    sectionA_right = 0
    sectionA_wrong = 0

    for data in sectionOneArray:
        if sectionOneArray[data] == "Correct Answer":
            sectionA_right += 1

        if sectionOneArray[data] == "Wrong Answer":
            sectionA_wrong += 1

        if sectionOneArray[data] == "Not Answered":
            sectionA_notAttempted += 1


    # print("-------- SECTION B ------------ ")
    # # Section B

    sectionTwoArray = { }

    for data in range(25, 50):
        # print(data)
        if data == 48:
            questions = str(checkOptionConditions(soup, data, 4, 5, 6, 7)).split("#")[1]
        else :
            questions = str(checkOptionConditions(soup, data, 3, 4, 5, 6)).split("#")[1]

        sectionTwoArray["q"+str(data)] = questions


    sectionB_notAttempted = 0
    sectionB_right = 0
    sectionB_wrong = 0

    for data in sectionTwoArray:
        if sectionTwoArray[data] == "Correct Answer":
            sectionB_right += 1

        if sectionTwoArray[data] == "Wrong Answer":
            sectionB_wrong += 1

        if sectionTwoArray[data] == "Not Answered":
            sectionB_notAttempted += 1

    # SECTION C

    # print("-------- SECTION C ------------ ")

    sectionThreeArray = { }

    for data in range(50, 75):
        # print(data)
        if data == 55 or data == 69 or data == 70 or data == 73 :
            questions = str(checkOptionConditions(soup, data, 4, 5, 6, 7)).split("#")[1]
        else :
            questions = str(checkOptionConditions(soup, data, 3, 4, 5, 6)).split("#")[1]

        sectionThreeArray["q"+str(data)] = questions


    sectionC_notAttempted = 0
    sectionC_right = 0
    sectionC_wrong = 0

    for data in sectionThreeArray:
        if sectionThreeArray[data] == "Correct Answer":
            sectionC_right += 1

        if sectionThreeArray[data] == "Wrong Answer":
            sectionC_wrong += 1

        if sectionThreeArray[data] == "Not Answered":
            sectionC_notAttempted += 1

    # SECTION D
    # print("-------- SECTION D ------------ ")

    sectionFourArray = { }

    for data in range(75, 100):
        # print(data)
        if data == 95 or data == 96 or data == 97 or data == 98 or data == 99  :
            questions = str(checkOptionConditions(soup, data, 7, 8, 9, 10 )).split("#")[1]
        else :
            questions = str(checkOptionConditions(soup, data, 3, 4, 5, 6)).split("#")[1]

        sectionFourArray["q"+str(data)] = questions


    sectionD_notAttempted = 0
    sectionD_right = 0
    sectionD_wrong = 0

    for data in sectionFourArray:
        if sectionFourArray[data] == "Correct Answer":
            sectionD_right += 1

        if sectionFourArray[data] == "Wrong Answer":
            sectionD_wrong += 1

        if sectionFourArray[data] == "Not Answered":
            sectionD_notAttempted += 1

    
    # find candidtate details
    table = soup.find('div', attrs = {'class':'main-info-pnl'})
    examName = table.div.strong.span.text

    print("--------" , examName , "-----------")

    findUserDetailsRow = table.table.tbody.find_all("tr")

    candidateRollNo = findUserDetailsRow[0].find_all("td")[1].text
    candidateName = findUserDetailsRow[1].find_all("td")[1].text
    candidateVenueName = findUserDetailsRow[2].find_all("td")[1].text
    candidateExamDate = findUserDetailsRow[3].find_all("td")[1].text
    candidateExamTime = findUserDetailsRow[4].find_all("td")[1].text
    candidateSubject = findUserDetailsRow[5].find_all("td")[1].text

    print( "candidateRollNo - ", candidateRollNo )
    print( "candidateName - ", candidateName )
    print( "candidateVenueName - ", candidateVenueName )
    print( "candidateExamDate - ", candidateExamDate )
    print( "candidateExamTime - ", candidateExamTime )
    print( "candidateSubject - ", candidateSubject )

  
    # .count total sections
    findQuestionsSection = soup.find_all(class_="section-cntnr")
    print( "Total Sections  ", len(findQuestionsSection)  )


    print(
        "-------------------- Marks in each subjects ----------------------------------- "
    )
    print("Section . - ", "Attempted ", "NotAttempted", "Right", "Wrong", "Marks")

    print(
        "Section A - ",
        (sectionA_right + sectionA_wrong),
        "         ",
        sectionA_notAttempted,
        "         ",
        sectionA_right,
        "    ",
        sectionA_wrong,
        " ",
        "marks",
    )
    print(
        "Section B - ",
        (sectionB_right + sectionB_wrong),
        "         ",
        sectionB_notAttempted,
        "         ",
        sectionB_right,
        "    ",
        sectionB_wrong,
        " ",
        "marks",
    )
    print(
        "Section C - ",
        (sectionC_right + sectionC_wrong),
        "         ",
        sectionC_notAttempted,
        "         ",
        sectionC_right,
        "    ",
        sectionC_wrong,
        " ",
        "marks",
    )
    print(
        "Section D - ",
        (sectionD_right + sectionD_wrong),
        "         ",
        sectionD_notAttempted,
        "         ",
        sectionD_right,
        "    ",
        sectionD_wrong,
        " ",
        "marks",
    )

    allSectionAttemptedSum = (
        (sectionA_right + sectionA_wrong)
        + (sectionB_right + sectionB_wrong)
        + (sectionC_right + sectionC_wrong)
        + (sectionD_right + sectionD_wrong)
    )
    allSectionNotAttemptedSum = (
        sectionA_notAttempted
        + sectionB_notAttempted
        + sectionC_notAttempted
        + sectionD_notAttempted
    )
    allSectionRightSum = (
        sectionA_right + sectionB_right + sectionC_right + sectionD_right
    )
    allSectionWrongSum = (
        sectionA_wrong + sectionB_wrong + sectionC_wrong + sectionD_wrong
    )
    print(
        "OverALL   - ",
        allSectionAttemptedSum,
        "         ",
        allSectionNotAttemptedSum,
        "         ",
        allSectionRightSum,
        "    ",
        allSectionWrongSum,
        " ",
        "marks",
    )

    print(
        "-------------------- END SUMMARY RESULT ----------------------------------- "
    )


    return HttpResponse("from scrapper its working ")
