
if test $# -eq 0
then
	sh system_status_menu.sh
	read cmd
else if test $1 -eq 1
then 
	sh status_expertmenu.sh
	read cmd
fi
fi
case "$cmd" in
	"1") #Display current date and time
		date "+%D %R"
	;;
	"2") #Current Disk usage
		df -h | less
	;;
	"3") #List current local and environment 
		printenv | less
	;;
	"4") #Display Process status information
		ps -e | less
	;;
	"5") #Return to main menu
		if test $# -eq 0 
		then
			sh myhelp.sh
		else
			exit 1
		fi
	;;
	*)
		printf "\nInvalid Choice!\n"
		exit 1
	;;
esac


