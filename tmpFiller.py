#Roll20MacroCreator
from bottle import run, route, get, error, template, request

@route('/')
def home():
    return template("TmpCreatorLanding.tpl")

@get('/create')
def create():
    tmp ="&{template:atkdmg} {{rname=mname}} {{r1=[[d20cs>critcattm]]}} {{normal=1}} {{attack=1}} {{damage=1}} {{dmg1flag=1}} {{dmg1=[[dmgr]]}} {{dmg1type=dmgt}} {{crit1=[[critdmg]]}} {{desc=descr}}"
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
        tmp = tmp.replace("critc", "19")
    else:
        tmp =tmp.replace("critc", str(int(critc) -1))

    if "+" in dmgr:
        critsplit = dmgr.split("+")
        tmp = tmp.replace("critdmg", critsplit[0])
    else:
        tmp = tmp.replace("critdmg", dmgr)

    return tmp


run(host='localhost', port=8080)
