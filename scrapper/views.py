from django.http import HttpResponse
from django.shortcuts import render
import requests
from bs4 import BeautifulSoup


def checkOptionConditions(soup, qNo):
    questionNo = soup.find_all("td", attrs={"class": "rw"})
    answerStatus = soup.find_all("table", attrs={"class": "menu-tbl"})

    try:
        questionOption = questionNo[qNo].table.tbody.find_all("tr")
        answeredStatus = answerStatus[qNo].tbody.find_all("tr")
        questionOptionsLength = len(questionOption)
        # print("len " , questionOptionsLength )

        rightAnsUrl = "/tick.png"

        # print("Your chosed  Option " ,  str(answeredStatus[2].text)[15:] )
        # print( "Q -" , qNo+1 , "Option A" , str(questionOption[questionOptionsLength-4].img["src"])[-9:] == rightAnsUrl  , str( questionOption[questionOptionsLength-4].text) )
        # print( "Q -" , qNo+1 , "Option B" , questionOption[questionOptionsLength-3].img["src"][-9:] == rightAnsUrl , str( questionOption[questionOptionsLength-3].text) )
        # print( "Q -" , qNo+1 , "Option C" , questionOption[questionOptionsLength-2].img["src"][-9:] == rightAnsUrl , str( questionOption[questionOptionsLength-2].text) )
        # print( "Q -" , qNo+1 , "Option D" , questionOption[questionOptionsLength-1].img["src"][-9:] == rightAnsUrl , str( questionOption[questionOptionsLength-1].text) )

        if (
            str(answeredStatus[1].text)[8:] == "Answered"
            or str(answeredStatus[1].text)[8:] == "Marked For Review"
        ):
            # print(  "Q - " , qNo+1 , " option 1 -->  ",   str(answeredStatus[1].text)[8:]  )

            # ----------------
            # ----- Option 1
            # ---------------
            if questionOption[questionOptionsLength - 4].img["src"][-9:] == rightAnsUrl:
                # print("Option A ")
                if (
                    str(answeredStatus[2].text)[15:]
                    == str(questionOption[questionOptionsLength - 4].text)[3]
                ):
                    # print( "Q No - " , qNo+1 , " Correct Option A - " , str(questionOption[questionOptionsLength-4].text)  )
                    return "Q No -{qNo}  #Correct Answer".format(qNo=qNo + 1)
                else:
                    # print( "Q No - " , qNo+1 , "Option A-> Wrong Answer your Option is " , str( answeredStatus[2].text )[15:]  )
                    return "Q No -{qNo}  #Wrong Answer".format(qNo=qNo + 1)

            # ----------------
            # ----- Option 2
            # ---------------
            elif (
                questionOption[questionOptionsLength - 3].img["src"][-9:] == rightAnsUrl
            ):
                # print("Option B ")
                if (
                    str(answeredStatus[2].text)[15:]
                    == str(questionOption[questionOptionsLength - 3].text)[0]
                ):
                    # print( "Q No - " , qNo+1 , " Correct Option B - " , str(questionOption[questionOptionsLength-3].text)  )
                    return "Q No -{qNo}  #Correct Answer".format(qNo=qNo + 1)
                else:
                    # print( "Q No - " , qNo+1 , "Option B-> Wrong Answer your Option is " , str( answeredStatus[2].text )[15:]  )
                    return "Q No -{qNo}  #Wrong Answer".format(qNo=qNo + 1)

            # ----------------
            # ----- Option 3
            # ---------------
            elif (
                questionOption[questionOptionsLength - 2].img["src"][-9:] == rightAnsUrl
            ):
                # print("Option C ")
                if (
                    str(answeredStatus[2].text)[15:]
                    == str(questionOption[questionOptionsLength - 2].text)[0]
                ):
                    # print( "Q No - " , qNo+1 , " Correct Option C - " , str(questionOption[questionOptionsLength-2].text)  )
                    return "Q No -{qNo}  #Correct Answer".format(qNo=qNo + 1)
                else:
                    # print( "Q No - " , qNo+1 , "Option C-> Wrong Answer your Option is " , str( answeredStatus[2].text )[15:]  )
                    return "Q No -{qNo}  #Wrong Answer".format(qNo=qNo + 1)

            # ----------------
            # ----- Option 4
            # ---------------
            elif (
                questionOption[questionOptionsLength - 1].img["src"][-9:] == rightAnsUrl
            ):
                # print("Option D ")
                if (
                    str(answeredStatus[2].text)[15:]
                    == str(questionOption[questionOptionsLength - 1].text)[0]
                ):
                    # print( "Q No - " , qNo+1 , " Correct-> Option D - " , str(questionOption[questionOptionsLength-1].text) )
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
    # anjali
    # URL = "https://ssc.digialm.com///per/g27/pub/2207/touchstone/AssessmentQPHTMLMode1//2207O23185/2207O23185S14D95912/16903650363776245/3201002499_2207O23185S14D95912E1.html"
    # prv
    # URL = "https://ssc.digialm.com///per/g27/pub/2207/touchstone/AssessmentQPHTMLMode1//2207O23185/2207O23185S20D98078/16903723090571825/3205012168_2207O23185S20D98078E1.html#"
    # puja
    URL = "https://ssc.digialm.com//per/g27/pub/2207/touchstone/AssessmentQPHTMLMode1//2207O23185/2207O23185S43D104333/16957123642475521/3201005689_2207O23185S43D104333E1.html"

    r = requests.get(URL)
    # print(r.content)

    soup = BeautifulSoup(r.content, "html5lib")

    notAnswered = 0

    # ------------------------------------------------
    # ----------------- SECTION A
    # ------------------------------------------------

    sectionOneArray = {}

    for sectionA in range(25):
        # print("sectionA")
        # print(checkOptionConditions(soup, sectionA ) )
        questions = str(checkOptionConditions(soup, sectionA)).split("#")[1]
        sectionOneArray["q" + str(sectionA + 1)] = questions

    # print(sectionOneArray)

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

    # ------------------------------------------------
    # ----------------- SECTION B
    # ------------------------------------------------

    sectionTwoArray = {}

    for sectionB in range(25, 50):
        questions = str(checkOptionConditions(soup, sectionB)).split("#")[1]
        sectionTwoArray["q" + str(sectionB + 1)] = questions

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

    # ------------------------------------------------
    # ----------------- SECTION C
    # ------------------------------------------------

    sectionThreeArray = {}

    for sectionC in range(50, 75):
        questions = str(checkOptionConditions(soup, sectionC)).split("#")[1]

        sectionThreeArray["q" + str(sectionC + 1)] = questions

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

    # ------------------------------------------------
    # ----------------- SECTION D
    # ------------------------------------------------

    sectionFourArray = {}

    for sectionD in range(75, 100):
        questions = str(checkOptionConditions(soup, sectionD)).split("#")[1]
        sectionFourArray["q" + str(sectionD + 1)] = questions

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
    table = soup.find("div", attrs={"class": "main-info-pnl"})
    examName = table.div.strong.span.text

    print("--------", examName, "-----------")

    findUserDetailsRow = table.table.tbody.find_all("tr")

    candidateRollNo = findUserDetailsRow[0].find_all("td")[1].text
    candidateName = findUserDetailsRow[1].find_all("td")[1].text
    candidateVenueName = findUserDetailsRow[2].find_all("td")[1].text
    candidateExamDate = findUserDetailsRow[3].find_all("td")[1].text
    candidateExamTime = findUserDetailsRow[4].find_all("td")[1].text
    candidateSubject = findUserDetailsRow[5].find_all("td")[1].text

    print("candidateRollNo - ", candidateRollNo)
    print("candidateName - ", candidateName)
    print("candidateVenueName - ", candidateVenueName)
    print("candidateExamDate - ", candidateExamDate)
    print("candidateExamTime - ", candidateExamTime)
    print("candidateSubject - ", candidateSubject)

    # print(sectionOneArray )
    # print(sectionTwoArray )
    # print(sectionThreeArray )
    # print(sectionFourArray )

    # .count total sections
    findQuestionsSection = soup.find_all(class_="section-cntnr")
    print("Total Sections  ", len(findQuestionsSection))

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
