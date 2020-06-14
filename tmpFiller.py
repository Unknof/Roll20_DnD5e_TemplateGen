#Roll20MacroCreator
from bottle import run, route, get, error, template, request

@route('/')
def home():
    return template("TmpCreatorLanding.tpl")

@get('/create')
def create():
    tmp ="&{template:atkdmg} {{always=1}} {{rname=mname}} {{r1=[[d20cs>critcattm]]}} {{r2=[[d20cs>critcattm]]}} {{normal=1}} {{attack=1}} {{damage=1}} {{dmg1flag=1}} {{dmg1=[[dmgr]]}} {{dmg1type=dmgt}} {{crit1=[[critdmg]]}} {{desc=descr}}"
    mname = request.GET.get("mname")
    tmp =tmp.replace("mname", mname)
    descr = request.GET.get("descr")
    tmp =tmp.replace("descr", descr)
    attm = request.GET.get("attm")
    tmp =tmp.replace("attm", "+" + attm)

    dmgr = request.GET.get("dmgr")
    tmp =tmp.replace("dmgr", dmgr)

    dmgt = request.GET.get("dmgt")
    tmp =tmp.replace("dmgt", dmgt)

    critc = request.GET.get("critc")
    if critc == "":
        tmp = tmp.replace("critc", "20")
    else:
        tmp =tmp.replace("critc", str(int(critc)))

    if "+" in dmgr:
        critsplit = dmgr.split("+")
        tmp = tmp.replace("critdmg", critsplit[0])
    else:
        tmp = tmp.replace("critdmg", dmgr)

    saveatt = request.GET.get("saveatt")
    savedescp = request.GET.get("savedescp")
    savedcm = request.GET.get("savedcm")

    if saveatt != "" and savedescp != "" and savedcm != "":
        tmp = tmp + " {{save=1}} {{saveattr=" + saveatt+ "}} {{savedesc=" + savedescp + "}} {{savedc=" + savedcm + "}}"

    dmgr2 = request.GET.get("dmgr2")
    dmgt2 = request.GET.get("dmgt2")

    if dmgr2 != "" and dmgt2 != "":
        tmp = tmp + " {{dmg2flag=1}} {{dmg2=[["+ dmgr2 + "]]}} {{dmg2type=" + dmgt2 + "}}"

    dmgc2 = request.GET.get("dmgc2")

    if dmgc2 == "y" and dmgr2 != "":
        if "+" in dmgr2:
            critsplit = dmgr2.split("+")
            tmp = tmp + " {{crit2=[[" + critsplit[0] + "]]}}"
        else:
            tmp = tmp + "{{crit2=" + dmgr2 + "}}"
    return tmp


@route('/<filepath>')
def NewWay(filepath):
    return template(filepath)

run(host='localhost', port=8080)
