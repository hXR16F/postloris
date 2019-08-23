#NoTrayIcon
#Region ;**** Directives created by AutoIt3Wrapper_GUI ****
#AutoIt3Wrapper_Compression=4
#AutoIt3Wrapper_UseUpx=y
#EndRegion ;**** Directives created by AutoIt3Wrapper_GUI ****

#include <ButtonConstants.au3>
#include <ComboConstants.au3>
#include <EditConstants.au3>
#include <GUIConstantsEx.au3>
#include <GuiStatusBar.au3>
#include <StaticConstants.au3>
#include <WindowsConstants.au3>
#Region ### START Koda GUI section ###
$Postloris = GUICreate("Postloris GUI", 343, 255, 373, 203)
$URL = GUICtrlCreateLabel("Target:", 8, 8, 38, 17)
$Input1 = GUICtrlCreateInput("http://localhost/login.php", 16, 28, 311, 21)
$Threads = GUICtrlCreateLabel("Threads:", 8, 58, 46, 17)
$Combo1 = GUICtrlCreateCombo("", 16, 78, 41, 25, BitOR($CBS_DROPDOWN,$CBS_AUTOHSCROLL))
GUICtrlSetData(-1, "1|5|10|12|15|20|25|30", "25")
$Fields = GUICtrlCreateLabel("Fields:", 88, 58, 34, 17)
$Input2 = GUICtrlCreateInput("email", 98, 78, 121, 21)
$Input3 = GUICtrlCreateInput("password", 98, 108, 121, 21)
$Input4 = GUICtrlCreateInput("", 98, 138, 121, 21)
$Input5 = GUICtrlCreateInput("", 98, 168, 121, 21)
$Input6 = GUICtrlCreateInput("", 98, 198, 121, 21)
$Button1 = GUICtrlCreateButton("Check", 252, 6, 75, 19)
GUICtrlSetState(-1, $GUI_DISABLE)
$Button2 = GUICtrlCreateButton("Attack", 228, 188, 105, 33)
$StatusBar1 = _GUICtrlStatusBar_Create($Postloris)
Dim $StatusBar1_PartsWidth[1] = [-1]
_GUICtrlStatusBar_SetParts($StatusBar1, $StatusBar1_PartsWidth)
_GUICtrlStatusBar_SetText($StatusBar1, @TAB & "Programmed by hXR16F", 0)
GUISetState(@SW_SHOW)
#EndRegion ### END Koda GUI section ###

While 1
	$nMsg = GUIGetMsg()
	Switch $nMsg
		Case $GUI_EVENT_CLOSE
			Exit

		Case $Button2
			Local $TargetData = GUICtrlRead($Input1)
			Local $ThreadsData = GUICtrlRead($Combo1)
			Local $Field1Data = GUICtrlRead($Input2)
			Local $Field2Data = GUICtrlRead($Input3)
			Local $Field3Data = GUICtrlRead($Input4)
			Local $Field4Data = GUICtrlRead($Input5)
			Local $Field5Data = GUICtrlRead($Input6)

			FileWrite(@ScriptDir & "\input.ini", $TargetData & @CRLF & $ThreadsData & @CRLF & $Field1Data & @CRLF & $Field2Data & @CRLF & $Field3Data & @CRLF & $Field4Data & @CRLF & $Field5Data)
			ShellExecute(@ScriptDir & "\GUI.bat")

	EndSwitch
WEnd
