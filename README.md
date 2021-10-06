# practica-uno-inicio-git
$TEXTO = '2806:109f:13:98a2:d589:fdd4:8bd0:57a7'
$ENCODED1 = [Convert]::ToBase64String([Text.Encoding]::Unicode.GetBytes($TEXTO))
Write-Output $ENCODED 1
$TEXTO = '192.168.1.139'
$ENCODED1 = [Convert]::ToBase64String([Text.Encoding]::Unicode.GetBytes($TEXTO))
Write-Output $ENCODED1
