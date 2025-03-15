	Do {
Print “Enter Score”
Input score
If ( score < 0 or score > 100){
Print “คะแนนไม่ถูกต้อง”
	}Else if ( score >= 80){
		Print “A”
	}Else if ( score >= 75){
		Print “B+”
	}Else if ( score >= 70){
		Print “B”
	}Else if ( score >= 65){
		Print “C+”
	}Else if ( score >= 60){
		Print “C”
	}Else if ( score >= 55){
		Print “D+”
	}Else if ( score >= 50){
		Print “D”
	}Else{
		Print “E”}

	Print “อยากทำอีกครั้งมั้ย?”
	Input answer (yes or no)
	
	If ( answer.lowercase()  == “yes” ) {
		ต่อ = True
	} Else {
		ต่อ = False }
} While ( ต่อ )
