from pyhwpx import Hwp
import pyperclip as cb
#from pyhwpx import *  # (선택) 로우레벨 API 및 스크립트매크로 호환 필요시 실행

hwpxx = Hwp(visible=False)  
#hwpxx = Hwp()  

#hwpxx.clipboard_to_pyfunc()



def main_title():
    pset = hwpxx.HParameterSet.HSelectionOpt
    hwpxx.HAction.Run("MoveTopLevelBegin")
    hwpxx.HAction.Run("MoveDown")
    hwpxx.HAction.Run("MoveDown")
    hwpxx.HAction.Run("MoveDown")
    hwpxx.HAction.Run("MoveDown")
    hwpxx.HAction.Run("MoveRight")
    hwpxx.HAction.Run("MoveRight")
    hwpxx.HAction.Run("MoveRight")
    hwpxx.HAction.Run("MoveRight")
    hwpxx.HAction.Run("MoveRight")
    hwpxx.HAction.Run("MoveRight")
    hwpxx.HAction.Run("MoveSelLineEnd")
    hwpxx.HAction.Run("MoveSelLeft")
    hwpxx.HAction.Run("Copy")
    hwpxx.HAction.Run("MoveUp")
    hwpxx.HAction.Run("MoveUp")
    hwpxx.HAction.Run("MoveUp")
    hwpxx.HAction.GetDefault("Paste", pset.HSet)
    hwpxx.HAction.Execute("Paste", pset.HSet)
    hwpxx.HAction.Run("PasteTextOnly")
    hwpxx.HAction.Run("MoveDown")
    hwpxx.HAction.Run("MoveDown")
    hwpxx.HAction.Run("MoveDown")
    hwpxx.HAction.Run("MoveDown")
    hwpxx.HAction.Run("MoveLineBegin")
    hwpxx.HAction.Run("MoveRight")
    hwpxx.HAction.Run("MoveRight")
    hwpxx.HAction.Run("MoveRight")
    hwpxx.HAction.Run("MoveRight")
    hwpxx.HAction.Run("MoveRight")
    hwpxx.HAction.Run("MoveRight")
    hwpxx.HAction.Run("MoveSelLineEnd")
    hwpxx.HAction.Run("MoveSelLeft")
    hwpxx.HAction.Run("Copy")
    hwpxx.HAction.Run("MoveUp")
    hwpxx.HAction.Run("MoveUp")
    hwpxx.HAction.Run("MoveUp")
    hwpxx.HAction.GetDefault("Paste", pset.HSet)

def sub_title():
    pset = hwpxx.HParameterSet.HSelectionOpt
    hwpxx.HAction.Run("MoveDown")
    hwpxx.HAction.Run("MoveDown")
    hwpxx.HAction.Run("MoveDown")
    hwpxx.HAction.Run("MoveLineBegin")
    hwpxx.HAction.Run("MoveRight")
    hwpxx.HAction.Run("MoveRight")
    hwpxx.HAction.Run("MoveRight")
    hwpxx.HAction.Run("MoveRight")
    hwpxx.HAction.Run("MoveRight")
    hwpxx.HAction.Run("MoveRight")
    hwpxx.HAction.Run("MoveSelLineEnd")
    hwpxx.HAction.Run("MoveSelLeft")
    hwpxx.HAction.Run("Copy")
    hwpxx.HAction.Run("MoveUp")
    hwpxx.HAction.Run("MoveUp")
    hwpxx.HAction.Run("MoveUp")
    hwpxx.HAction.GetDefault("Paste", pset.HSet)
    hwpxx.HAction.Execute("Paste", pset.HSet)
    hwpxx.HAction.Run("PasteTextOnly")

def clean():
	hwpxx.HAction.Run("MoveDown")
	hwpxx.HAction.Run("MoveDown")
	hwpxx.HAction.Run("MoveLineBegin")
	hwpxx.HAction.Run("MoveSelDown")
	hwpxx.HAction.Run("MoveSelDown")
	hwpxx.HAction.Run("MoveSelDown")
	hwpxx.HAction.Run("DeleteBack")


def make_hwp():
        hwpxx = Hwp(visible=False)  
        hwpxx.open("static/templete.hwp", arg="suspendpassword:false;forceopen:true;versionwarning:false")
        hwpxx.Run("Paste")

        main_title()
        sub_title()
        clean()
        hwpxx.save_as("static/test.hwp")

make_hwp()
