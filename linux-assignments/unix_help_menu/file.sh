if test $# -eq 0
then 
	sh file_management_menu.sh
	read cmd
else if test $1 -eq 1
then 
	sh file_expertmenu.sh
	read cmd
fi
fi

if test $cmd -gt 0 -a $cmd -lt 6
then printf "\nEnter file name: "
read file
fi
case "$cmd" in
	"1") #Display content of a file
		
		if test -f $file
		then	
			cat $file | less
		else
			echo "$file: does not exist"
			exit 1
		fi
	;;
	"2") #Remove a file
		if test -f $file
		then
			rm $file
		else
			if test -d $file
			then
				rm -r $file
			else
				echo "$file: does not exist"
				exit 1
			fi
		fi 
	;;
	"3") #Copy a file
		if test -f $file
		then
			printf "Enter new file name: "
			read newfile
			cp $file $newfile
		else 
			if test -d $file
			then
				printf "Enter new directory name: "
				read newfile
				cp -r $file $newfile
			else
				echo "$file: does not exist"
				exit 1
			fi
		fi
	;;
	"4") #List a file
		if test -f $file
		then	
			ls -l $file
		else
			echo "$file: does not exist"
			exit 1
		fi
	;;
	"5") #Size of a file
		if test -f $file
		then
			echo `ls -lh file.sh | cut -d ' ' -f 5`
		else
			if test -d $file
			then
				echo `du -hs $file| awk '{print $1}'` 
			else
				echo "$file: does not exist"
				exit 1
			fi
			
		fi
	;;
	"6") #Return to main menu
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
