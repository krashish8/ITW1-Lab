
if test $# -eq 0
then
    sh text_processing_menu.sh
    read cmd
else if test $1 -eq 1
then 
	sh text_expertmenu.sh
	read cmd
fi
fi
if test $cmd -lt 4 -a $cmd -gt 0
then printf "\nEnter file name: "
read file
fi
case "$cmd" in
	"1") #Search a file for a pattern
		printf "Enter pattern: "
		read p
		grep $p $file
	;;
	"2") #Count lines, words, and characters in specified file
		echo "Lines: `cat $file | wc -l`"
		echo "Words: `cat $file | wc -w`"
		echo "Characters: `cat $file | wc -c`"
	;;
	"3") #Differences between two files
	
		printf "Enter another file name: "
		read 'file2'
		
		diff "$file" "$file2"
	;;
	"4") #Return to main menu
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

