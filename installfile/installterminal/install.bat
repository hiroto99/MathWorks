@echo off

rem pathgetを実行してtemp=に貼り付けてください
set temp=
set path=%temp%
rem 上の作業を行わないと236番のエラーになります
if [%path%] == [] (
    echo "変数「temp」に値はありません。"
    eventcreate /id 236 /l system /so ERROR_INVAILD_TEMP /t error /d "変数「temp」に値はありません。"
) else (
    echo "変数「temp」の中身があることを確認しました。"
    eventcreate /id 235 /l system /so ERROR_TEMP_SUCCESS /t information /d "変数「temp」の中身があることを確認しました。"
    echo path:%path%
    SET /P ANSWER="MathWorksのフォルダーは%path%ですか？(Y,N)"
    if /i {%ANSWER%}=={y} (goto :yes)
    if /i {%ANSWER%}=={yes} (goto :yes)
    if /i {%ANSWER%}=={n} (goto :no)
    if /i {%ANSWER%}=={no} (goto :no)
)

:yes
    echo "処理は正常に開始されました。"
    eventcreate /id 0 /l system /so ERROR_BEGIN_SUCCESS /t success /d "処理は正常に開始されました。"
    
    exit

:no
    echo "セッションが取り消されました。"
    eventcreate /id 240 /l system /so ERROR_VC_DISCONNECTED /t information /d "セッションが取り消されました。"